**Labels:**

reviewed



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Sunday Oct 25, 2020 at 21:35:27_
_Originally opened as: project-topaz/topaz - Issue 1434_

----

Adds Healing Salve I/II, Clear Salve I/II, Dusty Elixir

Lowered use timers from 4s to 1s (per bg wiki, 1s use time).
Clear Salve I can remove randomly up to two effects at random (https://translate.google.com/translate?hl=en&sl=ja&u=http://wiki.ffo.jp/html/20179.html&prev=search&pto=aue). Interpreted this to mean can remove between 1 and 2 effects.


<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 08:16:02_

----

Ohhhh I didn't know Lua had repeat/until (do/while)!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 08:18:22_

----

No need for these braces:
https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#no-parentheses-unless-needed-to-clarify-order-of-operations


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 08:18:56_

----

https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#no-parentheses-unless-needed-to-clarify-order-of-operations


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 08:20:14_

----

I know this section probably exists somewhere else, but there _has_ to be a better way of doing this...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 08:21:27_

----

 `local totalHP = (pet:getMaxHP() / 100) * percent`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 03:25:18_

----

```lua
    local effects =
    {
        tpz.effect.PETRIFICATION,
        tpz.effect.SILENCE,
        tpz.effect.BANE,
        tpz.effect.CURSE_II,
        tpz.effect.CURSE_I,
        tpz.effect.PARALYSIS,
        tpz.effect.PLAGUE,
        tpz.effect.POISON,
        tpz.effect.DISEASE,
        tpz.effect.BLINDNESS
    }
```
to conform to the [style guide](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#allman-braces)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 08:16:02_

----

Ohhhh I didn't know Lua had repeat/until (do/while)!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 08:18:22_

----

No need for these braces:
https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#no-parentheses-unless-needed-to-clarify-order-of-operations


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 08:18:56_

----

https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#no-parentheses-unless-needed-to-clarify-order-of-operations


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 08:20:14_

----

I know this section probably exists somewhere else, but there _has_ to be a better way of doing this...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 08:21:27_

----

 `local totalHP = (pet:getMaxHP() / 100) * percent`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 03:25:18_

----

```lua
    local effects =
    {
        tpz.effect.PETRIFICATION,
        tpz.effect.SILENCE,
        tpz.effect.BANE,
        tpz.effect.CURSE_II,
        tpz.effect.CURSE_I,
        tpz.effect.PARALYSIS,
        tpz.effect.PLAGUE,
        tpz.effect.POISON,
        tpz.effect.DISEASE,
        tpz.effect.BLINDNESS
    }
```
to conform to the [style guide](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#allman-braces)
