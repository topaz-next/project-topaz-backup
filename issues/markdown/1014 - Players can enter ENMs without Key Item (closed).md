**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Aug 27, 2020 at 21:00:01_
_Originally opened as: project-topaz/topaz - Issue 1014_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Only one player needs to have the key item to begin the ENM, and the rest can join with or without one.  This allows a full party to do the same ENM as many times as they have party members, a pure exploit.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Aug 28, 2020 at 06:15:06_

----

**More information**

https://ffxiclopedia.fandom.com/wiki/Category:ENM

Is this as simple as adding an entry to `bcnm.lua` for each offending ENM?

Registrant checking
```lua
    -- Definition
     { 3,  643,    0},   -- Brothers (ENM) -- TODO: Chthonian Ray mobskill

    ...

    -- requirements to register a battlefield
    local registerReqs =
    {
        ...
        [ 643] = function() return ( player:hasKeyItem(tpz.ki.ZEPHYR_FAN) 
        ...
    }

    ...

    -- requirements to enter a battlefield already registered by a party member
    local enterReqs =
    {
        -- No entry for 643
    }
```

So, adding `[ 643] = function() return ( player:hasKeyItem(tpz.ki.ZEPHYR_FAN) `  to `enterReqs ` would run that check on other party members.

Inside the BCNM in this case, removing the KI is already handled for everyone:
```lua
function onBattlefieldEnter(player, battlefield)
    if player:hasKeyItem(tpz.ki.ZEPHYR_FAN) then
        player:delKeyItem(tpz.ki.ZEPHYR_FAN)
    end
end
```
