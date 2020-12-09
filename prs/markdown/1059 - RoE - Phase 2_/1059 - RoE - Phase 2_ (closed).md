**Labels:**

approved

reviewed



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Saturday Sep 05, 2020 at 02:37:57_
_Originally opened as: project-topaz/topaz - Issue 1059_

----

Where to even begin with this one?? This update has something for everyone, and beyond this point it's mostly a matter of adding more records. The core system should support all future phase 3 development desires. This leans into the more Lua-forward design methodologies under development through other PRs (1 short entry in the Lua table is very often all that's needed to completely implement a record.) while also allowing Core handling of trigger events and determining callback eligibility for greatest performance.

### What's new?!
- Highly flexible and Core RoE record + check handling system (roeutils)
- Dynamic (and optional) registration and automatic calling of record check functions from Core based on trigger conditions.
- ~~36~~ 54 new records of various types
- Records implemented in Lua are automatically tracked by Core, and unimplemented records can no longer be taken. (Message will be displayed saying so, with the record # if you want to help add it yourself)

#### What's adding a record look like?
Every record must have an entry in the `tpz.roe.records` table or players won't be able to take it; Core is called to scrub this table to determine which records are available. Even a minimal entry is sufficient, and all values are optional. Here's one table entry as an example.
```lua
    [71  ] = { -- Spoils - Fire Crystals
        trigger = triggers.lootitem,
        goal = 10,
        reqs = { itemid = set{ 4096 } },
        reward = { sparks = 200, xp = 1000, unity = 20, repeatable = true },
    },
```
**Trigger** - triggers are a way to register your record in core based on an event occurring. By selecting one, core will then call your function when a player *has* that trial active, and the appropriate event has actually occurred. This is optional, and many records which are manually handled through other Lua scripts and don't need core registration won't use one.
**Reqs** - Each key should be the name of a function in the tpz.roe.checks table. All must pass in order for the trial to be considered "successful" and any number of them (or none) can be specified.
**reward** - The only entry I consider "completely necessary". Table of reward parameters used when completed. See `completeRecord` in `roeutils` for all format options.
There are more additional parameters, support for custom inline/anon functions and default parameters available for advanced use.

#### Which records work?
It will tell you if you try and take records which aren't implemented and refuse, so try! The full list is anything in `tpz.roe.records` (roe.lua) but here's a few of the new ones:
- 95% of Combat (Wide Area)
- 100% of Combat (Region) -> Original Areas 2, (about 24 records)
- 33% of Spoils I -> (Loot crystals - 8 records)

#### And?
Probably a dozen more things I forgot to mention.
###### This space intentionally left blank





<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 15:12:20_

----

I... did not know this was possible...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 15:20:49_

----

I'm fine with this implementation, so no need to change it, but this would be a good place to use `std::variant`:
- All the types are the same size
- You're using a `type` key to pull out what you want and do different things in a switch in `roeutils::event(...)`
- Mabe everything is looking like a nail because I'm currently holding the `std::variant` hammer


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 15:21:35_

----

Surprised we didn't have this before


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 15:27:24_

----

I don't have much of a leg to stand on in this regard (see trust gambits), but this syntax is pretty funky.

Can we not just infer the type of the data in the datagram from the `ROE_WSKILL_USE` tag and cast it on the other side?

Also, the cast to MobEntity happens within event, so do you need to be doing it here?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 15:44:31_

----

~~I don't know what options you've explored for this, but how possible is it to move these sorts of lookups into the `Zone.lua` for these areas to reduce bloat?~~

I've now read the main post properly and understand why these are listed in here.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 07, 2020 at 16:52:08_

----

Hmm. I'm curious what seems funky about it? `event(EVENT, PLAYER, none/one/list of datagrams)`

We "could" infer the type based on the event but one of the considerations I was keenly aware of with this was that there will undoubtedly be edge-cases later which may need passing different data in different circumstances, even for the same event. This was a core design principle, and why these Datagram structures worked well since I can pass Lua any arbitrary number I wish. *This* time I wanted to pass just a mob, but I can foresee a circumstance exists where there are multiple locations where an event trigger needs to be called, but different data / extra data should be passed in one but not the other. Lua can handle extra params if desired.

To stop these calls from being even messier/completely onerous, I use overloaded constructors to dynamically generate the Datagrams, which are built and assign type based on the type of the payload object given. In 90% of cases I'm sure casting isn't necessary, but it's why I explicitly cast here. And why I was always keen to explicitly specify the cast to what I wanted in the calls, especially with entities, as a wrong entity type here could mean a wrong entity type passed to Lua. It is correct that the additional cast in `event` is superflous, though, so I can certainly remove that (I believe it was leftover from before the overloaded constructors.)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 07, 2020 at 16:55:32_

----

As the records list gets bigger, I may certainly part out the main record list into its own Lua file, (ala how Magian does) but for now the list was small enough. :+1: 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 07, 2020 at 17:01:49_

----

Ha ha, noted. In a future phase, type-safing `union` to `variant` may be prudent I just know and liked the struct/union paradigm; you reach for the tools you know best. :shrug: (Fee Fi Fo Fum, I smell C programmers!)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Sep 08, 2020 at 05:12:12_

----

Oh, upon re-reading I felt I should point out that the first argument to the RoeDatagram constructor isn't repeating the type; it's the key-name you'd like the data to have when it's passed to Lua. Thus allowing passing many objects of the same type, just with different keys.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 15:12:20_

----

I... did not know this was possible...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 15:20:49_

----

I'm fine with this implementation, so no need to change it, but this would be a good place to use `std::variant`:
- All the types are the same size
- You're using a `type` key to pull out what you want and do different things in a switch in `roeutils::event(...)`
- Mabe everything is looking like a nail because I'm currently holding the `std::variant` hammer


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 15:21:35_

----

Surprised we didn't have this before


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 15:27:24_

----

I don't have much of a leg to stand on in this regard (see trust gambits), but this syntax is pretty funky.

Can we not just infer the type of the data in the datagram from the `ROE_WSKILL_USE` tag and cast it on the other side?

Also, the cast to MobEntity happens within event, so do you need to be doing it here?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 15:44:31_

----

~~I don't know what options you've explored for this, but how possible is it to move these sorts of lookups into the `Zone.lua` for these areas to reduce bloat?~~

I've now read the main post properly and understand why these are listed in here.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 07, 2020 at 16:52:08_

----

Hmm. I'm curious what seems funky about it? `event(EVENT, PLAYER, none/one/list of datagrams)`

We "could" infer the type based on the event but one of the considerations I was keenly aware of with this was that there will undoubtedly be edge-cases later which may need passing different data in different circumstances, even for the same event. This was a core design principle, and why these Datagram structures worked well since I can pass Lua any arbitrary number I wish. *This* time I wanted to pass just a mob, but I can foresee a circumstance exists where there are multiple locations where an event trigger needs to be called, but different data / extra data should be passed in one but not the other. Lua can handle extra params if desired.

To stop these calls from being even messier/completely onerous, I use overloaded constructors to dynamically generate the Datagrams, which are built and assign type based on the type of the payload object given. In 90% of cases I'm sure casting isn't necessary, but it's why I explicitly cast here. And why I was always keen to explicitly specify the cast to what I wanted in the calls, especially with entities, as a wrong entity type here could mean a wrong entity type passed to Lua. It is correct that the additional cast in `event` is superflous, though, so I can certainly remove that (I believe it was leftover from before the overloaded constructors.)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 07, 2020 at 16:55:32_

----

As the records list gets bigger, I may certainly part out the main record list into its own Lua file, (ala how Magian does) but for now the list was small enough. :+1: 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 07, 2020 at 17:01:49_

----

Ha ha, noted. In a future phase, type-safing `union` to `variant` may be prudent I just know and liked the struct/union paradigm; you reach for the tools you know best. :shrug: (Fee Fi Fo Fum, I smell C programmers!)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Sep 08, 2020 at 05:12:12_

----

Oh, upon re-reading I felt I should point out that the first argument to the RoeDatagram constructor isn't repeating the type; it's the key-name you'd like the data to have when it's passed to Lua. Thus allowing passing many objects of the same type, just with different keys.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 05, 2020 at 05:30:08_

----

At a glance:
![image](https://user-images.githubusercontent.com/1389729/92298483-f92bad00-ef51-11ea-810b-356edf8d6254.png)



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Sep 08, 2020 at 15:47:56_

----

Clang-formatted and Lua variables renamed. Did a quick compile-n-check and *hopefully* didn't miss anything; there's really no comprehensively good refactor tools for Lua.
