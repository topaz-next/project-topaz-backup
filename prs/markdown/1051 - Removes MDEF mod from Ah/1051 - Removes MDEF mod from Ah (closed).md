**Labels:**

reviewed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Monday Aug 31, 2020 at 23:10:36_
_Originally opened as: project-topaz/topaz - Issue 1051_

----

…T mod

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #259

Teo confirmed that on retail ahriman just have the -25% magic damage taken mod... MDEF can just be removed.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Sep 03, 2020 at 14:37:24_

----

1000 Needles (Hanatori, Lower Right): https://www.youtube.com/watch?v=wy9t26F8_l4&t=34m - 1000 damage

Water Shot (Astrena, Lower Left): https://www.youtube.com/watch?v=wy9t26F8_l4&t=42m50s - 206 damage

Astrena's regular QD in Espial is 260 (Can see on Five Moons earlier at https://www.youtube.com/watch?v=wy9t26F8_l4&t=24m19s)
102 Eminent Gun + 3 Bronze Bullet = 105, 105 * 2 = 210.
210 * 1.24 (100 + 24 MAB from /RDM sub / 100 Base MDB) = 260

Astrena had 3000 TP at the time Water Shot went off on the Ahriman, so the latent on Eminent Gun was no longer active:
97 Eminent Gun + 3 Bronze Bullet = 100, 100 * 2 = 200
200 * 1.2 (100 + 24 MAB / 100 + 20 MDB) = 206.667, floored

Edit: Eminent Gun's latent resulting in lower damage can be seen after it transforms into Nicholas (https://www.youtube.com/watch?v=wy9t26F8_l4&t=43m20s), resulting in a 750 damage 1000 Needles and a 248 damage QD:
(97 + 3) * 2 = 200
200 * 1.24 (100 + 24 MAB / 100 Base MDB) = 248

So the only thing with MDB in the fight was the Ahriman. It did not have MDT; only Nicholas did.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:23:34_

----

I am potat, I have no idea what any of that means 🤷 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 03, 2020 at 18:31:44_

----

:potato: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Sep 03, 2020 at 18:34:39_

----

It means more Dispels, 1000 Needles, and Quick Draws are needed - on stated targets.

The capture shows an Ahriman with 0% MDT and 20 MDB. This is the _reverse_ of what this Pull Request does.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 03, 2020 at 18:35:02_

----

I will translate: Ibm is saying Teo wrong, mob in log parse showing no mdt. 




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 03, 2020 at 18:35:35_

----

@ibm2431 yer to fast /sulk


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:37:23_

----

Danke danke


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Sep 03, 2020 at 18:41:46_

----

Precise MDT is given by 1000 Needles, which is an AoE Magical Attack when used by BLU players. Target needs to be fully Dispelled to not have Shell affecting the number.

Here is what happens to 1000 Needles damage when the target has Shell
Log excerpt from: https://youtu.be/H6tVvHDgI0Q
[1000_needles.txt](https://github.com/project-topaz/topaz/files/5170575/1000_needles.txt)


MDB is given by the way [Quick Draw damage is calculated](https://www.bg-wiki.com/bg/Quick_Draw). It ignores MDT. Provided you're not resisted, you can calculate a mob's MDB if you know your own MAB and use a Quick Draw that isn't affected by day/weather.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Sunday Sep 06, 2020 at 04:48:16_

----

Final final revisions done for this family according to Ibm's research.  Possibly will need to be tweaked in the future, but we now know that -25% MDT is plain wrong, and both wiki and bgwiki are wrong.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Sunday Sep 06, 2020 at 13:23:13_

----

this is ready, per zach's notes can try to merge release into this to remove the check fails


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 06, 2020 at 14:22:07_

----

> this is ready, per zach's notes can try to merge release into this to remove the check fails

This change is simple enough, there's not much need to go through a merge and waiting for CI - going to merge 💣 
