**Labels:**

reviewed



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 20, 2020 at 02:06:02_
_Originally opened as: project-topaz/topaz - Issue 1169_

----

Adds latent for target being specified mob family to of with mob ecosystem latent
- Also fixed max latent ID
- Also fixed missing latent ID in status.lua
- Also renamed plain text field currently unused anywhere, this is purely for human readability


<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


This was needed for my add effect rework to handled some items that only prov vs a single mob family instead of their ecosystem (which we already have a latent for. As soon as this makes its way to release, please update the effect-rework branch by pulling release into it) thank you.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 20, 2020 at 05:44:52_

----

Also, 
```
src/map/latent_effect_container.cpp: In member function ‘bool CLatentEffectContainer::ProcessLatentEffect(CLatentEffect&)’:
src/map/latent_effect_container.cpp:1120:35: error: ‘class CBattleEntity’ has no member named ‘m_Family’; did you mean ‘m_Immunity’?
             expression = PTarget->m_Family == latentEffect.GetConditionsValue();
                                   ^~~~~~~~
                                   m_Immunity
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 20, 2020 at 05:52:49_

----

i had start this in a diff branch which was where my test and build was at, then decided I needed it in release and missed a colon. _and also a whole block of code in another file, apparently! TEST IN THE BRANCH YOU PR FROM TEO. BAD TEO :newspaper_roll:_

~~all fixed~~ and comma'd


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 20, 2020 at 06:19:06_

----

will fix missing chunk in morning..


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 20, 2020 at 06:33:58_

----

Decided to just recast it and add family to the entity at a later time.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 20, 2020 at 06:55:11_

----

Thanks for battling with this when you should have been sleeping :)
