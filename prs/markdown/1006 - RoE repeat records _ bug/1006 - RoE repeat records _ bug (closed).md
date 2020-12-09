**Labels:**

reviewed



<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Apocarypse](https://github.com/Apocarypse)**
_Wednesday Aug 26, 2020 at 02:52:58_
_Originally opened as: project-topaz/topaz - Issue 1006_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR lays the framework for repeatable records, allowing the current record number 12 (kill 200 monsters) to properly repeat.
Also general fixes for bugs pointed out to me in discord.

Selecting Chain Mitts no longer gives Seer's Slacks in the spark shop
Fhelm Jobeizat's initial RoE quest dialogue now displays either 11,111 gil or player's current gil, whichever is higher.
Also added an independent exp modifier for RoE to global settings.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Aug 27, 2020 at 07:19:36_

----

Y'all got any of them Allman-style braces?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Aug 27, 2020 at 15:53:38_

----

Alright, but they're just so damned ugly! `</YouManiacsYouBlewItUp>`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 16:00:55_

----

```
Im
{
    ugly?
    ;_;
}
```

well now you hurt Curly's feelings. Meanie.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Aug 27, 2020 at 16:04:31_

----

```c++
    bool status = true;
    if (lua_gettop(L) > 2)
    {
        status = lua_tointeger(L, 3) != 0;
    }

    if (repeat)
    {
        charutils::SetEminenceRecordProgress(PChar, recordID, 0);
    }
    else
    {
        charutils::DelEminenceRecord(PChar, recordID);
    }
```

Now they can go surfing on all these waves!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 16:06:27_

----

![image](https://user-images.githubusercontent.com/6871475/91466853-b8e77300-e85d-11ea-8ca2-028f8b5a5edd.png)



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 16:07:57_

----

the only thing I really hate is when someone does half their conditionals one way and half the other:
```
if something
{
    stuff
}
else
    WHY AM I DANGLING
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 16:08:58_

----

this one of the special cases where we need the explicit comparison?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Aug 27, 2020 at 16:11:31_

----

I don't think so. Just a style choice? @Apocarypse 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Aug 27, 2020 at 16:16:50_

----

Maybe we can agree on 

```c++
if something
    { stuff }
else
    { I'm not dangling! }
```
:smirk: 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Aug 27, 2020 at 19:06:21_

----

Space these out please, then approval is nigh


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Aug 27, 2020 at 20:51:56_

----

Good improvement either way @TeoTwawki . Put it in the recent commit.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Aug 27, 2020 at 07:19:36_

----

Y'all got any of them Allman-style braces?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Aug 27, 2020 at 15:53:38_

----

Alright, but they're just so damned ugly! `</YouManiacsYouBlewItUp>`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 16:00:55_

----

```
Im
{
    ugly?
    ;_;
}
```

well now you hurt Curly's feelings. Meanie.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Aug 27, 2020 at 16:04:31_

----

```c++
    bool status = true;
    if (lua_gettop(L) > 2)
    {
        status = lua_tointeger(L, 3) != 0;
    }

    if (repeat)
    {
        charutils::SetEminenceRecordProgress(PChar, recordID, 0);
    }
    else
    {
        charutils::DelEminenceRecord(PChar, recordID);
    }
```

Now they can go surfing on all these waves!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 16:06:27_

----

![image](https://user-images.githubusercontent.com/6871475/91466853-b8e77300-e85d-11ea-8ca2-028f8b5a5edd.png)



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 16:07:57_

----

the only thing I really hate is when someone does half their conditionals one way and half the other:
```
if something
{
    stuff
}
else
    WHY AM I DANGLING
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 16:08:58_

----

this one of the special cases where we need the explicit comparison?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Aug 27, 2020 at 16:11:31_

----

I don't think so. Just a style choice? @Apocarypse 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Aug 27, 2020 at 16:16:50_

----

Maybe we can agree on 

```c++
if something
    { stuff }
else
    { I'm not dangling! }
```
:smirk: 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Aug 27, 2020 at 19:06:21_

----

Space these out please, then approval is nigh


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Aug 27, 2020 at 20:51:56_

----

Good improvement either way @TeoTwawki . Put it in the recent commit.
