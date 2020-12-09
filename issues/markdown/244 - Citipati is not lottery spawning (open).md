**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:39_
_Originally opened as: project-topaz/topaz - Issue 244_

----

<a href="https://github.com/davismj"><img src="https://avatars2.githubusercontent.com/u/3845823?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [davismj](https://github.com/davismj)**
_Thursday Dec 06, 2018 at 06:22 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5442_

----

- [x] I have searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] Provided detailed steps to diagnose and resolve the issue.

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

1. Citipati is a lottery spawn off of Corses. Corses despawn at 04:00, triggering `phOnDespawn` for each Corse, allowing Citipati to spawn.
2. Additionally, Citipati will not despawn at 04:00 since he also has the `SPAWNTYPE_LOTTERYFLAG` which would skip [this if statement](github/DarkstarProject/darkstar/blob/master/src/map/zone_entities.cppDarkstar Issue L693) .
3. Finally, if the two above issues are fixed, then Citipati will despawn at 04:00, which will fire the [DESPAWN listener in `phOnDespawn`](github/DarkstarProject/darkstar/blob/master/scripts/globals/mobs.luaDarkstar Issue L69), causing Citipati's cooldown to restart.

I'm not sure if (3) is desired.

