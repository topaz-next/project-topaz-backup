**Labels:**

reviewed



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 11, 2020 at 00:44:49_
_Originally opened as: project-topaz/topaz - Issue 1497_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 11, 2020 at 00:55:09_

----

Errata:
- Mentors may speak in these channels
- New players may speak in these channels, until such time as their new player status wears off (removing via the helpdesk menu does not remove access
- Returning players may speak in these channels, until 48 hours have passed
- For everyone else its just spam
- access is via `/assistj` and `/assiste` have fun confusing them with the existing `/assist` command that has nothing to do with chat :+1: 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Nov 11, 2020 at 15:17:21_

----

Are all of those conditions enforced by the client? Or are we going to have to do something with them?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 11, 2020 at 15:41:54_

----

> Are all of those conditions enforced by the client? Or are we going to have to do something with them?

I would think at a min the 48 hr timer has to be purely server side and we’d want the rest enforced there anyway when we get around to full implementation because packets can be sent by tools. 

Right now the server ignores these because there is no case entry in the switch.
