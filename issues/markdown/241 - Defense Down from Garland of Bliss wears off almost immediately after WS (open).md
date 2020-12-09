**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:27_
_Originally opened as: project-topaz/topaz - Issue 241_

----

<a href="https://github.com/Whitechaser"><img src="https://avatars0.githubusercontent.com/u/24844126?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Whitechaser](https://github.com/Whitechaser)**
_Wednesday Oct 24, 2018 at 04:35 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5339_

----

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

**_Client Version_** **:** 30180904_0

**_Source Branch_** **:** master

**_Additional Information_** **:** 
The WS is supposed to apply Defense Down lasting 60/120/180 seconds according to [BG Wiki](https://www.bg-wiki.com/bg/Garland_of_Bliss).

Current script gives 60/90/120-second duration and multiplies it with a resistance formula, which...well, is that part necessary? Whatever it's returning, it's reducing the duration by a factor so big, the additional effect wears off within 3 or so seconds.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:28_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 24, 2018 at 21:06 GMT_

----

probably should be applied to a check if the effect happens at all rather than effect duration (I am guessing. Otherwise our resistance formula is very seriously useless)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:30_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Oct 24, 2018 at 21:09 GMT_

----

I'd guess it's using the wrong skill or something if it's always giving
high resists

On Wed, Oct 24, 2018, 3:06 PM TeoTwawki, <notificationsgithub.com> wrote:

> probably should be applied to a check if the effect happens at all rather
> than effect duration (I am guessing. Otherwise our resistance formula is
> very seriously useless)
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 5339Darkstar Issue issuecomment-432828160>,
> or mute the thread
> <github/notifications/unsubscribe-auth/ABGI_2p85sQcTRX6nDFes7ysLsl00gRLks5uoNZcgaJpZM4X3HIT>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:31_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 24, 2018 at 21:12 GMT_

----

I mean, duration is already adjusted by TP. Do we know for sure it has partial resist effecting duration as well as sticking it? Reist check on duration seems like we'd not get that 60/90/120 split. unless I missed something.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:32_

----

<a href="https://github.com/Whitechaser"><img src="https://avatars0.githubusercontent.com/u/24844126?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Whitechaser](https://github.com/Whitechaser)**
_Friday Oct 26, 2018 at 09:05 GMT_

----

I tried using the weaponskill again with /BLM, magic accuracy food, and Elemental Seal active (dunno if that contributes anything), and the Defense Down wore off much later than I was used to. Perhaps the resistance checking on WS additional effects needs to give players a boost? It appears caster level is the only thing powering it looking at magic.lua. And food of course, but I figure most jobs' weaponskills' additional effects are supposed to be serviceable without relying heavily on magic accuracy food like crepes.

I'm looking through a Japanese wiki/board of sorts circa 2008 and the comments don't seem to mention anything about duration resists. If the BRD mythic has a "% chance of applying gravity" based on TP while the SMN mythic has simply "duration" based on TP then I think that makes it clear that there shouldn't be. Also, the 60/120/180 durations are apparently legit based on some other comments, so those could be changed here, at least.

Edit: That said, moving the resist check to applying the status break itself only shifts the problem. Instead of the effect always landing but for very short durations, they would hardly land at all. It's also quite interesting how a single crepe overcame the resist rate. There's something suspicious there.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:33_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 27, 2018 at 12:02 GMT_

----

> Edit: That said, moving the resist check to applying the status break itself only shifts the problem. Instead of the effect always landing but for very short durations, they would hardly land at all. It's also quite interesting how a single crepe overcame the resist rate. There's something suspicious there.

Not necessarily true. We can specify what resist tier its checked against for example: always land unless FULL resisted, which **should not** be happening all that often..


**But yeah I don't think something with duration set by tp should also be applying math to its duration based on resist, if resist is involved there it should be changing which tier it lands as.**



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:35_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 27, 2018 at 12:05 GMT_

----

I don't think anybody would have arrived at the 60/120/180 or 60/90/120 conclusions if they were regularly getting 3/45/whatever durations because of resists on retail...

