**Labels:**

merge ready



<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 01, 2020 at 22:03:13_
_Originally opened as: project-topaz/topaz - Issue 459_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:37:14_

----

should keep this commented out until the battle is fully coded (i.e. the mobs have their battle mechanics that make the fight challenging)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:38:23_

----

Only want to set this charvar on players currently on this quest / at this stage


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:42:45_

----

Remove unnecessary parentheses.  Because this PR is specifically about adding the questline content, I recommend NOT fixing semicolons and parens on unrelated lines.  But for new lines you're adding, follow the "no unnecessary parentheses" rule, even if the existing file has them.  We'll clean up the existing ones in later, style-specific PRs.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:43:38_

----

Unnecessary parens here and elsewhere.  Will stop commenting on them.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:45:15_

----

unused import of keyitems
missing import of quests, which is used on lines 41 and 42.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:45:42_

----

lower camel case variable names.
`local earring =`

also, this variable isn't used anywhere in the script.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:48:40_

----

line-wrap these very long lines, so they're easier for reviewers to see on GitHub.  I usually line break them something like this:

```
    if
        player:getCurrentMission(COP) == tpz.mission.id.cop.THE_LAST_VERSE and 
        (
            player:hasItem(15962) or
            player:hasItem(15963) or
            player:hasItem(15964) or
            player:hasItem(15965) or
            player:hasItem(15966)
        )
    then
        return
    else	
        player:startEvent(5)
    end
```


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:50:07_

----

this doesn't do anything.  can just leave the function empty and get same result


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:50:40_

----

these function comments aren't needed.  we removed them from most files in the project a while back.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:51:17_

----

tabs causing weird indentation here


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:52:18_

----

missing indentation


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:53:34_

----

unused import: keyitems


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:56:09_

----

where is event 234 being started?


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 03:02:30_

----

this whole function is improperly indented, and when you fix the indentation it makes some logic errors apparent.  here's what it looks like with fixed indentation:

```
function onEventFinish(player,csid,option)

    if (csid == 99) then
        player:tradeComplete();
        player:setCharVar("MissionStatus",3);
    elseif (csid == 232 or csid == 234) then -- 
        local reward = 0;
        if (option == 1) then
            reward = 15962; -- Static Earring
        elseif (option == 2) then
            reward = 15963; -- Magnetic Earring
        elseif (option == 3) then
            reward = 15964; -- Hollow Earring
        elseif (option == 4) then
            reward = 15965; -- Ethereal Earring
        end

        if (reward ~= 0) then
            if (player:getFreeSlotsCount() >= 1 and player:hasItem(reward) == false) then
                player:addItem(reward);
                player:messageSpecial(ID.text.ITEM_OBTAINED,reward)
                player:completeQuest(JEUNO,tpz.quest.id.jeuno.APOCALYPSE_NIGH)
                player:addMission(COP, tpz.mission.id.cop.THE_LAST_VERSE)
                player:addMission(ZILART,tpz.mission.id.zilart.THE_LAST_VERSE)
            end
            player:setCharVar("ApocalypseNigh",0)
        else
            player:messageSpecial(ID.text.ITEM_CANNOT_BE_OBTAINED,reward)
        end
    end		
end;
```

this would set the player's variable to 0 when they didn't have inventory space for the reward.  it would also give an "Item cannot be obtained" message then reward was 0.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 03:03:48_

----

unused import: missions
missing import: keyitems, which is used on line 11 and elsewhere

same for other two fluxes


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 03:05:56_

----

can join case 1 and 3:

```
function onTrigger(player, npc)
    if
        player:getQuestStatus(JEUNO,tpz.quest.id.jeuno.SHADOWS_OF_THE_DEPARTED) == QUEST_ACCEPTED and
        not player:hasKeyItem(tpz.ki.PROMYVION_DEM_SLIVER)
    then
        player:addKeyItem(tpz.ki.PROMYVION_DEM_SLIVER)
        player:messageSpecial(ID.text.KEYITEM_OBTAINED, tpz.ki.PROMYVION_DEM_SLIVER)
    else
        player:messageSpecial(ID.text.NOTHING_OUT_OF_ORDINARY)
    end
end
```

same for other two fluxes


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 03:07:29_

----

indentation issues


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 03:08:15_

----

long lines, unnecessary parens


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:45:17_

----

Seconding leaving this commented out; Ealdnarche isn't finished.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:46:27_

----

You're setting and then immediately checking for the same char var here~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:49:00_

----

Can remove this second line header


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:50:43_

----

Be sure to remove requires you're not going to use~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:52:00_

----

For new files you're adding, you can go ahead and make sure new semi-colons aren't being introduced


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:57:26_

----

Semi-colon here


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:57:53_

----

Be sure new commas you're adding have spaces between them:
`function onTrade(player, npc, trade)`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:59:50_

----

And to kill these empty lines at the start of functions~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:00:06_

----

Indent please~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:01:43_

----

Also do me a favor: for the new files you're adding, make sure there's a final newline at the end of the line (and that there isn't trailing spaces on the end of lines).

mrhappyasthma recently did a PR to make sure all lines ended with a newline character, so we wanna try to keep them that way! 😄 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:03:23_

----

Your `elseif` indenting (and subsequent lines) here is one too much~

(Also remember spaces after commas and removing excess parens)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:45:51_

----

There should be checks for the two ZM-17 CSes here (Aldo and Gilgamesh). Both are required to flag the quest, and they can be done in either order.

Check for quest completion of Storms of Fate instead of possessing the Whisper KI, if you would~

Wiki also says a game day wait is involved since completing Storms of Fate

(And indenting seems off here)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:48:15_

----

You can [use `npcUtil.giveKeyItem` to make these into one call](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L284-L293).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:49:36_

----

These extra parens aren't needed 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 04:04:07_

----

Don't need params around each condition here


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 04:34:59_

----

Again, can use npcUtil to make it only one call


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 04:36:26_

----

Text should be "It appears to be a barrier woven from the energy of overflowing memories..."


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 06:57:11_

----

Few things:
1) As written, this will trigger for players that haven't done anything. Despite the slightly confusing name of the enum, `QUEST_AVAILABLE` is just zero, which is the default for players who haven't touched a quest - the functions don't check the actual requirements for you (in the current quest system; this will be addressed in the future) 😅 

2) So you'll need to check for completion of Shadows of the Departed

3) There's also a game day wait

4) You don't/shouldn't need to check if the ApocalypseNigh var is zero if you're checking for QUEST_AVAILABLE; the var will _always_ be zero if the quest has never been started or reset, because the var should be cleared upon quest completion

5) And indenting is off 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 09:28:58_

----

The `ApocalypseNigh` var starts out at zero, and in the case of resets/repeats, should already be zero (either after the original completion of the quest, or during the reset itself)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 10:46:24_

----

Be sure to set the gameday wait for Apoc Nigh too~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 10:56:01_

----

bgwiki says there's a rank 5 check as well; which might seem redundant since ZM is supposed to have been completed, but it is possible for players to change nations and reset their rank.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:06:34_

----

[`getMidnight` is what you want, which returns the next midnight](https://github.com/project-topaz/topaz/blob/release/scripts/globals/common.lua#L48-L71)

Your later check can then just be `os.time() >= player:getCharVar("Apoc_Nigh_Reward")`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:07:52_

----

When using `getMidnight` with Aldo, this line won't be needed~! 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:09:16_

----

And as before, `os.time() > player:getCharVar("Apoc_Nigh_Reward")`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:10:36_

----

Which of these params are needed? I suspect the last three might not be.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:20:23_

----

Gilgamesh starts event 232 the first time you speak to him; and if you select the option to decide later, he'll start 234 instead. There should be a var set for if the player has already asked to decide later, and Gilgamesh should be choosing the appropriate event based on that.

(Also, option should be 99; option 1 seems to be sent in response to the player choosing an earring)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:21:06_

----

232 or 234

And if you wrap this in an if check to make sure the option is _not_ the cancel option, you shouldn't need to check if you've assigned a reward down below.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:28:37_

----

[npcUtil.giveItem can be used here; it attempts to give an item, and returns true if it succeeded](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L185-L195)

```lua
if npcUtil.giveItem(player, reward) then
    player:completeQuest(JEUNO, tpz.quest.id.jeuno.APOCALYPSE_NIGH)
    -- etc
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:34:20_

----

This doesn't happen; if you choose to cancel the event, Gilgamesh will say the proper lines as part of 232. If he doesn't by default, the client might need an event update in response to the cancel option.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:35:16_

----

Indenting here is off


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:39:33_

----

Looking at captures, they're both level 78

(And when you have to pick pool IDs, do a favor for the more OCD inclined and have the pool IDs be sequential 😅 )


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:44:46_

----

These will cause a merge conflict if they already haven't (my fault, I quick-merged trust ID reservations)

The next free ID after eye-of-the-storm is merged into release (this week) will be 1141

If you're new to Git, I should point out that Git doesn't care about the value of lines, only if they were changed since the last time you tried to edit the same line (in this case, line 3464). It's the "history" that causes the merge conflict; so you'll need to "rebase" on top of current release to resolve the conflict - just adjusting the skill (and later, spell) list IDs won't be enough.

Please let us know if you need help with this!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:45:01_

----

Comment the skill names, please~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:45:34_

----

And reorder these so they go up sequentially by skill ID, if you would!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:46:19_

----

Will this need a skill script?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:47:50_

----

These spell list IDs will also be a conflict with the recently-merged reservations for trusts; the next free ID is 429


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:48:34_

----

The elemental -agas should be listed before the AM (increasing spell IDs), and Sleepga II should be between Flood and Bindga


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:48:48_

----

And comment these please~!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 07, 2020 at 12:34:36_

----

since the name field is purely for human readability, how about
 `'EaldNarche (Apoc Nigh)'` ? 
Standard practice is to strip the apostrophes rather than turn them to underscores, and this makes it easier to see which one he is since the 1st two versions of him are in the same zilart mission. and this one is not.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 12:50:56_

----

+1 on stripping and renaming


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 07, 2020 at 12:53:12_

----

Same for Kamlawhatever :)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 07, 2020 at 16:26:02_

----

`cop == player:getQuestStatus(JEUNO, tpz.quest.id.jeuno.APOCALYPSE_NIGH) == QUEST_ACCEPTED`

should be just

`player:getQuestStatus(JEUNO, tpz.quest.id.jeuno.APOCALYPSE_NIGH) == QUEST_ACCEPTED`


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 07, 2020 at 16:27:56_

----

Also, this code is setting ApocalypseNigh variable to 5 on all players in the battle, even those not currently on that quest.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 07, 2020 at 16:34:52_

----

Naming convention for battlefield luas is: `all_lower_case.lua`

Note: to fix this, don't use Windows to rename the file.  Instead, use your Git client to do it, so Git knows about the rename.  You use TortoiseGit, so you could either:

* right click the file > TortoiseGit > rename

or if you prefer bash command line,

* `git mv <old filename> <new filename>`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 10:59:24_

----

I don't know if we have official style rules for multi-line if checks, but this `then` might be clearer if moved back an indent:

```lua
if
    condition1 and
    condition2
then
    do_this()
else
    do_something_else()
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 10:59:50_

----

Blank line between closing `end` and start of next function please~ 😄 

(Through this file)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:22:40_

----

Pull the indent on this `elseif` back by one indent


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:25:09_

----

Break the `then` onto the next line if this is going to be a multi-line `if`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:26:58_

----

You've got event 234 starting now, but will need to have an `or` in the update to account for both 232 and 234


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:35:54_

----

Remember to delete quest vars too~

(And spaces after commas!)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:40:37_

----

Got some spaces between the `player:startEvent` and opening paren to your arguments `(161)` here and elsewhere in section


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:41:25_

----

Indenting of these ends is off, and might mean there's some logic errors going on


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:42:00_

----

There's tabs on these lines instead of spaces~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:13:42_

----

Think you'll want [`getVanaMidnight` (next game day)](https://github.com/project-topaz/topaz/blob/release/scripts/globals/common.lua#L73-L78) here instead of `getMidnight` (server midnight)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:16:32_

----

Might wanna require the quests global 😉 

(Here and the other fluxes)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:19:45_

----

Do both players that are and aren't on the quest get event 7?

Is there an option to skip the event?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:20:10_

----

Indenting is off


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:36:28_

----

Hate sounding picky: Stellar Burst (985) should be listed before Vortex (986)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:42:22_

----

Now that the skill and spell list IDs have been adjusted in `mob_skill_lists` and `mob_spell_list`, they'll need to be updated in the original `mob_pools` too~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:47:08_

----

You actually might need parens here to clarify the order of operations; since
they can enter `if`:
they've completed `or` **(** are on quest `and` on step 4 **)**
```lua
    player:hasCompletedQuest(JEUNO, tpz.quest.id.jeuno.APOCALYPSE_NIGH) or 
    (player:getQuestStatus(JEUNO, tpz.quest.id.jeuno.APOCALYPSE_NIGH) == QUEST_ACCEPTED and 
    player:getCharVar('ApocalypseNigh') == 4)
```


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 14, 2020 at 05:20:59_

----

It's okay as coded.  AND happens before OR.  That said, parens don't hurt in cases like this, where it makes the order of operations clear to people reading it in the future.
*edit: Oh, this is outdated code.  Leaving comment for posterity.*


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 14, 2020 at 13:58:00_

----

Oh, I see it seems to already have a script; I assumed it didn't because it was previously commented out and wasn't being added. 😅 


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:37:14_

----

should keep this commented out until the battle is fully coded (i.e. the mobs have their battle mechanics that make the fight challenging)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:38:23_

----

Only want to set this charvar on players currently on this quest / at this stage


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:42:45_

----

Remove unnecessary parentheses.  Because this PR is specifically about adding the questline content, I recommend NOT fixing semicolons and parens on unrelated lines.  But for new lines you're adding, follow the "no unnecessary parentheses" rule, even if the existing file has them.  We'll clean up the existing ones in later, style-specific PRs.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:43:38_

----

Unnecessary parens here and elsewhere.  Will stop commenting on them.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:45:15_

----

unused import of keyitems
missing import of quests, which is used on lines 41 and 42.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:45:42_

----

lower camel case variable names.
`local earring =`

also, this variable isn't used anywhere in the script.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:48:40_

----

line-wrap these very long lines, so they're easier for reviewers to see on GitHub.  I usually line break them something like this:

```
    if
        player:getCurrentMission(COP) == tpz.mission.id.cop.THE_LAST_VERSE and 
        (
            player:hasItem(15962) or
            player:hasItem(15963) or
            player:hasItem(15964) or
            player:hasItem(15965) or
            player:hasItem(15966)
        )
    then
        return
    else	
        player:startEvent(5)
    end
```


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:50:07_

----

this doesn't do anything.  can just leave the function empty and get same result


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:50:40_

----

these function comments aren't needed.  we removed them from most files in the project a while back.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:51:17_

----

tabs causing weird indentation here


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:52:18_

----

missing indentation


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:53:34_

----

unused import: keyitems


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 02:56:09_

----

where is event 234 being started?


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 03:02:30_

----

this whole function is improperly indented, and when you fix the indentation it makes some logic errors apparent.  here's what it looks like with fixed indentation:

```
function onEventFinish(player,csid,option)

    if (csid == 99) then
        player:tradeComplete();
        player:setCharVar("MissionStatus",3);
    elseif (csid == 232 or csid == 234) then -- 
        local reward = 0;
        if (option == 1) then
            reward = 15962; -- Static Earring
        elseif (option == 2) then
            reward = 15963; -- Magnetic Earring
        elseif (option == 3) then
            reward = 15964; -- Hollow Earring
        elseif (option == 4) then
            reward = 15965; -- Ethereal Earring
        end

        if (reward ~= 0) then
            if (player:getFreeSlotsCount() >= 1 and player:hasItem(reward) == false) then
                player:addItem(reward);
                player:messageSpecial(ID.text.ITEM_OBTAINED,reward)
                player:completeQuest(JEUNO,tpz.quest.id.jeuno.APOCALYPSE_NIGH)
                player:addMission(COP, tpz.mission.id.cop.THE_LAST_VERSE)
                player:addMission(ZILART,tpz.mission.id.zilart.THE_LAST_VERSE)
            end
            player:setCharVar("ApocalypseNigh",0)
        else
            player:messageSpecial(ID.text.ITEM_CANNOT_BE_OBTAINED,reward)
        end
    end		
end;
```

this would set the player's variable to 0 when they didn't have inventory space for the reward.  it would also give an "Item cannot be obtained" message then reward was 0.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 03:03:48_

----

unused import: missions
missing import: keyitems, which is used on line 11 and elsewhere

same for other two fluxes


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 03:05:56_

----

can join case 1 and 3:

```
function onTrigger(player, npc)
    if
        player:getQuestStatus(JEUNO,tpz.quest.id.jeuno.SHADOWS_OF_THE_DEPARTED) == QUEST_ACCEPTED and
        not player:hasKeyItem(tpz.ki.PROMYVION_DEM_SLIVER)
    then
        player:addKeyItem(tpz.ki.PROMYVION_DEM_SLIVER)
        player:messageSpecial(ID.text.KEYITEM_OBTAINED, tpz.ki.PROMYVION_DEM_SLIVER)
    else
        player:messageSpecial(ID.text.NOTHING_OUT_OF_ORDINARY)
    end
end
```

same for other two fluxes


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 03:07:29_

----

indentation issues


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Apr 02, 2020 at 03:08:15_

----

long lines, unnecessary parens


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:45:17_

----

Seconding leaving this commented out; Ealdnarche isn't finished.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:46:27_

----

You're setting and then immediately checking for the same char var here~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:49:00_

----

Can remove this second line header


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:50:43_

----

Be sure to remove requires you're not going to use~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:52:00_

----

For new files you're adding, you can go ahead and make sure new semi-colons aren't being introduced


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:57:26_

----

Semi-colon here


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:57:53_

----

Be sure new commas you're adding have spaces between them:
`function onTrade(player, npc, trade)`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 02:59:50_

----

And to kill these empty lines at the start of functions~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:00:06_

----

Indent please~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:01:43_

----

Also do me a favor: for the new files you're adding, make sure there's a final newline at the end of the line (and that there isn't trailing spaces on the end of lines).

mrhappyasthma recently did a PR to make sure all lines ended with a newline character, so we wanna try to keep them that way! 😄 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:03:23_

----

Your `elseif` indenting (and subsequent lines) here is one too much~

(Also remember spaces after commas and removing excess parens)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:45:51_

----

There should be checks for the two ZM-17 CSes here (Aldo and Gilgamesh). Both are required to flag the quest, and they can be done in either order.

Check for quest completion of Storms of Fate instead of possessing the Whisper KI, if you would~

Wiki also says a game day wait is involved since completing Storms of Fate

(And indenting seems off here)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:48:15_

----

You can [use `npcUtil.giveKeyItem` to make these into one call](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L284-L293).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 03:49:36_

----

These extra parens aren't needed 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 04:04:07_

----

Don't need params around each condition here


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 04:34:59_

----

Again, can use npcUtil to make it only one call


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 04:36:26_

----

Text should be "It appears to be a barrier woven from the energy of overflowing memories..."


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 06:57:11_

----

Few things:
1) As written, this will trigger for players that haven't done anything. Despite the slightly confusing name of the enum, `QUEST_AVAILABLE` is just zero, which is the default for players who haven't touched a quest - the functions don't check the actual requirements for you (in the current quest system; this will be addressed in the future) 😅 

2) So you'll need to check for completion of Shadows of the Departed

3) There's also a game day wait

4) You don't/shouldn't need to check if the ApocalypseNigh var is zero if you're checking for QUEST_AVAILABLE; the var will _always_ be zero if the quest has never been started or reset, because the var should be cleared upon quest completion

5) And indenting is off 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 09:28:58_

----

The `ApocalypseNigh` var starts out at zero, and in the case of resets/repeats, should already be zero (either after the original completion of the quest, or during the reset itself)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 10:46:24_

----

Be sure to set the gameday wait for Apoc Nigh too~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 10:56:01_

----

bgwiki says there's a rank 5 check as well; which might seem redundant since ZM is supposed to have been completed, but it is possible for players to change nations and reset their rank.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:06:34_

----

[`getMidnight` is what you want, which returns the next midnight](https://github.com/project-topaz/topaz/blob/release/scripts/globals/common.lua#L48-L71)

Your later check can then just be `os.time() >= player:getCharVar("Apoc_Nigh_Reward")`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:07:52_

----

When using `getMidnight` with Aldo, this line won't be needed~! 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:09:16_

----

And as before, `os.time() > player:getCharVar("Apoc_Nigh_Reward")`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:10:36_

----

Which of these params are needed? I suspect the last three might not be.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:20:23_

----

Gilgamesh starts event 232 the first time you speak to him; and if you select the option to decide later, he'll start 234 instead. There should be a var set for if the player has already asked to decide later, and Gilgamesh should be choosing the appropriate event based on that.

(Also, option should be 99; option 1 seems to be sent in response to the player choosing an earring)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:21:06_

----

232 or 234

And if you wrap this in an if check to make sure the option is _not_ the cancel option, you shouldn't need to check if you've assigned a reward down below.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:28:37_

----

[npcUtil.giveItem can be used here; it attempts to give an item, and returns true if it succeeded](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L185-L195)

```lua
if npcUtil.giveItem(player, reward) then
    player:completeQuest(JEUNO, tpz.quest.id.jeuno.APOCALYPSE_NIGH)
    -- etc
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:34:20_

----

This doesn't happen; if you choose to cancel the event, Gilgamesh will say the proper lines as part of 232. If he doesn't by default, the client might need an event update in response to the cancel option.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:35:16_

----

Indenting here is off


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:39:33_

----

Looking at captures, they're both level 78

(And when you have to pick pool IDs, do a favor for the more OCD inclined and have the pool IDs be sequential 😅 )


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:44:46_

----

These will cause a merge conflict if they already haven't (my fault, I quick-merged trust ID reservations)

The next free ID after eye-of-the-storm is merged into release (this week) will be 1141

If you're new to Git, I should point out that Git doesn't care about the value of lines, only if they were changed since the last time you tried to edit the same line (in this case, line 3464). It's the "history" that causes the merge conflict; so you'll need to "rebase" on top of current release to resolve the conflict - just adjusting the skill (and later, spell) list IDs won't be enough.

Please let us know if you need help with this!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:45:01_

----

Comment the skill names, please~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:45:34_

----

And reorder these so they go up sequentially by skill ID, if you would!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:46:19_

----

Will this need a skill script?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:47:50_

----

These spell list IDs will also be a conflict with the recently-merged reservations for trusts; the next free ID is 429


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:48:34_

----

The elemental -agas should be listed before the AM (increasing spell IDs), and Sleepga II should be between Flood and Bindga


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 11:48:48_

----

And comment these please~!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 07, 2020 at 12:34:36_

----

since the name field is purely for human readability, how about
 `'EaldNarche (Apoc Nigh)'` ? 
Standard practice is to strip the apostrophes rather than turn them to underscores, and this makes it easier to see which one he is since the 1st two versions of him are in the same zilart mission. and this one is not.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 07, 2020 at 12:50:56_

----

+1 on stripping and renaming


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 07, 2020 at 12:53:12_

----

Same for Kamlawhatever :)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 07, 2020 at 16:26:02_

----

`cop == player:getQuestStatus(JEUNO, tpz.quest.id.jeuno.APOCALYPSE_NIGH) == QUEST_ACCEPTED`

should be just

`player:getQuestStatus(JEUNO, tpz.quest.id.jeuno.APOCALYPSE_NIGH) == QUEST_ACCEPTED`


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 07, 2020 at 16:27:56_

----

Also, this code is setting ApocalypseNigh variable to 5 on all players in the battle, even those not currently on that quest.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 07, 2020 at 16:34:52_

----

Naming convention for battlefield luas is: `all_lower_case.lua`

Note: to fix this, don't use Windows to rename the file.  Instead, use your Git client to do it, so Git knows about the rename.  You use TortoiseGit, so you could either:

* right click the file > TortoiseGit > rename

or if you prefer bash command line,

* `git mv <old filename> <new filename>`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 10:59:24_

----

I don't know if we have official style rules for multi-line if checks, but this `then` might be clearer if moved back an indent:

```lua
if
    condition1 and
    condition2
then
    do_this()
else
    do_something_else()
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 10:59:50_

----

Blank line between closing `end` and start of next function please~ 😄 

(Through this file)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:22:40_

----

Pull the indent on this `elseif` back by one indent


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:25:09_

----

Break the `then` onto the next line if this is going to be a multi-line `if`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:26:58_

----

You've got event 234 starting now, but will need to have an `or` in the update to account for both 232 and 234


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:35:54_

----

Remember to delete quest vars too~

(And spaces after commas!)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:40:37_

----

Got some spaces between the `player:startEvent` and opening paren to your arguments `(161)` here and elsewhere in section


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:41:25_

----

Indenting of these ends is off, and might mean there's some logic errors going on


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 11:42:00_

----

There's tabs on these lines instead of spaces~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:13:42_

----

Think you'll want [`getVanaMidnight` (next game day)](https://github.com/project-topaz/topaz/blob/release/scripts/globals/common.lua#L73-L78) here instead of `getMidnight` (server midnight)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:16:32_

----

Might wanna require the quests global 😉 

(Here and the other fluxes)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:19:45_

----

Do both players that are and aren't on the quest get event 7?

Is there an option to skip the event?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:20:10_

----

Indenting is off


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:36:28_

----

Hate sounding picky: Stellar Burst (985) should be listed before Vortex (986)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:42:22_

----

Now that the skill and spell list IDs have been adjusted in `mob_skill_lists` and `mob_spell_list`, they'll need to be updated in the original `mob_pools` too~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 12:47:08_

----

You actually might need parens here to clarify the order of operations; since
they can enter `if`:
they've completed `or` **(** are on quest `and` on step 4 **)**
```lua
    player:hasCompletedQuest(JEUNO, tpz.quest.id.jeuno.APOCALYPSE_NIGH) or 
    (player:getQuestStatus(JEUNO, tpz.quest.id.jeuno.APOCALYPSE_NIGH) == QUEST_ACCEPTED and 
    player:getCharVar('ApocalypseNigh') == 4)
```


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 14, 2020 at 05:20:59_

----

It's okay as coded.  AND happens before OR.  That said, parens don't hurt in cases like this, where it makes the order of operations clear to people reading it in the future.
*edit: Oh, this is outdated code.  Leaving comment for posterity.*


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 14, 2020 at 13:58:00_

----

Oh, I see it seems to already have a script; I assumed it didn't because it was previously commented out and wasn't being added. 😅 


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Apr 01, 2020 at 23:38:54_

----

Please don't keep deleting and recreating your fork and PRs.  You only need to fork once, ever, and you only need to create one PR from your branch.  This is your current open PR, so it shouldn't be deleted until it's finished.  Everything that gets messy is fixable without deleting; just have patience and ask for help when needed.  Otherwise you end up leaving a bunch of garbage in the project's commit or PR history.

If you have time this evening, ping me on Discord and I'll help you neaten this PR up.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 14, 2020 at 13:00:48_

----

Notes from the latest commit

### General changes:

* Some style stuff (tabs -> spaces, fix indendation, add newline at bottom of files)
* Some missing includes
* Some post-quest-stage NPC dialog

### Shadows of the Departed:

* Quest now requires player to have finished Awakening
* Fixed default message on Memory Fluxes
* Fixed Memory Fluxes in Promyvion-Mea to match retail captures
* Added post-event message to "trade in three slivers" event

### Apocalypse Nigh:

* Rename Transcendental Radiance script
* Reordered Kam'lanaut and Eald'narch pools and lists
* Reassigned skill and spell lists
* Removed ancient magic from Eald'narch's spell list
* Set levels and immunities.
* Eald'narch now teleports
* Kam'lanaut now uses en-element weapon skills
* Apoc Nigh now progresses and warps characters who are on the correct stage of quest
* Midnight wait happens on Gilgamesh's door, rather than on Gilgamesh.
* Fixed options and parameters on "get earring" events
* Memory Reset NPC now sets progress so that it matches retail capture

### What's left to do:

* Kam'lanaut and Eald'narch are facing the wrong way when players enter arena.
* Kam'lanaut "Can perform three TP attacks upon reaching 100%+ TP, giving very little rest for healers. He can do 3 Great Wheels in a row, devastating any melee jobs in range."
* Kam'lanaut has trait "When using enspell TP moves, nukes of the matching element heal him."
* Eald'narch is "Highly evasive. Sushi and/or Madrigal recommended."
* Eald'narch has "Very high magic defense (e.g., Thunder IV ~65 dmg)."

Once these points are addressed, I think we can toggle the battlefield on in bcnm.lua.

Otherwise, I believe the rest of the questline is working/retail accurate and could merge into Topaz.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 14, 2020 at 15:20:31_

----

Thanks for the assist, Wren! 👍 

(I'm embarrassed I spaced checking and handling Zilart progress)

Pushed a small commit with my final nitpicks:
- Commented Ealdnarche 2's moves since the file diff from your rename brought them up. Saw he had the skills "ark_guardian_tarutaru" (936) and "tarutaru_warp_ii" (962). Went out on a limb and assumed it was someone trying to handle warping by copying TT and removed the skills now that there's Warp In and Warp Out.
- On that note, Ealdnarche's skill list was the only one using those two skills, so they are now orphaned.
- Cleared the var after the midnight wait between Shadows of the Departed and Apocalypse Nigh
- Overly pick spell list order correction
