**Labels:**

reviewed



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Wednesday Nov 11, 2020 at 21:58:58_
_Originally opened as: project-topaz/topaz - Issue 1503_

----

Fixes Ready Recast timer would not add charges, and would sit at 0 charges
without ever refilling. Adds 1s recast timer to trigger charges and regular
refilling based on values in sql/abilities_charges.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 12:24:18_

----

Don't worry about the CI, it's just complaining about nothing:
```
Error: ;31m[Error] bind failed with error: 98
Error: Process completed with exit code 255.
```
