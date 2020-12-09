**Labels:**

crafting



<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Sunday May 31, 2020 at 11:51:58_
_Originally opened as: project-topaz/topaz - Issue 671_

----

The Fishing GP menu does not purchase the correct items as is in Master. I've been able to resolve almost all of the items except Robber Rigs, the first selection in the GP menu, by making the edit below to scripts\zones\Port Windurst\npcs\Fennella.lua :


local items = {
    [1] = {
        id = 17002, -- Robber's Rig
        rank = 3,
        cost = 1500
    },
    [0] = {
        id = 15452, -- Fisherman's Belt
        rank = 4,
        cost = 10000
    },
    [1] = {
        id = 14195, -- Pair of Waders
        rank = 5,
        cost = 70000
    },
    [2] = {
        id = 14400, -- Fisherman's Apron
        rank = 7,
        cost = 100000
    },
    [3] = {
        id = 191, -- Fishing hole map
        rank = 9,
        cost = 150000
    },
    [4] = {
        id = 340, -- Fisherman's Signboard
        rank = 9,
        cost = 200000
    },
    [6] = {
        id = 3670, -- Fish and Lure
        rank = 7,
        cost = 50000
    },
    [7] = {
        id = 3330, -- Fishermen's Emblem
        rank = 9,
        cost = 15000
    }
};


I have tried changing the value for Robber Rig, with no correction of the behavior. The topaz console throws this error:
[Error] luautils::onEventUpdate: .\scripts/globals/crafting.lua:279: attempt to index local 'i' (a nil value)

 That section referenced appears to deal with HQ crystals, which are the first options in other crafting GP menus.

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 


