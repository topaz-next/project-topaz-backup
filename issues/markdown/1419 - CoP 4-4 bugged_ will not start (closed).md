**Labels:**



<a href="https://github.com/residentevil80"><img src="https://avatars2.githubusercontent.com/u/54491714?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [residentevil80](https://github.com/residentevil80)**
_Saturday Oct 24, 2020 at 00:36:53_
_Originally opened as: project-topaz/topaz - Issue 1419_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

https://www.bg-wiki.com/bg/Promathia_Mission_4-4
    Check the Iron Gate in Sealion's Den for another cutscene.

Clicking the iron gate does not trigger cutscene. Gate also open which it is not ever supposed to do.
server spits out error 
[Error] luautils::onTrigger: scripts/zones/Sealions_Den/npcs/_0w0.lua:21: attempt to index field 'cop' (a nil value)




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 24, 2020 at 02:05:22_

----

I believe ninja-fixed this last night if you wanna try another pull~!


----
<a href="https://github.com/residentevil80"><img src="https://avatars2.githubusercontent.com/u/54491714?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [residentevil80](https://github.com/residentevil80)**
_Saturday Oct 24, 2020 at 18:14:50_

----

*EDIT* 
Had to get 1st cutscene again and now the door triggers the second. Problem fixed!
Just pulled fresh canary. Clicking the gate no longer opens it, but also does not trigger cutscene


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Oct 24, 2020 at 18:32:31_

----

Good stuff
