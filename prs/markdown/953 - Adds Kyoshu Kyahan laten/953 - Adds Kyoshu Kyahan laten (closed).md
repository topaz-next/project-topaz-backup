**Labels:**

hold



<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Saturday Aug 15, 2020 at 10:18:28_
_Originally opened as: project-topaz/topaz - Issue 953_

----

Adds Kyoshu Kyahan latent effects and new item latent mod for LATENT_STATUS_ACTIVE_NO_JOBSPECIAL for use when an item specifically does not work during SP. Core work for LATENT_STATUS_ACTIVE_NO_JOBSPECIAL by the ever helpful @TeoTwawki .

Kyoshu Kyahan:
https://ffxiclopedia.fandom.com/wiki/Kyoshu_Kyahan

> Latent Effect: Accuracy +20 Attack +20
> 
>     Active while using Footwork
>     Effect is cancelled during Hundred Fists, even if Footwork status is active.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Aug 18, 2020 at 13:40:29_

----

since this is currently only applicable on 100 fists, can we add that information to the definitions here and in status lua? otherwise people may try to use it to no effect.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 18, 2020 at 15:06:54_

----

Should we just add an effect flag to check against? I thought we had a way to tell if something was a 2hr already but I've been unable to locate it. We could nip it in the bud right now.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Aug 19, 2020 at 11:17:15_

----

Can we get a newline at the end here?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Aug 19, 2020 at 11:17:51_

----

Space after angle-bracket please


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Aug 19, 2020 at 11:18:07_

----

Thanks for aligning these!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Aug 19, 2020 at 11:20:46_

----

I think I agree with these guys; just making the all-SP change now will stop the TODO sitting there and rotting forever, especially because it isn't much extra work.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Aug 19, 2020 at 13:39:25_

----

@Era-Lusiphur example of using an effectflag:
https://github.com/project-topaz/topaz/commit/d099abc12c8f682520672f7c6acb7435f12857e3

adding the effectflag used above:
https://github.com/project-topaz/topaz/commit/53398a83daf8734319e98800723a1d60a61d88a0

So we could flag 2hr statuses, and then check the flag. alternatively you can check each status, or come up with a 3rd option - effectflag is just all I could think of to avoid a bunch of `||` to check multiple effects.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Aug 18, 2020 at 13:40:29_

----

since this is currently only applicable on 100 fists, can we add that information to the definitions here and in status lua? otherwise people may try to use it to no effect.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 18, 2020 at 15:06:54_

----

Should we just add an effect flag to check against? I thought we had a way to tell if something was a 2hr already but I've been unable to locate it. We could nip it in the bud right now.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Aug 19, 2020 at 11:17:15_

----

Can we get a newline at the end here?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Aug 19, 2020 at 11:17:51_

----

Space after angle-bracket please


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Aug 19, 2020 at 11:18:07_

----

Thanks for aligning these!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Aug 19, 2020 at 11:20:46_

----

I think I agree with these guys; just making the all-SP change now will stop the TODO sitting there and rotting forever, especially because it isn't much extra work.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Aug 19, 2020 at 13:39:25_

----

@Era-Lusiphur example of using an effectflag:
https://github.com/project-topaz/topaz/commit/d099abc12c8f682520672f7c6acb7435f12857e3

adding the effectflag used above:
https://github.com/project-topaz/topaz/commit/53398a83daf8734319e98800723a1d60a61d88a0

So we could flag 2hr statuses, and then check the flag. alternatively you can check each status, or come up with a 3rd option - effectflag is just all I could think of to avoid a bunch of `||` to check multiple effects.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 15, 2020 at 18:23:27_

----

Just a suggestion, you could turn this into two commits. One for the content and the second for the white space changes (including fixing the new white space misalignment by adding a well named but long new latent). The reason is this will help keep our history clean.

Otherwise, looks good to me (haven't tested myself, but I trust).


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Sunday Aug 16, 2020 at 04:26:51_

----

@m241dan Reduced latent mod name length to preserve original whitespacing. I think increasing the whitespace for just one line would reduce readability, so made the adjustment that way.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Aug 16, 2020 at 04:31:02_

----

@m241dan kinda my fault when I quick proof of concept'ed it last night my auto format made some adjustments which carried into the diff I handed off


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Aug 28, 2020 at 03:43:11_

----

do we want to merge and issue, or just get this done?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 28, 2020 at 04:29:42_

----

> do we want to merge and issue, or just get this done?

lets just add an effect flag, add said flag to the effects that 2hrs place on players. check for flag instead of for hundred wiffs.

Flags are as easy to add as mods. Easier..since you don't deal with collision baggage or duplication. [Example.](https://github.com/project-topaz/topaz/commit/a795e51e75d8ff344f73382522462f13af7bcd9f#diff-3207659a2e7b5decb0068fa2b4cb96bc)


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Monday Aug 31, 2020 at 16:16:57_

----

@Era-Lusiphur you want to take care of adding effect flag or do you need help?
