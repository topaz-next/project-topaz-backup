**Labels:**

approved

reviewed



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday May 02, 2020 at 20:20:17_
_Originally opened as: project-topaz/topaz - Issue 572_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Still a ton to do before this is ready: see issue #792


Future plans but not in the scope of this pull request: spike effects on armor too. Some ground work is set here but I have made no attempt to transition those at this time.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 28, 2020 at 16:07:41_

----

I am now -reasonably- sure I won't be changing the procType enum I am using, if anyone wants to throw item mods to the additional Effect branch I am working off I'd be very grateful. This could go to a tpz branch to be easier to pr too, while I continue to clean up the global script (its functional right now, if mods are added for items) if that is desired. I still have a lot of work to do on the script end to make it maintainable.
```lua
    local procType =
    {
        -- These are arbitrary, make up new ones as needed.
        NORMAL = 1,
        HP_HEAL = 2,
        MP_HEAL = 3,
        HP_DRAIN = 4,
        MP_DRAIN = 5,
        TP_DRAIN = 6,
        HPMPTP_DRAIN = 7,
        DISPEL = 8,
        SELF_BUFF = 9,
        DEATH = 10,
    }
```
```lua
ITEM_ADDEFFECT_TYPE     = 431, -- see procType table in scripts\globals\assitional_effects.lua
ITEM_SUBEFFECT          = 499, -- Animation ID of Spikes and Additional Effects
ITEM_ADDEFFECT_DMG      = 500, -- Damage of an items Additional Effect or Spikes
ITEM_ADDEFFECT_CHANCE   = 501, -- Chance of an items Additional Effect or Spikes
ITEM_ADDEFFECT_ELEMENT  = 950, -- Element of the Additional Effect or Spikes, for resist purposes
ITEM_ADDEFFECT_STATUS   = 951, -- Status Effect ID to try to apply via Additional Effect or Spikes
ITEM_ADDEFFECT_POWER    = 952, -- Base Power for effect in MOD_ITEM_ADDEFFECT_STATUS
ITEM_ADDEFFECT_DURATION = 953, -- Base Duration for effect in MOD_ITEM_ADDEFFECT_STATUS
```
```lua
tpz.subEffect =
{
    -- ATTACKS
    FIRE_DAMAGE         = 1,   -- 110000        3
    ICE_DAMAGE          = 2,   -- 1-01000       5
    WIND_DAMAGE         = 3,   -- 111000        7
    CHOKE               = 3,   -- Shares subeffect
    EARTH_DAMAGE        = 4,   -- 1-00100       9
    LIGHTNING_DAMAGE    = 5,   -- 110100       11
    WATER_DAMAGE        = 6,   -- 1-01100      13
    LIGHT_DAMAGE        = 7,   -- 111100       15
    DARKNESS_DAMAGE     = 8,   -- 1-00010      17
    DISPEL              = 8,   -- Verified with video of Lockheart Greatsword proc.
    SLEEP               = 9,   -- 110010       19
    POISON              = 10,  -- 1-01010      21
    PARALYSIS           = 11,
    AMNESIA             = 11,  -- Verified uses same animation as para
    BLIND               = 12,  -- 1-00110      25
    SILENCE             = 13,
    PETRIFY             = 14,
    PLAGUE              = 15,
    STUN                = 16,
    CURSE               = 17,
    DEFENSE_DOWN        = 18,  -- 1-01001      37
    EVASION_DOWN        = 18,  -- Same subeffect as DEFENSE_DOWN
    ATTACK_DOWN         = 18,  -- Same subeffect as DEFENSE_DOWN
    DEATH               = 19,
    SHIELD              = 20,
    HP_DRAIN            = 21,  -- 1-10101      43
    MP_DRAIN            = 22,  -- This is correct animation
    TP_DRAIN            = 22,  -- Verified this should look exactly like Aspir Samba.
    HASTE               = 23,
    -- There are no additional attack effect animations beyond 23. Some effects share subeffect/animations.
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 01, 2020 at 23:38:10_

----

Finally got my latest changes tested.


----
<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Monday Jul 06, 2020 at 03:56:10_

----

@TeoTwawki I am adding some "item_mods" 431 additional effect, and since I am not submitting the scripts for these items, the (id,431,1) is just orphaned. I will just add them in using this style, but I need to know how to do it.
Based on your above, for example, item_mods for example, poison.
`INSERT INTO `item_mods` VALUES (16404,431,1);   -- Venom Katars - Additional effect: Poison`

How would I make this a full entry in your style?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jul 06, 2020 at 04:34:34_

----

@helixhamin The new style takes more than one mod. The mods already exist in both release and canary but aren’t used until my pr merges.

In addition to 431, you need 499 (subeffect, this is the animation. Poison animation is 10) 501 (proc rate, 1-100 %) for any and all add effects.

For status such as en-posion, you also need:
951: status effect id
952: power - how big a poison are you inflicting?
953: duration - how long does the poison last?

Those 3 are not needed for damage effects, only status. Damage will use 950 however to tell it which elemental resistance to check, and 500 to tell it how hard to hit. 


----
<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Monday Jul 06, 2020 at 07:13:17_

----

Okay, so I have:
`function onAdditionalEffect(player,target,damage)
    local chance = 10

    if (math.random(0,99) >= chance or target:isUndead()) then
        return 0,0,0
    else
        target:delStatusEffect(tpz.effect.POISON)
        target:addStatusEffect(tpz.effect.POISON, 4, 3, 30)
        return tpz.subEffect.POISON, tpz.msg.basic.ADD_EFFECT_STATUS, tpz.effect.POISON
    end
end`

This should be converted as follows:
`INSERT INTO `item_mods` VALUES (16404,431,1);   -- Venom Katars - Additional effect: Poison

INSERT INTO `item_mods` VALUES (16404,499,10);  -- Venom Katars - Additional effect: Poison

INSERT INTO `item_mods` VALUES (16404,951,3);   -- Venom Katars - Additional effect: Poison

INSERT INTO `item_mods` VALUES (16404,952,4);   -- Venom Katars - Additional effect: Poison

INSERT INTO `item_mods` VALUES (16404,953,30);  -- Venom Katars - Additional effect: Poison`

Just to make sure this is being done right. Is this correct?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jul 06, 2020 at 14:19:27_

----

You missed 501 for the proc chance. you want:
```sql
-- Venom Katars - Additional effect: Poison
INSERT INTO `item_mods` VALUES (16404,431,1);  -- Additional effect type
INSERT INTO `item_mods` VALUES (16404,499,10); -- Additional effect animation (subeffect)
INSERT INTO `item_mods` VALUES (16404,501,10); -- Additional effect proc chance
INSERT INTO `item_mods` VALUES (16404,951,3);  -- Additional effect status ID
INSERT INTO `item_mods` VALUES (16404,952,4);  -- Additional effect status potency
INSERT INTO `item_mods` VALUES (16404,953,30); -- Additional effect status duration
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 15, 2020 at 17:15:32_

----

The target branch needs to be even with release now, due to shiva's claws.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 15, 2020 at 17:17:04_

----

Future items can be added this way:
https://github.com/project-topaz/topaz/pull/572/commits/840993d3f276f99c02cd207bf55b9424be272a7a


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 15, 2020 at 17:33:48_

----

gdi github


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 17:34:28_

----

I'm sorry! 😭 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 19:41:38_

----

@ibm2431 rest api thing fixed it?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 16, 2020 at 22:21:19_

----

It did, yeah!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 00:33:38_

----

I have actually found a few more mistakes on my own, will cleanup this weekend. Hopefully before they get noticed. Wasn't as ready as I thought. it *looked* working in game, but only visually.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 29, 2020 at 12:29:55_

----

ok, except for what I am trying to put to a separate pr after, I think I have this all cleaned up now

(reasoning: I want to enable people to add the sql lines while I kill the if/else blocks without having to wait for me to see that their sql is correct)


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Aug 19, 2020 at 14:05:32_

----

@project-topaz/developer  @project-topaz/reviewer  this seems in a good place for a final review, if anyone can assist. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 07:55:38_

----

Also, thanks for opening up a worklist for what you've planned to do after!
