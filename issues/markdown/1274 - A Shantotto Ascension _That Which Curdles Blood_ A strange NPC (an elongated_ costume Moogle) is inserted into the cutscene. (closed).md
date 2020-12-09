**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 04:15:16_
_Originally opened as: project-topaz/topaz - Issue 1274_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

It occurs when you move from "Port Windurst" to "West Sarutabaruta".
It does not occur when moving from "Windurst Woods" to "East Sarutabaruta".
The cutscene IDs for the problem are "62" and "63" in "West Sarutabaruta".

- npc_list.sql
INSERT INTO `npc_list` VALUES (17248862,'csnpc','     ',0,0.000,0.000,0.000,0,50,50,0,0,112,6,2075,0x0100000375113321333133413351756182720000,32,NULL,1);

This is caused by the above records.
Deleting the above record resolves the problem.








----
<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [EpicTaru](https://github.com/EpicTaru)**
_Thursday Oct 08, 2020 at 06:30:22_

----

Is your client version the same as the server version? Oddities like this in cutscenes are usually caused by version mismatches. 


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 07:09:14_

----

Thank you for your comment.

The client version is "302000904_2".
"VER_LOCK" is "2".
There is no version mismatch warning on login.

- version.conf
```
#Topaz Version Info

#Expected Client version (wrong version cannot log in)
CLIENT_VER: 30200904_2

#WE STRONGLY ADVISE AGAINST LOCKING THE SERVER TO OLDER VERSIONS. IT IS A UNIVERSALLY BAD IDEA.

#0 - disabled (every version allowed)
#1 - enabled - strict (only exact CLIENT_VER allowed, default)
#2 - enabled - greater than or equal  (matching or greater than CLIENT_VER allowed)
VER_LOCK: 2

#Current Server Version.
#TOPAZ_VER: C202008-01
```




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 08, 2020 at 23:18:44_

----

#281


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 09, 2020 at 00:52:07_

----

Capture with NPCL entry that would fix this:
https://discord.com/channels/443544205206355968/443552899675717633/733519453697998859

(Need to be in FFXI Captures Discord for link to work).
