**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Aug 30, 2020 at 14:42:40_
_Originally opened as: project-topaz/topaz - Issue 1042_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
see #489
Elemental dots work currently, but it appears the underlying cause of the problem it had with the manner it was previously scripted has to do with a problem handling subIDs in the effect parameters in the core.

### ***This is not a problem specific to elemental DOTs, as those currently function.***
Just making sure nobody misses that. >.>

Quote from old issue:
> [Trying to set an effect with an ID of a elemental DoT, with a sub ID of any other elemental DoT](https://github.com/project-topaz/topaz/blob/0ada5cc5e43635984a9f9aa6d38a51cddd788d3c/scripts/globals/spells/burn.lua#L58) will cause the effect to fail to reach the lua script for the primary effect. This is true for having a sub with the same ID, _and_ any other ID in the elemental DoT family. Setting a sub ID of anything else causes the status to reach the effect script just fine.
> 
> Potential culprits:
> 
>  * Container somehow seeing both the main and sub IDs as separate effects when [checking overwrite IDs](https://github.com/project-topaz/topaz/blob/0ada5cc5e43635984a9f9aa6d38a51cddd788d3c/src/map/status_effect_container.cpp#L283) while [attempting to "remove clean up" effects](https://github.com/project-topaz/topaz/blob/0ada5cc5e43635984a9f9aa6d38a51cddd788d3c/src/map/status_effect_container.cpp#L364-L365)
> 
>  * [Effects getting deleted for being the same type](https://github.com/project-topaz/topaz/blob/0ada5cc5e43635984a9f9aa6d38a51cddd788d3c/src/map/status_effect_container.cpp#L371-L372)
> 
> 
> Oddly enough, the base effect _does_ get saved to the spell container, in that if you attempt to cast an elemental DoT on the same target, it will fail, because the target already has the effect. The effect is being added, but it somehow doesn't reach and execute the effect file.



----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Sunday Aug 30, 2020 at 16:43:57_

----

Twas my bad for not understanding the underlying cause I suppose
