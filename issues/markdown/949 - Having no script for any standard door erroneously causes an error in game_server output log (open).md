**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Friday Aug 14, 2020 at 21:17:34_
_Originally opened as: project-topaz/topaz - Issue 949_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Having no script for these standard door npcs that just function to open/close is the Topaz norm.  Unfortunately, we always get hit with an error message in our server logs because the door has no script, and our code always looks for a script to match the npc name in the database.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 14, 2020 at 21:29:57_

----

@ devs :
- In the past we had turned off this message completely, but it was at the timed deemed more valuable to not have to do a lookup of a non responsive pc to see if it existed so it was turned back on. I would like see these missing script file errors changed from ShowError type to ShowNotice type, which we use for other notifications that are not critical. This might require a little reworking if we're just letting lua itself feed us the error. If I had time to do the work, I'd have a pr for it already but I don't so I'm commenting here. I despise non-error error messages.. 
- And giving every door object a script is a non option to me, It kills the automatic functionality and makes us do extra calls to get the functionality back in addition to being tedious and annoying when NPC shifts affect a door.. "flagging" door NPCs was looked at in the past as well: it can work has similar problems to making them all scripted (just minus the script creation part. Right now the default situation when a door NPC is added to the client is "it just works". A script or a flag makes thr default situation "someone needs to contribute that door".
