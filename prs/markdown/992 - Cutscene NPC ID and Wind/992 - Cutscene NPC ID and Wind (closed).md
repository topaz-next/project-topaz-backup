**Labels:**



<a href="https://github.com/NiQ1"><img src="https://avatars3.githubusercontent.com/u/23407689?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [NiQ1](https://github.com/NiQ1)**
_Friday Aug 21, 2020 at 21:54:00_
_Originally opened as: project-topaz/topaz - Issue 992_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

1. Changed CS packet first argument to the NPC triggering the CS, which is how retail behaves (before it would set it to the player's char id, which would cause issues in some cases according to Teo). Kept a fallback to player char id if no NPC or NPC ID cannot be determined.

2. Fixed Windurst mission 3-2 (Written in the Stars) - When repeating it will now give the correct mission of obtaining 3 rusty daggers (before it would repeat the initial mission). Gate guards will also give the correct dialog.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 21, 2020 at 22:03:45_

----

> -- Note: Includes Topaz modifications which may be subject to Topaz license

since that's true for the entire project (anything not stuck under dsp's gpl is) is it really needed to say it in each file?


----
<a href="https://github.com/NiQ1"><img src="https://avatars3.githubusercontent.com/u/23407689?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NiQ1](https://github.com/NiQ1)**
_Friday Aug 21, 2020 at 22:12:24_

----

Well, I mainly wanted to mark the files. Some downstream servers apparently pull without thinking. This was mainly my way of pointing them to actual code which is not regular GPL.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 21, 2020 at 22:21:43_

----

maybe we do need to draw more attention to it, esp for servers that still don't pull but instead cherry pick or copy paste code (both of which they should not ever do but I digress). I'd prefer we somehow make it obvious at the commit level though.


----
<a href="https://github.com/kamajii7"><img src="https://avatars0.githubusercontent.com/u/13575698?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kamajii7](https://github.com/kamajii7)**
_Monday Aug 24, 2020 at 18:16:21_

----

I am pretty sure you don't need to add '== true' here. Lua assess the value is true and will continue. Also don't think you need the == 1 since the function getMissionRankPoints() already returns 1 or 0 which evaluates to true / false respectively. I could be wrong and I will let someone else correct me if I am. 

Nothing technically wrong here, just style things. 


----
<a href="https://github.com/NiQ1"><img src="https://avatars3.githubusercontent.com/u/23407689?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NiQ1](https://github.com/NiQ1)**
_Monday Aug 24, 2020 at 20:16:09_

----

> I am pretty sure you don't need to add '== true' here. Lua assess the value is true and will continue. Also don't think you need the == 1 since the function getMissionRankPoints() already returns 1 or 0 which evaluates to true / false respectively. I could be wrong and I will let someone else correct me if I am.
> 
> Nothing technically wrong here, just style things.

Regarding the ==true, you're correct of course. I preferred to write it this way just to be constant with other similar lines in the same files.
Regarding your second comment, I did not change the getMissionrankPoints() logic. I added a call to hasCompletedMission(), which returns a Boolean. I'm not very familiar with LUA to be honest so I wasn't even sure if casting Boolean to integer is allowed but I doubt it's not discouraged anyway.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 21, 2020 at 22:03:45_

----

> -- Note: Includes Topaz modifications which may be subject to Topaz license

since that's true for the entire project (anything not stuck under dsp's gpl is) is it really needed to say it in each file?


----
<a href="https://github.com/NiQ1"><img src="https://avatars3.githubusercontent.com/u/23407689?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NiQ1](https://github.com/NiQ1)**
_Friday Aug 21, 2020 at 22:12:24_

----

Well, I mainly wanted to mark the files. Some downstream servers apparently pull without thinking. This was mainly my way of pointing them to actual code which is not regular GPL.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 21, 2020 at 22:21:43_

----

maybe we do need to draw more attention to it, esp for servers that still don't pull but instead cherry pick or copy paste code (both of which they should not ever do but I digress). I'd prefer we somehow make it obvious at the commit level though.


----
<a href="https://github.com/kamajii7"><img src="https://avatars0.githubusercontent.com/u/13575698?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kamajii7](https://github.com/kamajii7)**
_Monday Aug 24, 2020 at 18:16:21_

----

I am pretty sure you don't need to add '== true' here. Lua assess the value is true and will continue. Also don't think you need the == 1 since the function getMissionRankPoints() already returns 1 or 0 which evaluates to true / false respectively. I could be wrong and I will let someone else correct me if I am. 

Nothing technically wrong here, just style things. 


----
<a href="https://github.com/NiQ1"><img src="https://avatars3.githubusercontent.com/u/23407689?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NiQ1](https://github.com/NiQ1)**
_Monday Aug 24, 2020 at 20:16:09_

----

> I am pretty sure you don't need to add '== true' here. Lua assess the value is true and will continue. Also don't think you need the == 1 since the function getMissionRankPoints() already returns 1 or 0 which evaluates to true / false respectively. I could be wrong and I will let someone else correct me if I am.
> 
> Nothing technically wrong here, just style things.

Regarding the ==true, you're correct of course. I preferred to write it this way just to be constant with other similar lines in the same files.
Regarding your second comment, I did not change the getMissionrankPoints() logic. I added a call to hasCompletedMission(), which returns a Boolean. I'm not very familiar with LUA to be honest so I wasn't even sure if casting Boolean to integer is allowed but I doubt it's not discouraged anyway.


----
<a href="https://github.com/NiQ1"><img src="https://avatars3.githubusercontent.com/u/23407689?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NiQ1](https://github.com/NiQ1)**
_Saturday Aug 22, 2020 at 16:43:41_

----

> Logic all looks good, but I have some style requests:
> C++: Allman style braces, please
> Lua: Check your indents
> 
> Then the real question is how to deal with:
> 
> ```lua
> -- Note: Includes Topaz modifications which may be subject to Topaz license
> ```
> 
> Currently, I don't really know at what level the TPZL applies and what the ramifications are for pullers and cherry-pickers of this code. I'm actively reading and trying to figure it out, but it's going to take some time still (even though you have patiently tried to explain to me at least 3 times).
> 
> After some reformatting, I'm happy for a staff to pull the trigger on this with these warnings in place and we'll figure it out later...

Good old Notepad++ tabs/spaces issue. Please let me know if there's something I missed.
About that comment - Note that it says "may" and does not clarify any further, as you've says that's still undecided. The comment is there just to mark the file so downstream servers know it may be subject to a license different than DSP's GPL. Nothing more.
