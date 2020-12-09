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
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 04:45:13_

----

Shouldn't need this.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday May 28, 2020 at 06:19:49_

----

TODO: Remove these, these are set inside the constructor of CTrustEntity


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 03:45:47_

----

Should this be added to the battlefield status as well?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 04:06:59_

----

Also these should be `target:getObjType()` not `player:getObjType()`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Jun 03, 2020 at 06:30:52_

----

Good catch, thanks!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:04:59_

----

Does this forcible despawn happen when the status is granted?

What fights does this apply to?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:11:40_

----

I worry that NOT_HAS_ENMITY might be confused for not having _any_ enmity. Uncertain about best descriptor. NOT_MOB_TARGET is the best I've got.

NOT_ENEMY_TARGET?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:14:09_

----

According to bgwiki, Volker uses a weaponskill which gives beserk, not the actual JA


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:17:15_

----

👀 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:18:00_

----

Maybe comment out the printf so people running canary won't complain about message spam when trusts are summoned.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:26:14_

----

TODO: Enum class the triggers 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:27:08_

----

Why the distance check change?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:33:59_

----

Dunno if we want to make the fact that this is for MP restoring WSes more explicit up front (if we _can_, I'm not certain), rather than assuming that it is if it's self-targetting. I was a little confused upon first seeing the `addMP`.

If we can't check explicitly, maybe a comment next to the else, `else { // Self-targetting WS restoring MP`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Jun 05, 2020 at 19:45:08_

----

I was just going on the wikis:
https://ffxiclopedia.fandom.com/wiki/Confrontation


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Jun 05, 2020 at 19:45:28_

----

I see it, now that you mention it


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Jun 05, 2020 at 19:46:15_

----

AddFullGambit isn't used at the moment, and I think its too arcane for anyone to try, so this isn't called


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Jun 05, 2020 at 19:46:48_

----

For vague spell range, there were reports of Kupipi spamming buffs because someone was out of landable range


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:58:48_

----

Wiki feels off. Are trusts despawned when spawning a Dynamis zone boss?

@project-topaz/researcher if anyone feels like running in and popping one


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 20:01:30_

----

Oh, I thought that addSimpleGambit was using `build_gambit`, nevermind~


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jun 06, 2020 at 07:48:42_

----

Recurse all the things! 
This is probably over-engineered BS, considering the depths and possible shapes of tree that are possible.
I'll swap this out for something iterative down the line


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 27, 2020 at 21:13:32_

----

Vid from cloudchief as of the 5th of June says no
https://youtu.be/97QYZQxY9dA?t=2331


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 04:45:13_

----

Shouldn't need this.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday May 28, 2020 at 06:19:49_

----

TODO: Remove these, these are set inside the constructor of CTrustEntity


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 03:45:47_

----

Should this be added to the battlefield status as well?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 04:06:59_

----

Also these should be `target:getObjType()` not `player:getObjType()`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Jun 03, 2020 at 06:30:52_

----

Good catch, thanks!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:04:59_

----

Does this forcible despawn happen when the status is granted?

What fights does this apply to?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:11:40_

----

I worry that NOT_HAS_ENMITY might be confused for not having _any_ enmity. Uncertain about best descriptor. NOT_MOB_TARGET is the best I've got.

NOT_ENEMY_TARGET?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:14:09_

----

According to bgwiki, Volker uses a weaponskill which gives beserk, not the actual JA


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:17:15_

----

👀 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:18:00_

----

Maybe comment out the printf so people running canary won't complain about message spam when trusts are summoned.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:26:14_

----

TODO: Enum class the triggers 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:27:08_

----

Why the distance check change?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:33:59_

----

Dunno if we want to make the fact that this is for MP restoring WSes more explicit up front (if we _can_, I'm not certain), rather than assuming that it is if it's self-targetting. I was a little confused upon first seeing the `addMP`.

If we can't check explicitly, maybe a comment next to the else, `else { // Self-targetting WS restoring MP`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Jun 05, 2020 at 19:45:08_

----

I was just going on the wikis:
https://ffxiclopedia.fandom.com/wiki/Confrontation


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Jun 05, 2020 at 19:45:28_

----

I see it, now that you mention it


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Jun 05, 2020 at 19:46:15_

----

AddFullGambit isn't used at the moment, and I think its too arcane for anyone to try, so this isn't called


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Jun 05, 2020 at 19:46:48_

----

For vague spell range, there were reports of Kupipi spamming buffs because someone was out of landable range


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 19:58:48_

----

Wiki feels off. Are trusts despawned when spawning a Dynamis zone boss?

@project-topaz/researcher if anyone feels like running in and popping one


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jun 05, 2020 at 20:01:30_

----

Oh, I thought that addSimpleGambit was using `build_gambit`, nevermind~


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jun 06, 2020 at 07:48:42_

----

Recurse all the things! 
This is probably over-engineered BS, considering the depths and possible shapes of tree that are possible.
I'll swap this out for something iterative down the line


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 27, 2020 at 21:13:32_

----

Vid from cloudchief as of the 5th of June says no
https://youtu.be/97QYZQxY9dA?t=2331


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Jun 02, 2020 at 07:02:55_

----

@cocosolos this might need a re-review :sweat_smile: 
