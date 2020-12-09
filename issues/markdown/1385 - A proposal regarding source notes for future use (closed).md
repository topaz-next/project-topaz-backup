**Labels:**

good first issue

help wanted



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 17, 2020 at 22:19:39_
_Originally opened as: project-topaz/topaz - Issue 1385_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Often times we will find ancient notes regarding things that couldn't implemented in full [intended to help future contributors and developers.](https://github.com/zach2good/topaz/blob/cdece0618871ad8b813c83a3cfb9a44a8aed1e6c/src/map/packet_system.cpp#L926) The only issue with this is that it is also often not cleaned up [after the thing is implemented](https://github.com/project-topaz/topaz/blob/53a6d4b728ccf128e72134709ba39eb7b481db4c/src/map/lua/lua_baseentity.h#L508). I propose requiring a new issue each time one of these is added to the source, with the issue number in the comment. This will make the comment easily searchable when fixing the issue. Visual Studio has a feature where you can find [#TODO](https://github.com/project-topaz/topaz/blob/8648c4071c1885ad1a388d74e7f868e39df2f75e/src/map/ai/ai_container.cpp#L167) comments. so we could do:

```cpp
//#TODO should happen after y but z needs refactored before that can happen. See issue #12345
```
We could then grep for the issue in the source or windows folks can use visual studio's TODO tracking. And anybody can grep the todo's and see all of them that we have marked so far. Todo's can even be their own labeled issue type here on github which may even help some folks looking for particular things that need done.



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Oct 18, 2020 at 21:03:01_

----

I see the logic in this idea, but another part of me sees this as a lot of unnecessary paperwork; TODO: is recognized by basically every IDE and it's easy to get the list of TODOs. As long as the comment accompanying the TODO: is descriptive enough. :shrug: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 21:18:55_

----

@Kreidos right now we have many comments that do not as all include the keyword `TODO ` though Kreidos..I am trying to encourage its use here.
![image](https://user-images.githubusercontent.com/6871475/96386050-f255a400-1165-11eb-94cb-86bf8148784f.png)

Note it does not say TODO at all.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 21:20:11_

----

And Joe random contributor rarely knows this stuff.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Oct 18, 2020 at 21:20:46_

----

Whaaaa? Who wouldn't use TODO, those maniacs. Well in these cases, that's definitely an issue. :sweat_smile: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 21:22:01_

----

![image](https://user-images.githubusercontent.com/6871475/96386107-6db75580-1166-11eb-8c52-508e683ea962.png)



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 12:19:54_

----

It's very much busywork, but could we hunt down all of these lone "false TODOs" by searching for "needs", "future", "later", "right now" etc. 

And then mark them as actual TODO's?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 26, 2020 at 12:24:36_

----

Maybe. Worth a shot. I’d still like to start requiring ppl to use actual Todo and or make an issue for the thing they were missing to prevent future piles of long forgotten invalid comments. I mean I think we wanted ppl to make issues for the stuff they could not do in the prs anyway right? But I think even just having todo is fine as long as its a real todo that gets removed later when its done.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 26, 2020 at 23:10:09_

----

This sounds like it should definitely be added to the style guide as a general rule if you want to push it. (Which you both confirmed)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 27, 2020 at 04:52:19_

----

Added guideline about TODO messages:
https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#general-code-guidlines-all-languages
