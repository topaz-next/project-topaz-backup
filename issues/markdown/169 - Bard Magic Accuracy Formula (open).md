**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:55_
_Originally opened as: project-topaz/topaz - Issue 169_

----

<a href="https://github.com/LyleVertigo"><img src="https://avatars2.githubusercontent.com/u/26503842?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [LyleVertigo](https://github.com/LyleVertigo)**
_Saturday Mar 18, 2017 at 12:52 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3814_

----

I need clarification on the resistance check code for Bard song debuffs.

The correct formula for calculating the magic accuracy for bard debuff songs is:
**Singing Skill + Wind Instrument Skill or 1/2 of String Instrument Skill.**

If you look at any of the debuff songs, carnage elegy for example:
github/DarkstarProject/darkstar/blob/master/scripts/globals/spells/carnage_elegy.lua
you see the following line regarding resistance checks:
`local resm = applyResistanceEffect(caster,spell,target,dCHR,SINGING_SKILL,0,EFFECT_ELEGY);`

As you can see, Singing_Skill is applied, but nothing I can see that uses wind or string instrument skill.

Is there a reason for this?  Am I missing something?  If Wind and String instrument skills are in fact missing from the resistance formula, how would they be correctly added in the same line, since string is supposed to only give half skill as opposed to wind?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:57_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Saturday Mar 18, 2017 at 19:16 GMT_

----

Are you sure they're supposed to use half the instrument skill? Is there a source? Because songs on retail aren't very accurate compared to other spells, so it would make sense that it uses only the ~C level skill.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:58_

----

<a href="https://github.com/Nilretep"><img src="https://avatars1.githubusercontent.com/u/6565148?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Nilretep](https://github.com/Nilretep)**
_Monday May 29, 2017 at 22:01 GMT_

----

https://www.bg-wiki.com/bg/Category:Song

It doesn't look like there is anywhere that accounts for Wind or String skill. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:59_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 30, 2017 at 03:58 GMT_

----

> Magic Accuracy for Songs is proportional to the sum of Singing skill and Instrument skill for the equipped instrument type

https://www.bg-wiki.com/bg/Magic_Accuracy

So yeah they get used. Formula I was always taught back in the day on retail was they were just additive for whichever instrument you were using, and that this was why bard didn't have a higher rated skill in either of the 3.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:00_

----

<a href="https://github.com/Nilretep"><img src="https://avatars1.githubusercontent.com/u/6565148?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Nilretep](https://github.com/Nilretep)**
_Tuesday May 30, 2017 at 14:34 GMT_

----

Sorry, my last comment was confusing. I meant it doesn't look like wind or string are used in the code. I agree with Singing+Instrument skill.

When you say "they get used" do you mean they are supposed to get used or that there is a magic accuracy formula coded here that uses wind and string skills? Is singing the only skill being taken into account with song accuracy?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:02_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 30, 2017 at 18:32 GMT_

----

ah sorry you linked bg when yous aid that so thought you were talking retail. in darkstar we're not doing things correctly yet. github/DarkstarProject/darkstar/blob/155308e1370596ad4071ad1421fac1398f0fc0ec/src/map/entities/charentity.cppDarkstar Issue L670 only place in entire trunk I see them checked right now.

github/DarkstarProject/darkstar/search?utf8=%E2%9C%93&q=SKILL_WND&type=




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:04_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday May 30, 2017 at 20:09 GMT_

----

I imagine you could do a blanket check in magic.lua in the applyResistenceEffect function, where if skill used is singing, to add whatever amount of skill for the corresponding instrument type equipped? Problem is, how much of the instrument skill gets used for accuracy? Even half makes songs extremely accurate, when they're not particularly accurate on retail, in comparison to spells of other skills.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:05_

----

<a href="https://github.com/LyleVertigo"><img src="https://avatars2.githubusercontent.com/u/26503842?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [LyleVertigo](https://github.com/LyleVertigo)**
_Tuesday May 30, 2017 at 20:23 GMT_

----

I guess the formula will need to be adjusted depending on the server.  The one I was on is not era and many monster resistance settings are set much higher than retail.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:06_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 30, 2017 at 20:34 GMT_

----

LyleVertigo servers doing non retail things can adjust their own yeah. Here in project *at some point* we will try to as close as we can match retail.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:08_

----

<a href="https://github.com/Nilretep"><img src="https://avatars1.githubusercontent.com/u/6565148?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Nilretep](https://github.com/Nilretep)**
_Tuesday May 30, 2017 at 21:12 GMT_

----

The buff songs are working correctly, they check caster:getWeaponSkillLevel(SLOT_RANGED) and that's how its combining wind+singing or string+singing depending on what instrument you are using. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:10_

----

<a href="https://github.com/LyleVertigo"><img src="https://avatars2.githubusercontent.com/u/26503842?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [LyleVertigo](https://github.com/LyleVertigo)**
_Tuesday May 30, 2017 at 21:20 GMT_

----

Yes, everything else with bard songs is as it should be.

