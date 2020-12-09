**Labels:**

reviewed



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 06, 2020 at 23:50:36_
_Originally opened as: project-topaz/topaz - Issue 1267_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I apologize for the size of this commit but I'm positive it's very well structured  and commented just the right amount to not be a burden to review.

**This commit adds all missing optional dialogues and cut-scenes to the San d'Oria mission line.**
*(Because San d'Oria is epic, and now it's even more!)*
It additionally cleans up a large amount of code and fits it to the style guide.
Some quests were re-arranged for better prioritization: (RDM AF over Savage Blade WS quest e.g.)
Nesting was added for less condition checks where possible and sensible.
A lot of operators have been reduced/optimized and conditions were generally reviewed for effectiveness.
Two of the optional cut-scenes that were already there but in series have been re-written in parallel so that the viewing order doesn't matter (Trion's & Pieuje's doors).

Missions directly affected by this change are
- 5-1 The Ruins of Fei'Yin
- 5-2 The Shadow Lord
- 8-2 Lightbringer
- 9-1 Breaking Barriers
- 9-2 The Heir to the Light
- New: Epilogue

*Some other missions have not been altered in the sense of the script but were also affected by the clean up.*

NPCs affected by this change in Chateau d'Oraguille are Halver, Curilla, Rahal, Aramaviont, Milchupain, Nachou, Perfaumand, _6h0 (Trion), _6h1 (Pieuje), _6h4 (Great Hall) and in Northern San d'Oria _6fc (Papal Chambers).

Given the rather large scope of this commit I tested this very thoroughly during two days.
- [x] **I tested all missions from 1-1 to 9-2 and Epilogue several times with debugging commands and once without.**
- [x] **I tested all the quests that are not missions but are also affected by this commit:**
  - Lure of the wildcat
  - General's Secret
  - Enveloped in Darkness
  - Peace for the Spirit
  - Savage Blade quest
  - A Boy's Dream
  - Under Oath
- [x] **I re-viewed code several times**

If despite all the above, and me being very positive about the correctness of this commit, someone should find a bug, a failing condition or just spelling mistakes I apologize in advance and if called out directly in this commit I'll fix it as soon as possible.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 07, 2020 at 00:35:23_

----

Style request:
```lua
        elseif
            player:hasCompletedMission(SANDORIA, missions.LIGHTBRINGER) and
            player:getRank() == 9 and player:getRankPoints() == 0
        then
```
Since its 2 wide to be one line, this is the preferred way to break them in lua


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 06:38:20_

----

Caching this table here, and then bailing out if you're not Sandorian at the start of the trigger logic has the unpleasant side effect of making it hard to parse what's going on if you dive into the middle of the file.
In order to know "Oh this is for Sandorians only" or "all of these missions are for Sandoria" you have to scroll up and read the whole file.
I don't think any of the tabled quest id's are so verbose that they benefit from this improvement.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 06:40:06_

----

These would make more sense over 3 lines


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Oct 10, 2020 at 20:04:01_

----

@zach2good I set this as a top priority variable to also re-use it in `onEventFinish()`. It's one of the more used arrays in the whole script and **is unconditionally called three times in `onTrigger()` right at the beginning** to cache a few San d'Orian quests that are ***not missions*** (this was already in place, they're cached because they're checked for several times):

- "The General's Secret"
- "Peace for the Spirit" (RDM AF Body)
- "Enveloped in Darkness" (RDM AF Shoes)

So if you call that three times `onTrigger()` anyways, why not cache it right away and make good use of it? Missions are handled completely on their own with `missions` inside of the mission branch. I was thinking it makes sense to cache it right away for that reason.

> bailing out if you're not Sandorian at the start of the trigger logic

I can not find this to be true at all? A nation check is only made for the missions branch.

To be honest I don't see how you would have to scroll up to see what `questList` calls, to understand in a blink of an eye that it's basically an array that holds the name of the quest currently looked at. And the comments are very explicit about what quest is being checked.

Of course whatever you think to be correct here I'll happily just correct it right away.
What do you think? Will implement your answer.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Oct 10, 2020 at 23:00:43_

----

Also how would you prefer to organize the incredible amount of parallelism in such a case? I branched the San d'Oria missions into their own condition so they can be skipped fast if you're just RDM or somebody doing Wildcat etc. I think this behavior is also very well documented in the file and does not require scanning a lot. The variables names are quite verbose as well.

Curilla was looking like Halver, you had to read every line very carefully to try to get a grasp of what's going on, and adding all those optional dialogues she would've ended up *exactly* like Halver. I think opening a path for missions on any NPC might be a good idea to reduce requests if there are more than two missions involved. Why would a Bastok MNK need to go through all those mission checks?

Would like to hear your opinion for feedback here :)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:31:59_

----

I think my issue here is that `questList` doesn't give away that it's Sandorian quests without further context.  But if you're already looking in that file, you probably know the context, so I'm probably worrying over nothing.

I wasn't saying that a Bastoker would need to go through those checks, I was suggesting that the reader would be doing a CTRL+SHIFT+F or some other operation that dumps them in the middle of the file and then they have to spend more time figuring out whats going on.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 07, 2020 at 00:35:23_

----

Style request:
```lua
        elseif
            player:hasCompletedMission(SANDORIA, missions.LIGHTBRINGER) and
            player:getRank() == 9 and player:getRankPoints() == 0
        then
```
Since its 2 wide to be one line, this is the preferred way to break them in lua


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 06:38:20_

----

Caching this table here, and then bailing out if you're not Sandorian at the start of the trigger logic has the unpleasant side effect of making it hard to parse what's going on if you dive into the middle of the file.
In order to know "Oh this is for Sandorians only" or "all of these missions are for Sandoria" you have to scroll up and read the whole file.
I don't think any of the tabled quest id's are so verbose that they benefit from this improvement.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 06:40:06_

----

These would make more sense over 3 lines


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Oct 10, 2020 at 20:04:01_

----

@zach2good I set this as a top priority variable to also re-use it in `onEventFinish()`. It's one of the more used arrays in the whole script and **is unconditionally called three times in `onTrigger()` right at the beginning** to cache a few San d'Orian quests that are ***not missions*** (this was already in place, they're cached because they're checked for several times):

- "The General's Secret"
- "Peace for the Spirit" (RDM AF Body)
- "Enveloped in Darkness" (RDM AF Shoes)

So if you call that three times `onTrigger()` anyways, why not cache it right away and make good use of it? Missions are handled completely on their own with `missions` inside of the mission branch. I was thinking it makes sense to cache it right away for that reason.

> bailing out if you're not Sandorian at the start of the trigger logic

I can not find this to be true at all? A nation check is only made for the missions branch.

To be honest I don't see how you would have to scroll up to see what `questList` calls, to understand in a blink of an eye that it's basically an array that holds the name of the quest currently looked at. And the comments are very explicit about what quest is being checked.

Of course whatever you think to be correct here I'll happily just correct it right away.
What do you think? Will implement your answer.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Oct 10, 2020 at 23:00:43_

----

Also how would you prefer to organize the incredible amount of parallelism in such a case? I branched the San d'Oria missions into their own condition so they can be skipped fast if you're just RDM or somebody doing Wildcat etc. I think this behavior is also very well documented in the file and does not require scanning a lot. The variables names are quite verbose as well.

Curilla was looking like Halver, you had to read every line very carefully to try to get a grasp of what's going on, and adding all those optional dialogues she would've ended up *exactly* like Halver. I think opening a path for missions on any NPC might be a good idea to reduce requests if there are more than two missions involved. Why would a Bastok MNK need to go through all those mission checks?

Would like to hear your opinion for feedback here :)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:31:59_

----

I think my issue here is that `questList` doesn't give away that it's Sandorian quests without further context.  But if you're already looking in that file, you probably know the context, so I'm probably worrying over nothing.

I wasn't saying that a Bastoker would need to go through those checks, I was suggesting that the reader would be doing a CTRL+SHIFT+F or some other operation that dumps them in the middle of the file and then they have to spend more time figuring out whats going on.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 11, 2020 at 00:51:10_

----

d5690fc49ad1e4d3b26be662bab1b28664962cba adds two more very short additional dialogues to the gate guards in front of the Great Hall in Chateau d'Oraguille as mentioned in #1311 
That issue would therefore be closed with this PR.
