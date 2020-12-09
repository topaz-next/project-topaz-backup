**Labels:**



<a href="https://github.com/brianmask"><img src="https://avatars2.githubusercontent.com/u/33399423?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [brianmask](https://github.com/brianmask)**
_Sunday May 03, 2020 at 05:14:54_
_Originally opened as: project-topaz/topaz - Issue 576_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

change GetName() from packet_name to name
resolves #569 trust spells do not work on Linux


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 06:51:32_

----

Does the packetName still get sent in the packet to the client? As in if you cast `Trust: Selh'teus` does he pop on screen as `Selh'teus` or as `Selh_teus`/`Selh teus` ?

I think we need to do what allied mobs do, and have name and packetName as separate things, because both get used but for different purposes. Possibly this already happens because trusts are still mobs:
https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/src/map/entities/mobentity.h#L244

If there's nothing to worry about then just mark my comment as resolved. :)


----
<a href="https://github.com/brianmask"><img src="https://avatars2.githubusercontent.com/u/33399423?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [brianmask](https://github.com/brianmask)**
_Sunday May 03, 2020 at 13:00:02_

----

Looks like it's properly pulling in the display name for the client.  I just checked Selh'teus, and his punctuation is correct.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 06:51:32_

----

Does the packetName still get sent in the packet to the client? As in if you cast `Trust: Selh'teus` does he pop on screen as `Selh'teus` or as `Selh_teus`/`Selh teus` ?

I think we need to do what allied mobs do, and have name and packetName as separate things, because both get used but for different purposes. Possibly this already happens because trusts are still mobs:
https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/src/map/entities/mobentity.h#L244

If there's nothing to worry about then just mark my comment as resolved. :)


----
<a href="https://github.com/brianmask"><img src="https://avatars2.githubusercontent.com/u/33399423?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [brianmask](https://github.com/brianmask)**
_Sunday May 03, 2020 at 13:00:02_

----

Looks like it's properly pulling in the display name for the client.  I just checked Selh'teus, and his punctuation is correct.
