**Labels:**

reviewed



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Mar 29, 2020 at 10:21:04_
_Originally opened as: project-topaz/topaz - Issue 450_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Thanks again to @Omnione for having a more reasonable solution for having trusts follow each other.

**Combat and Roaming Movement**
- Trusts spawn in a line and run in just a little bit
- Trusts roam as "follow the leader"
- Trusts cleanly form up in combat
- No more randomness
- No more strange lerping and jittering
- No more trusts fighting for position
- No more Trusts getting trapped behind one another
- No more Trusts getting trapped on top of each other and running round in circles... (even though that one was funny)

**Enmity**
There is a new binding for hasEnmity(), which checks all nearby mobs if an entity has ANY enmity. Used during trust summoning, probably shouldn't be used in battle (or often).

**Resting**
Trusts heal 3% HP and MP per tick after waiting 10 seconds after combat finishes. If your 3% doesn't go above 1hp/mp it will try 5%, after that you don't get anything.

**Engagement**
There was a PLastAttacker all along. I've done a good bit of testing and everything works. No strange edge cases, I'm sure those will come out in time.

**Job Latents and Party Jobs**
Summoned trusts are taken into account for job-related latents. Tested with Nanaa Mihgo with Forte Earring (Latent: +1 Dex with THF in party).
They are also now counted in hasPartyJob(), used in COR rolls.

Still not perfect, but at least 90% better than before.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 03, 2020 at 23:12:55_

----

I know you said you tested trusts activating latent effects, but was the test on Topaz or retail?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 03, 2020 at 23:35:38_

----

I'm a little surprised that there isn't already a struct keeping track of all the different hate lists a player is on (player->onEnmityLists = { *container a, *container b}).

"Surely we have to have something - cure would use it, right?"
[No, every cure checks the entire mob list too.](https://github.com/project-topaz/topaz/blob/release/src/map/utils/battleutils.cpp#L3461-L3466)

(A struct like that isn't a request, just me musing something we might consider in the future.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 03, 2020 at 23:38:44_

----

`EnmityContainer` does have `HasID` though, so you can save yourself a little effort.
```cpp
CMobEntity* mob = static_cast<CMobEntity*>(it->second);
if (mob->PEnmityContainer->HasID(m_PBaseEntity->id))
{
    hasEnmity = true;
    break;
}
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 04, 2020 at 04:47:35_

----

Would it be better for a trust's party position to be set on spawn, and only recalculated when another trust is despawned?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 04, 2020 at 07:08:05_

----

I'm wondering if it might be better to have declumping occur after distance checks so trusts aren't too preoccupied declumping from each other when they should pathing to the master.

(Or if kept here, add in a check here to make sure the _current_ trust isn't already following a path)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 04, 2020 at 07:14:36_

----

A thought occurred that we might be able to cheat by setting a special regen status effect on disengage - which is cleared on engage - and then letting the status effect container handle it.

I don't know if it'd be _better_ than doing it yourself here; just bringing it up as an option in case someone else might say, "Yes, that'd be better because X and Y".


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 07:55:40_

----

It was on Topaz, because I `!additem`'d myself a `Forte Earring`. I don't have confirmation that Trusts trigger Latents, but (the wikis say) that they affect COR Rolls, so that was my logical jump


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 07:57:28_

----

Yeah, out of scope of this PR, but would be super useful


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 08:21:12_

----

I shall test and see how it looks 👍 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 08:59:08_

----

All the different combinations look about the same, so I changed to use your suggestions


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 09:00:22_

----

Probably, the trust could keep their own position, and the char could re-calculate when things change and tell each trust. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Apr 04, 2020 at 15:19:52_

----

@ibm2431 suggestion : should track the little weird things like that on a spreadsheet in a gist for the future so they don't get lost.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Apr 05, 2020 at 09:40:12_

----

I think it would probably be better to do the sneaky regen, this system I'm using has the healing "ticks" not in line with regular healing ticks


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Apr 05, 2020 at 10:40:16_

----

Hmmm, I tried it out with a regen/refresh status and I couldn't get it to work as cleanly as I'd like, I'll come back to this later if needed


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 03, 2020 at 23:12:55_

----

I know you said you tested trusts activating latent effects, but was the test on Topaz or retail?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 03, 2020 at 23:35:38_

----

I'm a little surprised that there isn't already a struct keeping track of all the different hate lists a player is on (player->onEnmityLists = { *container a, *container b}).

"Surely we have to have something - cure would use it, right?"
[No, every cure checks the entire mob list too.](https://github.com/project-topaz/topaz/blob/release/src/map/utils/battleutils.cpp#L3461-L3466)

(A struct like that isn't a request, just me musing something we might consider in the future.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 03, 2020 at 23:38:44_

----

`EnmityContainer` does have `HasID` though, so you can save yourself a little effort.
```cpp
CMobEntity* mob = static_cast<CMobEntity*>(it->second);
if (mob->PEnmityContainer->HasID(m_PBaseEntity->id))
{
    hasEnmity = true;
    break;
}
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 04, 2020 at 04:47:35_

----

Would it be better for a trust's party position to be set on spawn, and only recalculated when another trust is despawned?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 04, 2020 at 07:08:05_

----

I'm wondering if it might be better to have declumping occur after distance checks so trusts aren't too preoccupied declumping from each other when they should pathing to the master.

(Or if kept here, add in a check here to make sure the _current_ trust isn't already following a path)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 04, 2020 at 07:14:36_

----

A thought occurred that we might be able to cheat by setting a special regen status effect on disengage - which is cleared on engage - and then letting the status effect container handle it.

I don't know if it'd be _better_ than doing it yourself here; just bringing it up as an option in case someone else might say, "Yes, that'd be better because X and Y".


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 07:55:40_

----

It was on Topaz, because I `!additem`'d myself a `Forte Earring`. I don't have confirmation that Trusts trigger Latents, but (the wikis say) that they affect COR Rolls, so that was my logical jump


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 07:57:28_

----

Yeah, out of scope of this PR, but would be super useful


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 08:21:12_

----

I shall test and see how it looks 👍 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 08:59:08_

----

All the different combinations look about the same, so I changed to use your suggestions


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 09:00:22_

----

Probably, the trust could keep their own position, and the char could re-calculate when things change and tell each trust. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Apr 04, 2020 at 15:19:52_

----

@ibm2431 suggestion : should track the little weird things like that on a spreadsheet in a gist for the future so they don't get lost.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Apr 05, 2020 at 09:40:12_

----

I think it would probably be better to do the sneaky regen, this system I'm using has the healing "ticks" not in line with regular healing ticks


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Apr 05, 2020 at 10:40:16_

----

Hmmm, I tried it out with a regen/refresh status and I couldn't get it to work as cleanly as I'd like, I'll come back to this later if needed
