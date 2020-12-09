**Labels:**

discussion



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 24, 2020 at 04:42:46_
_Originally opened as: project-topaz/topaz - Issue 999_

----

Given recent issues with maintaining duplicate enums, I would like to try tackle that issue after I complete my additional effects work and the recent flurry of additional modifier PRs die down. Due to peoples schedules not aligning, I have chosen to make an issue for the discussion instead of only speaking in discord where it can be scrolled off and forgotten.

The problem:
multiple lists of IDs are having to be maintained in multiple files. Status effects live in status.lua, status_effects.h, and status_effects.sql and the only thing keeping them in sync is the fact that they have to match the client and we extract them from it. modifiers don't have that requirement and are made up, requiring reviewer to be watchdogs to make sure IDs aren't used twice for 2 different things - which sometimes happens even in the same file!

I would like us to have only ONE list for each thing, and pass that data along between core and lua to whichever one did not have the list. Ideally I would not use the database for this, but this may be the option that is least confusing. I would especially like to avoid doing what the currencies do (quoted string names for the identifier).

If an SQL table is used, I want to have a human readable description field, something a lot of folks will balk at. We do it elsewhere already - the mob pool name originally field only existed for this reason. Others might balk at the idea of even using the database at all. Its a lot easier to maintain if either the lua linting or the sql execution on our automated builds catch duplication mistakes like #998. Presently on the core side a duplicate mod ID will build without issue. I'm open to suggestions that keep adding a new modifiers newbie friendly while enumerating once, not twice or thrice.  Once modifiers are taken care of we can start looking at applying similar methods to other duplicated enumerations. **Status.lua is almost entirely copies of core enums put to lua.**


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 24, 2020 at 04:42:59_

----

issue 999 get


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Aug 24, 2020 at 07:56:47_

----

I think raising an issue and tagging it as a discussion is a really good move ⭐. 

I was originally going to throw my hat in on the side of keeping the current C++ enums and scraping them on start-up, until you reminded me that enums (by design) can handle duplicates:

```cpp
enum class MOD : int
{
  STR = 0,
  DEX = 0,
};
// no warnings, no errors
```

There is a proposal to introduce `std::enum_traits` to be able to inspect an enum at compile-time, but it hasn't landed yet (http://aantron.github.io/better-enums/demo/C++17ReflectionProposal.html)

So, if we can't easily detect at compile-time, and at runtime it's already too late - we have to go with CI-time. We already have sanity checks for being able to insert all the SQL files, so that's a good place to put it.

===

In this new world where we've loaded everything in on startup - how will we interact with the new mods?

It's unreasonable to think that anyone is going to be hot-reloading MOD values at runtime, so we can dump them into an `unordered_map` on the Core side so lookup is constant. A binding to access the C++ map from Lua comes with a teeny-tiny performance cost and will add up over time, so the obvious next step then is to plop them into a similar structure on the Lua side.

This performance cost would be erased if we eventually transitioned away from Lunar into FFI, but that's a discussion for another time.

===

Is this _another_ thing that's going to be loaded at startup, slowing everything down a bit? Sure.
Is this going to be loaded and duplicated on _every_ map server instance? Yes.
Do we have a solution for that yet? No.

If someone wants to start work on a content server so all of this stuff is only ever loaded once, be my guest, but I'm not yet feeling the urge to spin out another executable quite yet.

/2cents


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Tuesday Aug 25, 2020 at 18:49:49_

----

This is going to be a super unpopular idea, but I think we need to throw-out the concept of using ENUMs and any identifier that isn't unique, either a UUID or just a string equivalent. This will eliminate all collisions. We keep the list in lua so it's easy to use and modifiable, core can load it no problem, and pull requests don't have to watch out for each other and no "tracking" spares.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 25, 2020 at 19:41:00_

----

with effects you can't even do that. its got an ID because thats what the client uses, and we needed something human readable to know what effect we were dealing with. with mods transporting a number was less expensive than porting around a string, but that is quickly being offset by human error..


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Tuesday Aug 25, 2020 at 19:47:23_

----

Yes, we would have to map effects, but we have a limited number of effects included in the client.

We can dynamically generate string to number at run-time as long as we don't save any of those numbers to the database anywhere. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 25, 2020 at 20:07:07_

----

Effects have a lot of baggage that needs connected to them, so you'd need an efficient system for doing that elsewhere first that is easy to edit. I'd like to murder that sql table in particular with an atom bomb, and start storing the effect flags in hex. Or just make each effect have a properties table.

Invisible Effect, what do you do?
```lua
someName =
{
    I_wear_off_on_being_cast_at_Teo,
    I_set_the_invis_bit_Teo,
}
```
*pats invis on the imaginary head*
Sit. Good script. Now play dead.

Edit:
> but we have a limited number of effects included in the client.

forgot for a min, but we exceed whats in the client using higher ID values to avoid collision. just worth a mention. They still need a numeric value for the client though so it knows what assets to load up.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Tuesday Aug 25, 2020 at 20:25:52_

----

And its those ones that exceed whats in the client that we need to deal with. 

However, usually those are invisible effects anyway since there is no corresponding icon that matches the effect ID... so do we really need to track those with non-unique identifiers?

Anyway, Ithink we need to have unique identifiers to avoid collision on PRs, "id tracking", and people who have custom mods and effects.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 25, 2020 at 20:49:40_

----

We usually connect them to a legit effects Icon. very few are invisible, and for those that are we tie them to index zero for the icon part. We should rework how we do those a bit for other reasons too. I don't think they will be a problem since we just make crap up for those - I just mention it so they do not get forgotten in whatever we finally decide on doing. More importantly we've veered more towards "theoretically this would be great let the great refactor of our time begin" and away from "Teo can knock this out in a weekend and the existing scripts will be handled by a simple find+replace to fix that function argument". :sweat_smile: /nervouslaugh


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Tuesday Aug 25, 2020 at 20:57:18_

----

part of the design process, I suppose.

Well, do we do a half measure with a human readable sql file?

If human readability is the goal, we shouldn't use an sql table. Just a lua file that the core loads on launch. That's a great first step. Put them in an unordered map or the fastest data structure in the STL that can map strings to ints and call it a day for now.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 25, 2020 at 21:20:51_

----

I took a proof of concept stab at sql'ing it last night and I gotta say I did -not- like the result. Too much having to escape strings.


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Thursday Sep 10, 2020 at 15:02:21_

----

I spent a few hours attempting to solve this by copying the Mod enum into the tpz global namespace as a table at startup. Enums not being inspectable and not being iterable makes it a bit of a chore. 

I did for a while consider just converting the Mod enum to a map (which would solve the iterability issue), but haven't pulled the trigger on trying that.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Wednesday Sep 30, 2020 at 18:43:14_

----

Going to zombie this a bit as I have been thinking about this a lot due to some of my future PRs getting messed up by this junk.

My proposal is thus...

We keep a singular master list of effect and status IDs in Lua, that maps Strings to IDs.
Then, we manage a separate script that is invoked at build time by cmake to generate, using the Lua files, the C++ that map ID to String and String to ID.

Then, when we write to Database, mods are not stored as ID values, but the strings instead.

What this allows us to do is freely generate IDs that we track at a development level by their string nomenclatures (which are unique) and at run-time by their numerical values. This gives us freedom add new mods or effects without having to worry about collision (especially in the database). 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 01, 2020 at 20:04:15_

----

Mods stored in DB as strings feels like a code approach to a tool problem.

There needs to be a centralized location for string / ID pairs.

But if it were also a SQL table, it can be referenced from the same location that item mods are. If the problem is that people don't know what a mod ID represents, that can be fixed with a Join on the `mods` table.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Oct 01, 2020 at 20:32:29_

----

> Mods stored in DB as strings feels like a code approach to a tool problem.
> 
I disagree. It is a solution to the fact that our mods don't have unique identifiers. A value of "1" or even "850" is not unique. What if some people want to have custom mod IDs or effect IDs? Well, most of us just jam them up at a higher value, sure that's great, but it's not really clean. And the loading code is limited, so we have go to modify C++ code to account for our high effect items, it's a mess and frustrating. Mods are unique and we should start treating them as such. This gives our code much more flexibility for customization and completely eliminates the need for any special considerations. Also, remember during operation, they are still going to be integer values, just integer values that are generated at build-time, so we lose no efficiency there.

> There needs to be a centralized location for string / ID pairs.
> 
Hence using Lua as the central location and then auto-generating a C++ file on build. Lua makes the most sense because the long-term goal is to have loadable modules for customization, and the build-time script could load modules before generating its cpp/h files. Also, imagine two loadable modules by two different creators end up using the same "high value" for their custom modifier.

> But if it were also a SQL table, it can be referenced from the same location that item mods are. If the problem is that people don't know what a mod ID represents, that can be fixed with a Join on the `mods` table.

If I'm quickly browsing on Github through item_mods.sql, how do I do join? You can't. On top of that, I will state now (and for people who have heard me say this before, I apologize), but we NEED to start moving static data OUT of the database. We are using a transactional database for single transactions at run-time for almost everything that isn't character related. This is a waste, it's clumsy at best to manage, and it again limits our overall flexibility especially when looking forward into loadable modules for customization (more reason to move this to Lua).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 01, 2020 at 20:49:59_

----

> but we NEED to start moving static data OUT of the database. We are using a transactional database for single transactions at run-time for almost everything that isn't character related

hard disagree and no we aren't "at runtime"\*. You and I clashed on this topic before because the examples you want to move out were not at runtime, they were at startup. We are not querying item mods constantly. We load them _one time._

We have a database for reasons, and that one of them is to not hard code things everywhere when a table is so much easier. Likewise gigantic lists in lua are not a good idea and in many cases we haven't got a better option atm. This could be one of those things that has to go primarily in lua. I was hoping I could core it.  And I detest using quoted strings with doomsday hunting kal-el levels of fury. I used to think that was great. I learned how wrong I was much later. I will never be for "string_here" in place of the id or where we currently use MODIFIER_NAME variables. I wanted to generate/unify a list that matches up both lists without humans maintaining them both, but I want to avoid doing it by quote strings if at all possible. when its the only option left, then and only then will I eat my hat and accept it. 

There is a possible path forward from Lua into C++ or C++ to Lua using the same styling we have in the lua end right now, but I do not yet know the performance impact of it. I really shouldn't be difficult to do, but I can't fiddle with it when I still need to finish my add effect work.


###### \*Runtime to you may begin when the exe starts. To me is when we're up and running and you can log in. Don't give 2 squirts about efficiency prior to when ppl can get in game if it means sacrificing sane data management or sane workflow to get there.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Oct 01, 2020 at 22:11:23_

----

Okay, yes runtime to me includes start  up.

When we clashed previously, are you talking like 5+ years ago? Because right now I'm talking about the static data only needs to be moved out of database. It makes no sense for it to go there. Lua is a configuration management language as well, it is meant to hold and load static data like mod on items, where mobs spawn quickly, etc.

The reason we keep a transactional database is for data that has state that gets saved and loaded on a regular basis, ie character data. If we are keeping data in that database that we only load once and never save to, we are not only polluting our database with non-sense but using a less than "good" method to handle this type of data (ie, see all reasons I've already listed about about why Lua). I just want to move the static data out. 

I will again re-iterate the point that large lists stored in Lua is practically the point of Lua, and I think seeing them as "hardcoded" is flawed at best. Hardcoding is where we check for specific values like "item ID" instead of "does this item have this property?" IE, can it be generalized. 

So, let me give a quick example of what I'm talking about.

lua_script:
```
tpz.etc.etc.etc.modifiers = {
   STR,
   DEX,
   ...
}
```

generator_lua_script_invoked_by_cmake_or_manually:
`This is fed into a script, this creates CPP/H files at build time or when invoked.`

modifier.h:
```
class enum Mod
{
    STR,
    DEX,
}

std::map<int,string> mod_int_to_str = {
    { Mod::STR, "str" },
    { Mod::DEX, "dex" },
    ...
}

std::map<string,int> mod_str_to_int = {
    { "str", Mod::STR },
    { "dex", Mod::DEX },
}
```

Those two maps are for when reading mods from the database, or, when talking about effects which would handled similarly, when writing char_effects. We'd have to update the SQL stuff, but that's easy to automate those with the db tool as a migration. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 01, 2020 at 23:07:03_

----

no. just..no..

And no that is not the point of lua. You're idea of normalcy is about the most inconvenient thing I can conceive of. And I am aware of the dictionary definition of hard coding thanks.

> it is meant to hold and load static data like mod on items, **where mobs spawn** quickly, etc.

I'd quit the project entirely or fork if that were ever to be done in lua. period.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 01, 2020 at 23:07:59_

----

We have far to much data to manage via lua. you can't query a lua table. This entire discussion is so absurd I am finding it difficult to remain polite, so I am exiting.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Oct 01, 2020 at 23:11:20_

----

 mean, I can cite the creators when I get home if you want.

Also, we don't query data now! we load is using queries but we aren't
querying any of this data lol.

On Thu, Oct 1, 2020, 5:08 PM TeoTwawki <notifications@github.com> wrote:

> We have far to much data to manage via lua. you can't query a lua table.
> This entire discussion is so absurd I am finding it difficult to remain
> polite, so I am exiting.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/issues/999#issuecomment-702442160>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AA3KLWJDZVCPTQSRBIOA7CLSIUDVZANCNFSM4QJCOZUQ>
> .
>



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 01, 2020 at 23:16:17_

----

I know one of the creators ffs. Its tailored for embedding, not to store everything in creation!

> Also, we don't query data now!

when I need to look up something I know it in a db table I query my database. I don't go searching through flat files F that nonsense.


edit edit edit: Teo always has one last post in him yadda yadda blah blah


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Oct 01, 2020 at 23:18:09_

----

And why might you want to embed Lua into your system? Maybe so you don't
have to recompile everytime you change the ... configuration?

On Thu, Oct 1, 2020, 5:16 PM TeoTwawki <notifications@github.com> wrote:

> I know one of the creators ffs. Its tailored for embedding, not to store
> everything in creation!
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/issues/999#issuecomment-702444655>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AA3KLWPQQVGDMWMYQPPPBDDSIUEU5ANCNFSM4QJCOZUQ>
> .
>



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 01, 2020 at 23:22:13_

----

_We_ query it when we're searching for mobs with given skill lists, updating groups, ensuring that pools have the right family, etc.

The data management aspect aside, storing and loading data like mob spawn points from flat files would create never-ending merge conflict nightmares for any server currently changing that information in their DB. I'll acknowledge that it'd be _possible_ to side load in a custom "replacement" lua table, but someone manually inputting a new lua table row in a secondary flat file is a lot more effort than updating the value in their local SQL db.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Oct 01, 2020 at 23:59:56_

----

Alright, well, I've already addressed some of the concerns that keep coming  up so I guess I'm not communicating well enough. I will drop this, as it's going nowhere.
