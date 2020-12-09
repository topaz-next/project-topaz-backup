**Labels:**



<a href="https://github.com/Mortium"><img src="https://avatars1.githubusercontent.com/u/4663812?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Mortium](https://github.com/Mortium)**
_Monday Jun 22, 2020 at 19:29:15_
_Originally opened as: project-topaz/topaz - Issue 757_

----

With the unlocked option 1 outpost teleport the following showed up in the menu but did not work:
Li'Telor, Kuzotz, Vollbow, Elshimo Lowlands, Elshimo Uplands. (Animation happens, no currency taken and no teleport)

With OP teleports unlocked option 2 you should have access to all including: Tu'Lia, Tavnazia

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Jun 22, 2020 at 19:46:55_

----

This part should already be behaving properly, all you've done is make it allow all outposts if the setting is either 1 or 2. Do you meet the minimum level requirement for the outpost? If so the problem may be in `tpz.conquest.teleporterOnEventFinish` or possibly `teleports.lua`.


----
<a href="https://github.com/Mortium"><img src="https://avatars1.githubusercontent.com/u/4663812?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Mortium](https://github.com/Mortium)**
_Monday Jun 22, 2020 at 19:50:43_

----

If you try to use it ingame, it does not work with the previous code. Like this it does. It only actually teleports to: Ronfaure, Zulkheim, Norvallen, Gustaberg, Derfland, Sarutabaruta, Kolshushu, Aragoneu, Fauregandi, Valdeaunia and Qufim Island regions. None of the above I posted will actually teleport you anywhere, they just show up on the list.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jun 22, 2020 at 19:50:48_

----

~~Sidenote: I’d really love somebody making the setting just cause the event to treat you as having these unlocked, instead of its present form of causing nee players to start with them unlocked.~~

~~But I’m able to teleport just fine with the current code, which had not changed in awhile.~~

Change I was talking about happened and I didn’t know/remember ¯\\\_(ツ)\_/¯



----
<a href="https://github.com/Mortium"><img src="https://avatars1.githubusercontent.com/u/4663812?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Mortium](https://github.com/Mortium)**
_Monday Jun 22, 2020 at 19:52:29_

----

> Sidenote: I’d really love somebody making the setting just cause the event to treat you as having these unlocked, instead of its present form of causing nee players to start with them unlocked.
> 
> But I’m able to teleport just fine with the current code, which had not changed in awhile.

This only applies to the unlocked options 1 or 2, not the new player no unlocked version.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Jun 22, 2020 at 19:54:10_

----

> Sidenote: I’d really love somebody making the setting just cause the event to treat you as having these unlocked, instead of its present form of causing nee players to start with them unlocked.

It should already be doing this. If you don't have the outpost (new players don't even with this setting) then it checks if the settings are enabled and just returns true.


----
<a href="https://github.com/Mortium"><img src="https://avatars1.githubusercontent.com/u/4663812?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Mortium](https://github.com/Mortium)**
_Monday Jun 22, 2020 at 19:56:27_

----

In settings there are 3 options:

UNLOCK_OUTPOST_WARPS = 0 -- Set to 1 to give starting characters all outpost warps.  2 to add Tu'Lia and Tavnazia.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Jun 22, 2020 at 19:57:39_

----

1 is only supposed to be all outposts except Tu'Lia and Tavnazia, the way this is being done allows all outposts with either 1 or 2, there is no difference.


----
<a href="https://github.com/Mortium"><img src="https://avatars1.githubusercontent.com/u/4663812?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Mortium](https://github.com/Mortium)**
_Monday Jun 22, 2020 at 19:58:52_

----

It does not work if you try it with the current code. The way I changed it, it actually does. :) Been tested.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Jun 22, 2020 at 20:00:28_

----

Ok but your fix is to change what the setting means, creating a redundancy with options 1 and 2, and disabling the option of allowing all teleports except Tu'Lia and Tavnazia.


----
<a href="https://github.com/Mortium"><img src="https://avatars1.githubusercontent.com/u/4663812?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Mortium](https://github.com/Mortium)**
_Monday Jun 22, 2020 at 20:02:14_

----

With option 1 Tu'lia and Tavnazia do not show up on the list at the NPC the way I fixed it, with option 2, it shows and allows Tu'Lia and Tavnazia.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jun 22, 2020 at 20:09:17_

----

> This only applies to the unlocked options 1 or 2, not the new player no unlocked version.

I know what the options are and was not at all commenting on what you did here. It just turns out the changes I wished for happened and I never got the memo.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Jun 22, 2020 at 20:10:45_

----

Those options show up in the list because of `getAllowedTeleports`, `hasOutpost` is only used in the event finish if you have those options enabled.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jun 22, 2020 at 20:16:45_

----

> Some servers are a bit more quality of life style like newer MMO's (like the one I play on as well) sp they do allow more freedom but the good thing is that there is the options at least.

what does that even have to do with what I said??

I dunno what you think you read but I guarantee you misunderstood


----
<a href="https://github.com/Mortium"><img src="https://avatars1.githubusercontent.com/u/4663812?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Mortium](https://github.com/Mortium)**
_Monday Jun 22, 2020 at 20:20:53_

----

> I dunno what you think you read but I guarantee you misunderstood

Possible, if so my apologies. 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Jun 23, 2020 at 05:06:38_

----

what happened her why did it get closed? =(
