**Labels:**



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Sunday Apr 19, 2020 at 21:24:24_
_Originally opened as: project-topaz/topaz - Issue 508_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
During The Emissary Bastok mission 2-3, Entering the Rank 2 Final Battlefield in Balga's Dais will result in the cutscene playing (sans any models being visible), then getting stuck. The cutscene will not release the camera and the player will need to re-log; whereupon the battlefield will be empty. Thus, 2-3 cannot be completed. Leaving and re-entering will have the same result.

Tested on release branch



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 21:33:21_

----

I just completed this very recently, but I am likely not on the same client version as you. The described problem has happened before when client and server go out of sync on the NPC IDs used in the cs event. This could be either the server's IDs in the release branch being incorrect (something missed in the ID shifts maybe), or the client being either newer or older than the release branches last version update.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Apr 20, 2020 at 02:21:44_

----

> I am likely not on the same client version as you

That's possible... I'm using 3019xxxx but it happened on another PC with the latest version. Maybe it's something in my account/DB related from migrating DSP->TPZ. If someone else happens to try the mission and it also works for them, I think this can just be closed as a 'me issue'.


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Wednesday Apr 22, 2020 at 08:08:32_

----

Hello Kreidos, thanks for reporting this! I was unable to reproduce it. I'm on the latest client/Canary versions, /ver 30200327_2 as of 04/22/2020. Feel free to reopen an issue if you come across it again (I hope not!). Thank you!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 08:13:53_

----

I am interested in this Issue, though. I have heard a _lot_ of complaints about it over time on a couple private server Discords, and this hasn't been the first time it's been reported on a tracker.

Confirmation that it's caused by an ID shift (ie: by intentionally using outdated NPC IDs in the db and then testing the CS) would make it easier to pinpoint problems with 2-3 in the future~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 08:47:34_

----

With my 30200217_0 client, and I don't know how old an NPC DB (was ages since I've run `npc_list.sql`): `!cs 32001` in Balga's Dais seemed to work to completion (although map server did throw out errors for needing NPCs 17375848, 17375849, 17375850).

After updating my npc_list to whatever our current version is (leaving my client on 30200217), the map server threw out errors for the same NPCs, but the event played normally, exited cleanly, and I didn't notice any oddities.

Running Windower _with_ Enternity. 30 FPS.

Tried again with 60 FPS, and uncapped FPS (averaging 750). Was not able to reproduce a hang.
