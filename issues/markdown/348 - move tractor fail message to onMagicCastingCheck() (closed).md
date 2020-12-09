**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 16, 2020 at 21:37:18_
_Originally opened as: project-topaz/topaz - Issue 348_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

(cherry picked from commit 695a2bcf646b4a0b98e5017774d6c2938358a566 in my personal project, under GPL)

The existing tractor check in magic_state.cpp is crashy. It has been the cause of another servers recent crashes. This morning I sorted out the cause, and decided to move the check into lua anyway since not all the spell functions are bound yet and we normally set the message right there in the onMagicCastingCheck() anyway and no longer have to check if the object we're sending the message to is a player or not as that's baked into the function. 

Also included: 
kill magic number in alexander.lua
translated a comment to english


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 18, 2020 at 00:56:51_

----

So guys, the new binding was not at all needed because turns out there was something in the core I had missed and I cannot remember what else I thought I'd use it for. Its really easy to create..Should I remove that until a use case exists?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 10:41:52_

----

I'd be okay with adding the binding now even if there's nothing using it if there's an example of what _might_ use it in the future.

I'm trying to think of spells that might not always be allowed when general spellcasting is. Trusts? Geomancy?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 10:49:47_

----

Although now I'm wondering; [we have player:canUseMisc](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/src/map/lua/lua_baseentity.cpp#L5065). Is there a distinction to be made between checking the flags "as a player" versus checking it "as the spell"?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 18, 2020 at 14:38:12_

----

Contexts in which we have no player but do have a spell? 
But this turned out how it did because reused existing darkstar code [which acts on the spell](https://github.com/project-topaz/topaz/blob/2943fab983cc1457ce75f15dd9dca9d3bfa21b05/src/map/spell.cpp#L177) so I just rolled with it.

only one I could think of was mazurka, which is presently handled elsewhere but I didn't see where.

