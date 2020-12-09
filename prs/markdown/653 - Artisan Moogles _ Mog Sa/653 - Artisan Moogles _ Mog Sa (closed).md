**Labels:**

reviewed



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Monday May 25, 2020 at 16:24:38_
_Originally opened as: project-topaz/topaz - Issue 653_

----

Fully implemented code for the 4 Artisan Moogles and accompanying Mog Sack purchase/expansion abilities. They also now provide Warp Scrolls to players once per day as in retail. As retail-like capability exists now for purchasing Mob Sacks, this also sets default Mog Sack size for new players to 0 (as retail). Existing DBs will not be migrated, so as to not cause surprise issues for server admins & players.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 05:56:29_

----

Might wanna use `getMidnight()` instead, will keep this in line with everything else that resets at "JP" midnight.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday May 26, 2020 at 07:02:24_

----

Updated.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jun 08, 2020 at 21:34:25_

----

Let's make this mogVisited assignment if the sackSize is > 0 or the var is one. Then when the player purchases a sack (probably every player will), we can nuke the charVar, and not have a forever var lingering in char_vars table.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jun 08, 2020 at 22:52:02_

----

note: in other similar cases where you can't avoid what would be a forever var, you can start newly created characters at 1 and then zero them after, instead of starting 0 and moving to one. (see existing examples in player.lua)

Here, you don't have to do player.lua because we can check what ibm said.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Jun 08, 2020 at 22:56:07_

----

Great idea, ibm. I've changed it so it'll only be set 1 for as long as the player has no sack, and has talked to a moogle. It will be zeroed once they have a bag and check will be based on either or.

I'll push it once I've tested a bit later.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 05:56:29_

----

Might wanna use `getMidnight()` instead, will keep this in line with everything else that resets at "JP" midnight.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday May 26, 2020 at 07:02:24_

----

Updated.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jun 08, 2020 at 21:34:25_

----

Let's make this mogVisited assignment if the sackSize is > 0 or the var is one. Then when the player purchases a sack (probably every player will), we can nuke the charVar, and not have a forever var lingering in char_vars table.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jun 08, 2020 at 22:52:02_

----

note: in other similar cases where you can't avoid what would be a forever var, you can start newly created characters at 1 and then zero them after, instead of starting 0 and moving to one. (see existing examples in player.lua)

Here, you don't have to do player.lua because we can check what ibm said.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Jun 08, 2020 at 22:56:07_

----

Great idea, ibm. I've changed it so it'll only be set 1 for as long as the player has no sack, and has talked to a moogle. It will be zeroed once they have a bag and check will be based on either or.

I'll push it once I've tested a bit later.


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Wednesday Jun 10, 2020 at 02:17:11_

----

This will still never be necessary until the change inventory code is removed from Bluffnix.
`
function onEventFinish(player,csid,option)

    local TheGobbieBag = gobQuest(player,player:getContainerSize(0));

    if (csid == 43 and option == 0) then
        if (player:getQuestStatus(JEUNO,TheGobbieBag[1]) == 0) then
            player:addQuest(JEUNO,TheGobbieBag[1]);
        end
    elseif (csid == 73) then
        if (gobbieBag == 5) then
            player:addTitle(tpz.title.GREEDALOX);
        elseif (gobbieBag == 10) then
            player:addTitle(tpz.title.GRAND_GREEDALOX);
        end

        player:changeContainerSize(0,5);
        player:changeContainerSize(5,5);
        player:changeContainerSize(6,5);
        player:addFame(JEUNO, 30);
        player:addExp(player:getContainerSize(0) * EXP_RATE);
        player:tradeComplete();
        player:completeQuest(JEUNO,TheGobbieBag[1]);
        player:messageSpecial(ID.text.INVENTORY_INCREASED);
    elseif (csid == 10056) then
        player:setMaskBit(player:getCharVar("WildcatJeuno"),"WildcatJeuno",12,true);
    end
end;
`
