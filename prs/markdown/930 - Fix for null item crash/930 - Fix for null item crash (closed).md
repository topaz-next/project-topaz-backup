**Labels:**

approved



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Friday Aug 07, 2020 at 20:30:17_
_Originally opened as: project-topaz/topaz - Issue 930_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Regression of PR #857:
We cannot unequip a weapon (main / sub and range slots) without crashing the server



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Aug 07, 2020 at 20:39:12_

----

This if just contains another if... Which does the same as the else statement below... I think we can simplify this to just one if with no else statement at all.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 07, 2020 at 20:40:04_

----

`if ((PItem)` is the same as `if ((PItem != nullptr)` and I think has been the format the project has been favoring (someone correct me if I am wrong)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 07, 2020 at 23:10:13_

----

```c++
auto PWeapon = dynamic_cast<CItemWeapon*>(PItem)
if (PWeapon && PWeapon->getSkillType() != SKILL_STRING_INSTRUMENT && PWeapon->getSkillType() != SKILL_WIND_INSTRUMENT)
```
That's what was meant on discord about casting. I haven't tested that and it was suggested to me by a 3rd party


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Aug 07, 2020 at 23:16:25_

----

This would work too; minor change on such a small fix but a bit cleaner.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Aug 09, 2020 at 12:43:36_

----

+1 on this recommendation, a rare and beautiful possible use of `dynamic_cast`


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Aug 07, 2020 at 20:39:12_

----

This if just contains another if... Which does the same as the else statement below... I think we can simplify this to just one if with no else statement at all.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 07, 2020 at 20:40:04_

----

`if ((PItem)` is the same as `if ((PItem != nullptr)` and I think has been the format the project has been favoring (someone correct me if I am wrong)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 07, 2020 at 23:10:13_

----

```c++
auto PWeapon = dynamic_cast<CItemWeapon*>(PItem)
if (PWeapon && PWeapon->getSkillType() != SKILL_STRING_INSTRUMENT && PWeapon->getSkillType() != SKILL_WIND_INSTRUMENT)
```
That's what was meant on discord about casting. I haven't tested that and it was suggested to me by a 3rd party


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Aug 07, 2020 at 23:16:25_

----

This would work too; minor change on such a small fix but a bit cleaner.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Aug 09, 2020 at 12:43:36_

----

+1 on this recommendation, a rare and beautiful possible use of `dynamic_cast`
