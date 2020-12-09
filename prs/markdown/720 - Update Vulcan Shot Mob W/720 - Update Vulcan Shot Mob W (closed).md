**Labels:**



<a href="https://github.com/mrmclaw"><img src="https://avatars2.githubusercontent.com/u/65800658?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrmclaw](https://github.com/mrmclaw)**
_Saturday Jun 13, 2020 at 05:13:43_
_Originally opened as: project-topaz/topaz - Issue 720_

----

Retail this WS should do roughly 750ish dmg. On Canaria it is doing roughly 1700 dmg to a player with Shellra V that is level 85 when its a 75 fight. It's performed in a level 75 cap BCNM during a TOAU mission. 

PR change involved reducing the weapon dmg modifier from 4 to 2, but other recommendations to change the potency would be accepted. Whatever you think would work best!

Thank you!

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 14, 2020 at 02:34:59_

----

dmgmod is a multiplier. So this script is multiplying mobs weapon wdmg by 4 in the line you changed and total damage by 8 after that when dmgmod gets used in the global. Changing either one will influence the dmg totals greatly. Both are kinda high but I've no idea how the move is calculated to arrive at its damage numbers on retail.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 14, 2020 at 02:34:59_

----

dmgmod is a multiplier. So this script is multiplying mobs weapon wdmg by 4 in the line you changed and total damage by 8 after that when dmgmod gets used in the global. Changing either one will influence the dmg totals greatly. Both are kinda high but I've no idea how the move is calculated to arrive at its damage numbers on retail.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Jun 14, 2020 at 07:18:41_

----

Yay thank you @mrmclaw for your PR

https://youtu.be/OycR1Ar1tx0?t=3200

Above is a capture of retail damage for it. I don't know what level @ibm2431  was but tagging him so he can give more feedback about this awesome fight.

Thank you @ibm2431  for the capture =D


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Jun 14, 2020 at 08:45:06_

----

Ned Idle:
```
sets.Idle = { -- PDT: 39%, 25% MDT
  head="Befouled Crown", --- 1 MP/tic -- BLU can't wear
  neck="Twilight Torque", -- DT: 5%
  ear1="Moonshade Earring", --- 1 MP/tic
  ear2="Ethereal Earring", --- Converts 3% dmg to MP
  body="Hagondes Coat +1", --- PDT: 4%
  hands="Hagondes Cuffs +1", -- PDT: 3%, MDT: 3%
  ring1="Defending Ring", -- DT: 10%
  ring2="Vocane Ring", -- DT: 7%
  back="Umbra Cape" -- PDT: 6%
  waist="Fucho-no-Obi", --- 1 MP/tic when < 50% MP
  legs={name="Merlinic Shalwar", augments={'"Drain" and "Aspir" potency +5','Accuracy+11 Attack+11','"Refresh"+1','Mag. Acc.+7 "Mag.Atk.Bns."+7',}},
  feet="Hag. Sabots +1" --- PDT: 4%
}
```
Idles with his nuke weapons, because only scrub BLMs lose TP by swapping staves for some extra PDT.
Ned has all merits and is JP master.

I apparently don't have notes in Hana's gearswap file for her augment PDT values, so can't say definitively what her stats are there (I also don't know her JP status offhand).

At the time, Rae's Idle set was:
```
    -- Aettir 5% PDT II
    ammo="Grenade Core",
    head="Despair Helm", -- STR+36, Atk+20, DEX+21, Acc+20, STP+3, Enmity+7
    neck="Warder's Charm", -- Elem Res+15, Occ. Absorb Magic, Enmity+1~8
    ear1="Grit Earring",
    body="Emet Harness +1", -- PDT -6%, HP+61, Evasion+70, MEva+64, Enmity+10, H+4%
    hands="Despair Fin. Gaunt.", -- STR+27, DEX+34, Atk+18, Acc+18, H+7%
    ring1="Defending Ring", -- 10% DT
    ring2="Enlivened Ring", -- DEX+2, Accuracy +7
    back="Engulfer Cape +1", -- MDT -4%, Occ. Absorb Magic (5%?)
    legs="Despair Cuisses", -- STR+46, Atk+23, Enmity+4, H+8%
    feet="Rawhide Boots" -- STR+28, Atk+15, Acc+23, STP+5, H+4%
```

Despite /lockstyle, Astrena is still just 5/5 Espial, spark sword, spark gun, and some bronze bullets.
Despite /lockstyle, Lunette is still just 5/5 Wayfarer and spark club. Don't think she even has a shield.

Sava's normally 5/5 Espial when on BRD, but it looks like she might be wearing an NQ Emet Harness she got from Largantua.

Rae, Sava, Astrena, and Lunette don't have any merits that'd factor into damage reduction, nor any JP of note.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Jun 14, 2020 at 08:48:27_

----

This move seems to be missing the -50% defense reduction.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Jun 14, 2020 at 15:40:18_

----

Is Eden Topaz yet? Most likely they might have already the correct damage for this WS and others since they are focused on ToAU


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 08, 2020 at 08:32:42_

----

What was the new damage multipler based on?


----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Monday Jul 20, 2020 at 20:57:45_

----

Hello, @mrmclaw !

Are you still working on this Pull Request?


----
<a href="https://github.com/mrmclaw"><img src="https://avatars2.githubusercontent.com/u/65800658?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrmclaw](https://github.com/mrmclaw)**
_Tuesday Jul 21, 2020 at 17:40:17_

----

Hey there,
      It might be better to change this to an issue instead of a PR. The PR really isn't based on anything because I can't find anything more concrete on how to lower the damage besides lowering it in half on the formula somewhere because currently, it does about double damage on Canaria which I can't even proceed past the mission as of this moment with it.

Sorry I can be more helpful...

________________________________
From: zircon-tpl <notifications@github.com>
Sent: Monday, July 20, 2020 1:58 PM
To: project-topaz/topaz <topaz@noreply.github.com>
Cc: Goliath <mrmclaw@outlook.com>; Mention <mention@noreply.github.com>
Subject: Re: [project-topaz/topaz] Update Vulcan Shot Mob WS to reflect retail DMG (#720)


Hello, @mrmclaw<https://github.com/mrmclaw> !

Are you still working on this Pull Request?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/project-topaz/topaz/pull/720#issuecomment-661329387>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/APWATUSECKORPX7MVXS2KHTR4SVVVANCNFSM4N42T6ZA>.



----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Thursday Jul 23, 2020 at 05:24:21_

----

Thank you for your reply, mrmclaw!

I have converted this into [`#878 - Damage for enemy ability "Vulcan Shot" inaccurate`](https://github.com/project-topaz/topaz/issues/878) .
