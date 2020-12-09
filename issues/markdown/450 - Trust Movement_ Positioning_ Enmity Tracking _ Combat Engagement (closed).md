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
