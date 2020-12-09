**Labels:**

reviewed



<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Nireya](https://github.com/Nireya)**
_Sunday Nov 01, 2020 at 09:22:00_
_Originally opened as: project-topaz/topaz - Issue 1465_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Implements the retrace spell into the game, along with related usable items:
- Scroll of Instant Retrace
- Cobra staff
- Fourth staff
- Ram staff

The staves have separate teleport IDs from Retrace because you can use their teleports after joining a different allied nation.

Retrace was changed from an 8 second cast to a 5 second cast recently according to wiki so I adjusted that.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:05:15_

----

3.4 isn't actually valid because the function doesn't support floating point values. it will become just 3 at that point. I am aware we have some existing code making the same mistake that has not been corrected yet.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:07:13_

----

1 second? seems kinda short for that animation. But if you already checked and its retail accurate leave it.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 00:12:30_

----

I know the rest of this file sets a bad example, but does anyone have thoughts on this using the tables Nireya is defining above for the teleport destinations, rather than defining the same positions twice?

Nireya: `unpack(<table>)` is a lua method which takes a table and breaks it apart into multiple arguments. The order of both needs to line up - so it's not used too often - but it could theoretically be used in this case.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 00:14:34_

----

Standard "remove needless outer parens" comment 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 00:16:46_

----

Slightly fewer lines if you want them:
```lua
if not (target:getCampaignAllegiance() > 0) then
    return 0
else
    return 56
end
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:19:48_

----

outer parens not needed :P


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 00:23:38_

----

Lua can be odd with `not` at times 💦 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 00:27:11_

----

![not](https://user-images.githubusercontent.com/13112942/97819684-1fe03880-1ca2-11eb-9c3f-87c55aa1c105.png)



----
<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Nireya](https://github.com/Nireya)**
_Monday Nov 02, 2020 at 01:12:12_

----

I used Warp II as a reference since this spell also is cast on other people, it appears 4 is more correct though yeah. Wasn't aware of that, thanks.


----
<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Nireya](https://github.com/Nireya)**
_Monday Nov 02, 2020 at 01:13:26_

----

I was using the Scroll of Instant Warp item as a base line reference, but 1 did feel too short for this.


----
<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Nireya](https://github.com/Nireya)**
_Monday Nov 02, 2020 at 01:14:43_

----

I changed both item and spell to `if not` statements, and yeah the spell didn't work without the parentheses 😹 


----
<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Nireya](https://github.com/Nireya)**
_Monday Nov 02, 2020 at 04:12:15_

----

I re-ordered the tables to line up to allow for this method,  but after taking a look at examples and reading a bunch about it I was still pretty stumped at how `unpack` works exactly.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 04:26:11_

----

An easy way to think about `pack` and `unpack` is that they add brackets or remove them.

```lua
some_table = pack(1, 2, 3, 4) -- results in a table of {1, 2, 3, 4}
unpack(some_table) -- results in a return value of 1, 2, 3, 4 as separate arguments
```

Unpack is useful in the sense that lua lets you assign multiple values at once, because functions can return multiple values by default.

```lua
local pos = {123, 456, 789}
x, y, z = unpack(pos)
```
Would result in x being assigned to 123, y to 456, and z to 789

Since you'd be calling setPos directly, you can unpack it in the function call:
```lua
local pos = destinations[[ids.BASTOK_MARKETS_S]]
player:setPos(unpack(pos))
```
Should result in a function call to `setPos` equivalent to:
`player:setPos(-291, -10 , -107, 212, 87)`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:05:15_

----

3.4 isn't actually valid because the function doesn't support floating point values. it will become just 3 at that point. I am aware we have some existing code making the same mistake that has not been corrected yet.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:07:13_

----

1 second? seems kinda short for that animation. But if you already checked and its retail accurate leave it.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 00:12:30_

----

I know the rest of this file sets a bad example, but does anyone have thoughts on this using the tables Nireya is defining above for the teleport destinations, rather than defining the same positions twice?

Nireya: `unpack(<table>)` is a lua method which takes a table and breaks it apart into multiple arguments. The order of both needs to line up - so it's not used too often - but it could theoretically be used in this case.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 00:14:34_

----

Standard "remove needless outer parens" comment 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 00:16:46_

----

Slightly fewer lines if you want them:
```lua
if not (target:getCampaignAllegiance() > 0) then
    return 0
else
    return 56
end
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:19:48_

----

outer parens not needed :P


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 00:23:38_

----

Lua can be odd with `not` at times 💦 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 00:27:11_

----

![not](https://user-images.githubusercontent.com/13112942/97819684-1fe03880-1ca2-11eb-9c3f-87c55aa1c105.png)



----
<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Nireya](https://github.com/Nireya)**
_Monday Nov 02, 2020 at 01:12:12_

----

I used Warp II as a reference since this spell also is cast on other people, it appears 4 is more correct though yeah. Wasn't aware of that, thanks.


----
<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Nireya](https://github.com/Nireya)**
_Monday Nov 02, 2020 at 01:13:26_

----

I was using the Scroll of Instant Warp item as a base line reference, but 1 did feel too short for this.


----
<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Nireya](https://github.com/Nireya)**
_Monday Nov 02, 2020 at 01:14:43_

----

I changed both item and spell to `if not` statements, and yeah the spell didn't work without the parentheses 😹 


----
<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Nireya](https://github.com/Nireya)**
_Monday Nov 02, 2020 at 04:12:15_

----

I re-ordered the tables to line up to allow for this method,  but after taking a look at examples and reading a bunch about it I was still pretty stumped at how `unpack` works exactly.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 04:26:11_

----

An easy way to think about `pack` and `unpack` is that they add brackets or remove them.

```lua
some_table = pack(1, 2, 3, 4) -- results in a table of {1, 2, 3, 4}
unpack(some_table) -- results in a return value of 1, 2, 3, 4 as separate arguments
```

Unpack is useful in the sense that lua lets you assign multiple values at once, because functions can return multiple values by default.

```lua
local pos = {123, 456, 789}
x, y, z = unpack(pos)
```
Would result in x being assigned to 123, y to 456, and z to 789

Since you'd be calling setPos directly, you can unpack it in the function call:
```lua
local pos = destinations[[ids.BASTOK_MARKETS_S]]
player:setPos(unpack(pos))
```
Should result in a function call to `setPos` equivalent to:
`player:setPos(-291, -10 , -107, 212, 87)`
