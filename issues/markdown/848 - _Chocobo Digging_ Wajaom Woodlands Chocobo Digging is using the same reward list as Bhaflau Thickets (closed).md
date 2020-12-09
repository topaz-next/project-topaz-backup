**Labels:**



<a href="https://github.com/MrGideonWolfe"><img src="https://avatars0.githubusercontent.com/u/67240131?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MrGideonWolfe](https://github.com/MrGideonWolfe)**
_Tuesday Jul 14, 2020 at 16:59:54_
_Originally opened as: project-topaz/topaz - Issue 848_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [ ] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Chocobo digging in Wajaom Woodlands will result in receiving items that should be found in Bhaflau Thickets. After investigating on my side, I noticed that the rewards in chocobo_digging.lua are the same.

[tpz.zone.WAJAOM_WOODLANDS] = -- 51
    {
        {  770,  50, digReq.NONE    },
        { 2150,  60, digReq.NONE    },
        {  622, 197, digReq.NONE    },
        { 2155,  23, digReq.NONE    },
        {  739,   5, digReq.NONE    },
        {17296, 133, digReq.NONE    },
        {  703,  69, digReq.NONE    },
        { 2213, 135, digReq.NONE    },
        {  838,  21, digReq.NONE    },
        { 4096, 100, digReq.NONE    }, -- all crystals
        { 1255,  10, digReq.NONE    }, -- all ores
        {  688, 144, digReq.BURROW  },
        {  702,  14, digReq.BURROW  },
        {  690,  23, digReq.BURROW  },
        { 1446,   3, digReq.BURROW  },
        {  700,  14, digReq.BURROW  },
        {  699,  37, digReq.BURROW  },
        {  701,  28, digReq.BURROW  },
        {  696,  23, digReq.BURROW  },
        {  678,   9, digReq.BORE    },
        {  645,   3, digReq.BORE    },
        {  768, 193, digReq.BORE    },
        {  737,  22, digReq.BORE    },
        { 2475,   3, digReq.BORE    },
        {  738,   3, digReq.BORE    },
        { 4570,  10, digReq.MODIFIER},
        { 4487,  11, digReq.MODIFIER},
        { 4409,  12, digReq.MODIFIER},
        { 1188,  10, digReq.MODIFIER},
        { 4532,  12, digReq.MODIFIER},
    },
    [tpz.zone.BHAFLAU_THICKETS] = -- 52
    {
        {  770,  50, digReq.NONE    },
        { 2150,  60, digReq.NONE    },
        {  622, 197, digReq.NONE    },
        { 2155,  23, digReq.NONE    },
        {  739,   5, digReq.NONE    },
        {17296, 133, digReq.NONE    },
        {  703,  69, digReq.NONE    },
        { 2213, 135, digReq.NONE    },
        {  838,  21, digReq.NONE    },
        { 4096, 100, digReq.NONE    }, -- all crystals
        { 1255,  10, digReq.NONE    }, -- all ores
        {  688, 144, digReq.BURROW  },
        {  702,  14, digReq.BURROW  },
        {  690,  23, digReq.BURROW  },
        { 1446,   3, digReq.BURROW  },
        {  700,  14, digReq.BURROW  },
        {  699,  37, digReq.BURROW  },
        {  701,  28, digReq.BURROW  },
        {  696,  23, digReq.BURROW  },
        {  678,   9, digReq.BORE    },
        {  645,   3, digReq.BORE    },
        {  768, 193, digReq.BORE    },
        {  737,  22, digReq.BORE    },
        { 2475,   3, digReq.BORE    },
        {  738,   3, digReq.BORE    },
        { 4570,  10, digReq.MODIFIER},
        { 4487,  11, digReq.MODIFIER},
        { 4409,  12, digReq.MODIFIER},
        { 1188,  10, digReq.MODIFIER},
        { 4532,  12, digReq.MODIFIER},
    },
