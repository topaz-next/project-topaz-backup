**Labels:**

merge ready



<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Omnione](https://github.com/Omnione)**
_Monday Apr 27, 2020 at 21:22:09_
_Originally opened as: project-topaz/topaz - Issue 539_

----

• Added the ability to cast mazurka in appropriate zones.
• Added effect flags to wear on action against mob and wear on mob hit.

This fixes issue #528

BRD Mazurka should be allowed in dungeons (and removal on hit or attack)
issued by @kaincenteno

<!-- place 'x' mark between square [X] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Apr 27, 2020 at 22:02:16_

----

Brilliant @Omnione  thank you :D


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 10:54:46_

----

All the additions check out, but I'm curious, where does the list of allowed zones come from? For example, I'm seeing that Newton Movapolis and Alzadaal Undersea Ruins are getting the flag, but Oldton Movapolis and Salvage zones aren't


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 11:43:38_

----

Well for starters i did not touch any SOA area's due to them not even been touched properly yet,
As for Oldton Movapolis, i must have missed that one, my bad, i wasn't too sure on salvage, i need more info to be confident on adding them, but the rest is from research and logic, i.e. if a zone leads to a bcnm you cannot use Mazurka, stuff like this is really hard to find info on, alot was from memory, i went to every zone in the game and assesed it, and made a judgment, while i cannot 100% say for certain these are correct, i feel they are right given the what each zone i added did not give me any reason to not allow Mazurka.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 12:07:30_

----

right gonna push Oldton


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 12:08:33_

----

That works for me! I don't see any additions that I think would be _wrong_ - was just wondering if a site had a chart I didn't know about.


----
<a href="https://github.com/kain"><img src="https://avatars3.githubusercontent.com/u/445250?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kain](https://github.com/kain)**
_Tuesday Apr 28, 2020 at 12:09:08_

----

Guys, can you, please, not tag me? Use @kaincenteno not @kain 


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 12:09:46_

----

I wish, this was hard to do, took all day to go through every zone and asses it, i looked everywhere.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 12:10:19_

----

Oh sorry kain, you are right i used the discord tag, so sorry


----
<a href="https://github.com/kain"><img src="https://avatars3.githubusercontent.com/u/445250?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kain](https://github.com/kain)**
_Tuesday Apr 28, 2020 at 12:11:04_

----

No problems! Thank you!


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Apr 28, 2020 at 14:58:49_

----

@UynGH can you check if mazurka is allowed inside bcnm areas? if u check 3 random bcnm areas and it works then most likely this restriction has been lifted


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Apr 28, 2020 at 17:57:46_

----

@kaincenteno do you mean inside a battlefield or just in the general zones like balga's dias, boneyard gully, etc?
can tag @project-topaz/researcher and i'll see it too, Nyu pointed me here to help :)


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Apr 28, 2020 at 19:06:28_

----

tested boneyard gully (in bcnm and out), jade sepulcher (same) and qu'bia arena inside bcnm, mazurka can be cast. 


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 19:27:12_

----

Thanks guys, ill update soon


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 29, 2020 at 00:44:46_

----

Is it  unblocked everywhere now? Maybe can do away with its zone flag altogether?


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 29, 2020 at 09:40:02_

----

I dont belive its everywhere but it like 90% of zones, just not places like moghouse, colosseum, and stuff like that.
