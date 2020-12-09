**Labels:**



<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [hooksta4](https://github.com/hooksta4)**
_Tuesday Mar 31, 2020 at 17:19:54_
_Originally opened as: project-topaz/topaz - Issue 457_

----

Shadows of the Departed and ApocNigh

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:19:44_

----

Don't turn this BCNM on until its content is fully coded (mobs, drops, etc.)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:23:31_

----

No tabs.  Set your editor to use 4 spaces for indentation.

I use TextPad, and for this project,
```
configure > preferences > document classes > default >
    [X] Strip trailing spaces from lines when saving
    tabulation >
        default tab spacing 4
        indent size 4
        [X] convert new spaces to tabs
        [X] convert existing tabs to spaces when saving files
```


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:26:33_

----

this will set the charVar on everyone who participated in the battle.  we only want to set it on people who are currently on this quest.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:32:04_

----

event 32001 is the victory event on pretty much every battlefield I've seen.  Check other bcnm scripts for use.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:33:13_

----

tabs (not gonna keep mentioning them, but tabs continue to be an issue in later files)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:36:13_

----

unused imports


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:36:58_

----

unused imports


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:37:18_

----

bad indentation


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:37:43_

----

indentation


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:38:00_

----

unused imports


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:39:29_

----

lots of style changes here that shouldn't be here.  this is probably from wholesale copying over this file with a modified version of an older copy.  you want to start with a fresh copy of what's in release branch, then only modify lines related to your questline


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:40:04_

----

bad indentation


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Tuesday Mar 31, 2020 at 22:25:34_

----

Mobs are in there, no drops.


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 01, 2020 at 00:05:59_

----

For these two, thinking this would work? 
 onEventFinish(player, csid, option)
    if csid == 32001 and player:getCharVar('ApocalypseNigh') == 4 then
      player:setPos(-.0745,-10,-465.1132,63,33);
      player:setCharVar('ApocalypseNigh',5);
    else
      player:setPos(-.0745,-10,-465.1132,63,33);


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 01, 2020 at 00:16:05_

----

Grabbed textpad and changed to those settings. 


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 01, 2020 at 00:19:40_

----

When obtaining a key item, I don't need to put in keyitems import? 


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:19:44_

----

Don't turn this BCNM on until its content is fully coded (mobs, drops, etc.)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:23:31_

----

No tabs.  Set your editor to use 4 spaces for indentation.

I use TextPad, and for this project,
```
configure > preferences > document classes > default >
    [X] Strip trailing spaces from lines when saving
    tabulation >
        default tab spacing 4
        indent size 4
        [X] convert new spaces to tabs
        [X] convert existing tabs to spaces when saving files
```


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:26:33_

----

this will set the charVar on everyone who participated in the battle.  we only want to set it on people who are currently on this quest.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:32:04_

----

event 32001 is the victory event on pretty much every battlefield I've seen.  Check other bcnm scripts for use.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:33:13_

----

tabs (not gonna keep mentioning them, but tabs continue to be an issue in later files)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:36:13_

----

unused imports


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:36:58_

----

unused imports


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:37:18_

----

bad indentation


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:37:43_

----

indentation


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:38:00_

----

unused imports


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:39:29_

----

lots of style changes here that shouldn't be here.  this is probably from wholesale copying over this file with a modified version of an older copy.  you want to start with a fresh copy of what's in release branch, then only modify lines related to your questline


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Mar 31, 2020 at 21:40:04_

----

bad indentation


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Tuesday Mar 31, 2020 at 22:25:34_

----

Mobs are in there, no drops.


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 01, 2020 at 00:05:59_

----

For these two, thinking this would work? 
 onEventFinish(player, csid, option)
    if csid == 32001 and player:getCharVar('ApocalypseNigh') == 4 then
      player:setPos(-.0745,-10,-465.1132,63,33);
      player:setCharVar('ApocalypseNigh',5);
    else
      player:setPos(-.0745,-10,-465.1132,63,33);


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 01, 2020 at 00:16:05_

----

Grabbed textpad and changed to those settings. 


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 01, 2020 at 00:19:40_

----

When obtaining a key item, I don't need to put in keyitems import? 


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 01, 2020 at 22:16:07_

----

updated with new forks and tabs because i suck at github.
