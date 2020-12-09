**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Oct 24, 2020 at 16:11:31_
_Originally opened as: project-topaz/topaz - Issue 1426_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Clang:
```
-Wlogical-not-parentheses
Example: !PMob->getMobMod(MOBMOD_NO_DESPAWN) != 0

-Wenum-compare-switch
-Wabsolute-value
Using abs() on an unsigned value (negative isn't possible)

-Wtautological-constant-out-of-range-compare
Checking to see if a condition is true on a type where it isn't possible.  Example: is a uint8 larger than 10000?

-Wnon-virtual-dtor
-Wunused-lambda-capture
-Wmissing-field-initializers
-Wunused-private-field
-Wmissing-field-initializers
```




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Oct 28, 2020 at 05:42:39_

----

Closing for now, don't have time to do this audit :(
