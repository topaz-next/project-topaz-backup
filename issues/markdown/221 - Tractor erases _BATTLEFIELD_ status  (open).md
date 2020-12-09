**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:21_
_Originally opened as: project-topaz/topaz - Issue 221_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Saturday Apr 14, 2018 at 15:29 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4767_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30180203_1


**_Source Branch_** (master/stable) **:** master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
1. Go start a BCNM with a buddy that can cast Tractor and Raise
2. Die in said BCNM
3. Have buddy tractor you to safety.
4. Raise up.
5. Grats! You can no longer participate in the BCNM.





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:22_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Sunday Apr 15, 2018 at 21:21 GMT_

----

If we listen to what wiki's say, this might require some retail research, [on the tractor page](http://ffxiclopedia.wikia.com/wiki/Tractor):

`Tractor does not work in some BCNMs.`

So we should:

- Verify if this is even true.
- If true, determine a list of BCNMs that you can/can't tractor.
- Enable/disable tractor based on findings.
- Fix BCNM status being reapplied based on findings.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:23_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Apr 15, 2018 at 22:15 GMT_

----

Battlefield status being reapplied with tractor should be the exact same
process as when you log out (or disconnect) in a BCNM and log back.  If
one's broken, the other may be as well

On Sun, Apr 15, 2018 at 3:21 PM, Zynjec <notificationsgithub.com> wrote:

> If we listen to what wiki's say, this might require some retail research, on
> the tractor page <http://ffxiclopedia.wikia.com/wiki/Tractor>:
>
> Tractor does not work in some BCNMs.
>
> So we should:
>
>    - Verify if this is even true.
>    - If true, determine a list of BCNMs that you can/can't tractor.
>    - Enable/disable tractor based on findings.
>    - Fix BCNM status being reapplied based on findings.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 4767Darkstar Issue issuecomment-381438994>,
> or mute the thread
> <github/notifications/unsubscribe-auth/ABGI_z1lQ0BGLAm2W_V37rLq_ubJ-rqgks5to7nPgaJpZM4TVG8i>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:24_

----

<a href="https://github.com/dcasadevall"><img src="https://avatars0.githubusercontent.com/u/2498220?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dcasadevall](https://github.com/dcasadevall)**
_Monday Apr 23, 2018 at 18:35 GMT_

----

As far as I know, tractor is available in any BCNM.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:25_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Friday May 18, 2018 at 18:24 GMT_

----

Tractor is not available in some BCNM's but for those of which you are not able to use it, it will simply give you a message that you cannot use it and then not allow you to cast. vs. dsp which allows you to cast and then erases your battlefield status. It would take casting tractor in every single bcnm to prove which ones allow and which ones don't but I have a theory that any battles entered using orbs (beastman/kindred seals etc..) will not allow tractor while the mission type battlefield events will. I have tested this out in 'some' battles but there are so many it will most likely take a lot of time. Regardless, when it is allowed, it should not wipe battlefield status.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:27_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Friday May 18, 2018 at 18:35 GMT_

----

This video has the "No Tractor" message as well as a player DC'ing and reconnecting to the fight:
https://www.youtube.com/watch?v=_Tx7fPtT708



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:28_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday May 19, 2018 at 16:02 GMT_

----

Wiggo32 do you have the casters side of things? I didn't see the message for tractor because its the dead characters view of things in that video.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:29_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Sunday May 20, 2018 at 05:38 GMT_

----

both sides are in that vid
https://youtu.be/_Tx7fPtT708?t=758



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:30_

----

<a href="https://github.com/ffxisf"><img src="https://avatars3.githubusercontent.com/u/2270559?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ffxisf](https://github.com/ffxisf)**
_Saturday May 26, 2018 at 10:22 GMT_

----

tractor.lua : 
if (caster:getBattlefield() ~= nil) then
  target:setPos(caster:getXPos(), caster:getYPos(), caster:getZPos(), 0);
end



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:31_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 10, 2019 at 21:40 GMT_

----

Still a problem post BCNM rework? Wiggo32 

