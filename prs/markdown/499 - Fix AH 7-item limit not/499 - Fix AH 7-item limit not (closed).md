**Labels:**

merge ready



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Wednesday Apr 15, 2020 at 08:09:29_
_Originally opened as: project-topaz/topaz - Issue 499_

----

AH listing count is now checked at every sale,
and not just the cached value from the last time
player viewed their Sale History.

Fixes #86

As previously discussed, the limit is enforced on the client so there's no reason to make it a configurable value.
<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Apr 15, 2020 at 08:11:15_

----

This could also alleviate a common cause of #140, where players can list way too many items and overflow their mailboxes.


----
<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Wednesday Apr 15, 2020 at 10:02:01_

----

Not sure what the general consensus would be but, I know there are a good number of private servers that actually like the fact players can list more than 7 items (especially when the population is lower). Though this fix is definitely needed, I'm wondering if making a setting that would allow unlimited items to be listed would make things easier on a lot of the private servers who wish to run it that way.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 10:40:06_

----

+1 for wrapping this in a setting, where the default is retail behaviour. Otherwise looks good!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 12:03:41_

----

Unless its as simple as commenting something out, server owners would probably love a setting. I'm glad to see it finally getting fixed though. 

Seeing it required an additional query kind of tells me the original code structure could use some refactoring later.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Apr 15, 2020 at 14:12:14_

----

> +1 for wrapping this in a setting, where the default is retail behaviour. Otherwise looks good!

I agree, it would be handy to configure it and I had considered making it a config setting, the issue is that the client enforces the 7-item limit even if the server isn't. If the client ever learns there are 7 items or more in the history list, it won't allow any more to be posted.  Even previously, only the first 7 items of the "effectively unlimited" listings would be shown in the Sales History. From my understanding, the only proper way to do this would be to use a modified client which doesn't enforce the limit. 

Alternatively we could only show the last 6 listings to the client so it believes there's always room for one more. The issue with that is the listings become a 6-length FIFO window and any additional listings aren't shown and players can't see or cancel them. 

Third option we could remove the 7-item cap on the sales listing and just show them all. This should work, however the behaviour would still mirror the way it was; where if the player leaves the AH interface and comes back, or if they view sales history then the client forbids additional listings. This just feels buggy.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 14:59:10_

----

@Kreidos the client doesn't enforce its limit until the player views the history. this can then be reset by relogging or rezoning. If you don't look, the client will let you keep listing till you break AH (exceeding max number of a specific item, or max returnable items for the character).

There is also an addon for ahsita that bypasses this entirely.

I'm in favor of just getting the fix merged and worrying about how to make a setting after  if doing so is problematic in any way :+1: (as a server owner, I would just temporary roll back the change if I want infinity listings again, though an easy toggle is nice to have)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Apr 15, 2020 at 16:31:13_

----

> There is also an addon for ahsita that bypasses this entirely.

@TeoTwawki I wasn't aware such an easy client-side fix was available, any chance you could link which plugin that is?

I have made the value configurable but will need to test it when I get home. I'll push the new commit once I'm confident nothing blows up.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 16:41:02_

----

I shouldn't have said "bypasses". I just checked and all its doing is stopping the player from looking and tripping the client side check. the client doesn't apply its limit until we check the status of our current on sale items for some reason. I also thought this was on ashita's list but its not (though ahgo and instantah are - they allow using ah from anywhere and remove the delay in opening ah menus, respectively), which means I dunno where I got this from.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Apr 15, 2020 at 16:56:14_

----

That's unfortunate. Still, having it as-configurable-as-is-possible on the server end is probably good; someone may write a better client-side fix later.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Apr 16, 2020 at 01:17:02_

----

I've tested and pushed the new commit which makes it configurable. 

The existing client-side issues (blocking beyond 7 after viewing history, and history only showing the first 7 even when more are in the system.) will still be present if values above 7 are used. In testing, it wasn't possible to show more than 7 items in the AH Sale Status screen even if they exist in the DB, the client just ignores them.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 16, 2020 at 03:11:20_

----

Random trivia: client limit of 7 is due to retails AH server crashing and them giving up on getting it working. They started at 10, went to 8, then 7 and called it quits and in more than 14 years never revisited the issue other than to make excuses pretending this did not happen when people ask for a slot increase. I was in game when they pulled the emergency maintenance for it both times.
https://giphy.com/gifs/reactionseditor-xUPGcl3ijl0vAEyIDK
