**Labels:**

merge ready



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 11, 2020 at 11:09:31_
_Originally opened as: project-topaz/topaz - Issue 708_

----

Rename setting to epoch from offset to hopefully clarify usage.
Adjust luautils function used with GM command.

Fixes issue #552

GM command `!timeoffset <offset>` will let you move around in time. Must zone for client to reflect changes. `!timeoffset 144` will take you an hour ahead, `timeoffset -144` will take you an hour back. Setting the conf setting to 1 will set the epoch to the farthest time back, making the client as far into the future as it can currently go. Setting the conf setting to current timestamp will set the time to 886/1/1 on Firesday. Anything greater than the current timestamp will set the date to 886/1/1 but will result in different day elements until current time is reached, on Firesday.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jun 11, 2020 at 18:34:40_

----

Good stuff, Cocosolos!

I do have questions about how this will impact existing servers who choose to use the epoch; there are a fair number of scripts which save dates for timeouts and such in charvars. Many use functions directly linked to the current vanadiel year/month/day. (ie "No String Attached" or "Chocobo On The Loose") Any such quests could be softlocked for such a period of time that the offset catches up with it's pre-change value.

Edit: Also, I don't see the GM !timeoffset script in this branch. :(


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 11, 2020 at 21:39:46_

----

Anything using lockouts based on Vana'diel time will be effected by changing the epoch setting in map.conf or usage of the `!timeoffset` command since functions such as `VanadielDayOfTheYear` return a timestamp of Vana'diel time. Lockouts based on real time or JP midnight are based on the time offset supplied in settings.lua and use real time timestamps. The `!timeoffset` command is an existing command that currently does nothing since this functionality was removed at some point. Real usage for the map.conf setting would be setting a "birth" date for your server so the in game clock makes sense compared to the dates mentioned for major events. The `!timeoffset` command is more useful for testing development based on Vana'diel time.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 12, 2020 at 23:32:39_

----

Talk to us about the removal/replacement of the time offset setting~!

edit: Nevermind, was discussed on the issue; the original setting didn't do what the comment implied it did.
