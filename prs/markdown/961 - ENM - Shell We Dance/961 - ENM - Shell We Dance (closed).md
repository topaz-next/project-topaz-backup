**Labels:**



<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [m241dan](https://github.com/m241dan)**
_Sunday Aug 16, 2020 at 16:21:49_
_Originally opened as: project-topaz/topaz - Issue 961_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

The only thing missing is that the whole family of these mobs does not go into their shell like they are supposed to. It makes the BC a little easier than it should be but what can you do? Someone should make that mixin.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 20, 2020 at 16:58:14_

----

them sneaky tabs gotchu


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 20, 2020 at 17:01:06_

----

whitespace appears to have mixed tabs and spaces in same line here.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 18:30:30_

----

Is this the correct way to do this? I think this needs to be changed.
@TeoTwawki 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 20, 2020 at 19:35:17_

----

true immunity is a field in mob pools, don't add as a mod.

high resistance will be a mod but only put here if the mob is non-scripted and it affects all mobs using the pool (if its on mob, prolly belongs in the spawn mods if non-scripted)

you can tell apart resist from immunity by the log messages in retail. 

Regular old high resistance:
_"The \<player\> casts \<spell\>. \<target\> resists the spell."_

Immunity:
_"completely resists the spell"_

Job trait proc:
_"Resist!"_

Immunobreak (for completeness):
_"resists the spell"_
_"Immunobreak!"_


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 20, 2020 at 16:58:14_

----

them sneaky tabs gotchu


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 20, 2020 at 17:01:06_

----

whitespace appears to have mixed tabs and spaces in same line here.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 18:30:30_

----

Is this the correct way to do this? I think this needs to be changed.
@TeoTwawki 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 20, 2020 at 19:35:17_

----

true immunity is a field in mob pools, don't add as a mod.

high resistance will be a mod but only put here if the mob is non-scripted and it affects all mobs using the pool (if its on mob, prolly belongs in the spawn mods if non-scripted)

you can tell apart resist from immunity by the log messages in retail. 

Regular old high resistance:
_"The \<player\> casts \<spell\>. \<target\> resists the spell."_

Immunity:
_"completely resists the spell"_

Job trait proc:
_"Resist!"_

Immunobreak (for completeness):
_"resists the spell"_
_"Immunobreak!"_


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 14:43:37_

----

Rebased with Release and fixed the spell_list conflict created by adding the Puddings since submitting.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Aug 28, 2020 at 03:41:59_

----

not sure if the mixin should be implemented for this script now? they may have different properties, but figured i'd ask


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 12:06:39_

----

There is a very handy mixin you can copy/steal/appropriate that handles mobs going into a shell:
https://github.com/project-topaz/topaz/pull/989

EDIT: On closer inspection, this fight is Uragnites, the mixin is Uragnites... sounds like a match to me!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 12:02:13_

----

Merged into `feature/enm` and shifted around all the SQL required. Gonna open an issue for adding the Urganite mixin to the mobs. Thanks for the ENM!
