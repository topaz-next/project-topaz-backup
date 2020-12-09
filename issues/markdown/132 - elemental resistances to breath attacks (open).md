**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:21_
_Originally opened as: project-topaz/topaz - Issue 132_

----

<a href="https://github.com/whb07"><img src="https://avatars3.githubusercontent.com/u/15861355?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [whb07](https://github.com/whb07)**
_Wednesday Aug 31, 2016 at 19:54 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3347_

----

Looked into the issue of breath damage not properly being resisted-
Taking breath damage from fafnir he is still doing upwards of 1k damage to a setup of 268+ fire ele resistance on my WAR. Granted there are some times where I do resist, but its few and far between. I have seen some old forum threads on BG and others where they talk about getting above 200+ ele getting resists was very common, including pictures of a NIN tank taking as little as low 50s dmg on breath attack consistently. Resistance rate needs to be upped in order to open up more jobs and make the elemental resistances worthwhile to bring to HNMs and the like. Thats how other tanks were possible to tank hnms rather than just throwing a paladin at it. 

Edit: forgot link, this was an issue 3 years ago and supposedly fixed breath attacks.
github/DarkstarProject/darkstar/commit/3f165eb6519863b1afd2d1aa5c0bcda5191dc305




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:23_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Sep 01, 2016 at 02:20 GMT_

----

Breath attacks are pretty much normal magical mobskills with +200 magic accuracy, along with damage from HP. On DSP that is.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:24_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Sep 01, 2016 at 16:16 GMT_

----

Actually, I may be wrong about the +200 magic accuracy bonus on breaths, because I can't find it. However, they are using dINT as part of the formula: github/DarkstarProject/darkstar/blob/master/scripts/globals/monstertpmoves.luaDarkstar Issue L483

That would explain why I resisted every breath on my NIN in my nuke set. That... doesn't seem right.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:25_

----

<a href="https://github.com/whb07"><img src="https://avatars3.githubusercontent.com/u/15861355?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whb07](https://github.com/whb07)**
_Thursday Sep 01, 2016 at 18:13 GMT_

----

well like stated before, NIN has access to  a number of +ele resists sets which would help against breath damage or other elemental attacks. Getting above 250+ would mean you were actively resisting a significant portion of the attacks. I am arguing it doesnt resist as much as it should




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:26_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Thursday Sep 01, 2016 at 19:34 GMT_

----

If you can provide some documentation on the expected resist rates. I can tweak the equation.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:27_

----

<a href="https://github.com/whb07"><img src="https://avatars3.githubusercontent.com/u/15861355?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whb07](https://github.com/whb07)**
_Thursday Sep 01, 2016 at 23:16 GMT_

----

BG forum talking on fire resists=
https://www.bluegartr.com/threads/55795-Fire-resist-or-magic-damage
-essentially starts derailing but states 250+ or even breaking 300 is close to getting 0 dmg a considerable number of times from wyrms elemental attacks.

http://rukenshin.livejournal.com/?skip=12
-under "barfira owns tiamat" rukenshin blogs bout having a fire resist set saying 95%+ of fire attacks he resisted from tiamat

ffxi alla forum post:
http://ffxi.allakhazam.com/forum.html?forum=10&mid=118485558530974161&h=50
"When Tiamat is flying in the air, bard carol with crumhorn, and whm barspell is NOT enough, not even close. You need to get into the 270-290 total range to start resisting its attacks. With say about 130-150 in gear, which I understand is not the easiest to obtain, those 260-270 fire shots get reduced to 30 almost full time. To show that there is a tier, at around 240-250ish fire resistance, you rarely resist any attack and take the full 260-270ish damage. "
https://www.bluegartr.com/threads/74070-Question-about-Elemental-Resists-on-gear
-talks on tiers on elemental resists




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:28_

----

<a href="https://github.com/whb07"><img src="https://avatars3.githubusercontent.com/u/15861355?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whb07](https://github.com/whb07)**
_Thursday Sep 01, 2016 at 23:19 GMT_

----

trying to get at is once this issue with elemental attacks from wyrms and other hnms is fixed will open up the game to other possible tanks as was the case in retail with nin/drk, nin/brd, rdm, etc. and not just depending on a paladin to have high innate HP and vitality + aegis to just eat full dmg breath + ele attacks.

Also to add to this, not to derail but the allakahazam thread talks about moves like gates of hades which gives burn can be fully resisted with elemental setup which would make sense. This also opens up a new pathway for bards to actually give a damn about carols or whms meriting bar spells




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:30_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Friday Sep 02, 2016 at 02:11 GMT_

----

Well the aerial attacks are being resisted most of the time at the 270 total resist range, and it doesn't look like breath attacks have a different accuracy calculation so... I haven't been hit by a breath from Tiamat in a very long time so I don't know how the resist rate is at that amount.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:31_

----

<a href="https://github.com/whb07"><img src="https://avatars3.githubusercontent.com/u/15861355?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whb07](https://github.com/whb07)**
_Friday Sep 02, 2016 at 02:24 GMT_

----

It's also calculated for all attacks which are based on elemental magic: i.e wyrm breath, gates of hades for Cerberus, etc. opening up elemental resistance to work brings in more aspects to the current game than possible. As the forums presented state as long as you're properly equipped for the correct elemental attack 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:32_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Sep 02, 2016 at 12:05 GMT_

----

Elemental resistance aside, are breath moves _supposed_ to use dINT or any other dStat?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:33_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Friday Sep 02, 2016 at 13:28 GMT_

----

Thanks whb07, I'll tweak it this weekend.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:35_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Friday Sep 02, 2016 at 15:46 GMT_

----

I don't see why it should be using dINT or anything - breaths aren't even magic damage.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:36_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Sep 07, 2016 at 02:59 GMT_

----

The aspect of Wyrm breath where they do considerably less when standing on paws does not currently function on DSP.

```
angle = mob:getRotPos() - angle;
dmgmod = dmgmod * ((30-math.abs(angle))/30);
dmgmod = utils.clamp(dmgmod, 350, 1800);
```

This provides a much more realistic emulation of their damage.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:37_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Sep 07, 2016 at 03:12 GMT_

----

is that code supposed to be independent? or are you adding it on somewhere?

On Tue, Sep 6, 2016 at 8:59 PM, Deadwing888 notificationsgithub.com
wrote:

> The aspect of Wyrm breath where they do considerably less when standing on
> paws does not currently function on DSP.
> 
> angle = mob:getRotPos() - angle;
> dmgmod = dmgmod \* ((30-math.abs(angle))/30);
> dmgmod = utils.clamp(dmgmod, 350, 1800);
> 
> This provides a much more realistic emulation of their damage.
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> github/DarkstarProject/darkstar - Issue 3347Darkstar Issue issuecomment-245161216,
> or mute the thread
> github/notifications/unsubscribe-auth/ABGI__xZCLr3EF48Dq0t1LxtBCpDLwmiks5qniiXgaJpZM4Jx_4q
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:38_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Sep 07, 2016 at 03:43 GMT_

----

It's in individual breath mobskill scripts, values vary of course.

github/DarkstarProject/darkstar/blob/master/scripts/globals/mobskills/Dragon_Breath.luaDarkstar Issue L29




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:39_

----

<a href="https://github.com/whb07"><img src="https://avatars3.githubusercontent.com/u/15861355?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whb07](https://github.com/whb07)**
_Wednesday Sep 07, 2016 at 04:40 GMT_

----

Where does it account for elemental resistance of player?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:40_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Tuesday Sep 13, 2016 at 00:22 GMT_

----

teschnei 

Sorry for the late response on this. The code I posted is similar looking to the code which can be found in each wyrm breath mobskill lua currently--Firey Breath, Dragon Breath, etc. 

The difference being the angle math it's doing (which I do not understand) but guess and check shows these modified angle values to be the correct ones.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:42_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Sep 13, 2016 at 01:45 GMT_

----

ah, yes - the angle value (prev. 128) is in either direction, so 128 meant
it only went to 0 when standing directly behind (which is of course pretty
wrong)

On Mon, Sep 12, 2016 at 6:22 PM, Deadwing888 notificationsgithub.com
wrote:

> teschnei github/teschnei
> 
> Sorry for the late response on this. The code I posted is similar looking
> to the code which can be found in each wyrm breath mobskill lua
> currently--Firey Breath, Dragon Breath, etc.
> 
> The difference being the angle math it's doing (which I do not understand)
> but guess and check shows these modified angle values to be the correct
> ones.
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> github/DarkstarProject/darkstar - Issue 3347Darkstar Issue issuecomment-246536560,
> or mute the thread
> github/notifications/unsubscribe-auth/ABGI_3085glTbqbLowKZffReEoGWySs9ks5qpezYgaJpZM4Jx_4q
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:43_

----

<a href="https://github.com/whb07"><img src="https://avatars3.githubusercontent.com/u/15861355?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whb07](https://github.com/whb07)**
_Sunday Sep 25, 2016 at 23:44 GMT_

----

any updates?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:44_

----

<a href="https://github.com/nyczducky"><img src="https://avatars3.githubusercontent.com/u/20367923?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nyczducky](https://github.com/nyczducky)**
_Thursday Oct 27, 2016 at 15:38 GMT_

----

As a "fix" for this, I capped the damage done by breath attacks. This is not correct by any means and it is a really shitty way to handle it but at least the wyrms aren't one shotting fire resist PLDs in the meantime:

Go to the breath attacks in scripts\globals\mobskills\NAMEOFBREATHATTACK.lua

Look for this line:
dmgmod = utils.clamp(dmgmod, 50, 1600);

Change the last set of numbers (in this case 1600) to whatever you want the max damage to be.

I personally changed it to 600.

As for the breath radius, I just told people to stand on the wyrms side instead of at it's feet like retail. Not sure if this still works after the mob facing fix.


