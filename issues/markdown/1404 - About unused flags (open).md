**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 21, 2020 at 14:43:45_
_Originally opened as: project-topaz/topaz - Issue 1404_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The following flag "WWoodsRTenText" is not used anywhere.
In other words, once the flag is set, it remains as a meaningless flag.

https://github.com/project-topaz/topaz/blob/61a2558614fda01fd57767c37f85334999f819c9/scripts/zones/Windurst_Woods/npcs/Rakoh_Buuma.lua#L66-L68

This time, I happened to find such a meaningless flag.
Is it possible that there are many others?




----
<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [EpicTaru](https://github.com/EpicTaru)**
_Wednesday Oct 21, 2020 at 16:31:16_

----

Just my thoughts, but it may be related to this line for the Windy Rank 10 final mission (from FFXIclopedia, https://ffxiclopedia.fandom.com/wiki/Moon_Reading):

`Optional: Most NPCs around Heavens Tower will have additional dialogue after the final battle (Kupipi has a different line after the cutscenes as well), along with NPCs around the Windurst Gate Guards and others involved in the storyline, as usual.`


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Oct 22, 2020 at 04:10:03_

----

Well it is definitely included with "Moon Reading", the Rank 10 Windy mission.

It could be anything at any point though. I don't see that NPC even mentioned in the guides. Could be an optional dialogue or what EpicTaru said. It's also not clear from the name of the variable itself.

It's true that every nation has an epilogue cutscene (see my San d'Oria PR, in the case of Windy it's in Walls I think), but this doesn't seem to be for that to be honest, even says WWoods. The Rank 10 mission finishes by clicking Door: Vestal Chamber in Heaven's Tower, so any epilogue flag should be set there, not at this NPC.
