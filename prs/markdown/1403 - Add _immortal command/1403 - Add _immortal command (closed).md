**Labels:**



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 21, 2020 at 04:19:35_
_Originally opened as: project-topaz/topaz - Issue 1403_

----

Who wants to live forever?

Well, with this command we can be princes of the universe!

So while we're fighting to survive, we never fall to the darkest powers!

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 21, 2020 at 04:29:54_

----

um didn't catch the use of a status effect my first look over. lets not do that. 

Lets just used addStatusEX to make its a duplicate of brew effect instead, for the lols :+1: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 21, 2020 at 04:29:54_

----

um didn't catch the use of a status effect my first look over. lets not do that. 

Lets just used addStatusEX to make its a duplicate of brew effect instead, for the lols :+1: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 21, 2020 at 04:24:08_

----

Q: does unkillable prevent doom death and other instakills? :thinking: 

unkillable style instead of massive regen and 2hjhrs is legit how retail has their GMs not die. Thank you for thinking of this, it never occurred to me that flag would work on a player entity, I've been using a stripped down godmode instead for years when I want to test things.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Oct 21, 2020 at 04:24:25_

----

![image](https://user-images.githubusercontent.com/1389729/96673113-70849700-136e-11eb-8590-041adfa1f8e6.png)



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 21, 2020 at 04:50:49_

----

> Q: does unkillable prevent doom death and other instakills?

Looking like it doesn't. Unkillable just prevents your HP from falling down to 0 in `addHP`. Doom just calls `setHP(0)` outright. So you're still technically killable.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 21, 2020 at 04:58:45_

----

> 
> 
> > Q: does unkillable prevent doom death and other instakills?
> 
> Looking like it doesn't. Unkillable just prevents your HP from falling down to 0 in `addHP`. Doom just calls `setHP(0)` outright. So you're still technically killable.

K I still need doom screen and deathres if I test mobs with access to those then :( that sucks


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 21, 2020 at 05:02:11_

----

Actually! I may have lied! I didn't read `setHP` very closely!

```cpp
    ((CBattleEntity*)m_PBaseEntity)->health.hp = 0;
    auto value = (int32)lua_tointeger(L, 1);
    ((CBattleEntity*)m_PBaseEntity)->addHP(value);
```

Since `addHP` was called and the entity's HP is currently zero, unkillable bumps it back up to 1 (in `addHP`).

Just tested with `!immortal` and `!hp 0`!
