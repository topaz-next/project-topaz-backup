**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Apr 26, 2020 at 19:16:56_
_Originally opened as: project-topaz/topaz - Issue 530_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This has always seemed a little vestigial and I'd be interested to hear if anyone actually uses it


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 26, 2020 at 19:24:20_

----

Trivia:
Retail stopped supporting it ages ago but the bits are still in client and just so happen to work if we send the byte for the no longer used languages. 


No real reason to keep it, and we never did get around to supporting the Japanese one. All non-Asian languages can be put into the English server message without issue, but the Asian character set will come out trashed every time (SE uses a non-standard Shift JIS variant).




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 11:30:38_

----

Slapping a WIP label on this until you edit the title and/or say otherwise~!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday May 02, 2020 at 14:25:15_

----

Tested with `!updateservermessage`, all seems fine. Even with error (when I swap around to other branches), the error is just a single line log saying it couldn't find the file, so very safe to merge.
