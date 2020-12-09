**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 17:50:51_
_Originally opened as: project-topaz/topaz - Issue 1329_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

While I was working on the TOAU44 fix, I was using `instance:getEntryPos()` which gives back a table in the following form:
```lua
{
    x = xpos,
    y = ypos,
    z = zpos,
    r = rot,
}
```

setPos SHOULD take that as shown here:
https://github.com/project-topaz/topaz/blob/release/src/map/lua/lua_baseentity.cpp#L2732-L2752

But it was putting me through the floor.

I ended up using `setPos(table.x, table.y, table.z, table.r)` to skirt around the problem, but that isn't ideal


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Oct 11, 2020 at 18:00:15_

----

Looks like setPos only expects a plain list, or "numerically keyed" table. ie `{ xpos, ypos, zpos, rot }` and not the string-keyed tables which getEntryPos provides.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 22:06:01_

----

lua_rawgeti spaghetti did it


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 22:08:35_

----

Should be fixable using 
```cpp
        lua_getfield(L, 1, "x");
        posX = (float)lua_tonumber(L, -1);
        lua_getfield(L, 1, "y");
        posY = (float)lua_tonumber(L, -1);
        lua_getfield(L, 1, "z");
        posZ = (float)lua_tonumber(L, -1);
```
instead


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Oct 11, 2020 at 22:09:13_

----

I already rewrote a version of setPos to handle either numerical or string keys, however, in-so-doing it uncovered some problems with how pathfind.lua functions are written. (Since they are passed to setPos) The old lua_rawgeti didn't reveal these issues.

Here was my version if anyone feels like looking into it before I have time:

```c++
        lua_pushnil(L);
        while (lua_next(L, 1))
        {
            char key = lua_tostring(L, -2)[0];
            switch (key)
            {
                case '1':
                case 'x':
                    m_PBaseEntity->loc.p.x = (float)lua_tonumber(L, -1);
                    break;
                case '2':
                case 'y':
                    m_PBaseEntity->loc.p.y = (float)lua_tonumber(L, -1);
                    break;
                case '3':
                case 'z':
                    m_PBaseEntity->loc.p.z = (float)lua_tonumber(L, -1);
                    break;
                case '4':
                case 'r':
                    m_PBaseEntity->loc.p.rotation = (uint8)lua_tointeger(L, -1);
                    break;
            }
            lua_pop(L, 1);
        }
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 22:13:00_

----

yeah our path code has been failing to accept float values from our lua tables for a long while. https://github.com/project-topaz/topaz/commit/06758c41a7a94d4f51fbc8fff47c09be832cee51#diff-0af40b103e752b39d72d353b4907058e

(and instead of looking into why and fixing it, lazy Teo just gave Guivre a "good enough" non floating point set of coordinates)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Oct 11, 2020 at 22:16:30_

----

From what I see, the cause may be a misunderstanding of how Lua tables are passed as return values. They're passed by reference (as pointer to the table) and the table's variable and location are re-used between calls. We should be returning direct references to the parent table, not building new tables, as those intermediate tables are being modified right from underneath us by subsequent calls to the pathing functions..
