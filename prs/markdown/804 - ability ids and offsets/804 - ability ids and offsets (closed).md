**Labels:**

merge ready



<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [illzbee](https://github.com/illzbee)**
_Friday Jul 03, 2020 at 18:14:10_
_Originally opened as: project-topaz/topaz - Issue 804_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 04, 2020 at 07:28:11_

----

Nice find!

For anyone (like me) coming here and seeing this 62 and thinking something is up, it's meant to be 62 and not 64:
https://github.com/project-topaz/topaz/blob/release/src/map/entities/charentity.h#L196


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:22:18_

----

Seems to be tab characters throughout these lists~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:24:51_

----

I appreciate the placeholders 😄 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:29:48_

----

Looks like some spacing issues in this file too


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:31:08_

----

Should this be TORNADO?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:32:00_

----

Can remove these `//#TODO: unoffset this` messages since the TODO has finally be fulfilled! 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:32:20_

----

One here too.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:54:35_

----

[Windower packet library has the following to say regarding these packets](https://github.com/Windower/Lua/blob/dev/addons/libs/packets/fields.lua#L3223):
> --0x0AA, 0x0AC, and 0x0AE are all bitfields where the lsb indicates whether you have index 0 of the related resource.

PVLV has the fields starting at 0x46, but Zeromus may have just copied us.

This solution pulls all the bits back by two bytes, which seems to make all the abilities line up with client expectations. But I'm not _100% positive_ if this is "proper" or if we should be messing with a LSB instead for certain action categories to deal with whatever wonky indexing the client is doing with the DATs.

@TeoTwawki might know more about DAT-indexing once the ID hits the client. I do know that all the IDs put in this PR align with what the server sends out on retail. But I don't know if our offset has just always been wrong (either an index shift, or intentionally so to align 0-based ID bits to the packet), or if it _should_ still be at 0x46 _with_ these IDs and we're missing a flag in the packet telling it which index to use. This signification may be related to the #663 family of issues; as while not part of the original quote in that issue, Thorny expounded further:
> it isn't just going to be a wrong table pull, their mapping is wrong but there are also some kind of bitflags to tell the game which table it's pulling from and they aren't documented anywhere


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Tuesday Jul 07, 2020 at 22:36:50_

----

It should thanks for finding that!


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:09:52_

----

removed


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:10:01_

----

removed


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:10:21_

----

all set on spelling


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:10:41_

----

took out tab keys


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:10:54_

----

took out tab keys


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:11:46_

----

no problem, am also working on those abilities XD


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 08, 2020 at 02:14:03_

----

> TeoTwawki might know more about DAT-indexing once the ID hits the client. I do know that all the IDs put in this PR align with what the server sends out on retail. 

@ibm2431 back when darkstar was a young project the offset used to make it match a dat we were grabbing the IDs from at that time, however I believe that SE has drastically changed that dat since that time and I fidn nothing matching the 16 offset now. Some other things that will not be affected by this PR are offset _elsewhere_ to match dats currently. The only reason I know of to do so is easy client extraction.

As far as I knew, the wrong mapping was us not having pets use pet abilities proper and instead having player ability trigger a mobskill. sending out wrong packet from our pets. If that's happening with other things as well, I was not made aware of it.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 04, 2020 at 07:28:11_

----

Nice find!

For anyone (like me) coming here and seeing this 62 and thinking something is up, it's meant to be 62 and not 64:
https://github.com/project-topaz/topaz/blob/release/src/map/entities/charentity.h#L196


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:22:18_

----

Seems to be tab characters throughout these lists~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:24:51_

----

I appreciate the placeholders 😄 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:29:48_

----

Looks like some spacing issues in this file too


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:31:08_

----

Should this be TORNADO?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:32:00_

----

Can remove these `//#TODO: unoffset this` messages since the TODO has finally be fulfilled! 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:32:20_

----

One here too.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 07, 2020 at 00:54:35_

----

[Windower packet library has the following to say regarding these packets](https://github.com/Windower/Lua/blob/dev/addons/libs/packets/fields.lua#L3223):
> --0x0AA, 0x0AC, and 0x0AE are all bitfields where the lsb indicates whether you have index 0 of the related resource.

PVLV has the fields starting at 0x46, but Zeromus may have just copied us.

This solution pulls all the bits back by two bytes, which seems to make all the abilities line up with client expectations. But I'm not _100% positive_ if this is "proper" or if we should be messing with a LSB instead for certain action categories to deal with whatever wonky indexing the client is doing with the DATs.

@TeoTwawki might know more about DAT-indexing once the ID hits the client. I do know that all the IDs put in this PR align with what the server sends out on retail. But I don't know if our offset has just always been wrong (either an index shift, or intentionally so to align 0-based ID bits to the packet), or if it _should_ still be at 0x46 _with_ these IDs and we're missing a flag in the packet telling it which index to use. This signification may be related to the #663 family of issues; as while not part of the original quote in that issue, Thorny expounded further:
> it isn't just going to be a wrong table pull, their mapping is wrong but there are also some kind of bitflags to tell the game which table it's pulling from and they aren't documented anywhere


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Tuesday Jul 07, 2020 at 22:36:50_

----

It should thanks for finding that!


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:09:52_

----

removed


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:10:01_

----

removed


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:10:21_

----

all set on spelling


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:10:41_

----

took out tab keys


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:10:54_

----

took out tab keys


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jul 08, 2020 at 00:11:46_

----

no problem, am also working on those abilities XD


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 08, 2020 at 02:14:03_

----

> TeoTwawki might know more about DAT-indexing once the ID hits the client. I do know that all the IDs put in this PR align with what the server sends out on retail. 

@ibm2431 back when darkstar was a young project the offset used to make it match a dat we were grabbing the IDs from at that time, however I believe that SE has drastically changed that dat since that time and I fidn nothing matching the 16 offset now. Some other things that will not be affected by this PR are offset _elsewhere_ to match dats currently. The only reason I know of to do so is easy client extraction.

As far as I knew, the wrong mapping was us not having pets use pet abilities proper and instead having player ability trigger a mobskill. sending out wrong packet from our pets. If that's happening with other things as well, I was not made aware of it.
