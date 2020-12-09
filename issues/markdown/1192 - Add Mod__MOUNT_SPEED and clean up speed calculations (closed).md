**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Sep 26, 2020 at 08:14:32_
_Originally opened as: project-topaz/topaz - Issue 1192_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Minus mods to SPEED (and MOUNT_SPEED) would result in a speed of 0... Also, needed a way to tweak mount speed on the fly.

**Tested with**
```lua
-- Normal
!setmod 169 0 Test    -- No mod
!setmod 169 20 Test  -- +20% mod
!setmod 169 -20 Test -- -20% mod

-- Mounted
!setmod 972 0 Test    -- No mod
!setmod 972 20 Test  -- +20% mod
!setmod 972 -20 Test -- -20% mod
```
