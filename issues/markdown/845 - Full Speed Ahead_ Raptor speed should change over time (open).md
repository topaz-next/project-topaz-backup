**Labels:**

good first issue



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Jul 14, 2020 at 06:33:26_
_Originally opened as: project-topaz/topaz - Issue 845_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behaviour) **:** 

Once this PR goes in:
https://github.com/project-topaz/topaz/pull/774

- [Good First Issue][Core] Quest: Full Speed Ahead! raptor doesn't slow down as it runs out of pep
Mount speed is hard-coded, and needs to be modifiable (through mods or otherwise) for Full Speed Ahead!
battleentity.cpp
```cpp
uint8 CBattleEntity::GetSpeed()
{
    return (isMounted() ? 50 + map_config.speed_mod : std::clamp<uint16>(speed * (100 + getMod(Mod::MOVE)) / 100, std::numeric_limits<uint8>::min(), std::numeric_limits<uint8>::max()));
}
```

Also the speed is linked to variables in the minigame, like pep... or something...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Nov 10, 2020 at 06:49:17_

----

This should be easy to handle, now that https://github.com/project-topaz/topaz/pull/1192 is in
