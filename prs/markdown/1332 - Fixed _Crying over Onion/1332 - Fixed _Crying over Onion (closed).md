**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 11, 2020 at 22:11:00_
_Originally opened as: project-topaz/topaz - Issue 1332_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Nanaa Mihgo now increases the charVar bit responsible for this to not make her repeat the dialogue regarding this quest. The remaining NPCs involved in "Crying for Onions" got their bit increased accordingly. Tested working locally and extensively by talking to every NPC before the quest, in every step during the quest, and after the quest.
Closes #880


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 22:18:13_

----

when we make a conditional span multi line, I think its easier to read when we put a newline at both ends of the condition and align the `then` to the start:

```lua
    elseif
        csid == 782 and 
        npcUtil.completeQuest(player, WINDURST, tpz.quest.id.windurst.WILD_CARD, {
            title=tpz.title.DREAM_DWELLER, fame=135, var="WildCard"
        })
    then
```


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 11, 2020 at 22:33:20_

----

Changed in accordance with **Inline tables** section from [Style Guide](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 22:48:47_

----

break at curly brace is what the existing examples and guide did/do


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 22:18:13_

----

when we make a conditional span multi line, I think its easier to read when we put a newline at both ends of the condition and align the `then` to the start:

```lua
    elseif
        csid == 782 and 
        npcUtil.completeQuest(player, WINDURST, tpz.quest.id.windurst.WILD_CARD, {
            title=tpz.title.DREAM_DWELLER, fame=135, var="WildCard"
        })
    then
```


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 11, 2020 at 22:33:20_

----

Changed in accordance with **Inline tables** section from [Style Guide](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 22:48:47_

----

break at curly brace is what the existing examples and guide did/do


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 11, 2020 at 22:48:11_

----

Trying to git amend on behalf of the Style Guide suggestions left me with a broken merge conflict which I am unable to resolve,...sigh. Line 93-94 should be below the comment `"-- Wild Card"`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 22:50:40_

----


> Trying to git amend on behalf of the Style Guide suggestions left me with a broken merge conflict which I am unable to resolve,...sigh. Line 93-94 should be below the comment `"-- Wild Card"`

did you happen to try and pull after amending? coz you don't want to do that if git push errors, the error would likely be from failing to do a force push instead of a regular push.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 13, 2020 at 13:51:53_

----

Looks good to me, thanks for all the cleanup too 👍 
