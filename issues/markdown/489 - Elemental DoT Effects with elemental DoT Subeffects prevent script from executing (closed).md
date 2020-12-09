**Labels:**

bug



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 23:33:07_
_Originally opened as: project-topaz/topaz - Issue 489_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**
- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
[Trying to set an effect with an ID of a elemental DoT, with a sub ID of any other elemental DoT](https://github.com/project-topaz/topaz/blob/0ada5cc5e43635984a9f9aa6d38a51cddd788d3c/scripts/globals/spells/burn.lua#L58) will cause the effect to fail to reach the lua script for the primary effect. This is true for having a sub with the same ID, _and_ any other ID in the elemental DoT family. Setting a sub ID of anything else causes the status to reach the effect script just fine.

Potential culprits:
- Container somehow seeing both the main and sub IDs as separate effects when [checking overwrite IDs](https://github.com/project-topaz/topaz/blob/0ada5cc5e43635984a9f9aa6d38a51cddd788d3c/src/map/status_effect_container.cpp#L283) while [attempting to "remove clean up" effects](https://github.com/project-topaz/topaz/blob/0ada5cc5e43635984a9f9aa6d38a51cddd788d3c/src/map/status_effect_container.cpp#L364-L365)

- [Effects getting deleted for being the same type](https://github.com/project-topaz/topaz/blob/0ada5cc5e43635984a9f9aa6d38a51cddd788d3c/src/map/status_effect_container.cpp#L371-L372)

Oddly enough, the base effect _does_ get saved to the spell container, in that if you attempt to cast an elemental DoT on the same target, it will fail, because the target already has the effect. The effect is being added, but it somehow doesn't reach and execute the effect file.





----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 12, 2020 at 17:02:24_

----

additional related problem I don't know if I should open a separate issue for: some monster skills use different dot amounts or status-down amounts than the player spells, but those are currently tied together in the status effect. I had started to try and separate those here back in darkstar
https://github.com/DarkstarProject/darkstar/commit/8ab295d9b4ec67e28752c4ecea29203314481a0f?w=1
but I never finished, and it looks like tehre have been changes in topaz since then.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Aug 30, 2020 at 00:01:47_

----

Reported as resolved by #565, closing.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Aug 30, 2020 at 10:48:41_

----

Bypassed. Not resolved.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Aug 30, 2020 at 14:36:16_

----

lets make a new issue about the subID screwing up, because dots are working and people will be confused thinking thats what needs fixed (which is why this was asked to be closed, since those work now)

edit: done, no need to reopen this one to edit it
