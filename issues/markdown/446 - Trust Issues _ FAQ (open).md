**Labels:**

bug

feature

focus

help wanted



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Mar 28, 2020 at 22:34:36_
_Originally opened as: project-topaz/topaz - Issue 446_

----

**_Do Trusts work?_**
- Yes, but the systems that control them are only about ~90% done.

**_Which branches have trusts in?_**
- Both `release` and `canary` branch. You need to enable Trusts if you're in `release`, look in `scripts/globals/settings.lua`.

**_When will trusts reach release branch?_**
- See above: Right now! We'll switch Trusts on-by-default when all the issues (not optional extras) in this tracker are completed.

**_What trusts work?_**
- Only a few, see the table below

**_How do I unlock trusts?_**
- **Natural Way:** You must be Lv5 to flag the starting nation Trust quests: https://www.bg-wiki.com/bg/Category:Trust
- **GM Way:** You can give yourself all Trusts if you are a GM with `!addalltrusts` (Look on the Wiki for instructions on how to make yourself a GM)
- **GM Way:** You can give yourself the cipher for the trust you want and trade it to a trust NPC.  `!additem 10113` (for Lion, etc.)

_Remember that the amount of trusts you can summon is governed by the ROV Key Items. You can give yourself them with: `!addkeyitem 2884` and `!addkeyitem 2887`_

**_The trusts aren't very smart, what's up?_**
- The AI system for trusts is very much WIP and needs a lot of features added to it. They're getting better though! 

**_I've pulled a trust branch and it isn't working, what gives?_**
- All things trust-related involve brutal SQL, C++ and Lua changes, a full db update and rebuild is recommended for **every trust-related update!** It is now recommended to run your SQL updates through `tools/dbtool.py`, which will handles backups, updates and migrations for you.

**_Can I fill in the missing Trust AI?_**
- You can if you want, but we've agreed we won't accept PRs that fill in the Trust AI until the AI system is finalized (no time frame for this!).

**_Where's Cornelia?_**
- SE removed her from the game (and her animation files from the client) because she was OP.

| Trust Status  |
| ------------- |
| https://github.com/project-topaz/topaz/wiki/Trusts |

**On Canary as of 04/19/2020:**

| Bug | Squashed
| ------------- | ------------- |
| Placeholder skills/animations are all borked | ✅  |
| Disengaging a mob will force Trusts to disengage too (mob going unclaimed) BUT if you engage again WITHOUT claiming it, Trusts will attack the mob on their own (they shouldn't). | ✅ |
| Trusts are magic-based but like ninjutsu and songs, you can't be aggroed (by a mob that aggroes if you cast "regular" magic) if you cast one. | ✅  |
| Shouldn't be able to cast Trusts while engaged in combat/being on the hate list of a mob | ✅ |
| Correct system messages for trusts | ✅ |
| You shouldn't be able to cast spells on others Trusts (retail: "Spell cannot be cast on Trust." in yellow). | ✅ |
| Casting a Teleport-Spell with Trusts cause an infinite casting/R0/crash. | ✅ |
| Passing party leader should dismiss trusts | ✅  |
| Sometimes Trusts are getting stuck behind walls/doors/objects, preventing them to engage the target battle. | ✅ |
| ~~(not reproduced) Server crash on Trust summon while engaged but out of range~~ | ✅ |
| Warp II crashes server when cast on Trusts | ✅ |
| SMN Avatar can attack Masters Trusts | ✅ |
| When solo with only trusts, the party menu option is greyed out | ✅  |
| When solo with only trusts, the option to invite someone who is seeking party disappears and `/pcmd add <t>` says you are not authorised | ✅ |
| Disbanding a party releases trusts | ✅ |
| Changing party leader releases trusts | ✅ |

| Phase 1: Basics | Complete |
| ------------- | ------------- |
| `mob_pool` entries for all trusts  | ✅ |
| Spell scripts for all trusts  | ✅ |
| Trusts can be learned with `addSpell` or `addAllTrusts` and then cast  | ✅ |
| Can't cast Trusts if you aren't party leader | ✅ |
| Can't cast the same trust more than once  | ✅ |
| Can't cast different versions of the same trust together (Lion vs Lion II) | ✅ |
| Checking for ROV KI's when casting more than 3 Trusts | ✅ |
| Can't exceed a party of 6 with trusts | ✅ |
| Starter Trust quests (Kupipi, Excenmille, Naji) | ✅ |
| Bastok trust quest/cs's (Ayame, Volker, Iron Eater)  | ✅ |
| Sandoria trust quest/cs's (Curilla, Trion)  | ✅ |
| Windurst trust quest/cs's (Nanaa Mihgo, Ajido-Marujido, Shantotto)  | ✅ |
| Ciphers can be traded to Wetata, Gondebaud and Clarion Star | ✅ |
| Trust roaming movement (FF8 style) | ✅ |
| Trust combat movement and positioning | ✅ |
| Correct behaviour when fighting a mob - player's first melee | ✅  |
| Disengaging while fighting, trusts should disengage too | ✅ |
| Switching mobs in combat, trusts should switch too (on the first swing) | ✅ |
| Trust HP & MP regain after combat (3% per tick after 10 seconds) | ✅ |
| Trust summoner cannot cast Trusts while they have hate, other PT members can. | ✅  |
| Phantom Roll is affected by Alter Egos' main jobs, e.g. Zeid II gives a bonus to Chaos Roll  | ✅ |
| Having Trusts with certain jobs will trigger related latents (THF with Forte Earring etc.)  | ✅ |
| Trusts working correctly in BCNMs and Instances | ✅ |

| Phase 2: Magic | Complete |
| ------------- | ------------- |
| Trust spell list SQL reservation | ✅ |
| Trust spell list loading | ✅ |
| Trust spell filtering, triggers, and binding | ✅ |
| Bones of a gambit AI system | ✅ |
| Recast time tracking for Trusts | ✅ |
| Simple (Stupid) spellcasting logic | ✅ |
| Magic bursting | ✅ |

| Phase 3: Abilities | Complete |
| ------------- | ------------- |
| Trusts use player JAs | ✅  |
| Trust JAs | ✅ |

| Phase 4: Skills | Complete |
| ------------- | ------------- |
| Trust skill list SQL reservation | ✅ |
| Trust skill list loading | ✅ |
| Trust skill filtering, triggers, and binding | ✅ |
| Skillchains | ✅ |
| AI for all nation trusts | ✅ |
| Trust positioning (Melee, Medium, Far, StandStill etc.) | ✅ |
| Reverse enmity container | ✅ |

| Phase 5: Push towards `release` merge | Complete |
| ------------- | ------------- |
| Stability, performance, crushing crashes  | ⏳ (✅?) |
| Bugs. Crush all the bugs.  | ⏳(✅?) |
| Fix Naji's Bones! | ✅ |
| Settings for Trust speed, behaviour etc. | ✅ |
| Trust correct(ish) stats, ATT/ACC, STR/DEX..., Weapon DMG etc. | ✅ |
| Trust correct(ish) HP, MP | ✅ |
| Correct CS dialogues when trading player-race/non-player-race/special ciphers | ✅ |
| Job Traits | ✅ |
| Non-Job Traits (Excenmille's "Store TP", etc.) -> (just use mods!) | ✅ |
| Trust Spawn/Synergy/Despawn/Die Messages | ✅ |
| Trust System Messages | ✅ |
| Zone Flags where Trusts are allowed | ✅ |
| Delay on being able to summon trusts when you invite a party member | ✅ |
| Party properly disbanding and lose leader status on `ClearTrusts` or zone etc. | ✅ |
| Custom WS selection and AI for Ayame | ✅ |
| Support _correct_ Ranged Attacks for trusts | ✅ |
| Add localVars to stop trust quest NPCs blocking other quests | ✅ |

| Phase 6: Release | Complete |
| ------------- | ------------- |
| Merge `feature/trust` into `release` | ✅ |
| Add flags to disable Trusts by default | ✅ |

| Phase 7: Putting out fires & cleanup| Complete |
| ------------- | ------------- |
| Alliances may not be formed when in a party comprised of both players and alter egos. | ⏳ |
| Chat lines & teamwork messages for all trusts | |
| Go through **ALL** core changes and aggressively sanity check all pointers and entities | |
| Chat lines & teamwork messages for all trusts | |
| Run through all trust starter quests with new chars + ROE testing | |
| Balance & Tuning - WEAKER IS BETTER, too strong doesn't get fixed | |
| Make issues for anything leftover | |

| Phase X: Optional Goodies | Complete |
| ------------- | ------------- |
| Ark Angel cipher trade CSs | ✅ |
| "Bodyguard mode" + commands for engage conditions | |
| "Adaptive" spell selection (heal severity, level difference etc.) | |
| "Efficient" healing (marking heal targets with the strength of heal you're casting on them, and other trusts reading that so someone doesn't get 3x Cure V's) | |  
| "Smart" bard song selection | |
| The 2 min delay after someone joins your party before you can summon trusts only applied to the original leader, if you pass leadership the new leader can summon straight away. If you pass it back, the old leader is still ticking out they delay. |  |
| (aesthetic): Currently you're able to target Trusts and do any /emote or /jobemotes on them. On retail, if you try to target a Trust with a /jobemote, it will be redirected on you. Currently, you can do both on Trusts. |  |
| TrustMemory for Shantotto and Iron Eater quests |  |
| All GEO-style trusts (once auras are in)(also need to be untargettable and invincible) | ⏳ |

| Out of scope things |
| ------------- |
| Tracking spell resists & elemental immunities etc. | |
| Refactoring `mob_spelllist_container` to support trusts better | |
| iLvl support for trusts |
| Filling out AI for all trusts... |
| A guide to writing gambits + examples (gambits will be closed for a while, the system needs cleaning after first release) | |


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 12, 2020 at 07:24:01_

----

I prefer problems and bugs being listed as their own issues, so they can be tracked properly 👍 (removed existing comments and moved relevant things to issues)
