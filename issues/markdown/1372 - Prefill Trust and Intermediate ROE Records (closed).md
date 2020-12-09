**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Oct 16, 2020 at 05:30:30_
_Originally opened as: project-topaz/topaz - Issue 1372_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Need these for my trust branch - hitting level and speaking to ROE NPC when you have x sparks aren't implemented yet (I think?)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Oct 16, 2020 at 05:35:42_

----

I might recommend leaving them commented out until they're actually completeable, as their presence in the table is what allows people to take them. And just removing the `--` in a Trust branch commit when you are ready for them should still avoid any possible conflict issues from `release` if others want to work on other parts of the file.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 16, 2020 at 05:38:00_

----

Ah, I see what you mean!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 16, 2020 at 09:31:43_

----

_Ooof_

At this point in `roe_records` life, changing the already consistent style to something else is too much of a pain in the ass. While I've personally seen the benefit of all this data being in a flexible lua table that we can refresh, I don't think it should _always_ be that way. Since it is a somewhat static (but large) set of data I'd like to one day see it plopped into the db. 

How that happens in the future is anyone's guess. Thats a problem for future developers.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Oct 16, 2020 at 14:28:23_

----

if someone can offer of a way of storing something as highly varied as RoE record data in a db without it turning into a nightmare, I'm all ears. (Look at the magian table for just a tiny taste of that life.) Particularly records that don't behave like all the other records (take/deal damage, complete X mission, timed/scheduled 4-hour records, etc.) Plus the fact that records can have arbitrary number of requirements... Do we just make 6 requirement columns and hope that's enough? One row per requirement and have thousands of more rows? 

I also don't feel the overhead of using a Lua table is as high as may be indicated.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Oct 16, 2020 at 14:54:34_

----

PS. use vim! I can fix the table pretty quick if it's that bothersome. I was under the impression that same-line open braces were pretty standard Lua style but I see that it's in the new style guide for Lua too.
