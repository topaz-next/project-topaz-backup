**Labels:**



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Wednesday May 27, 2020 at 03:39:02_
_Originally opened as: project-topaz/topaz - Issue 658_

----

This fixes longstanding intermittent issues with Evening Mobs not spawning, not de-spawning, Day/Night Latents not always taking effect, guild shops not always restocking, and many more things which are dependent on reliable time-transition detections.

The long explanation of this problem is that the time_server runs based on a delay of 2400ms (one vanadiel minute), while the SyncTime() function uses the true system clock to generate the current Vanadiel Time. Since a delay-based sync cycle is variable given various system loads, conditions, and code execution, it will drift in and out of phase with the SyncTime() time generation, leading to vanadiel minutes periodically being skipped or repeated. If this skipped second was minute 0 of an hour, this would result in TOTD updates not firing.

TOTD updates are the only absolutely essential trigger based on this, and so should detect hour boundaries rather than "minute 0". I don't believe a rewrite of the clock mechanism is necessary or helpful, as the overall vanadiel timekeeping is still accurate; rather we just be cognizant of the granularity of its momentary accuracy.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #282


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 27, 2020 at 09:17:13_

----

Does this `if` still fire if we're assigning `lastTickedHour` to be `m_vHour` right before checking if the current hour is our (just-assigned) `lastTicked` hour plus one?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday May 27, 2020 at 13:50:26_

----

Hey @ibm2431 ! It will, because I've declared `lastTickedHour` as static. Static variables are only initialized once the first time they're declared, and will have indefinite lifespan like globals do, but they still maintain local scope. I selected static rather than a class variable since this variable never needs to be used outside of this local function. :)

*Edit:* I felt I should clarify that this means line 199 only does something the first run-through.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday May 27, 2020 at 19:07:21_

----

I actually had this same question lol. So the declaration happens once, then the reassignment happens every time?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday May 27, 2020 at 19:21:23_

----

The declaration and assignment happens only once. Basically, after the first pass, line 199 is inert and does nothing. The only time it'll be assigned is after the following `if` statement is true, since I have an assignment statement in there.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday May 27, 2020 at 19:47:32_

----

Yeah I meant the assignment on line 202. Makes sense, thanks for clarifying! Good work.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 27, 2020 at 09:17:13_

----

Does this `if` still fire if we're assigning `lastTickedHour` to be `m_vHour` right before checking if the current hour is our (just-assigned) `lastTicked` hour plus one?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday May 27, 2020 at 13:50:26_

----

Hey @ibm2431 ! It will, because I've declared `lastTickedHour` as static. Static variables are only initialized once the first time they're declared, and will have indefinite lifespan like globals do, but they still maintain local scope. I selected static rather than a class variable since this variable never needs to be used outside of this local function. :)

*Edit:* I felt I should clarify that this means line 199 only does something the first run-through.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday May 27, 2020 at 19:07:21_

----

I actually had this same question lol. So the declaration happens once, then the reassignment happens every time?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday May 27, 2020 at 19:21:23_

----

The declaration and assignment happens only once. Basically, after the first pass, line 199 is inert and does nothing. The only time it'll be assigned is after the following `if` statement is true, since I have an assignment statement in there.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday May 27, 2020 at 19:47:32_

----

Yeah I meant the assignment on line 202. Makes sense, thanks for clarifying! Good work.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Wednesday May 27, 2020 at 05:19:17_

----

Such an annoying bug... such a seemingly simple fix... well done, sir.
