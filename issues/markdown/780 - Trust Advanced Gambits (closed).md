**Labels:**

focus



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Jun 28, 2020 at 12:29:26_
_Originally opened as: project-topaz/topaz - Issue 780_

----

Behold, spaghetti! 

This PR allows multiple predicates and actions inside a single gambit and makes the `addFullGambit` binding usable.

**Ayame Meditate (Multiple Predicates):**
```
    mob:addFullGambit({
        ['predicates'] =
        {
            {
                ['target'] = ai.t.SELF,
                ['condition'] = ai.c.TP_LT,
                ['argument'] = 1000,
            },
            {
                ['target'] = ai.t.MASTER,
                ['condition'] = ai.c.TP_GTE,
                ['argument'] = 1000,
            },
        },
        ['actions'] = 
        {
            {
                ['reaction'] = ai.r.JA,
                ['select'] = ai.s.SPECIFIC,
                ['argument'] = tpz.ja.MEDITATE,
            },
        },
    })
```

**Shantotto Magic Burst (Multiple Actions):**
```
    mob:addFullGambit({
        ['predicates'] =
        {
            {
                ['target'] = ai.t.TARGET,
                ['condition'] = ai.c.MB_AVAILABLE,
            },
        },
        ['actions'] = 
        {
            {
                ['reaction'] = ai.r.MA,
                ['select'] = ai.s.MB_ELEMENT,
            },
            {
                ['reaction'] = ai.r.MESSAGE,
                ['argument'] = tpz.trust.message_offset.SPECIAL_MOVE_1  -- Ohohoho!
            },
        },
    })
```

**Ayame define WSs:**
```lua
mob:setTPSkills({
       ['skills'] = {
            { ai.r.WS, tpz.ws.TACHI_ENPI, 0 },
            { ai.r.WS, tpz.ws.TACHI_HOBAKU, 0 },
            { ai.r.WS, tpz.ws.TACHI_GOTEN, 0 },
            { ai.r.WS, tpz.ws.TACHI_KAGERO, 0 },
            { ai.r.WS, tpz.ws.TACHI_JINPU, 0 },
            { ai.r.WS, tpz.ws.TACHI_YUKIKAZE, 0 },
            { ai.r.WS, tpz.ws.TACHI_GEKKO, 60 },
            { ai.r.WS, tpz.ws.TACHI_KASHA, 60 },
        },
        ['mode'] = ai.tp.CLOSER,
        ['skill_select'] = ai.s.HIGHEST,
    })
```
**TODO:**
Targetting needs to be fixed, it's currently a nightmare.
Action queueing
More helpful gambit parsing errors
Combine Simple and Full gambits into one binding (ie. Make the format for full gambit not crazy)

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Thursday Aug 27, 2020 at 18:58:53_

----

Approved! Microsoft disabled a lot of my function for github because I won't use Edge or Chrome... So I can't officially hit the button.
