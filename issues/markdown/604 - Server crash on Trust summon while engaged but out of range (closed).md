**Labels:**

bug



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday May 09, 2020 at 06:35:28_
_Originally opened as: project-topaz/topaz - Issue 604_

----

Is it ok to chime in here? On canary branch as of May 8th I get a critical bug when casting a trust while being engaged, but not aggroed yet (which is not a situation mentioned in the bug/TODO table:

- Engage a mob from out of aggro distance
- Cast trust

The topaz_game application will silently close.

What visually happens to the player:
- Infinite casting animation
- No trust appearing
- Not able to disengage or cast anything
- Disconnect

The client errors out with:
code: FFXI-4001

When trying to log back in, the client will throw an error on log in attempt:
- code FFXI-3305 Unable to connect...etc..

(I suppose naturally because topaz_game is not even running anymore?)

_Originally posted by @MarianArlt in https://github.com/project-topaz/topaz/issues/446#issuecomment-626097565_


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday May 09, 2020 at 06:42:13_

----

So, all the results are (as you say) because the topaz_game process has died.

I've built canary (09/05/2020) and everything works as expected, Trusts are summoned and chill next to you until you swing your melee weapon.

I would recommend you do a full rebuild and run a db update, then try again.

If the crash is still there, launch topaz_game with Visual Studio or attach Visual Studio to the already running process and try to grab some information about the crash for us :)

If you're hosting on Linux you'll need to attach GDB, but I'm a little rusty with that so you'd be better served asking for help in our Discord.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Saturday May 09, 2020 at 21:50:12_

----

I rebuilt today and I still get the same behavior. Although my main operating system is running Obarun (Arch) Linux I'm not running either server nor client from that OS but rather from a virtualized Windows 10 in VMware Workstation 15. I've had weird issues with running games in a virtual environment before, so who knows...

How do I attach Visual Studio to the process? Or how do I launch it accordingly for more verbose error logs?



----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Oct 10, 2020 at 04:35:15_

----

![image](https://user-images.githubusercontent.com/21246949/95645768-628e6680-0a90-11eb-9086-b45071050474.png)

Person who originally posted this issue has not been able to replicate, and believes it can close.
