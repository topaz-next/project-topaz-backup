**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:33_
_Originally opened as: project-topaz/topaz - Issue 66_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Thursday Nov 26, 2015 at 23:02 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2440_

----

I'm making this to summarize everything off about the crafting system. Issues Darkstar Issue 1357 Darkstar Issue 2391 would be fixed as a result of fixing the following retail inconsistencies:
- [x] 1) In retail there is no such thing as fractions of a crafting skill level-- it is always a whole number. Day/Moon/Direction ~~do influence HQ rate~~ **do not influence HQ rate (Source: https://www.reddit.com/r/ffxi/comments/4ulgh1/official_ffxi_developer_ama_with_producer_akihiko/d5qp5k5)**, but they do not directly affect skill level. Simply removing this will fix the two issues listed above automatically. 

**EDIT: They are disabled by default, so server owners have to go out of their way to turn them on and go non retail. Seems fine to me.**
- [ ] 2) Darkstar is slightly too generous with T1 HQs. I have no parses to back me up on this, but as a level 100 crafter on retail my calculations for the base rate of HQ were: 
  T0= 0-10 skill above cap = 1/64 hq rate
  T1= 11-30 skill above cap = 1/16 hq rate
  T2= 31-50 skill above cap = 1/4 hq rate
  T3= 51+ skill above cap = 1/2 hq rate

~~Now I do believe day direction and moon all played a slight roll in HQ rate, but the key word here is slight. A 10% bonus for correct day and 10% penalty for incorrect day sounds about right to me. Moon and direction had even less effect ~5% tops. So T1 on correct day and moon would be roughly 1/14 synths hq.~~ **This information would have made it more correct than it was, but it turns out they have no effect at all as per the above source.**
- [ ] 3) Subcrafts should matter when it comes to HQ tier. With main craft 50 levels over and subcraft 11 levels over would result in a T1 hq rate.
- [x] 4) Uncapping your FPS will cause you to craft ~4x faster with a good GPU.
- [ ] 5) Going to the synthesis history menu and spamming enter fast enough will result in being able to craft without crystal in inventory. Darkstar Issue 2051 
- [ ] 6) On retail I never saw a a skillup value higher than .1 after passing level 60. 
  It was always my belief that skillups higher than .1 ceased after level 60; ~~although I have since been told I was wrong about this.~~ (I'm like 90% sure this was a thing)
- [ ] 7) Skillups are slightly too easy to earn at the lower levels, and become slightly too hard at the highest levels. It's close enough to be workable, but it's not quite right. Again, no parses to back me up.
- [x] 8) Darkstar Issue 2434 
- [ ] 9) The current crafting furniture doesn't affect skill level at all. It should add 1 skill level for one piece, and 1 skill level + a reduction to items lost on breaks for both pieces. Additionally on retail it is possible to stack furniture with elemental strength and that will reduce synth breaks of crystals of that element. Lots of fire furniture = less fire synth breaks.
- [ ] 10) There are certain synths for which the materials are never lost with breaks (for example lu shang's fishing rod repair) and certain synths for which the materials are always lost in breaks (for example relic steel)

Source: I had level 100 smithing in retail, 4 crafts 90+ on Nasomi




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:34_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Nov 26, 2015 at 23:38 GMT_

----

not going to do anything about day/moon/direction unless it can be 100% confirmed either way - my experience is it does not, so it will stay that way by default (the setting can be changed to affect rate instead of level, though)

for 4, that's client-side - is the server stopping subsequent synths?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:35_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Nov 26, 2015 at 23:41 GMT_

----

At any rate, issue "groups" are very annoying to deal with as you can't
mark certain parts as closed unless someone edits the original post (and
the title is not as descriptive)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:36_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Thursday Nov 26, 2015 at 23:54 GMT_

----

I can 100% confirm day/moon/direction do not affect skill in retail.

As for hq rates I can tell you it's currently boosting them by too much but can't give you rock hard numbers on what the correct rates should be.

I'll keep the issue groups thing in mind, and for this one I'll try to stay on top of editing strikethroughs into issues fixed by pull requests.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:37_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Friday Nov 27, 2015 at 00:21 GMT_

----

sorry, I was more clear in my first draft of the previous post before I removed it... I was referring specifically to day/moon/direction affecting HQ rates (already knew it didn't affect skill)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:38_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Friday Nov 27, 2015 at 01:15 GMT_

----

Correct me if I'm wrong but day/direction/moon currently affect hq rates on darkstar do they not?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:39_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Dec 02, 2015 at 03:47 GMT_

----

By default only the day affects it IIRC. But you can toggle each one in one of the config files.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:41_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [xipies](https://github.com/xipies)**
_Monday Dec 07, 2015 at 02:37 GMT_

----

(Assuming I understand the code / math correctly.)

There's no actual way direction can impact hq rates (apart from Darkstar Issue 2391). Direction is only +/- .5 and it takes a whole number of skill level change to have any real effect in hq rate.

Only moon/day have specific if/switch cases for directly affecting hq rate.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:42_

----

<a href="https://github.com/ZirkPrime"><img src="https://avatars3.githubusercontent.com/u/17181229?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ZirkPrime](https://github.com/ZirkPrime)**
_Thursday Feb 11, 2016 at 16:34 GMT_

----

Just FYI but I think these two links are the best sources of retail crafting behavior we have.
https://www.bluegartr.com/threads/57123-Before-you-ask-a-stupid-crafting-question-read-this!
https://www.bg-wiki.com/bg/Category:Craft

On some specific points Deadwing raised:

> There is to date absolutely no solid evidence to support a correlation between HQ rates and day, moon phase, direction, or any of the other voodoos various crafters have come up with over the years.
> 
> If your total skill is 10 or less over the item's skill cap (T0), the chance of a HQ synth is approximately 1~3%. (~1/64)
> If your total skill is between 11 and 30 over the item's skill cap (T1), the chance of a HQ synth is approximately 5~7%. (~1/16)
> If your total skill is between 31 and 50 over the item's skill cap (T2), the chance of a HQ synth is approximately 25%. (1/4)
> If your total skill is more than 50 over the item's skill cap (T3), the chance of a HQ synth is approximately 50%. (1/2)
> HQs with a total skill below the cap (T-1) have not been confirmed.
> 
> Above 60, skillup increments are always 0.1.
> 
> Under 50 skill, you have approximately between 66% to 75% chance to skill up on a successful synth.
> At or above 50 skill, you have approximately a 25% chance to skill up on a successful synth.


