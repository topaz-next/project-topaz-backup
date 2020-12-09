**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Sunday Aug 30, 2020 at 07:55:14_
_Originally opened as: project-topaz/topaz - Issue 1039_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

This was introduced with one of the recent additions to release, or at least noticed with it, likely #962 .

As a summoner, order an elemental spirit to assault a mob.  After it casts, the mob will not be claimed, but will aggro the spirit.  When your spirit is in melee range and melee attacks the mob, it will briefly claim, but once your spirit dies, the mob de-claims and sits there like you've done it no wrong.  WELL YOU HAVE!

This bug can obviously be abused to kill un-soloable enemies as a solo summoner, or even HNMs with a group.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Sunday Aug 30, 2020 at 08:14:35_

----

Further info: 
![image](https://user-images.githubusercontent.com/37684138/91654486-f9154400-ea5d-11ea-9b09-afac1312b11e.png)
At timestamp 00:37:19, the spider killed my spirit, and I sat there watching the spider remain unclaimed, until i summoned Ifrit to ensure the normal avatars were working right (which they were).

Comments updated to reflect most recent info.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Monday Aug 31, 2020 at 07:21:19_

----

Further testing today revealed that if the spirit's level is too low to cast spells, it acts like a normal avatar as far as enmity goes.

Using a lvl 14 smn's thunder spirit, I used assault on a fly in dunes, and it chased after me after the spirit died.  I then swapped to a lvl 22 smn thunder spirit, used assault on a fly, it cast a spell to open, then went to melee the fly.  After the spirit died, the fly didn't chase me, and lost claim.
