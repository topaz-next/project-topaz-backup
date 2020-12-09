**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:12_
_Originally opened as: project-topaz/topaz - Issue 94_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Tuesday Feb 23, 2016 at 04:18 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2803_

----

Client Version (type /ver in game) :
30160203_0

Server Version (type revision in game) :
3a852af

Source Branch (master/stable) :
master

Additional Information (Steps to reproduce/Expected behavior) :
The mobs in question are seemingly random. Or at least, I can't discern a pattern. So far I've identified Veteran Quadav, Yagudo Persecutor, and Marquis Andras. None of them should be swinging twice per round due to their job and/or level, let alone every time.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:13_

----

<a href="https://github.com/RwNigma"><img src="https://avatars3.githubusercontent.com/u/11567678?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [RwNigma](https://github.com/RwNigma)**
_Tuesday Feb 23, 2016 at 16:49 GMT_

----

I believe MNK type mobs have this problem as well. The Gigas in Upper Delkfutt Tower. Gatekeeper I believe. Looking at the weapon delay of 240 within the database it may work differently with H2H weapons at this delay.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:14_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Feb 23, 2016 at 19:01 GMT_

----

MNK mobs and delay? Oh... oh no....

I may have introduced a different bug with that... are MNK mobs considered having h2h skill?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:16_

----

<a href="https://github.com/RwNigma"><img src="https://avatars3.githubusercontent.com/u/11567678?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [RwNigma](https://github.com/RwNigma)**
_Tuesday Feb 23, 2016 at 20:07 GMT_

----

To be honest I am not sure. I just know that they swing at a speed slightly less than hundred fists. If the mobs you've listed are swinging with double strike then think quadrastrike for certain/all MNK mobs and that's how fast they swing.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:17_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Feb 23, 2016 at 20:35 GMT_

----

I don't think they are, but they have the double swing property for being MNK. Since the delay check is checking h2h skill... yeah. For mobs it needs to check h2h damage type, players skill (because of Birdbanes/Vampiric Claws). I'll have to fix that one in a little bit.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:18_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Feb 23, 2016 at 23:22 GMT_

----

Well I can't figure out why it's doing that anymore. Damn.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:20_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Feb 24, 2016 at 17:41 GMT_

----

This is a problem with Seiryu as well. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:21_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Saturday Feb 27, 2016 at 21:35 GMT_

----

I did a bit of digging, it's because the mobs weapon skill type is hand-to-hand, which comes from the cmbSkill column in the database.  Currently not known why mobs even have a combat skill, as they can't equip any weapons.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:22_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Saturday Feb 27, 2016 at 22:31 GMT_

----

Maybe it was for MNK mobs that aren't supposed to swing tw- ... nah I got nothing.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:23_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Sunday Feb 28, 2016 at 01:51 GMT_

----

hm since this wasn't an issue before the ai rewrite, maybe that column was used for something else?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:24_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Mar 03, 2016 at 01:32 GMT_

----

Maat is swinging stupidly fast on all jobs with this issue, with two swings regardless of job.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:25_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Mar 03, 2016 at 04:17 GMT_

----

Wait, I think the cmbSkill column would be the mob's skill rank, rather than their skill type, though that means for non-players it should probably be checking if the mob is a MNK instead of skill... though some MNK mobs don't have double swing (seiryu, maybe the MNK demon NM in xarc?), and some non-MNK mobs do have it (NIN aerns).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:26_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Mar 03, 2016 at 04:26 GMT_

----

what use would a skill rank column be for mobs?

On Wed, Mar 2, 2016 at 9:17 PM, Hozu notificationsgithub.com wrote:

> Wait, I think the cmbSkill column would be the mob's skill rank, rather
> than their skill type, though that means for non-players it should probably
> be checking if the mob is a MNK instead of skill... though some MNK mobs
> don't have double swing (seiryu, maybe the MNK demon NM in xarc?), and some
> non-MNK mobs do have it (NIN aerns).
> 
> —
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 2803Darkstar Issue issuecomment-191575153
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:28_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Mar 03, 2016 at 06:15 GMT_

----

Good point, about as useful as a skill type column I suppose, heh.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:29_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Saturday Mar 19, 2016 at 23:14 GMT_

----

I haven't been able to come up with any solution for this one, but people are having an extremely hard time beating Maat because of this.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:30_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Mar 20, 2016 at 00:52 GMT_

----

isn't he supposed to attack twice?

On Sat, Mar 19, 2016 at 5:14 PM, Hozu notificationsgithub.com wrote:

> I haven't been able to come up with any solution for this one, but people
> are having an extremely hard time beating Maat because of this.
> 
> —
> You are receiving this because you commented.
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 2803Darkstar Issue issuecomment-198805143




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:31_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Sunday Mar 20, 2016 at 03:05 GMT_

----

IIRC only on jobs that have native h2h skill.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:32_

----

<a href="https://github.com/waytim"><img src="https://avatars2.githubusercontent.com/u/12836865?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [waytim](https://github.com/waytim)**
_Wednesday Jun 01, 2016 at 23:15 GMT_

----

So after researching a bit, mobs like Alkyoneus that are MNK as main or subjob (he's war/mnk) and using cmbskill 1 (h2h) have crazy high dbl/triple attack proc rates, almost 100%. Charybdis also has stopped attacking 6 times which leads me to believe it's this area and below that's causing the issues:
github/DarkstarProject/darkstar/blob/314c2a1fc93d68c89b47984bf0b29187101e31aa/src/map/utils/battleutils.cppDarkstar Issue L2516




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:34_

----

<a href="https://github.com/abriasffxi"><img src="https://avatars1.githubusercontent.com/u/20671885?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [abriasffxi](https://github.com/abriasffxi)**
_Wednesday Jul 27, 2016 at 20:30 GMT_

----

I agree- will be testing removing cmbskil 1 for mobs with sub mnk later today.  It happens with many of the beastman mobs (Orcish Grunts, Sentinels, and the associated Quadavs, haven't checked Yagudo).

EDIT: Actually, now that I've noticed a few more mobs that do it, it's not related to the monk job at all and its purely cmbskill=1 that's causing issues.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:35_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Jul 27, 2016 at 20:43 GMT_

----

IMO cmbskill should be replaced by isH2H, and have the field be either 0 or 1. However, I bet the skill is also used to calculate the attack/acc for the mob based on their job.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:36_

----

<a href="https://github.com/abriasffxi"><img src="https://avatars1.githubusercontent.com/u/20671885?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [abriasffxi](https://github.com/abriasffxi)**
_Thursday Aug 04, 2016 at 15:39 GMT_

----

All - I was successful in changing all of my known instances of this bug with one query (from memory so please double check):

UPDATE dspdb.mob_pools SET cmbSkill=0 WHERE (cmbSkill=1 AND mJob <> 2 AND sJob <>2);

Not sure if mJob and sJob are exactly correct but this had about ~200mobs in the database that are not identified as monks, either by main or sub job, that it fixed.  I'm sure there are some thf mobs using h2h that it messed up but I didn't go through and fix them individually.  I feel like if someone checks that query and commits each individually if they know the mobs well it will be a pretty strong fix.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:37_

----

<a href="https://github.com/HeavensSword"><img src="https://avatars0.githubusercontent.com/u/12627703?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [HeavensSword](https://github.com/HeavensSword)**
_Thursday Aug 04, 2016 at 16:23 GMT_

----

I would advise against a massive UPDATE like that as some mobs still need to attack twice even without mnk main or sub.

For instance:
I'm in the middle of a change for mandragoras and some of the NM are rdm/blm, but still need to attack twice.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:38_

----

<a href="https://github.com/abriasffxi"><img src="https://avatars1.githubusercontent.com/u/20671885?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [abriasffxi](https://github.com/abriasffxi)**
_Thursday Aug 04, 2016 at 21:34 GMT_

----

Right, that's why I suggest someone runs the query and check the mobs.

On Thu, Aug 4, 2016 at 11:23 AM, Anthony notificationsgithub.com wrote:

> I would advise against a massive UPDATE like that as some mobs still need
> to attack twice even without mnk main or sub.
> 
> For instance:
> I'm in the middle of a change for mandragoras and some of the NM are
> rdm/blm, but still need to attack twice.
> 
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> github/DarkstarProject/darkstar - Issue 2803Darkstar Issue issuecomment-237605833,
> or mute the thread
> github/notifications/unsubscribe-auth/ATttjWaQq34ttDDZO5Usk7M8pohmagUbks5qchH7gaJpZM4HgQst
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:40_

----

<a href="https://github.com/phlare"><img src="https://avatars0.githubusercontent.com/u/692484?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [phlare](https://github.com/phlare)**
_Thursday Oct 13, 2016 at 00:46 GMT_

----

here's a pastebin with the results of: 
`SELECT poolid, name, familyid, mJob, sJob, cmbSkill, cmbDelay, mobType FROM mob_pools WHERE cmbSkill =1 AND mJob <> 2 AND sJob <> 2;`   just for perusing.

 We could create either a whitelist or blacklist of poolids for an `IN` clause and add that to the query above for a quick-and-dirty-but-not-so-destructive fix.

http://pastebin.com/Q3w5yqKw




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:41_

----

<a href="https://github.com/davismj"><img src="https://avatars2.githubusercontent.com/u/3845823?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [davismj](https://github.com/davismj)**
_Sunday Feb 25, 2018 at 02:34 GMT_

----

Cold Gigas in Beaucedine. Flagged as Warrior.

