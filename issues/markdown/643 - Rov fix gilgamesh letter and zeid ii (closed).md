**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday May 19, 2020 at 03:46:43_
_Originally opened as: project-topaz/topaz - Issue 643_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

gilgamesh letter was not given to chars with subjob locked. Also lion ii was given for RoV quest instead of zeid ii

Thank you Hiro and @ffxijuggalo from Canaria server :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday May 19, 2020 at 03:47:51_

----

ugh dunno why the SQL file got include it >.< dunno how to remove it from my PR


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday May 19, 2020 at 04:38:58_

----

yay fixed it =)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 04:24:12_

----

```lua
        if not player:hasJob(0) then -- Is Subjob Unlocked
            npcUtil.giveKeyItem(player, tpz.ki.GILGAMESHS_INTRODUCTORY_LETTER)
        else
```
Does that not give the key item to players without subjob unlocked?

Edit: This should be ` if player:hasJob(0) == 0 then -- Is Subjob Unlocked`
