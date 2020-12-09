**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:16_
_Originally opened as: project-topaz/topaz - Issue 61_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [xipies](https://github.com/xipies)**
_Sunday Nov 08, 2015 at 06:16 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2386_

----

When zoning multiple chars at the same time, sometimes a char may be invisible to another. Running to 50 yalms away and back close again shows the invisible char again. Not sure if this is totally isolated to multiboxing.

I think this started happening after support for multiple "zone" servers was added. (Hope I'm using the right terminology.)

This may be a related to Darkstar Issue 2202.

Revision: 982f0b0
Server: Classic




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:18_

----

<a href="https://github.com/OtianNgocnion"><img src="https://avatars2.githubusercontent.com/u/14980726?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [OtianNgocnion](https://github.com/OtianNgocnion)**
_Sunday Nov 08, 2015 at 18:01 GMT_

----

A note about isolation to multiboxing: this has definitely occurred where the two players (one of whom couldn't see the other) are totally different IPs, computers, people. However, I don't know if one or the other of those people were also multiboxing separately. 

And, I confirm that the problem can always be solved by having someone run >50y, and then running back. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:19_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Nov 08, 2015 at 19:43 GMT_

----

more information:
probably has to do with when I separated the entity update packet types.
 could be because the client receives an incomplete packet update for an ID
that hasn't had a complete (spawn) packet yet, or some other packet

On Sun, Nov 8, 2015 at 11:01 AM, OtianNgocnion notificationsgithub.com
wrote:

> A note about isolation to multiboxing: this has definitely occurred where
> the two players (one of whom couldn't see the other) are totally different
> IPs, computers, people. However, I don't know if one or the other of those
> people were also multiboxing separately.
> 
> And, I confirm that the problem can always be solved by having someone run
> 
> > 50y, and then running back.
> 
> —
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 2386Darkstar Issue issuecomment-154853533
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:20_

----

<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Oct 19, 2019 at 18:47 GMT_

----

just poking this ticket to confirm issue is still valid.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:21_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 19, 2019 at 19:01 GMT_

----

it does happen. 



----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Aug 14, 2020 at 20:53:32_

----

Still an issue.
