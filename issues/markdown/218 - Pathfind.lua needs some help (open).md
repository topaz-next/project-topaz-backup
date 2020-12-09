**Labels:**

improvement



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:11_
_Originally opened as: project-topaz/topaz - Issue 218_

----

<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ShelbyZ](https://github.com/ShelbyZ)**
_Wednesday Mar 07, 2018 at 02:31 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4633_

----

Right now we are treating entity paths as an array of coordinates and the path finding library has to do extra work to deal with each set of 3 being a point (x,y,z) in the path:

```lua
local path =
{
    41.878349, -6.282223, 10.820915,
    42.088036, -6.282223, 11.867051,
    42.096603, -6.282223, 12.939011,
    42.104187, -6.282223, 17.270992,
    42.126625, -6.282223, 14.951096,
    42.097260, -6.282223, 10.187170,
    42.104218, -6.282223, 17.303179,
    42.128235, -6.282223, 14.767291,
    42.097534, -6.282223, 10.223410
};
```

Ideal set of changes:

- [ ] Rework Pathfind.lua to expect each entry in the supplied path objects are entities with (x,y,z)
- [ ] Ensure support for an entity reversing path when end is reached **works**
- [ ] Ensure PATHFLAGs still work
- [ ] Update NPC/Mob scripts with path logic to new path list format
- [ ] ~~Install bitcoin miner~~





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:13_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Wednesday Mar 07, 2018 at 07:29 GMT_

----

probably gonna redo navmesh implementation and see if we can use HNA* after we get collision meshes

