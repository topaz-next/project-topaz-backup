**Labels:**

focus

reviewed



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Mar 06, 2020 at 12:35:33_
_Originally opened as: project-topaz/topaz - Issue 405_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Shout out to @cocosolos for doing some testing and @Omnione for looking up the event arguments! I'll be able to sit down properly on Monday and work out the bugs. 

This is about as far as I can take this, I'm pretty busy at the moment. Hopefully this gives a little boost to whever wants to pick this up 👍 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 20:56:16_

----

Think `GOBBIE_BOX_MINIMUM_AGE` might be sufficient; comment explains that the value is in days~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 20:57:05_

----

Is this comment how the string is in POLUtils?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:06:58_

----

I know the dial variables are currently placeholders - so I'm noting for future development - but we might be able to combine and store all of these into a single bitmask.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:08:27_

----

And make these a combined lua bitmask setting later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:09:07_

----

Then we wouldn't need this variable and can throw the setting straight into the event.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:10:55_

----

Bonus points if you give the `startEvent` csids a variable instead in preparation of globalization~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:13:43_

----

(And if you go full variable now, don't forget the csids here and the `onEventFinish`)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:16:19_

----

Fairly certain that `updateEvent` drops `true` values~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:19:35_

----

Squished variables are sad variables, they need some social distance!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:47:39_

----

I'll note the print here before someone else does later


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Mar 16, 2020 at 22:34:54_

----

MIN instead of MINIMUM is enough to.  I was actually going with `MYSTERY_BOX_MIN_AGE` but I think GOBBIE is better now that I see it.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 20:56:16_

----

Think `GOBBIE_BOX_MINIMUM_AGE` might be sufficient; comment explains that the value is in days~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 20:57:05_

----

Is this comment how the string is in POLUtils?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:06:58_

----

I know the dial variables are currently placeholders - so I'm noting for future development - but we might be able to combine and store all of these into a single bitmask.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:08:27_

----

And make these a combined lua bitmask setting later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:09:07_

----

Then we wouldn't need this variable and can throw the setting straight into the event.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:10:55_

----

Bonus points if you give the `startEvent` csids a variable instead in preparation of globalization~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:13:43_

----

(And if you go full variable now, don't forget the csids here and the `onEventFinish`)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:16:19_

----

Fairly certain that `updateEvent` drops `true` values~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:19:35_

----

Squished variables are sad variables, they need some social distance!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:47:39_

----

I'll note the print here before someone else does later


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Mar 16, 2020 at 22:34:54_

----

MIN instead of MINIMUM is enough to.  I was actually going with `MYSTERY_BOX_MIN_AGE` but I think GOBBIE is better now that I see it.
