**Labels:**

reviewed



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday May 22, 2020 at 05:59:53_
_Originally opened as: project-topaz/topaz - Issue 647_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I like to work out in the open and get feedback/help as soon as possible. 

This gives trusts the ability to use... abilities, calling the player scripts. It also gives each of the nation trusts something simple to. It also gives them the power to call player WSs.

I have converted the original `addGambit` into `addSimpleGambit` and added the more complex  `addFullGambit`, which is not in use yet.

Naji and Kupipi are still very much working!

```
    mob:addSimpleGambit(ai.t.TARGET, ai.c.ALWAYS, 0,
                        ai.r.JA, ai.s.SPECIFIC, tpz.ja.DESPOIL)
```


One day, for complex behaviours:
```
mob:addFullGambit(
{ -- Gambit
    {  -- Stage 1
        { -- Predicate(s) (AND)
            { ai.t.SELF, ai.c.TP_GTE, 1000 },
            { ai.t.TARGET, ai.c.NOT_SC_AVAILABLE, 0 }
        }, 
        { -- Action(s) (Dumb Chain)
            { ai.r.JA, ai.s.SPECIFIC, tpz.ja.BOOST },
            { ai.r.WS, ai.s.SPECIFIC, tpz.ws.BURNING_BLADE }
        }
    }, 
    { -- Stage 2
        { -- Predicate(s)
            { ai.t.SELF, ai.c.ALWAYS, 0 }
        }, 
        { -- Action(s)
            { ai.r.JA, ai.s.SPECIFIC, tpz.ja.WARCRY }
        }
    }, 
},
{
    -- options about when to bail out of chains etc.
    -- stage_break_on_fail = true/false (bail out of stage if a predicate/action fails)
    -- gambit_break_on_fail = true/false (as above, but for whole gambit) 
})
```


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Jun 02, 2020 at 07:02:55_

----

@cocosolos this might need a re-review :sweat_smile: 
