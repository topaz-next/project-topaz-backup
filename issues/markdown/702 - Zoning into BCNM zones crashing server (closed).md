**Labels:**



<a href="https://github.com/AvNytemare"><img src="https://avatars1.githubusercontent.com/u/66345297?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [AvNytemare](https://github.com/AvNytemare)**
_Wednesday Jun 10, 2020 at 02:29:31_
_Originally opened as: project-topaz/topaz - Issue 702_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [X] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [X] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Only addon loaded: Ashita Recast

There is about an 80% chance to crash the server upon zoning into an area containing a burning circle. It is not limited to just one specific BCNM area, it happens with all of them. There also seems to be a chance that if you successfully make it into the zone where you can enter the burning circle, that upon entering a BCNM fight it will also cause a crash, resulting in the loss of the fight and leaving you stuck in the zone, the only way out is to warp or get GM assistance if no warp is available.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jun 10, 2020 at 02:47:34_

----

if this is a windows based server, I suggest you attach the visual studio debugger. when it crashes again you can have visual studio save the crashdump to a folder, copy your executable and .pdb (program debug build file) and pack those with something like 7zip, throw it on drop box or googledrive or something so someone can download and review the crash. You might also be able to spot the problem yourself looking at the call stack with some practice.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jun 10, 2020 at 02:48:59_

----

if the server is linux based I've never done a crashdump there so we'd need to a ~~fireman~~ ~~police officer~~ ~~scientist~~ _linux programmer_ for help


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Jun 24, 2020 at 19:48:11_

----

Still happening with latest Canary from last week.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Jun 26, 2020 at 16:33:38_

----

here you go @TeoTwawki  (but this doesnt come from VS)
```
#0  0x00007f893eb6cd2d in __GI___pthread_timedjoin_ex (threadid=140227398309632, thread_return=0x0, abstime=0x0, block=<optimized out>)
    at pthread_join_common.c:89
#1  0x00007f893e058933 in std::thread::join() () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#2  0x000055c69a4521e5 in do_final (code=0) at src/map/map.cpp:280
#3  0x000055c69a39c45c in main (argc=1, argv=0x7ffd6374a058) at src/common/kernel.cpp:272
```

^thats the backtrace and the last message before the hange:

```
double free or corruption (out)
[26/Jun] [01:28:46][Debug] Message: Received message 0 from message server
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jun 26, 2020 at 17:09:59_

----

hmm.
```cpp

void do_final(int code)
{
    delete[] g_PBuff;
    delete[] PTempBuff;

    itemutils::FreeItemList();
    battleutils::FreeWeaponSkillsList();
    battleutils::FreeMobSkillList();

    petutils::FreePetList();
    trustutils::FreeTrustList();
    zoneutils::FreeZoneList();
    luautils::free();
    message::close();
    if (messageThread.joinable())
    {
        messageThread.join(); // this here is "src/map/map.cpp:280"
    }

    delete CTaskMgr::getInstance();
    delete CVanaTime::getInstance();

    Sql_Free(SqlHandle);

    timer_final();
    socket_final();

    exit(code);
}


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jun 26, 2020 at 19:53:09_

----

Thanks @kaincenteno . I was able to see some of the in-project calls from the core dump you provided, it looks like it ran through do_final part way, hit an exception (system library, no debug symbols available so not sure which one) which raised a SIG_ABRT and the sig handler tried to call do_abort which double free'd those resources which aren't being set and checked for nullptr.

I am reasonably sure this was all only a secondary spillover effect from whatever caused the server to originally exit, but it's obfuscated the original cause and sorting it out might be the first step to finding out what's really causing it.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jun 27, 2020 at 15:19:59_

----

from yesterday's crash (after teleporting out from bcnm area to the outside world) 
```sh
/bin/sh: 1: Syntax error: Bad fd number
double free or corruption (out)
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 27, 2020 at 15:22:49_

----

Fd was bad because that session was already gone. We’re still after whatever the initial problem was :(


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Jul 01, 2020 at 05:25:35_

----

I found out what was causing the isssue, it's releasing the trusts after finishing a BCNM on the waiting area.

How I was able to reproduce this issue:

* Went into Return to Delkfutt's Tower mission
* Summoned trust in battle
* Finished the fight and watched CS
* After CS finished was teleporting to area without a map
* did /refa all and it R0

This issue was never experienced before trusts were implemented so it makes sense it happens because of trusts, i haven't test it with pets


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Jul 06, 2020 at 05:29:08_

----

kain and I managed to get a core dump of that recurring BCNM crash. Here's the cliff notes version:
```
Thread #1 (Suspended : Signal : SIGSEGV:Segmentation fault)    
    0x7fffffff00a8    
    CZoneEntities::ZoneServer() at zone_entities.cpp:1,090 0x5555556bb749    
    CZone::ZoneServer() at zone.cpp:806 0x5555556b4b4b    
    zone_server() at zone.cpp:83 0x5555556b5923    
    CTaskMgr::DoTimer() at taskmgr.cpp:78 0x555555591ab9    
    main() at kernel.cpp:267 0x555555571440
```
Second from top it tried to call `PTrust->PRecastContainer->Check();` I confirmed, PTrust was not null. I couldn't see into PRecastContainer, as though it wasn't a valid object. The call to `check()` appears to be what resulted in the jump to 0x7fffffff00a8 causing the segfault.

@zach2good might know better than I.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Jul 06, 2020 at 09:09:46_

----

Commenting so this stays in my "recent activity tab", will check this out later


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Monday Jul 20, 2020 at 16:52:35_

----

Any news here? This is really the #1 Topaz issue atm, crashing multiple times per day now that Canary server has a 'decent' population...


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Jul 20, 2020 at 17:09:58_

----

According to the Discord, I believe Zach has been looking trying to reproduce the issue; when he has the time.

This is undoubtedly, a frustrating bug for all involved. That said, `canary` is the *testing* branch, and bugs are to be expected. If a less "unexpected" experience is desired, I would recommend using the `release` branch; all features will end up there when they are ready. :)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Jul 20, 2020 at 18:54:01_

----

The accessing of recast container is likely only happening because of the C-style cast on the line above. This original crash is looking very much like too many trusts are being removed from `m_trustList`. I wonder if it would be worth replacing that section with:
```
        CTrustEntity* PTrust = static_cast<CTrustEntity*>(trustit->second);
        if (!PTrust) { continue; } <--
        ...
        PTrust->PRecastContainer->Check();
```
or some such. The "quick fix" would be to put in enough error checking that a bogus trust pointer can't be made and then used. The real fix would be to make sure we don't remove too many trusts from the list etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Jul 27, 2020 at 08:39:04_

----

https://github.com/project-topaz/topaz/pull/877
