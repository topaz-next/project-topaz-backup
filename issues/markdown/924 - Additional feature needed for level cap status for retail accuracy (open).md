**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Aug 05, 2020 at 14:09:52_
_Originally opened as: project-topaz/topaz - Issue 924_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Retail has 1 lv cap status effect, but with multiple behaviors: 

 1. Plain old level cap, no frills (what we have now)
 2. Lv Cap with target restriction changes: only certain mobs can attack the player or be targeted by the player, other mobs will ignore the player and the player will be told they cannot attack that target, BUT anyone with the status can join in on any mob regardless of claim status or party status. **This is used by seasonal events.**  Unknown if you can cure a Lv capped player: its been to long and I do not remember. Probably pops a zero hp cure or prevents the cast.
 3. Lv Cap with restriction again but this time there is no free-for-all on claimed mobs, and outsiders can attack the mobs or heal players, but the dmg/heal amounts will always be zero and generate no hate.  **This is used by Garrison and Eco Quest fights**. Notes; I **think** you can get added to the mobs hate list briefly and **this version of lv cap may have been changed and collapsed into no.2 Minus the "free for all" part of it.** This may also sometimes but not always be paired with confrontation effects

Likely either `CCharEntity::CanAttack` or `CTargetFind::isMobOwner` are where we want to check for level cap. I doubt retail puts the status on the involved mobs but a packet cap during a seasonal event can confirm that. Likely we can/should use the existing place we already store battlefield IDs on the mob entity.

I may get time to work on this myself in the future if nobody else beats me to it, as I have plans for my own server involving this and I currently use an ugly hack to do this.
