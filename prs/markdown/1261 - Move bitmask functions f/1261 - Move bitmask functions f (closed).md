**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Monday Oct 05, 2020 at 23:07:24_
_Originally opened as: project-topaz/topaz - Issue 1261_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

No need to call core for these functions.  The only one that touched anything in core was setBitMask, and 1. it wasn't correctly documented and was misused in several places; and 2. we can just as easily setCharVar after setting the bit via LUA.

I kept each step of this process in its own commit for easier reviewing:

* Create bitmask functions on utils.mask
* Convert existing use cases
* Remove bitmask functions from lua_basentity
* Some minor lua cleanup
* Rewrite Mamaulabion's trade code because it bothered me

Before PRing, I tested without errors: Dynamis flagging; quest "Mama Mia"; and quest "Lure of the Wildcat (Windurst)"



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Oct 05, 2020 at 23:16:19_

----

Cool beans!

I'm sure this doesn't *have* to be micro-optimized, but simply adding all the bits without the `if` would be a bit neater.
```lua
count = count + bit.band(bit.rshift(mask, i), 1)
```


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Oct 06, 2020 at 13:12:49_

----

I like it!  Implemented, retested, and looks good.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Oct 05, 2020 at 23:16:19_

----

Cool beans!

I'm sure this doesn't *have* to be micro-optimized, but simply adding all the bits without the `if` would be a bit neater.
```lua
count = count + bit.band(bit.rshift(mask, i), 1)
```


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Oct 06, 2020 at 13:12:49_

----

I like it!  Implemented, retested, and looks good.
