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
