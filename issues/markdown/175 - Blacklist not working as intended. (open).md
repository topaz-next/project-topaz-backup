**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:26_
_Originally opened as: project-topaz/topaz - Issue 175_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday May 15, 2017 at 20:22 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3874_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
 30170304_1

**_Server Version_** (type `revision` in game) **:**
581b5e7da03d7e1f088057abccf4e5af4334a1c5

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
So some idiots finally gave people cause to actually use the blacklist function in game on a private server..the entries appear to be saved to the database correctly but their chat still gets through. Not sure why, because a second bug implies the filtering does work: Someone blacklisted *themselves* which should not be possible but the current implementation allows it. This resulting in their character being unable to use any `` commands.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:28_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday May 16, 2017 at 01:26 GMT_

----

IsBlacklisted isn't referenced anywhere but when adding/removing, so it
seems like it was never implemented.

On Mon, May 15, 2017 at 2:22 PM, TeoTwawki <notificationsgithub.com> wrote:

> *I have:*
>
>    - searched existing issues (http://github.com/darkstarproject/darkstar/
>    issues/ <github/darkstarproject/darkstar - Issue >) to see
>    if the issue I am posting has already been addressed or opened by another
>    contributor
>    - checked the commit log to see if my issue has been resolved since my
>    server was last updated
>
> *Client Version* (type /ver in game) *:*
> 30170304_1
>
> *Server Version* (type revision in game) *:*
> 581b5e7
> <github/DarkstarProject/darkstar/commit/581b5e7da03d7e1f088057abccf4e5af4334a1c5>
>
> *Source Branch* (master/stable) *:*
> master
>
> *Additional Information* (Steps to reproduce/Expected behavior) *:*
> So some idiots finally gave people cause to actually use the blacklist
> function in game on a private server..the entries appear to be saved to the
> database correctly but their chat still gets through. Not sure why, because
> a second bug implies the filtering does work: Someone blacklisted
> *themselves* which should not be possible but the current implementation
> allows it. This resulting in their character being unable to use any 
> commands.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 3874>, or mute the
> thread
> <github/notifications/unsubscribe-auth/ABGI_4yA_UZY14RGj9KHmN_OTSSQlWiBks5r6LP8gaJpZM4NbpIC>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:29_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 16, 2017 at 01:29 GMT_

----

That makes the self blacklist thing even more crazy - client doesn't stop you, but does self censor the chat?!




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:30_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 16, 2017 at 01:51 GMT_

----

It looks like the client handles it, and the problem may be relating to zoning and the b-list packet being re-sent. Since I'm about out of bandwidth already (retarded throttle to below dialup speed, even dc's me from chat) I've contracted a few guinea-pigs to test that theory further.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:32_

----

<a href="https://github.com/Brierre"><img src="https://avatars3.githubusercontent.com/u/20527593?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Brierre](https://github.com/Brierre)**
_Thursday May 18, 2017 at 15:40 GMT_

----

Can't we all just get along... (mom comment felt appropriate)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:33_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 08, 2017 at 19:00 GMT_

----

Its the size. Need a packet cap from someone with a larger number of names in their blacklist on retail.

> When I coded blacklist for DSP I had no way to test against 100+ names to see how retail handled multiple packets for the blacklist since it is sent as part of the zone-in packet to stop downloading. See here:
github/DarkstarProject/darkstar/blob/master/src/map/packets/stop_downloading.cpp

says guy who did the original implementation of it.

