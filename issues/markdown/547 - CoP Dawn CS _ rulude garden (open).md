**Labels:**

bug

good first issue



<a href="https://github.com/Arklus"><img src="https://avatars1.githubusercontent.com/u/61334622?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Arklus](https://github.com/Arklus)**
_Wednesday Apr 29, 2020 at 01:50:57_
_Originally opened as: project-topaz/topaz - Issue 547_

----

Looks like CS are not triggering before you get the rings in CoP
<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 01:52:25_

----

`apoc-nigh` branch is currently only in `canary` until the BCNM is 100% finished; I don't know if it'd fix the ring situation


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 27, 2020 at 21:21:38_

----

Has the player seen all the relevant cutscenes?

[I checked the script and it looks okay](https://github.com/project-topaz/topaz/blob/release/scripts/zones/RuLude_Gardens/Zone.lua#L52-L55). I also did a mass-find for each of the charVar names and they are all getting set.


----
<a href="https://github.com/Psyclosis"><img src="https://avatars1.githubusercontent.com/u/2892271?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Psyclosis](https://github.com/Psyclosis)**
_Wednesday Jul 15, 2020 at 03:11:20_

----

> Looks like CS are not triggering before you get the rings in CoP
> 
> **_I have:_**
> 
> * [] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
> * [] checked the commit log to see if the issue has been resolved since my server was last updated
> 
> **_Additional Information_** (Steps to reproduce/Expected behavior) **:**

found this bug today reported to IBM in discord .. i found that the server time is whats messing it up ...mission requires you wait till JP midnight  but in the DB under char vars its putting the date on the next date so the game is looking for wrong date ..i changed my vars manually to reflect correct date .. and boom all CS's and got the ring.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 16:09:36_

----

Thanks for reminding me!

Need to adjust whatever is setting the var to use the proper time mechanic - `getMidnight()` [instead of this](https://github.com/project-topaz/topaz/blob/release/scripts/zones/Empyreal_Paradox/bcnms/dawn.lua#L62), and update checks against the charVar "Promathia_kill_day" to be a `>=` check.
