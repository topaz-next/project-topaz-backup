**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:49_
_Originally opened as: project-topaz/topaz - Issue 23_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Kthulupwns](https://github.com/Kthulupwns)**
_Saturday Jun 06, 2015 at 18:39 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1526_

----

Not sure if its the formula itself for resistance vs dark magic skill or the spell itself, but it doesn't land nearly as much as it should, a good example would be like nin/drk or rdm drk landing stuns on tiamat fairly consistantly, whereas it's nigh impossible to land 1 10% of the time on pretty much anything over lvl 80




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:50_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Monday Jun 22, 2015 at 08:01 GMT_

----

dumping on maxtherabbit 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:51_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Monday Jun 22, 2015 at 08:18 GMT_

----

The problem is I have no idea how to rebalance the equation here

local dINT = caster:getStat(MOD_INT) - target:getStat(MOD_INT);
    local resist = applyResistanceEffect(caster,spell,target,dINT,37,0,EFFECT_STUN);
    if(resist <= (1/16)) then
        -- resisted!
        spell:setMsg(85);
        return 0;
    end

```
if(target:hasStatusEffect(EFFECT_STUN)) then
    -- no effect
    spell:setMsg(75);
else
    if(target:addStatusEffect(EFFECT_STUN,1,0,duration*resist)) then
        spell:setMsg(236);
    else
        spell:setMsg(75);
    end
end

return EFFECT_STUN;
```

end;




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:52_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Monday Jun 22, 2015 at 08:33 GMT_

----

it looks like thats not the actual problem
the problem is that dark magic skill is actually being calculated into stuns accuracy.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:54_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 23, 2015 at 10:16 GMT_

----

> the problem is that dark magic skill is actually being calculated into stuns accuracy.

That is not the problem, that is supposed to be happening. On retail you can stack +dark skill gear to increase success rate on high resistance mobs. Problem has to lie elsewhere, especially if you are only seeing the problem on specific mobs or at specific level ranges. 

A mobs lv, thunder resistance, stun resistance, int, and magic evasion stats will all aid its resistance while a players level, dark magic skill, int, and magic accuracy will aid in landing the spell. Maybe the level correction bits don't fair so well on higher levels? I've never seen the math for how that is done on retail, only how DarkStar does it in a handful of places like ranged ammo with add effects so I really can't be sure. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:55_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Tuesday Jun 23, 2015 at 19:24 GMT_

----

well i mean as a drk with Maxed merits on stun and + drk skill 75 cap i can barely land stuns on sky gods let alone jailers or tiamat, and a rdm/drk with a really low grade int dark skill should be able to land them at least 90% of the tiem




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:56_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Sunday Jun 28, 2015 at 05:35 GMT_

----

If MOD_STUNRES could be configured to accept a negative value, we could just lower stun resistance on every mob that matters? Or maybe add 50 magic accuracy on top of what gets calculated via dark magic skill etc?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:57_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Jun 28, 2015 at 06:43 GMT_

----

nobody is going to remember to add negative stun resistance every time they
add a new mob

the solution is not to throw random bonus accuracy for no reason, it is to
fix the actual resistance formula

On Sat, Jun 27, 2015 at 11:35 PM, Deadwing888 notificationsgithub.com
wrote:

> If RES_STUN could be configured to accept a negative value, we could just
> lower stun resistance on every mob that matters? Or maybe add 50 magic
> accuracy on top of what gets calculated via dark magic skill etc?
> 
> —
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 1526Darkstar Issue issuecomment-116196370
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:59_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Sunday Jun 28, 2015 at 12:07 GMT_

----

the base resistance formula is correct as far as I can tell, one option is to use the bonus param in the call to applyResistanceEffect(caster,spell,target,dINT,37,0,EFFECT_STUN);

the '0' param is bonus macc




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:00_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Jun 28, 2015 at 18:25 GMT_

----

well, I wrote the resistance formula and I definitely made up a ton of shit for it 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:01_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Thursday Jul 02, 2015 at 14:20 GMT_

----

Is there any info I could lift from retail that would help you with this?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:02_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Monday Jul 06, 2015 at 00:30 GMT_

----

I'm going to say that Flash is another spell that's supposed to have higher than usual accuracy. It almost never fully resists on retail.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:04_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Monday Jul 06, 2015 at 13:55 GMT_

----

a while back I reviewed the base magic resistance calculations and they appeared correct based on all information I was able to find online

it is my belief that either:
1) certain spells like flash and stun simply have bonus accuracy, in which case it would be appropriate to use the bonus param
or 2) divine magic and dark magic obey different rules from elemental and enfeebling with respect to resistance - this could be tested on retail by comparing drain/aspir and banish resistances against dsp




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:05_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Sunday Sep 20, 2015 at 07:14 GMT_

----

I been looking into magic resistance for a while now. I definitely believe flash / stun are special spells that have a bonus magic accuracy. They do not act like regular spells, I used to play blm and stun would rarely get resisted.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:07_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Thursday Oct 15, 2015 at 10:43 GMT_

----

bendangelo Any update on stun?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:08_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Thursday Oct 15, 2015 at 13:33 GMT_

----

I need a data point. I would say change to rdm/drk and chainspell stun an IT. Tell me the total number of casts and the number of resists.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:09_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Oct 15, 2015 at 14:32 GMT_

----

By the way, I was digging around for sudden lunge sets when I found someone
on xiah mention that the spell stun had bonus macc that head butt and
sudden lunge did not, if that helps




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:10_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Thursday Oct 15, 2015 at 16:23 GMT_

----

Yeah flash / stun / dispel / magic finale. They must all have a magic bonus of no higher than 50 because the formula just doesn't work for those spells. I'll probably hop onto retail and test it out later.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:12_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Oct 15, 2015 at 16:28 GMT_

----

Possibly Actinic Burst as well. If it doesn't, well then the 200 bonus mag acc it currently has should be removed, heh.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:13_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Thursday Oct 15, 2015 at 16:37 GMT_

----

That should be removed, with 200 magic acc it can land flash on anything




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:14_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 15, 2015 at 16:40 GMT_

----

I think that was the idea when it got added. Whoever added that assumed it'd work like the spell flash, which is crazy accurate.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:15_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Thursday Oct 15, 2015 at 16:57 GMT_

----

The thing is that's overkill, you'll end up always landing flash on Kirin and magic resistant mobs. It has to be balanced in some way. I think 50 magic accuracy is reasonable or maybe even 75.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:16_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 15, 2015 at 20:40 GMT_

----

Depends. In the case of that blu spell, it may not even be correct to have the bonus at all. I have no idea. Just stating what I think the thought was by whoever.

Somewhat unrelated thought, but: do we floor/cap the hit rate after all the math is done?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:18_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 15, 2015 at 20:41 GMT_

----

"does DSP" do that, I should say.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:19_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Thursday Oct 15, 2015 at 21:45 GMT_

----

Yeah magic is capped at 5-95%




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:20_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Oct 15, 2015 at 21:46 GMT_

----

Isn't floor 20?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:22_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Thursday Oct 15, 2015 at 21:48 GMT_

----

Floor is currently 5




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:23_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Oct 15, 2015 at 22:00 GMT_

----

I mean supposed to be




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:24_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Thursday Oct 15, 2015 at 22:07 GMT_

----

From what I've seen it's been 5%. http://ffxiclopedia.wikia.com/wiki/Magic_Hit_Rate




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:25_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Oct 15, 2015 at 22:18 GMT_

----

Ah, silly being different from melee hit rate..




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:26_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Oct 15, 2015 at 22:57 GMT_

----

Well if it were 20% it'd be pretty easy for a few people to say... spam silence on things like Suzaku. So probably balance reasons.


