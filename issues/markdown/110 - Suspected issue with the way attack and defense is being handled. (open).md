**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:24_
_Originally opened as: project-topaz/topaz - Issue 110_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Saturday Apr 02, 2016 at 03:59 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2976_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **30160203_0:**

**_Server Version_** (type `revision` in game) **:"Unknown"** (server was built using yesterday's code I assume it's up to date)

**_Source Branch_** (master/stable) **Master** 

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

I have for many months now suspected that something is off about the way darkstar handles attack/defense for players and mobs. I wish I could point out specifics, but I just don't know retail damage formulas as well as I do retail HNM behavior.

To give a couple of examples:
If I'm fighting a level 95 mob which possess 531 attack vs my 422 defense the average hit from that mob will be: 429

If I'm fighting that same level 95 mob after it has recieved a 75% attack boost (placing its attack at 929) the average hit will be: 531

That doesn't seem to me to be nearly the boost one would expect. If the test were conducted using physical- gear and phalanx the damage difference of adding 398 attack would shrink to the point where it's hard to even spot.

As another example there are a couple of retail mobs out there with very high defense. Genbu is a good example. If I have my Excalibur out at retail Genbu I will sometimes hit 0s. No matter how much defense I give Darkstar Genbu I cannot reproduce that behavior (and as far as I know retail genbu has no phalanx effects)

A year ago word on the street on nas server was that enmity, meva, accuracy, and attack were all functioning in a non-retail fashion. After several updates to address each of those systems, these days the word on the street is "Attack gear helps more than it did on retail." So all of this leads me to believe the attack/defense formulas need to be double checked for retail accuracy.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:25_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Saturday Apr 02, 2016 at 04:16 GMT_

----

tagging bendangelo because you fixed meva/acc/enmity




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:26_

----

<a href="https://github.com/towbes"><img src="https://avatars3.githubusercontent.com/u/7587673?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [towbes](https://github.com/towbes)**
_Sunday Apr 03, 2016 at 16:17 GMT_

----

Is this relevant? https://www.bg-wiki.com/bg/PDIF




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:27_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Sunday Apr 03, 2016 at 20:51 GMT_

----

It appears to be very relevant. 

It looks to me as if Tiamat's Ratio in the first test is 1.237 and cRatio moves to 2.237 (because Tiamat is 20 levels over.)

cRatio in the second example appears to me to be 3.201 (if I understand these formulas correctly)

If cRatio of 2.237=429 average hit, proportionally cratio of 3.201 would indicate an expected average hit closer to 614. The average attack appears to have only increased by roughly half that amount.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:28_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Monday Apr 04, 2016 at 04:37 GMT_

----

I really don't know much about this. Best thing to do would be to create some isolated test cases on retail, then we can run the same tests to compare the differences.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:29_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Apr 06, 2016 at 22:56 GMT_

----

I wonder if this is why SAMs are saying that their Tachi: Gekko yields average amounts lower than it did on retail. Even if the cratio is handled in a different location for WSs (scripts) than it does for (mob) melee attacks (core). Edit: SAMs with way better gear on DSP servers than they had on retail doing less than they would do on retail...

Edit 2: SAM WSs should probably be in line with retail now that Overwhelm works.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:30_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Saturday Apr 09, 2016 at 01:30 GMT_

----

I'm not a DD specialist, but I can absolutely vouch that something is wrong with Tachi: Gekko damage, whether it be this issue or another.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:31_

----

<a href="https://github.com/TheMuffinPirate"><img src="https://avatars3.githubusercontent.com/u/11020352?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TheMuffinPirate](https://github.com/TheMuffinPirate)**
_Saturday Apr 16, 2016 at 19:25 GMT_

----

Some other ws are also underperforming, Raging Rush for example




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:33_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Saturday Apr 16, 2016 at 19:27 GMT_

----

I'm inclined to say otherwise, unless you mean compared to how they were performing on DSP earlier. In that case, see github/DarkstarProject/darkstar - PR 2968, where double attack can no longer proc on every single hit.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:34_

----

<a href="https://github.com/TheMuffinPirate"><img src="https://avatars3.githubusercontent.com/u/11020352?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TheMuffinPirate](https://github.com/TheMuffinPirate)**
_Saturday Apr 16, 2016 at 19:30 GMT_

----

I meant in general, might be only at 75 cap though




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:35_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Wednesday Apr 27, 2016 at 17:29 GMT_

----

This is likely more to do with mob stats than the damage system. All my reviews of the system compared to BG-wiki show that it is accurate.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:36_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 27, 2016 at 18:11 GMT_

----

The majority of mobs should be fairly accurate just by being calculated based on their job, with _most_ deviations from that being NMs. If it is the mobs stats, then I think this and Darkstar Issue 3072 may actually be the same issue (though Darkstar Issue 3072 wasn't nearly as bad as I initially thought, because of someone derping a conf setting).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:38_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Wednesday Apr 27, 2016 at 18:14 GMT_

----

Mobs could have bonuses(in retail) that aren't part of their general calculations. For example, even after the magic system was "fixed," I still do way more dmg to groundskeepers than I did in retail with the same equipment. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:39_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 27, 2016 at 18:26 GMT_

----

Some definitely do, but the majority will be simple "my job is xxx/xxx".

I remember some guys on ffxi community sites arguing over what a mobs job was based solely on its vit score. I know exceptions exist, those guys did not. I know we have a ranking for the stats in the mob family table, and much of that is copy pasta that hasn't really been check against retail. As an example: someone adds a new type of rabbit from new expansion, copies an existing rabbits sql's line and changes only what they know for sure is different.

tl;dr
yeah very possible the stats are off. Not so easy to see which way they are off though.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:40_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Wednesday Apr 27, 2016 at 18:28 GMT_

----

Agreed. It's not easy at all. It will likely never be 100% retail accurate in this sense. 


