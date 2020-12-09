**Labels:**

merge ready



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 03, 2020 at 06:38:52_
_Originally opened as: project-topaz/topaz - Issue 462_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 03, 2020 at 06:41:00_

----

I couldn't verify this. If anyone has retail and can check the default message, that would be great.

Went through his chat options and I believe this is most likely to be the default.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 03, 2020 at 11:47:35_

----

If Octavien is flagged properly in the database, he won't even spawn if SoA is off.

You already would need to get into SoA and the NPCs involved with that shouldn't work with that off, so checking ENABLE_SOA isn't needed here.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 03, 2020 at 18:29:58_

----

Perhaps I misunderstood. I tried to follow the pattern elsewhere.

Granted you probably couldn't get to Adoulin if the expansion is flag is off, but if you somehow warped there (as a GM or if you had the homepoint before the expansion was disabled on a server or whatever), he certainly spawns.

It seems like these flags in Lua were intended to give runtime control for enabling/disabling expansions: 
https://github.com/project-topaz/topaz/blob/c52431e2c48516954aa2f5ebbb331238f43cc3d8/scripts/globals/settings.lua#L18-L28

However I'm happy to remove the check to simplify the code if I'm not using the flag correctly.

Here's an example that I based it off of:
https://github.com/project-topaz/topaz/blob/c52431e2c48516954aa2f5ebbb331238f43cc3d8/scripts/zones/Aht_Urhgan_Whitegate/npcs/Waoud.lua#L34


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Apr 04, 2020 at 04:50:30_

----

> Granted you probably couldn't get to Adoulin if the expansion is flag is off,

Correct. The starting mission that would let you arrive here should not activate.

> It seems like these flags in Lua were intended to give runtime control for enabling/disabling expansions:

Generally those settings are to prevent missions activating or prevent working NPCs confusing the players. They really shouldn't ever be disabled after the fact. I was not aware anyone had started adding them into job quests..

the whole point of my comment:
`INSERT INTO npc_list VALUES (17830003,'Octavien','Octavien',128,2.444,-11.442,-16.595,20,40,40,0,0,0,0,27,0x01000F0352115221523152415251006000700000,32,'SOA',1);`
If you are **actually** using the enable flags to turn off content, _the npc then doesn't even spawn_ because its flagged 'SOA' there. :man_shrugging: 

> -- Setting to lock content more accurately to the content you have defined above
-- This generally results in a more accurate presentation of your selected expansions
-- as well as a less confusing player experience for things that are disabled (things that are disabled are not loaded)
-- This feature correlates to the content_tag column in the SQL files
RESTRICT_CONTENT = 0

I mean, is anyone actually going to disable SOA and expect to do other things but then not allow to trigger the job quest? I would expect that if I am allowed into the zone, and the NPCs are up, its active. 

I guess we need to ask the devs what they think about including expansion checks on job quests. Feels redundant to me but either way we'll want them all consistent (all exp jobs do it or none do it, excluding zilart of course - no flag for it).


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Apr 04, 2020 at 23:35:59_

----

I wonder if those Lua settings flags are even needed at all then. They don't seem to be populated from the SQL, as far as I can tell.

But for the scope of this change, I'm happy to do whatever the consensus is. I'm also a big fan of consistency, so if folks prefer to keep these flag checks then we can leave it. Otherwise if the preference is to remove them then I'm happy to do so.

I actually prefer to remove the flag, if it's truly not needed, as it simplifies the code.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 05, 2020 at 00:24:20_

----

> I wonder if those Lua settings flags are even needed at all then. They don't seem to be populated from the SQL, as far as I can tell.

what? The core looks at the lua setting, and then find a matching sql tag to decide if the NPC spawns or not. That can't work without both parts involved. We even piggy backed that for the FoV books - by making a setting named `ENABLE_thing` and their expansion tag in the NPC list  `thing` you use it for any grouping of NPCs with the same matching tag.

> But for the scope of this change, I'm happy to do whatever the consensus is. 

I asked in discord last night but they didn't comment here. 

@ibm2431 I summon thee.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Apr 05, 2020 at 00:32:59_

----

> The core looks at the lua setting, and then find a matching sql tag to decide if the NPC spawns or not.

Would you mind sharing some links for my own learning? I couldn't find that just by searching around for the Lua flag name.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 05, 2020 at 01:18:09_

----

https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/src/map/lua/luautils.cpp#L1201

```cpp
            std::string contentVariable("ENABLE_");
            contentVariable.append(contentTag);
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 05, 2020 at 01:23:20_

----

and here's where it hits entity loading from sql

https://github.com/project-topaz/topaz/blob/5991d15a9a17549ca7a076b7a4a42ee3a26be262/src/map/utils/zoneutils.cpp#L279

```cpp
    if (ret != SQL_ERROR && Sql_NumRows(SqlHandle) != 0)
    {
        while(Sql_NextRow(SqlHandle) == SQL_SUCCESS)
        {
            const char* contentTag = (const char*)Sql_GetData(SqlHandle, 16);

            if (luautils::IsContentEnabled(contentTag) == false)
            {
                continue;
            }
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 06:17:04_

----

Yeah, go ahead an remove the ENABLE_SOA from Octavien, please. I said a bit when Teo asked on Discord, but the gist is that having the ENABLE_EXP setting in the NPC script, for an NPC that can't be reached without that setting already being true, is a both redundant and doesn't help server admins.

Waoud's a bad example, and he should have that check removed from him.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 06:25:28_

----

This char_var is _kind_ of long; a variable of `RUN_COTR_Reward` might work


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 08:18:25_

----

[`npcUtil.giveItem` can be leveraged here, which will do the free slot checks for you, display the message, and then return true/false depending on if it successfully gave the item](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L185-L195)

```lua
if npcUtil.giveItem(20781) then
    player:unlockJob(tpz.job.RUN)
    -- etc
else
    player:setCharVar("ChildrenOfTheRuneRewardPending", 1)
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 08:19:04_

----

`elseif` here~

Option 1 is what starts the rune inscribing process, which halves both your HP and MP provided they are greater than 5. Success is option 803 (at least, in my capture). See capture "Quests: Adoulin: Children of the Rune (RUN Unlock)".


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 08:22:41_

----

If the quest is refused, he remembers that he tried to give it to you, and will later give you CS 24 on later triggers


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 08:43:12_

----

Table lookups aren't _that_ expensive; you don't need this local 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 09:03:06_

----

[`npcUtil.giveKeyItem` will reduce these two lines to one call](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L285-L293)


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:14:50_

----

This was to ensure that the same value is used consistently throughout. I'm happy to copy/paste it throughout if that's preferable.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:17:41_

----

Although with the below suggestion, this is obsolete either way.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:20:07_

----

I was going based off of Youtube videos, which didn't show every option. I'll check out the capture and adjust.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:20:14_

----

Same as below.

I was going based off of Youtube videos, which didn't show every option. I'll check out the capture and adjust.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:21:38_

----

Sounds good. Removed!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:21:54_

----

Done. Much cleaner.

Had no idea this existed. Thanks for the pointer!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:22:14_

----

Never knew this existed. Thanks for the pointer!

Applied, which simplified the code :)


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:22:50_

----

Works for me.  Was going for something human readable and unique, but I think abbreviating RUN and COTR will still be clear.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 10, 2020 at 00:58:02_

----

`if and` oopsie?


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 05:38:49_

----

Yep. Was a typo. I had a few others too. Couldn't test out the latest changes until my client updated.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 05:39:07_

----

Reworked the whole state machine and verified it matched all options from the capture PTAL.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 05:39:11_

----

Reworked the whole state machine and verified it matched all options from the capture PTAL.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 05:40:00_

----

We do get the in-progress packet for 803. But it doesn't seem to cause any action to happen so I didn't bother putting it in the scripts. I just let the onEventFinish capture success.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 03, 2020 at 06:41:00_

----

I couldn't verify this. If anyone has retail and can check the default message, that would be great.

Went through his chat options and I believe this is most likely to be the default.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 03, 2020 at 11:47:35_

----

If Octavien is flagged properly in the database, he won't even spawn if SoA is off.

You already would need to get into SoA and the NPCs involved with that shouldn't work with that off, so checking ENABLE_SOA isn't needed here.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 03, 2020 at 18:29:58_

----

Perhaps I misunderstood. I tried to follow the pattern elsewhere.

Granted you probably couldn't get to Adoulin if the expansion is flag is off, but if you somehow warped there (as a GM or if you had the homepoint before the expansion was disabled on a server or whatever), he certainly spawns.

It seems like these flags in Lua were intended to give runtime control for enabling/disabling expansions: 
https://github.com/project-topaz/topaz/blob/c52431e2c48516954aa2f5ebbb331238f43cc3d8/scripts/globals/settings.lua#L18-L28

However I'm happy to remove the check to simplify the code if I'm not using the flag correctly.

Here's an example that I based it off of:
https://github.com/project-topaz/topaz/blob/c52431e2c48516954aa2f5ebbb331238f43cc3d8/scripts/zones/Aht_Urhgan_Whitegate/npcs/Waoud.lua#L34


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Apr 04, 2020 at 04:50:30_

----

> Granted you probably couldn't get to Adoulin if the expansion is flag is off,

Correct. The starting mission that would let you arrive here should not activate.

> It seems like these flags in Lua were intended to give runtime control for enabling/disabling expansions:

Generally those settings are to prevent missions activating or prevent working NPCs confusing the players. They really shouldn't ever be disabled after the fact. I was not aware anyone had started adding them into job quests..

the whole point of my comment:
`INSERT INTO npc_list VALUES (17830003,'Octavien','Octavien',128,2.444,-11.442,-16.595,20,40,40,0,0,0,0,27,0x01000F0352115221523152415251006000700000,32,'SOA',1);`
If you are **actually** using the enable flags to turn off content, _the npc then doesn't even spawn_ because its flagged 'SOA' there. :man_shrugging: 

> -- Setting to lock content more accurately to the content you have defined above
-- This generally results in a more accurate presentation of your selected expansions
-- as well as a less confusing player experience for things that are disabled (things that are disabled are not loaded)
-- This feature correlates to the content_tag column in the SQL files
RESTRICT_CONTENT = 0

I mean, is anyone actually going to disable SOA and expect to do other things but then not allow to trigger the job quest? I would expect that if I am allowed into the zone, and the NPCs are up, its active. 

I guess we need to ask the devs what they think about including expansion checks on job quests. Feels redundant to me but either way we'll want them all consistent (all exp jobs do it or none do it, excluding zilart of course - no flag for it).


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Apr 04, 2020 at 23:35:59_

----

I wonder if those Lua settings flags are even needed at all then. They don't seem to be populated from the SQL, as far as I can tell.

But for the scope of this change, I'm happy to do whatever the consensus is. I'm also a big fan of consistency, so if folks prefer to keep these flag checks then we can leave it. Otherwise if the preference is to remove them then I'm happy to do so.

I actually prefer to remove the flag, if it's truly not needed, as it simplifies the code.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 05, 2020 at 00:24:20_

----

> I wonder if those Lua settings flags are even needed at all then. They don't seem to be populated from the SQL, as far as I can tell.

what? The core looks at the lua setting, and then find a matching sql tag to decide if the NPC spawns or not. That can't work without both parts involved. We even piggy backed that for the FoV books - by making a setting named `ENABLE_thing` and their expansion tag in the NPC list  `thing` you use it for any grouping of NPCs with the same matching tag.

> But for the scope of this change, I'm happy to do whatever the consensus is. 

I asked in discord last night but they didn't comment here. 

@ibm2431 I summon thee.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Apr 05, 2020 at 00:32:59_

----

> The core looks at the lua setting, and then find a matching sql tag to decide if the NPC spawns or not.

Would you mind sharing some links for my own learning? I couldn't find that just by searching around for the Lua flag name.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 05, 2020 at 01:18:09_

----

https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/src/map/lua/luautils.cpp#L1201

```cpp
            std::string contentVariable("ENABLE_");
            contentVariable.append(contentTag);
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 05, 2020 at 01:23:20_

----

and here's where it hits entity loading from sql

https://github.com/project-topaz/topaz/blob/5991d15a9a17549ca7a076b7a4a42ee3a26be262/src/map/utils/zoneutils.cpp#L279

```cpp
    if (ret != SQL_ERROR && Sql_NumRows(SqlHandle) != 0)
    {
        while(Sql_NextRow(SqlHandle) == SQL_SUCCESS)
        {
            const char* contentTag = (const char*)Sql_GetData(SqlHandle, 16);

            if (luautils::IsContentEnabled(contentTag) == false)
            {
                continue;
            }
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 06:17:04_

----

Yeah, go ahead an remove the ENABLE_SOA from Octavien, please. I said a bit when Teo asked on Discord, but the gist is that having the ENABLE_EXP setting in the NPC script, for an NPC that can't be reached without that setting already being true, is a both redundant and doesn't help server admins.

Waoud's a bad example, and he should have that check removed from him.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 06:25:28_

----

This char_var is _kind_ of long; a variable of `RUN_COTR_Reward` might work


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 08:18:25_

----

[`npcUtil.giveItem` can be leveraged here, which will do the free slot checks for you, display the message, and then return true/false depending on if it successfully gave the item](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L185-L195)

```lua
if npcUtil.giveItem(20781) then
    player:unlockJob(tpz.job.RUN)
    -- etc
else
    player:setCharVar("ChildrenOfTheRuneRewardPending", 1)
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 08:19:04_

----

`elseif` here~

Option 1 is what starts the rune inscribing process, which halves both your HP and MP provided they are greater than 5. Success is option 803 (at least, in my capture). See capture "Quests: Adoulin: Children of the Rune (RUN Unlock)".


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 08:22:41_

----

If the quest is refused, he remembers that he tried to give it to you, and will later give you CS 24 on later triggers


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 08:43:12_

----

Table lookups aren't _that_ expensive; you don't need this local 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 09:03:06_

----

[`npcUtil.giveKeyItem` will reduce these two lines to one call](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L285-L293)


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:14:50_

----

This was to ensure that the same value is used consistently throughout. I'm happy to copy/paste it throughout if that's preferable.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:17:41_

----

Although with the below suggestion, this is obsolete either way.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:20:07_

----

I was going based off of Youtube videos, which didn't show every option. I'll check out the capture and adjust.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:20:14_

----

Same as below.

I was going based off of Youtube videos, which didn't show every option. I'll check out the capture and adjust.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:21:38_

----

Sounds good. Removed!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:21:54_

----

Done. Much cleaner.

Had no idea this existed. Thanks for the pointer!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:22:14_

----

Never knew this existed. Thanks for the pointer!

Applied, which simplified the code :)


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:22:50_

----

Works for me.  Was going for something human readable and unique, but I think abbreviating RUN and COTR will still be clear.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 10, 2020 at 00:58:02_

----

`if and` oopsie?


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 05:38:49_

----

Yep. Was a typo. I had a few others too. Couldn't test out the latest changes until my client updated.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 05:39:07_

----

Reworked the whole state machine and verified it matched all options from the capture PTAL.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 05:39:11_

----

Reworked the whole state machine and verified it matched all options from the capture PTAL.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 05:40:00_

----

We do get the in-progress packet for 803. But it doesn't seem to cause any action to happen so I didn't bother putting it in the scripts. I just let the onEventFinish capture success.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 03, 2020 at 07:35:46_

----

Someone will need to re-trigger the checks.

```
apt-get install failed
```


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 00:24:05_

----

Resolved a lot of the comments. (And sorry about the whitespacing. Used VIM which took my default style and I hadn't thought about it before I pushed.)

Left 2 comments to go. Will watch the capture to handle some of the option choices that vary from the ones I was able to decipher from videos on Youtube.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 05:42:47_

----

Resolved all the comments and reworked the state machine to match all possible options from the capture.

Please take another look.
