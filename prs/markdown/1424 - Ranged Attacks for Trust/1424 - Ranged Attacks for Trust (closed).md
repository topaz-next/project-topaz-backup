**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Oct 24, 2020 at 10:44:45_
_Originally opened as: project-topaz/topaz - Issue 1424_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**TODO**
- Ranged WS animations for Semih are messed up.

```
        [3487] = {['name']="Sidewinder",                     ['category']=11, ['id']=3487, ['animation']=429,  ['message']=185, },
        [3489] = {['name']="Stellar Arrow",                  ['category']=11, ['id']=3489, ['animation']=430,  ['message']=185, },
        [3490] = {['name']="Lux Arrow",                      ['category']=11, ['id']=3490, ['animation']=431,  ['message']=185, },
```

- Actionview shows the category, id, animation and message are all same between retail and my changes...
- Model is correct, capped from retail...

**DONE**
- Basic RA for trusts
- AI for Semih
- Trusts stop running are 3 ticks of being chased 💀
- I think I'm going to have to move all the RA stuff down into BattleEntity, it just makes sense. Even if it's stubbed.
- Sane damage and delay for RA
- Throwing support for Joachim
- Bindings to tell Trusts to use RA
```lua
    mob:addSimpleGambit(ai.t.TARGET, ai.c.ALWAYS, 0,
                        ai.r.RA, 0, 0) -- Try RA all the time, but bound by your weapon's delay
```



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 24, 2020 at 16:14:30_

----

> I think I'm going to have to move all the RA stuff down into BattleEntity, it just makes sense.

I'm surprised it already isn't. Do Goblin Ambushers currently not Ranged Attack?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 24, 2020 at 19:47:01_

----

There are 2 types of ranged attack mob type objects can use. one is a "real" ranged attack, the other is a mobskill faking a ranged attack. A case of SE having multiple devs who didn't communicate to each other how they implemented. In game on retail, you can tell them apart by how the message displays: 1 line of text with no line break, or 2.

_both_ types should be handled at battelentity imo.
