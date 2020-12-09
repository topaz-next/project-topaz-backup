**Labels:**

bug

good first issue



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jan 08, 2020 at 15:40:04_
_Originally opened as: project-topaz/topaz - Issue 325_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**
- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened or fixed
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Weaponskills which get an attack multiplier based on the player's current TP, like Tachi: Gekko, [do not have the player's current TP passed into the fTP function](https://github.com/project-topaz/topaz/blob/3eb1c1570f276c8510300a2993fc225fc50d4ba7/scripts/globals/weaponskills.lua#L671). `ftp()` ends up taking the WS's TP 1000 multiplier as the first argument, [but then bumps it up to 1000](https://github.com/project-topaz/topaz/blob/3eb1c1570f276c8510300a2993fc225fc50d4ba7/scripts/globals/weaponskills.lua#L641-L643), averting [the nil of ftp3 being undefined](https://github.com/project-topaz/topaz/blob/3eb1c1570f276c8510300a2993fc225fc50d4ba7/scripts/globals/weaponskills.lua#L646-L648).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 12, 2020 at 16:54:43_

----

#585 
