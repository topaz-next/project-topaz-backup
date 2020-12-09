**Labels:**

focus

merge ready



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Sunday May 03, 2020 at 04:23:29_
_Originally opened as: project-topaz/topaz - Issue 575_

----

Adds key trading feature for special, abjuration, fortune, and anniversary dials. Anniversary dial loot is currently not populated and will either give an item from the special dial or give the key back. Fortune key loot is populated based on best guess for what fits (wikis are incomplete).

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 21:21:27_

----

We don't need to check if `trade:getItemCount() ~= 1` because we've already confirmed the item count is 1 back on L92.

(And we may not need the nil or ID range checks either, because the trade container is already saying there's at least one valid item in it.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 21:23:05_

----

Also don't need to check ` if player:getFreeSlotsCount() == 0 then` here on L100 because we already did so on L97 (so L100-L102 are impossible to reach).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 21:25:48_

----

Thoughts on checking against keyToDial[keyID instead of the item IDs themselves?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 21:21:27_

----

We don't need to check if `trade:getItemCount() ~= 1` because we've already confirmed the item count is 1 back on L92.

(And we may not need the nil or ID range checks either, because the trade container is already saying there's at least one valid item in it.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 21:23:05_

----

Also don't need to check ` if player:getFreeSlotsCount() == 0 then` here on L100 because we already did so on L97 (so L100-L102 are impossible to reach).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 21:25:48_

----

Thoughts on checking against keyToDial[keyID instead of the item IDs themselves?
