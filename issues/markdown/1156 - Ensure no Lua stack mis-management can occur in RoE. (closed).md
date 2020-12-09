**Labels:**

approved

reviewed



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Friday Sep 18, 2020 at 15:34:08_
_Originally opened as: project-topaz/topaz - Issue 1156_

----

I've seen no issues in testing, but just so nobody can say it's RoE blowing the Lua stack (ala Canaria reports).

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 15:34:58_

----

I should probably also do this for trust stuff 👀 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Sep 18, 2020 at 15:38:34_

----

It might be good in future reviews if we suggest that all Lua functions which return no values to Lua clear the stack before returning for good measure? :shrug: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 18, 2020 at 15:42:22_

----

> 
> 
> It might be good in future reviews if we suggest that all Lua functions which return no values to Lua clear the stack before returning for good measure? shrug

we could..just..DO this? the whole time? we could have been wiping it instead of keeping track carefully of how much it went up/down? Up is down and down is up. Existence is meaningless. Everything I knew was wrong. The sky has fallen, it hit the directv dish and my moogle is freaking out that he can't watch the apocalypse in HD.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Sep 18, 2020 at 15:48:55_

----

> we could..just..DO this? the whole time? ...

I think this is really only an issue with functions called directly from C, as Lua itself should cleanup its own stack upon returning. In fact I'm not entirely sure how Lua would react to having the stack values it passed-in hosed clean by C++ before returning (never tried)... I should perhaps change that here.

Edit: Indeed. I tried and it doesn't always like when you do. I'm going to put a few extra checks to ensure nothing gets thrown out that shouldn't.
