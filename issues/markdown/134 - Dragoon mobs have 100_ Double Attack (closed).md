**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:47_
_Originally opened as: project-topaz/topaz - Issue 134_

----

<a href="https://github.com/vickycat"><img src="https://avatars1.githubusercontent.com/u/9993832?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [vickycat](https://github.com/vickycat)**
_Monday Sep 05, 2016 at 20:18 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3353_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [X] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [X] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30160602_0

**_Server Version_** (type `revision` in game) **:**
c5249ca0d6d9d3ce34025fe6b0064f08827ca293

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

(DS Oldschool server)

Dragoon mobs are attacking with 100% double attack rate

Tested against:

Orcish Dragoon
Orcish Grunt (too low level to even have DA)
Maat (DRG)
Brook Sahagin




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:48_

----

<a href="https://github.com/abriasffxi"><img src="https://avatars1.githubusercontent.com/u/20671885?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [abriasffxi](https://github.com/abriasffxi)**
_Thursday Sep 08, 2016 at 21:09 GMT_

----

Hey vickycat 

I've actually done some work on this before but never bothered to finish up on it.  If you would like to put in the research that would be great so we could get it fixed.

It is not drg mob- it's actually related to the flag cmbSkill 1 in mob_pool

Any mob that has cmbSkill 1 will attack twice, as that is the setting that the server counts as a "monk" type attack (really h2h).  In all reality, cmbSkill is probably outdated and it needs no other values than 0 and 1, and should probably be isH2H.  Either way, if you run a query for mobs that have cmbSkill 1 (and aren't monks?  Check against the mjob and sjob in the same sql table)

The result of that query gave me ~250 mobs but I didn't bother to go through and check each one individually if they should or should not be  hand2hand.  This needs to be done for us to fix correctly.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:49_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 08, 2016 at 22:36 GMT_

----

abriasffxi its possible we might not need isH2H either. I'm not sure its universal but I think mobs that look like they use h2h but aren't really monks don't actually attack twice on retail to begin with. And we have a diff thing for multi hitters like Charybdis. (Gigas who are non monk but have no weapon in their model, only punch me once in retail).

The original intent of that column looks to be for setting what skill type the mobs attacks was. Its feeding it into `setSkillType()`. I don't know if that would have an impact on a mobs base attack or base accuracy (or if mobs even have "skill" with weapon types for their job) seems unlikely since we have columns for setting their stats elsewhere. I doubt retail calcs them that way either, when you think of all the blm mobs that can actually melee you pretty well and I think I recall reading tests on charmed pets that indicated all mobs non-jug mobs had the same basic dmg type but I can't find that forum thread now.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:50_

----

<a href="https://github.com/abriasffxi"><img src="https://avatars1.githubusercontent.com/u/20671885?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [abriasffxi](https://github.com/abriasffxi)**
_Monday Sep 26, 2016 at 09:35 GMT_

----

TT,

I think you're probably right on the damage type.

By default, on retail h2h mobs did attack twice.  However they had a higher
delay than normal mobs.  I remember leveling Nin in Kazham around 2004 and
it was a double edged sword; they took two shadows per attack but it was
also easy to get ichi up between attacks.  Beast men h2h (freaking
yagudo....) are the same.

https://m.youtube.com/watch?v=QEluIom5Ces

The only thing that really strikes me as contrary is that Maat, except for
maybe monk and ninja(?), only attacks once.

I propose we create a new column, baseAtkPerRnd, or something and migrate
the cmbSkill 1 to there and fix all those mobs, alter the h2h call in
battle entity to use that, and leave the cmbSkill stuff in place.  This
wouldn't work for special mobs (Charby) but should work for the rest.
Also propose moving the delay higher on h2h mobs.  I'll see if I can find a
source for typical delay.

Unless someone knows for sure we can blow out cmbSkill, which would be a
better option of course.

On Thu, Sep 8, 2016, 5:36 PM TeoTwawki notificationsgithub.com wrote:

> abriasffxi github/abriasffxi its possible we might not
> need isH2H either. I'm not sure its universal but I think mobs that look
> like they use h2h but aren't really monks don't actually attack twice on
> retail to begin with. And we have a diff thing for multi hitters like
> Charybdis. (Gigas who are non monk but have no weapon in their model, only
> punch me once in retail).
> 
> The original intent of that column looks to be for setting what skill type
> the mobs attacks was. Its feeding it into setSkillType(). I don't know if
> that would have an impact on a mobs base attack or base accuracy (or if
> mobs even have "skill" with weapon types for their job) seems unlikely
> since we have columns for setting their stats elsewhere. I doubt retail
> calcs them that way either, when you think of all the blm mobs that can
> actually melee you pretty well and I think I recall reading tests on
> charmed pets that indicated all mobs non-jug mobs had the same basic dmg
> type but I can't find that forum thread now.
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> github/DarkstarProject/darkstar - Issue 3353Darkstar Issue issuecomment-245763453,
> or mute the thread
> github/notifications/unsubscribe-auth/ATttjZcLOA50Mn503_cqWT-hRIQaGQ74ks5qoI31gaJpZM4J1TQD
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:52_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 26, 2016 at 22:41 GMT_

----

I'm a little late coming back to this.

> By default, on retail h2h mobs did attack twice. However they had a higher delay than normal mobs. I remember leveling Nin in Kazham 

The only stuff attacking twice around khazam are actual monks though, pretty sure. I was saying I wasn't sure about stuff thats not monk, but has no weapon in its model. My retail account isn't currently  active to go find one of these niche cases to check. And I don't remember about nin mobs either (I think nin tonberry etc only have 1 weapon/attack?). But my memory swears I remember a gigas with no weapon, that wasn't a monk.

We should def correct the delays in the meantime. 
Perhaps later change the cmbSkill column out like you suggested (baseAtkPerRnd) or remove it. We can use a mobmod to handle any non h2h multihitting like Charybdis, if we don't use a  column on that.

**disclaimer: I no longer remember wtf I was talking about between my previous post and this one. Or wtf we actually do for Charybdis currently.**




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:53_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Oct 26, 2016 at 22:44 GMT_

----

Nin varies (tonberries like you said, but also there's also ark angel HM)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:54_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 26, 2016 at 22:44 GMT_

----

I think Maat's fixed now, btw. He was being spawned before he was initialized or something like that, was randomly being nilled.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:56_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Friday Jan 27, 2017 at 18:50 GMT_

----

Rather than mobs having specific weapon skills, shouldn't the field just be a yes/no as to whether or not it attacks like h2h/dual wield? Though I wonder if the specific weapon skill affects the attack/accuracy of the mob when combined with the job...



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:57_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jan 28, 2017 at 02:23 GMT_

----

Hozu that or a field for the kind of multi hit they do (or zero for normal), depending on if we want it to cover situations like charybdis to or use a mobmod for that.

mob family system has a base acc for them so I think this skilltype silliness is only being used for type of phys damane and to determine 2 swings or not



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:58_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Jan 28, 2019 at 23:56 GMT_

----

Tying this issue to Darkstar Issue 5421 which fixed lots of dragoon mobs, though the underlying system probably still needs a'fixin'



----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Monday Mar 09, 2020 at 21:10:40_

----

Hello. Some of these issues were fixed but like Wren said there's an underlying issue still going on which is a duplicate of https://github.com/project-topaz/topaz/issues/9, https://github.com/project-topaz/topaz/issues/94 and https://github.com/project-topaz/topaz/issues/125 to some extent. Closing, thank you.
