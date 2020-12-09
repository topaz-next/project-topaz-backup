**Labels:**

crafting

hold



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Friday Jul 31, 2020 at 16:23:02_
_Originally opened as: project-topaz/topaz - Issue 914_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

(this is @ Tokenr on Discord, btw!)

Should solve:
Fixes https://github.com/project-topaz/topaz/issues/750
Fixes https://github.com/project-topaz/topaz/issues/875
and the first item of:
https://github.com/project-topaz/topaz/issues/22

The way the guild rank items are set up, the reset must happen on JP midnight, independant on server timezone.



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 31, 2020 at 16:32:30_

----

Not sure if we still want to show debug logs every hour once we're quite sure it works? :thinking: 


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Jul 31, 2020 at 18:15:20_

----

It's every day only


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 01, 2020 at 19:00:28_

----

a vana day is just shy of 1 earth hr.

Suggestion: -if- this is going to be kept even after we're sure it works, change it to ShowNotice, which will display the same but under a diff message type. we use that type for other "thing has happened" notifications in the log.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Aug 03, 2020 at 02:11:57_

----

This will only print when the server boots.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Aug 03, 2020 at 02:31:58_

----

Moving this call to here will call the update function every vanadiel day. It checks `CVanaTime::getInstance()->getSysYearDay()` so it's still going to be using the server timezone. It also refreshes all the guilds patterns, even if it didn't change, so creating a lot of work for no real end result. I think to get the result you want you would need to do something ~~like adding `luautils::GetSettingsVariable("TIMEZONE_OFFSET")` to the midnight check, but then you'd need to also deal with `guildutils::UpdateGuildPointPattern()` since it uses `CVanaTime::getInstance()->getSysYearDay()` as the server var.~~ else.

Edit: I misunderstood how TIMEZONE_OFFSET is used.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 04, 2020 at 01:40:09_

----

Didn't even notice we were talking about code in an initialization function.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 31, 2020 at 16:32:30_

----

Not sure if we still want to show debug logs every hour once we're quite sure it works? :thinking: 


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Jul 31, 2020 at 18:15:20_

----

It's every day only


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 01, 2020 at 19:00:28_

----

a vana day is just shy of 1 earth hr.

Suggestion: -if- this is going to be kept even after we're sure it works, change it to ShowNotice, which will display the same but under a diff message type. we use that type for other "thing has happened" notifications in the log.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Aug 03, 2020 at 02:11:57_

----

This will only print when the server boots.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Aug 03, 2020 at 02:31:58_

----

Moving this call to here will call the update function every vanadiel day. It checks `CVanaTime::getInstance()->getSysYearDay()` so it's still going to be using the server timezone. It also refreshes all the guilds patterns, even if it didn't change, so creating a lot of work for no real end result. I think to get the result you want you would need to do something ~~like adding `luautils::GetSettingsVariable("TIMEZONE_OFFSET")` to the midnight check, but then you'd need to also deal with `guildutils::UpdateGuildPointPattern()` since it uses `CVanaTime::getInstance()->getSysYearDay()` as the server var.~~ else.

Edit: I misunderstood how TIMEZONE_OFFSET is used.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 04, 2020 at 01:40:09_

----

Didn't even notice we were talking about code in an initialization function.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 31, 2020 at 16:34:59_

----

Looks good to me. If you want to add "Fixes" in front of the 2 issues mentioned in your description, GitHub will automatically close them when this merges. :)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 31, 2020 at 16:43:28_

----

Also, if I'm not mistaken I think the offset feature was removed due to "doing nothing" when the vanadiel epoch feature was implemented, so perhaps #22 could be marked Fixes as well.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 28, 2020 at 16:25:23_

----

Just so I and others don't forget, I mentioned to @jarmengaud on Discord that I've already written system-timezone-agnostic JST timekeeping functions, as my upcoming RoE Phase 3 work relies on correct JST time for doing daily/timed record scheduling. I will try to find time to clean up and PR that code separately so he can use it. Should make this fix as easy as moving 1 line of code from local midnight block to the new JST midnight one. (Or if we want, ditch the whole local midnight block entirely)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Sep 29, 2020 at 16:52:12_

----

Superseded by #1215
