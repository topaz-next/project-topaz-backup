**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Jun 26, 2020 at 08:44:29_
_Originally opened as: project-topaz/topaz - Issue 774_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Tested a bunch, I'm getting pretty good at the minigame...

**New:**
Added tracking via Quest Log
Fixed missing Item and NPC IDs in completion CS
Changed motivation/pep relationship
Added clamping to motivation and pep to fix any weirdness with the bar rendering
Added failure CS when you dismount or run out of motivation, which lets you enable easy mode (or not)
Added easy mode: tracked through the effect's power (acts as a modifier for motivation decay and pep growth)
Fixed bug where the final Raptor Food region was acting like it was Syrillia's region
Added MEET_SYRILLIA text when you've eaten 5 foods

**Not doing in this PR:**
Additional Raptor animations
Varying pep and speed depending on terrain slope etc.
Best time tracking

**Once this PR goes in, I think it would be fair to open two new issues:**
**- [Good First Issue] Quest: Full Speed Ahead! doesn't track server best time**
Using `Get/SetServerVariable`

**- [Good First Issue][Core] Quest: Full Speed Ahead! raptor doesn't slow down as it runs out of pep**
Mount speed is hard-coded, and needs to be modifiable (through mods or otherwise) for Full Speed Ahead!

`battleentity.cpp`
```
uint8 CBattleEntity::GetSpeed()
{
    return (isMounted() ? 50 + map_config.speed_mod : std::clamp<uint16>(speed * (100 + getMod(Mod::MOVE)) / 100, std::numeric_limits<uint8>::min(), std::numeric_limits<uint8>::max()));
}
```
