**Labels:**



<a href="https://github.com/bope12"><img src="https://avatars0.githubusercontent.com/u/2702250?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [bope12](https://github.com/bope12)**
_Friday Oct 23, 2020 at 16:09:43_
_Originally opened as: project-topaz/topaz - Issue 1414_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Basic 2005 Harvest Festival event, all feedback is greatly welcome as I am going to be adding events as they come up in the year with content up to time permitting.
There is most likely easy ways to clean this up even more but I wanted to get this pr up before the start of the event on retail.
There are npc's that I did did not have captures of what their costumed look was so I made up based on the zones I did have they are marked with Missing in the zones ID file, I went with only 4 patrol paths one for each zone and two in waters as I did not know their exact paths but wanted them to at least wonder around some. Currently if you talk to a npc it will freeze them.
I included a new binding to change npc's look.size value as that was needed to change their look without requiring a sql change and reboot.
atPoint() was using float values and failed the check so I clamped the check to three decimal points allowing for paths not limited to whole digits.
pathfinds patrol method looks like it was meant to start from any point on the path so I cleaned it up to make that work


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 16:26:26_

----

That byte in the look value on these NPCs is not really size and we should stop calling it that.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 16:28:16_

----

check not check for != TYPE_PC instead, and then avoid having the empty conditional?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 16:30:46_

----

indents off


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 16:31:56_

----

brace spacing inconsistent. some lines got spaces, some didn't.
@zach2good whats our convention now for spacing?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 16:39:23_

----

inconsistency here trips my OCD. functions contents isn't indented, the comments aren't up to standard `-- space` instead of `--nospace` and while it may not technically be a problem having some be function contents and others not really throws me off reading it.

I'll let someone else weigh in because unfortunately my er..condition..causes me to zero in on formatting and miss the bigger picture, which isn't fair to you.


----
<a href="https://github.com/bope12"><img src="https://avatars0.githubusercontent.com/u/2702250?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [bope12](https://github.com/bope12)**
_Friday Oct 23, 2020 at 16:43:19_

----

It's all fair I'll fix up all that you mentioned when I get home tonight


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 16:26:26_

----

That byte in the look value on these NPCs is not really size and we should stop calling it that.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 16:28:16_

----

check not check for != TYPE_PC instead, and then avoid having the empty conditional?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 16:30:46_

----

indents off


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 16:31:56_

----

brace spacing inconsistent. some lines got spaces, some didn't.
@zach2good whats our convention now for spacing?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 16:39:23_

----

inconsistency here trips my OCD. functions contents isn't indented, the comments aren't up to standard `-- space` instead of `--nospace` and while it may not technically be a problem having some be function contents and others not really throws me off reading it.

I'll let someone else weigh in because unfortunately my er..condition..causes me to zero in on formatting and miss the bigger picture, which isn't fair to you.


----
<a href="https://github.com/bope12"><img src="https://avatars0.githubusercontent.com/u/2702250?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [bope12](https://github.com/bope12)**
_Friday Oct 23, 2020 at 16:43:19_

----

It's all fair I'll fix up all that you mentioned when I get home tonight
