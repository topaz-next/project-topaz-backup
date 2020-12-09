**Labels:**

reviewed



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 30, 2020 at 04:09:06_
_Originally opened as: project-topaz/topaz - Issue 666_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Changes made are for oneventstart to show correct price and
oneventfinish to charge the new lower price.

Dunno why its also commiting old commits? (i just forked this)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Jun 03, 2020 at 05:43:19_

----

any soul willing to review this? all i did was just add an if statement to check for a param that decides if u have key item or not, then copied one of the tables but with the newer price deducted if u have keyitem ^^;;


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 07:41:57_

----

I've looked through this and I believe it works. I'm not sure if we should duplicate the table just for a different price, or if it would be better for the table to return functions, something like this:
```lua
[117] = function (rhapsodyInWhite) if rhapsodyInWhite then return {act = "DRIED_MEAT",      cost = 25, food = true} else return {act = "DRIED_MEAT",      cost = 50, food = true} end end,
```
or
```lua
[117] = function (rhapsodyInWhite) return {act = "DRIED_MEAT",      cost = function() if rhapsodyInWhite then return 25 else return 50 end end, food = true} end,
```
then check the key item like this
```lua
    for k,v in pairs(regimeInfo[regimeType].finishOptions) do
        out[k] = v(hasKI)
```
So I'll let someone chime in on that otherwise I have no problems merging.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jun 03, 2020 at 18:11:35_

----

another possibility is to leave it one table and leave cost alone, but then add another entry for the RoV modified cost like
`[ 21] = {act = "REPATRIATION",    cost = 50, discounted = 10},`
and then change the for loop part to check if you have KI before deciding which one to use in the loop.

I'd go with the functions coco suggested if thats not easy to do.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 18:25:21_

----

> `[ 21] = {act = "REPATRIATION", cost = 50, discounted = 10},`

I like this, much cleaner. Would have to update 2 places in `bookOnEventFinish` to check for KI and use either `opt.cost` or `opt.discounted`.



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Jun 05, 2020 at 22:24:43_

----

@cocosolos done :cat: 
That SQL file came back again >.< can you remove it please


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jun 06, 2020 at 02:39:04_

----

it's the curse of the 666 

changes done.
