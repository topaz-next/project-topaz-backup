**Labels:**

focus

help wanted

research needed



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 07:59:19_
_Originally opened as: project-topaz/topaz - Issue 513_

----

# QUESTIONS
## *Temenos*
### **Temenos North**
- Floor 1:
  - Does only the upper Slaughterman need to be killed for chests to spawn, or both, or random? **both**
  - Do chests always spawn at the same spot? If you kill the upper Slaughterman then the lower Slaughterman, do they spawn by the lower one? **spawn by last Slaughterman killed**
  - Do only Dustman open the door to the next floor, or can a Slaughterman? **only Dustman**

- Floor 3:
  - Does only the BRD need to be killed for chests to spawn, or BRD and WHM, or random? **same as floor 1**
  - Do chests always spawn at the same spot? If you kill the BRD then the WHM, do they spawn by the WHM? **same as floor 1**
  - Do only MNK and DRG open the door to the next floor, or can a BRD/WHM? **MNK and DRG**

- Floor 5:
  - Does the door always open on the first Antica killed? **yes**

- Floor 6:
  - Does only the Skulker need to be killed for chests to spawn, or the Skulker and the Charmer, or random? **same as floor 1**
  - Do chests always spawn at the same spot? If you kill the Charmer then the Skulker, do they spawn by the Charmer? **same as floor 1**
  - Does the first Designator or Abductor killed always open the door? **yes**

### **Temenos West**
- Is it possible to get more than 3 chests on 1 floor or multiples of the same chest? **no**

### **Temenos Central 2**
- How does killing the elementals/avatars effect Carbuncles damage taken/resistance? **[link](https://github.com/project-topaz/topaz/issues/513#issuecomment-650861989)**

### **Temenos Central 4 (Ultima)**
- How does Nuclear Waste Elemental Resist Down effect work? Does it last a certain amount of time, or wear off when hit by the next ability, or some combination? **random duration 1-3 mins?**

### **Temenos Central Basement**
- How are coin drops actually determined? (wiki says 1 coin per RR, I experienced 1->2->4 drops.) **it appears to be 1->2->3 for each reraise, with the rare possibility of one or possibly all 3 adding a +1, e.g. 2->2->3, 1->3->3, 1->2->4**
- Which Aerns are actually the time extensions? Is it completely random, random within set groups, or set mobs? **[link](https://github.com/project-topaz/topaz/issues/513#issuecomment-652149187)**

## *Apollyon*
### **NW Apollyon**
- How does killing the normal mobs effect the floor boss? **[link](https://github.com/project-topaz/topaz/issues/513#issuecomment-653620469)**

### **SW Apollyon**
- Floor 1:
  - Is it random if the chests or portal spawns first?

### **CS Apollyon**
- What are these mobs weakness/resistance numbers? **[link](https://github.com/project-topaz/topaz/issues/513#issuecomment-653645064)**

# ISSUES
- Rocs shouldn't be linking with birds in NE Apollyon.
- Mobs 16933045 and 16933046 (Barometz, Borametz) should be groups 98 and 99, while 16933055 and 16933056 should be groups 38 and 39.
- Apollyon time extensions are wrong duration.
- Apollyon Elementals shouldn't link. Same-type linking is handled in mob scripts.
- NW Apollyon Apollyon Scavenger should pick from 5 (not 6) mobs when choosing the portal mob for floor 4. [link](https://github.com/project-topaz/topaz/blob/d00576bbfef00c8560526e51cef0413188191cd3/scripts/zones/Apollyon/mobs/Apollyon_Scavenger.lua#L70)
- Chest spawn mechanics and placement in Temenos North floors 1, 3, and 6.
- Nuclear Waste elemental resistance down status effect duration is incorrect, and should not be removed on additional mobskill usage.
- Coin drop mechanics and time extension randomness in Temenos Central Basement are incorrect.
- Cynoprosopi in NW Apollyon needs strength/weaken mechanics.
- Mimics do not draw in (draw in needs a maximum range set)
- Borametz, Barometz, Jidra, Kerkopes should probably be a random ID, but involves changing flags/model for that ID (large Borametz, Barometz, Kerkopes, leafless Jidra).
- Proto-Omega is missing Target Analysis.

# NEEDS TESTING/ADJUSTMENT
- All mob stats.
- All mob drops/rates.
- All chest drops/rates.


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Friday Jun 05, 2020 at 16:43:15_

----

Temenos - Northern Tower (did 4-5 runs back to back):

General observations:

Armoury Crates:
Brown/gold: items.
Brown/gray: HP/MP.
Blue/gold: time.
![FLOOR 2 ARMOURY](https://user-images.githubusercontent.com/40763842/83902763-4898ec00-a75d-11ea-8f8e-5049a113a340.jpg)

Armoury Crates order may vary when they spawn (for example, from left to right: Brown/gold, brown/gray and blue/gold and on another run the total opposite) but NOT their spawning position (when meeting conditions ie. killing trigger mob 1 or 2 last). They'll share 3 IDs (per group of 3 Crates), no matter if they're HP/MP, items or time.
Every mob's job is retail accurate, based on the BGWiki list below.
Each mob will use their 1hr ability (unless you one shot them).
Followed BGWiki maps: https://www.bg-wiki.com/bg/Northern_Temenos (I corrected some and/or included Armoury Crates spawn locations and mobs path (red line)/standing points (black)).
Position and mobs level can be found here: https://github.com/KnowOne134/NPC-MOB-Logger.

Floor 1:
![TemenosN_Floor1](https://user-images.githubusercontent.com/40763842/83901993-e986a780-a75b-11ea-9d8b-8591726bc8cc.jpg)

Killing one of the four RDMs will open the door to the next floor.
Armoury Crates will spawn when the last of the two Goblin Slaughterhouse will die, on the spawn point of the last one you killed.
RDMs from the first toom are moving back and forth, not side by side, in parallel (16928776 and 16928777). Marking a pause of 3 seconds each time they reach one side of the room.
RDM 16928775 is moving back and forth (will mark a pause of 8 seconds each time he's moving to one side).
RDM 16928774 is moving back and forth (will mark a pause of 8 seconds each time he's moving to one side).
First WAR (when entering) is 16928773.
Last WAR is 16928772.

First Goblin Slaughterman (when entering the zone) killed last:
Items (16928771).
HP/MP (16928770).
Time (16928769).
BGWiki map: Armoury Crates placement was not displayed.

Last Goblin Slaughterman killed last:
Items (16928769).
HP/MP (16928771).
Time (16928770).
BGWiki map: Armoury Crates placement is correctly displayed.

Floor 2:
![TemenosN_Floor2](https://user-images.githubusercontent.com/40763842/83902037-ff946800-a75b-11ea-9193-f04f191c7690.jpg)

Skadi - BST (has no pet, uses Charm as a 1h animation).
Kari is moving around the square, stopping at each corner for 5 seconds. The other 3 are static.
Killing Kari will open the door to the next floor. Not the other ones.
Armoury Crates will spawn when the last Giga will die, in the middle of the room.

Items (16928780).
HP/MP (16928779).
Time (16928778).
BGWiki map: Armoury Crates placement is slightly wrong.

Floor 3:
![TemenosN_Floor3](https://user-images.githubusercontent.com/40763842/83902049-028f5880-a75c-11ea-8b88-7f5001627ae0.jpg)

Killing the DRG or one of the MNKs will open the door to the next floor.
Armoury Crates will spawn when the last Sahagin, the White Mage or the Bard will die, on the spawn point of the last one you killed.
The MNK in the first room is 16928793.
The two MNKs and the DRG are moving back and forth in both rooms, marking a stop when crossing each other (5 seconds pause).

Telchines White Mage killed last:
Items (16928786).
HP/MP (16928785).
Time (16928787).
BGWiki map: Armoury Crates placement was not displayed.

Telchines Bard killed last:
Items (16928787).
HP/MP (16928786).
Time (16928785).
BGWiki map: Armoury Crates placement is correctly displayed.

Floor 4:
![TemenosN_Floor4](https://user-images.githubusercontent.com/40763842/83904570-6287fe00-a760-11ea-8b9f-401c68780684.jpg)

Killing one of the four BLMs will open the door to the next floor.
Armoury Crates will spawn when the last Demon from the middle of the room, the WAR, the DRK or the SMN will die, in the middle of the room.
The first two BLMs (when entering) moving back and forth are from left to right are 16928804 and 16928805.
The two BLMs (on the other side of the room when entering) moving back and forth are from left to right are 16928802 and 16928803.
They marking a 5 seconds pause each time they reach the side of the room.
Kindred Summoner's Elemental is already summoned when entering the floor.

Items (16928795).
HP/MP (16928794).
Time (16928796).
BGWiki map: Armoury Crates placement was not displayed.

Floor 5:
![TemenosN_Floor5](https://user-images.githubusercontent.com/40763842/83902063-07540c80-a75c-11ea-85ce-943cebf3ffd5.jpg)

Killing any of the Antica will open the door to the next floor.
Armoury Crates will spawn when the last Antica will die, on top of the intersection of both rooms.
They're all static.

Items (16928807).
HP/MP (16928806).
Time (16928808).
BGWiki map: Armoury Crates placement is wrongly displayed (wrong position).

![FLOOR 5 ARMOURY](https://user-images.githubusercontent.com/40763842/83902662-1c7d6b00-a75d-11ea-9d6e-82c9df1d6ec1.jpg)
(floor 5 "weird" disposition of Crates)

Floor 6:
![TemenosN_Floor6](https://user-images.githubusercontent.com/40763842/83902064-091dd000-a75c-11ea-81d9-c3240171dd63.jpg)

Killing one of the SMNs/THFs will open the door to the next floor.
Armoury Crates will spawn when the last Cryptoberry, the NIN (Skulker) or the BLM (Charmer) will die, on the spawn point of the last one you killed.
16928822 and 16928823 are the two Cryptoberrys moving together when arriving, staying almost side by side and moving back and forth in front of the Cryptoberry Skulker (pausing 8 seconds each time).
16928818 is the solo Cryptoberry Designator moving back and forth too (from left to right) on the right side of the map (pausing 25 seconds each time).
16928826 and 16928827 are the two Cryptoberrys moving together when moving past the first round of mobs, staying almost side by side and moving back and forth in front of the Cryptoberry Charmer (pausing 8 seconds each time).
16928819 is the solo Cryptoberry Abductor moving back and forth too (from left to right) on the left side of the map (pausing 25 seconds each time).
Two Tonberry's Elemental that were missing from the NPCL logs:
16928824 and 16928828.

Cryptoberry Skulker (NIN) killed last:
Items (16928814).
HP/MP (16928813).
Time (16928815).
BGWiki map: Armoury Crates placement is correctly displayed.

Cryptoberry Charmer (BLM) killed last:
HP/MP (16928815).
Items (16928813).
Time (16928814).
BGWiki map: Armoury Crates placement was not displayed.

Floor 7:
![TemenosN_Floor7](https://user-images.githubusercontent.com/40763842/83902070-0ae79380-a75c-11ea-8dc6-d43dcdcb83da.jpg)

Armoury Crates will spawn when the last Goblin will die (even if you started with the Warlord (DRK) one), in the middle of the room (where the DRK was standing).
They're all static, RDMs and BLMs around the DRK facing "outside" of the circle.
Mobs from floor 7 can drop up to two Ancient Beastcoins (other floors is 1 maximum).

Armoury Crate (16928830) (keep the same ID no matter the run, brown/gold color).
BGWiki map: Armoury Crates placement was not displayed.



----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Thursday Jun 25, 2020 at 02:29:36_

----

(still open to have things double checked, general observations)
Followed BGWiki pages (will list if there's more to it): https://www.bg-wiki.com/bg/Category:Limbus.

**TEMENOS - WESTERN TOWER**:
(3 runs, back to back)

I was unable to get more than 3 Caskets pop on a single floor, nor having multiple ones of the same type.
BGWiki says there's a possibility of not having any Casket pop on a floor, didn't experienced it, there was always one minimum per floor.
Caskets pop where the mob dies, no matter where he is.

**CENTRAL TEMENOS - 4F** (Proto-Ultima):
(2 runs, back to back)

BGWiki: "Chips traded become dim, and so cannot be used again. Similar to BCNM orbs. "
Wrong, they just removed from your inventory upon trading.

Every model of Caskets is the same one on the floor: gold/brown.
You can get up to 3 AB/mob, spawning from Caskets (when you open the _wrong_ one).

![LimbusFloor4](https://user-images.githubusercontent.com/40763842/85645704-cedc8a00-b69a-11ea-99da-5873f285a840.jpg)
(BGWiki map)

Casket showed in the middle of the map is wrongly displayed, there's 3 there:
![img_20200625_020724](https://user-images.githubusercontent.com/40763842/85645847-24189b80-b69b-11ea-9553-495a7ecb317d.jpg)

---

Proto-Ultima seems to Attacks every 2 seconds and sometimes have Double Attack.

**Nuclear Waste** (6 times, landed 3, missed 3):

Nuclear Waste has no sign of it landing in the chatlog, nor one when it wears off. Not even displayed in the status bar. The only one showed is when it misses:
![img_20200625_032820](https://user-images.githubusercontent.com/40763842/85646175-d0f31880-b69b-11ea-9794-37277e0af939.jpg)

The only way to see if it landed (and when it wears off) is through the equipment menu, which showed, as a THF99/DNC49 without any elemental resistance:
![img_20200625_032328](https://user-images.githubusercontent.com/40763842/85646237-f97b1280-b69b-11ea-9479-7b7c4c79ebf7.jpg)

It's duration seems to be random:
1st time: 1+ minute.
2nd time: 2 minutes and 05 seconds.
3rd time: 2 minutes and 39 seconds.

It doesn't wear off if Proto-Ultima lands another TP move on top of it, in this case he used Flame Thrower (100% damages).


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Monday Jun 29, 2020 at 01:59:38_

----

### **Temenos Central 2**

>     How does killing the elementals/avatars effect Carbuncles damage taken/resistance?


- helix damage 23, shoots to 250 after corresponding element's ele kill
- next kill jumps the damage to 349 per unlocked helix
- no further reduction on the whole with each kill, just unlocks the element for full 349 damage
- no apparent regen or regain, though at one point when i looked away while weakened carby gained 20% on second fight. my only guess is an unlogged cure, it typically was not regenning even when unclaimed. will need additional validation.
- mdb remains pretty high though. in an (admittedly) non nuking lvl 75 set on 99 sch with a chicken knife, my tier 1s hit between 0-85 after unlocking the element
- carbuncle starts out with either: a very high attack speed, an offhand hit like a monk/dual wield, or a 100% rate of double attack. 
- perhaps a bug, but killing the mystic avatar last did not increase my helix damage, cryohelix remained ~20 damage. this is directly against what the wiki says
- attack damage from carbuncle remains consistent, as well as damage on it, no apparent reduction after each elemental kill
- diabolos' nether blast did not see any upped damage until at least 5 ele/avatars died, and i believe all (just became unable to stay alive on 75....74 smn) straight 231 damage from nether blast jumped to 342
- killing "unaffiliated" light eles did not confer additional bonus to nether blast

> All mob drops/rates.
> All chest drops/rates.

- light elementals and carby are loot pinatas and consistently dropped 7 coins. eles and other mystic avatars dropped 1-2.
- final crate 6 abcs, 1 af upgrade item, and cerulean chip both runs

sch run with helix damage
https://www.dropbox.com/s/8g8hug2yptz4uod/central%20temenos%202%20smn.rar?dl=0
smn run with nether blast
|https://www.dropbox.com/s/8g8hug2yptz4uod/central%20temenos%202%20smn.rar?dl=0

video just to see attack speed (logs all cut off :()
https://youtu.be/hK52WFRwXtw
things still needed:
is there a regen below 50% i missed or was that just a light ele curing it/healing ruby not caught in the logs
how much does searing light do when no eles are dead? all eles did 1166 to a 75 smn in crappy gear


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Jul 01, 2020 at 02:26:33_

----

Temenos Central Basement

>   How are coin drops actually determined? (wiki says 1 coin per RR, I experienced 1->2->4 drops.)
it seemed entirely random whether 1-4 coins dropped, but never experienced 4 on first kill.

 Which Aerns are actually the time extensions? Is it completely random, random within set groups, or set mobs?
it appears completely random. we received TEs from all jobs, all group sizes. it is upon death of the mob (i.e. when it winks out of existence)
rough notes run 1, run 2 took better notes. 6 total 5 minute TEs
- 4 coins is extremely rare
- 1 reraise is most common

16929058 RDM         run 2: 2, 2
16929060 BST 1, 1    run 2; 1,2,TE
16929053 MNK 3     run 2: 1,3
16929054 SAM        run 2: 1,2,3
16929057 WHM 1, 2  run 2: 1,2,4
16929061 NIN 2         run 2: 1,2
16929062 DRK TE       run 2: 1,2
16929069 DRG 2       run 2: 1,2,3
16929071 WHM 2     run 2: 1
16929072 BLM 3      run 2: 1,3,3 TE
16929073 BST 1, 2   run 2: 1
16929063 RNG 1,3,3  run 2: 1
16929064 BLM 2,2   run 2: 1,2
16929075 RNG         run 2: 2,2
16929083 BRD 1, 2   run 2: 1,2,4
16929085 DRK         run 2: 1,2
16929084 MNK 1,2,3  run 2: 1,2,3 TE
16929086 NIN 2,2,3    run 2: 1,2
16929055 DRG           run 2: 1,2,4
16929065 WAR 2       run 2: 1,2
16929066 SMN 1       run 2: 2,2 TE
16929082 RDM 1,1    run 2: 1,2 TE
16929079 SMN 2,3    run 2: 1,2
16929078 PLD          run 2,2
16929082 RDM, 4        run 2: 1,2, TE
16929077 THF 2, 4, TE   run 2: 1,2
run 1: 8 coins in crate
run 2: 8 coins in crate
run 1 https://www.dropbox.com/s/x2tacxlwoh72z27/central%20temenos%20basement%202.rar?dl=0
run 2 https://www.dropbox.com/s/3pt3jwlov04nrnc/central%20temenos%20basement%203.rar?dl=0
jobs stay the same, and the ghrah mob has some innate fast cast as well as high MDB and defense. probably pld/blm for job
ghrah is immune to silence, sleep, bind, gravity, and break
aern have no immunities
aggro range is pretty small 7 yalms or less, but they do aggro. aerns are able to summon their pets while asleep.




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 01, 2020 at 20:38:53_

----

> aerns are able to summon their pets while asleep

I wish _we_ could break the rules like that!


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Jul 03, 2020 at 16:46:54_

----

### **NW apollyon** - 

> How does killing the normal mobs effect the floor boss?

other than the dragon, who is CONSIDERABLY affected by mob kills, no bosses are affected by killing the other mobs in the area.
interesting notes:
pluto possesses addl effect paralysis on his attacks. did not see this noted anywhere.
zlatorg can mighty strikes at 100%
cyanoscopi possesses mdt, increased damage (double) until all mobs are killed.  0 dmg helices, unable to chekc after 4 as i kept dying from his hits, but end result was 150 dmg helices after all mobs dead, so most likely mdt scales with the attack values.
@ no mobs dead - 950 dmg on 99 sch with no protect wearing level 75ish gear
@1 mob dead same
@2 mob dead damage reduced per hit to 834
@3 mobs dead damage at 813
theory - every 2 mobs dead decreases values?
@4 701 damage
@5 dead ~450 damage, so my guess is its attack is halved.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Jul 03, 2020 at 18:34:43_

----

### **CS Apollyon**

> What are these mobs weakness/resistance numbers?

yagudo per wiki are Weak to Blunt, resistant to Piercing and nukes 
blunt: [13:57:18] Titan uses Megalith Throw.The Yagudo Archpriest takes 918 points of damage.
blunt: [14:04:52] Ifrit uses Flaming Crush.The Yagudo Archpriest takes 1726 points of damage.
blunt: [14:05:59] Shiva uses Rush.The Yagudo Archpriest takes 3148 points of damage.
piercing: [14:01:00] Garuda uses Claw.The Yagudo Archpriest takes 402 points of damage.
piercing: [14:13:15] Fenrir uses Crescent Fang.The Yagudo Archpriest takes 540 points of damage.
slashing:  [14:02:00] Garuda uses Predator Claws.The Yagudo Archpriest takes 3172 points of damage.
slashing: [14:03:10] Leviathan uses Spinning Dive.The Yagudo Archpriest takes 2689 points of damage.
magic: [14:16:44] Shiva uses Blizzard IV.The Yagudo Archpriest takes 23 points of damage.

quadav per wiki Weak to Piercing and nukes, resistant to Slashing
blunt: [14:07:45] Shiva uses Rush.The Wootz Quadav takes 3530 points of damage.
slashing: [14:08:45] Garuda uses Predator Claws.The Wootz Quadav takes 236 points of damage.
piercing: [14:10:30] Garuda uses Claw.The Wootz Quadav takes 410 points of damage.
piercin: [14:11:56] Fenrir uses Crescent Fang.The Wootz Quadav takes 778 points of damage.
slashing: [14:14:46] Leviathan uses Spinning Dive.The Wootz Quadav takes 172 points of damage.
magic: [14:15:45] Shiva uses Blizzard IV.The Wootz Quadav takes 473 points of damage.

honestly do not know what to make of this data?
confirmed 10 mins between wave with TE not affecting the data seemingly
:56 pull
:06 quadav link
:16 orc link

