**Labels:**

crafting



<a href="https://github.com/TheWhaler"><img src="https://avatars0.githubusercontent.com/u/28814616?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TheWhaler](https://github.com/TheWhaler)**
_Saturday Jun 20, 2020 at 17:26:44_
_Originally opened as: project-topaz/topaz - Issue 750_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Had a player report that NPC wasnt accepting bowl of puls for guild points even though it was asking for that. It did work on the previous item that the guild asked for. 

Looked up the item and it should be a guild item that is accepted based on:

https://ffxiclopedia.fandom.com/wiki/Puls




----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Jul 28, 2020 at 14:21:35_

----

This is happening quite a lot on Canary server too, and my understanding is that it happens after a server restart and before the next midnight guild point reset.

We just had one today, and even though I had already done my points for the day, after the restart the Woodworking guy is saying:

![image](https://user-images.githubusercontent.com/52013132/88677722-eec5fa00-d0ed-11ea-9f88-3f998f59c3d8.png)

Its obviously a bug, as there is no item that would allow up to 64006 daily points...!

So far I haven't been able to reproduce the issue on my local test server.
The server when update guild items, correctly store the current year day in the database, so that this update is never done more than once per day. Will continue to investigate though...


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Wednesday Jul 29, 2020 at 15:28:16_

----

Ok I finally managed to understand whats happening. It's again because of this mismatch between JP midnight and server midnight. Hopefully i should be able to propose a fix soonish.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 29, 2020 at 16:34:30_

----

https://github.com/DarkstarProject/darkstar/issues/1519

> The client is hardcoded to tell you the next Japanese
midnight (and currently the reset time is the servers time, including
offset)

So the server's time either needs set to JP timezone+the correct time it is in japan, OR the settings need adjusted so that the game is getting the time offset to make Japanese midnight line up. Plus no matter which method you use to put JP midnight at the correct time (where I am that's 10 or 11am depending on daylight savings time) we still need to fix an error that is putting the days off by 1 (noticeable when conquest tally is a day late..) which might also be impacting this.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Thursday Jul 30, 2020 at 11:32:24_

----

I think it's better if, for guild reset, I change it to always happen on JP midnight.
As it was mentioned in other bug reports, some bugs will always be present if you start changing this, as the client supposes that things happen at JP midnight too...


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 31, 2020 at 15:51:23_

----

The prob is the server gets when jp midnight is, wrong. That needs adjusted, along with doing it at jp midnight.
