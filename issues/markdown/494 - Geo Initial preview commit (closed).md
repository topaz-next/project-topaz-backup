**Labels:**

WIP

hold



<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 14, 2020 at 20:00:03_
_Originally opened as: project-topaz/topaz - Issue 494_

----

<!-- place 'x' mark between square [X] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR adds the basic functions for geo, including the auras or bubbles as some like to call them.
only spells available are as follows:
• indi-regen
• indi-poison
• indi-refresh
• geo-regen
• geo-posion
• geo-refresh

Abilities:
• Full Circle returns a fraction of mp based on the intial cost of the geo spell and luopans remaing HP

This is a WIP so feel free to test and make changes accordingly.

Credit to zach2good for making this possible and to actually move ahead.

NOTE: the animations when casting will look odd untill the mID for the bells are added if they are not added already.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 29, 2020 at 09:47:50_

----

You can mark this as a WIP if you want, seems i got alot of work to do on it.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 10:06:33_

----

I'd be okay with the _current_ targeting solutions put into a new GEO/aura branch!

My musing on performance improvements are for "before work is done to add more bubbles" not "before I'll hit the merge button"! You should know by now I'm usually a proponent of "if it's a lot of weight for one person, take the code off their hands to be worked on collaboratively later". 😉 

(And the one regarding the "reverse-enmity" container for players should be a new branch based on release _anyway_ so we can merge it into both GEO/aura _and_ trust.)


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 29, 2020 at 11:34:56_

----

I'll work on this some more if you want before you merge it, get some of the issues resolved


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 12:38:10_

----

If you want to do some of the easier things, I'll merge after you say "I'm satisfied for now". 😃 


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 29, 2020 at 12:53:58_

----

ok that sounds good


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 14:38:58_

----

Well i tried to rebase and squash commits, grr, damn git


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 14:46:30_

----

thats a bit cleaner, now i can actually work on this


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 14:59:15_

----

Quick note, this wont build until ive fixed some stuff, i made a few changes, so ignore that


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 11:00:14_

----

I'll change the labels to hold/WIP for now so others know you're still working on this!


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Monday May 11, 2020 at 18:57:08_

----

Aww man did the spell list change allready?, damn it


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday May 14, 2020 at 22:52:04_

----

finaly figured out the perpetuation per level cost, so thats all good now for each level, also the hp scale of the luopan.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 24, 2020 at 02:33:33_

----

Ok i think its ready for testing, have at it


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday May 26, 2020 at 13:02:05_

----

Have a few tweaks comming soon, including plates of indi spell item to learn the spells


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 22:42:52_

----

Can you split the .sql changes to a separate PR, I guess with status_effects.h as well. That way we can reserve this stuff on `release` and work on GEO in a feature branch.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jun 06, 2020 at 06:36:54_

----

Okay, this PR is now post-April only, targeting an already merged GEO branch from April, based off our release with most of the SQL/headers in it.

I'll do more butchering later to split bubbles, elemental magic, and abilities.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jun 08, 2020 at 05:12:51_

----

Pushed the final commit for splitting up the branch (geomancer abilities, merits, and adjustments). As the original work in April was merged into our geo branch, going to close this PR so the later work is all fresh new PRs and distinguished from the initial bubble PR.
