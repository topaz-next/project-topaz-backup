**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:12_
_Originally opened as: project-topaz/topaz - Issue 47_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 20, 2015 at 13:33 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2109_

----

In retail a 2 man party cannot hold claim over 12 mobs. 1 claim per character, and if in a party any one member switches targets to a different monster, claim gets lost (I think of that part more as feature, not a bug >.> hated losing claim via stupid in retail). For the purposes this issue, consider pets as if they were their master: a single bst+pet gets 1 claim and pet changing target would lose claim, last I knew.

Claim should remain as long as:
1) somebody has non zero enmity with the mob
2) Nobody from the party has switched to another mob
3) Possibly things I have forgotten will hold a mob.

An unclaimed mob (smn astral burn party anyone?) would still give exp / gold / drops to the party that caused its death as long as: 
1) The reason is isn't claimed is **_not**_ from claim **_loss**_ (monster lost interest / lack of enmity).
2) Their party got the killing blow.
3) they were still in exp range. 
4) exp wasn't "dirtied" by non party members attacking it - this applied to the exp part only, not loot. (saw that check in the core already, so I believe this part is implemented)

That's everything I can think of right now. Unless retail nerfed both astral burns and fell cleave burns after I quit, that should be how it works.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:14_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Sunday Sep 20, 2015 at 21:18 GMT_

----

Ok so how does it currently work? How does it differ from that?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:15_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 20, 2015 at 21:30 GMT_

----

Currently, I can claim and keep claim on many monsters at once, declaiming doesn't seem to make sense at all - I can keep a monsters attention forever without trying, yet often dot killing a mob it will lose claim before expected (someone opened an issue that I think is about that), pets hold a claim separate from their owners, and switching my engage target to another mob or casting on another mob does not trigger claim loss.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:16_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 20, 2015 at 21:30 GMT_

----

So pretty much..everything?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:17_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Monday Sep 21, 2015 at 22:41 GMT_

----

I'm glad Teo added this, and I can confirm everything he said is still how it works in retail.

I'll describe some additional things I noticed, perhaps it will inspire an easy and logical way to do the coding. 

Basically if you were in an alliance say at Tiamat and your alliance had claim on the mob, it's always one individual person that's actually got the claim and this person is shifting around constantly. For instance if your weapon swings you've "got the claim" until someone else's weapon swings or until someone else casts a spell or action on it. You'll notice the name shifting from red (claimed by current party) to reddish purple (claimed by another party in the alliance) a lot due to this. To people watching from the outside the name should stay completely purple (claimed by someone else).

Now this means that if I swing my weapon and immediately drop party then I essentially take Tiamat with me, he will go purple to the entire old alliance and will only be red for me. I can at this point take him to a new party or alliance via a party invite (none of this changes based on current party hate, he could be attacking the old alliance's tank even though they no longer have claim).

Now the act of disengaging your weapon (or dieing with your weapon drawn) when you've "got the claim" relinquishes your claim on the mob. If you're solo, the mob will go white. If you're in an alliance that claim will shift to the next person down in the list, but if it can't find anyone the mob will go white. Now if the mob goes white in this fashion and another alliance wants to steal it, it's not enough that they tag it or swing their weapon, they have to perform an action on it while they are Darkstar Issue 1 on the hate list. If nobody in the wiping alliance had hate higher than a provoke, then provoke would steal the claim. If a healer had a lot of hate the tank might need to flash > invincible > shield bash to take claim. During this time if anyone from the original alliance manages to perform any action on Tiamat the claim will go back to them.

I'm glad Teo brought up the 1 claim per person thing because there are a couple of scenarios in which it's important that the claim system should work something like this. 

In the first scenario a red mage gathers up all the beastmaster mobs in let's say middle of delkfutt's tower and has active claim on all of them. Now they summon pets with low HP which are white. Now a black mage can come along and -aga these pets **without hitting the beastmasters** because the red mage has claim on all of them. This sort of thing leads to massive exp/hr which would be impossible in retail in this fashion.

The second is while a person is solo holding an HNM and gets an add. In retail you were in real trouble because you couldn't sleep or do anything to the add or you'd lose claim on the HNM.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:19_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 21, 2015 at 23:37 GMT_

----

Deadwing brings up some important details with good examples. I forgot about the red>purple>red>purple claim thing, right now DSP doesn't even have both colors because the packet was being a pain in the rear last time it got refactored.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:20_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Sep 22, 2015 at 00:12 GMT_

----

i am never touching that godforsaken packet ever again




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:22_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 22, 2015 at 00:13 GMT_

----

:laughing: 


