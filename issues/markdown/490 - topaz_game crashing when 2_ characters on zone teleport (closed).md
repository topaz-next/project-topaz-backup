**Labels:**

bug



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Monday Apr 13, 2020 at 05:51:15_
_Originally opened as: project-topaz/topaz - Issue 490_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- x[] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
This is happening on the Canary branch.
When 2+ characters are zoning at the same time from one zone to another it will make the map server crash.

```[12/Apr] [16:07:10][Info] parse: 016 | 16AD 169B 04 from user: Mio
[12/Apr] [16:07:11][Info] parse: 05E | 176A 1758 0C from user: Hiro
[12/Apr] [16:07:11][Info] Zoning from zone 100 to zone 102: Hiro
[12/Apr] [16:07:11][Info] parse: 00D | 176B 1759 04 from user: Hiro
[12/Apr] [16:07:11][Debug] CZone:: West_Ronfaure DecreaseZoneCounter <2> Hiro
[12/Apr] [16:07:11][Debug] Message: Received message 8 from message server
[12/Apr] [16:07:12][Info] parse: 016 | 17A8 1797 04 from user: Mei
/bin/sh: 1: Syntax error: Bad fd number
[12/Apr] [16:07:14][Fatal Error] --- gdb backtrace ---
[12/Apr] [16:07:14][Status] luautils::free:lua free...         - [OK]
topaz_game: /usr/include/zmq.hpp:406: zmq::context_t::~context_t(): Assertion `rc == 0' failed.
[12/Apr] [16:07:14][Fatal Error] --- gdb backtrace ---
double free or corruption (!prev)```



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Apr 17, 2020 at 02:51:59_

----

issue still happening on latest version of canary branch (just built today)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Apr 17, 2020 at 03:16:56_

----

If possible you may want to install **gdb** on your server, this way it should print a stacktrace the next time it crashes. That would help someone know where to start looking.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Apr 17, 2020 at 06:05:47_

----

just installed it. Weird i cannot reproduce it on my machine, I'm now curious what it will show up as it's only seen by one user.

Thanks for the suggestion @Kreidos 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Apr 17, 2020 at 15:31:23_

----

Here is the better debug. Thank you @Kreidos  for teaching me something new today =)

```[17/Apr] [02:58:13][Info] parse: 00D | 1F58 1F57 04 from user: Nanaamihgo
[17/Apr] [02:58:13][Debug] CZone:: South_Gustaberg DecreaseZoneCounter <0> Nanaamihgo
[17/Apr] [02:58:13][Debug] Message: Received message 8 from message server
/bin/sh: 1: Syntax error: Bad fd number
[17/Apr] [02:58:13][Fatal Error] --- gdb backtrace ---
[17/Apr] [02:58:13][Status] luautils::free:lua free...         - [OK]
topaz_game: /usr/include/zmq.hpp:406: zmq::context_t::~context_t(): Assertion `rc == 0' failed.
[17/Apr] [02:58:16][Fatal Error] --- gdb backtrace ---
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
0x00007f7b46c1423a in __waitpid (pid=3685, stat_loc=0x0, options=0) at ../sysdeps/unix/sysv/linux/waitpid.c:30
Saved corefile core.1736
#0  0x00007f7b46c1423a in __waitpid (pid=3685, stat_loc=0x0, options=0) at ../sysdeps/unix/sysv/linux/waitpid.c:30
#1  0x000056322b4aed03 in dump_backtrace () at src/common/kernel.cpp:126
#2  0x000056322b4af0a5 in sig_proc (sn=6) at src/common/kernel.cpp:160
#3  <signal handler called>
#4  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#5  0x00007f7b45a70801 in __GI_abort () at abort.c:79
#6  0x00007f7b45a6039a in __assert_fail_base (fmt=0x7f7b45be77d8 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=assertion@entry=0x56322b5f5c67 "rc == 0", file=file@entry=0x56322b5f5c52 "/usr/include/zmq.hpp", line=line@entry=406, function=function@entry=0x56322b5f60c0 <zmq::context_t::~context_t()::__PRETTY_FUNCTION__> "zmq::context_t::~context_t()") at assert.c:92
#7  0x00007f7b45a60412 in __GI___assert_fail (assertion=assertion@entry=0x56322b5f5c67 "rc == 0", file=file@entry=0x56322b5f5c52 "/usr/include/zmq.hpp", line=line@entry=406, function=function@entry=0x56322b5f60c0 <zmq::context_t::~context_t()::__PRETTY_FUNCTION__> "zmq::context_t::~context_t()") at assert.c:101
#8  0x000056322b4ea264 in zmq::context_t::~context_t (this=<optimized out>, __in_chrg=<optimized out>) at /usr/include/zmq.hpp:406
#9  0x00007f7b45a73041 in __run_exit_handlers (status=status@entry=1, listp=0x7f7b45e1b718 <__exit_funcs>, run_list_atexit=run_list_atexit@entry=true, run_dtors=run_dtors@entry=true) at exit.c:108
#10 0x00007f7b45a7313a in __GI_exit (status=status@entry=1) at exit.c:139
#11 0x000056322b5505f9 in do_final (code=code@entry=1) at src/map/map.cpp:287
#12 0x000056322b55061e in do_abort () at src/map/map.cpp:298
#13 0x000056322b4af0aa in sig_proc (sn=11) at src/common/kernel.cpp:161
#14 <signal handler called>
#15 0x000056322b585be7 in CParty::ReloadParty (this=0x56325ccebaf0) at src/map/party.cpp:755
#16 0x000056322b5b1a58 in charutils::ReloadParty (PChar=0x56325d0e4100) at src/map/utils/charutils.cpp:4876
#17 0x000056322b4fdc9e in CCharEntity::PostTick (this=0x56325d0e4100) at src/map/entities/charentity.cpp:531
#18 0x000056322b4c46a2 in CAIContainer::Tick (this=0x56325d1a6170, _tick=_tick@entry=...) at src/map/ai/ai_container.cpp:371
#19 0x000056322b5e21f8 in CZoneEntities::ZoneServer (this=0x56323da16290, tick=..., check_regions=true) at src/map/zone_entities.cpp:1138
#20 0x000056322b5db4fb in CZone::ZoneServer (this=0x56323da161a0, tick=..., check_regions=<optimized out>) at src/map/zone.cpp:799
#21 0x000056322b5dc320 in zone_server_region (tick=..., PTask=<optimized out>) at src/map/zone.cpp:104
#22 0x000056322b4be789 in CTaskMgr::DoTimer (this=0x56322cc19cf0, tick=...) at src/common/taskmgr.cpp:69
#23 0x000056322b49e040 in main (argc=1, argv=0x7ffe244e6ba8) at src/common/kernel.cpp:267
double free or corruption (!prev)```


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Apr 17, 2020 at 22:05:19_

----

https://github.com/project-topaz/topaz/blob/09312396c0836f5e72fd5d8d78d731f873776c52/src/map/party.cpp#L755-L762

Looks like the main issue is happening here. I'm not real familiar with all those sections, but I did a little digging. Looks like there's a brief window in the zone-out -> zone-in process where the player's loc.zone is set to null. 

https://github.com/project-topaz/topaz/blob/09312396c0836f5e72fd5d8d78d731f873776c52/src/map/zone.cpp#L985-L989

My gut says the ReloadParty() code blindly referencing and calling a null loc.zone is likely causing it to crash. The window may be very small, but since that line is called once for each party member, and might fail if *either* player or leader's value is null it does strike me as a likely culprit. 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Apr 17, 2020 at 22:25:01_

----

I have ideas that I could try testing but that code block was added recently as part of trust changes @zach2good has been working on. He might be able to confirm/disprove my theory or have some ideas regarding a course of action.

https://github.com/project-topaz/topaz/pull/364


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 18, 2020 at 05:51:16_

----

Yup, this is pretty damming! 😅

I have a little bit of time free today to dig through the logic here, it'd be better to fix the order of operations here rather than slap on a check to see if the zone is null. 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Apr 18, 2020 at 10:05:24_

----

I did some testing and unfortunately I was still able to reproduce the crash. In the crash I got, `PLeader` is null when line 755 is called.
https://github.com/project-topaz/topaz/blob/a017f729cba391ca74ce8b2643269e6671b3e05b/src/map/party.cpp#L755
Far as I can tell, at L744 `PChar->PParty->members` contains only 1 member, while `info` still contains 2, causing RefreshFlags(info) to set PLeader to null when it fails to cross-check the two.
https://github.com/project-topaz/topaz/blob/09312396c0836f5e72fd5d8d78d731f873776c52/src/map/party.cpp#L744-L745


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 18, 2020 at 18:28:28_

----

Was this fully resolved by #505 ? I can't tell from the timeline of comments and commits.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 18, 2020 at 19:03:37_

----

I think so
~~but I think this lack of else statement has lead to the new bug on multi-server setups where parties are not shown correctly:
https://github.com/project-topaz/topaz/pull/505/files#diff-ebeab214ebd159b0a8e27b66d5ef5bc7L761~~

EDIT: Wait no, I am potato, I've been looking at this bug for too long


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jul 18, 2020 at 21:52:12_

----

no this bug is still ongoing, i have canaria currently running on gdb to get more crash logs. @Kreidos  musta have shared the memory dump along with the binary to @zach2good  this month.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Jul 18, 2020 at 21:55:00_

----

> @Kreidos musta have shared the memory dump along with the binary to @zach2good this month.

I provided link over Discord DM. I can always provide again if needed just hit me up there; we've all understandably been quite busy! :)




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Jul 19, 2020 at 08:27:56_

----

I have the dump and the binary, but I can't gdb it because I have massive library mismatch with kain's setup. I'll keep trying to repro from scratch this week and see what I can find


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Jul 19, 2020 at 16:33:18_

----

Most recent core dump from canary commit: 
`6544d08b021e49bb4ee60d0abe264dda3a4f4db5`
Or more likely this one (because of line numbers: `ed1f2840a7834358211bb6f573e4fa784302898e`
```
#0  0x00007fffffff00a8 in ?? ()
#1  0x00005555556bb749 in CZoneEntities::ZoneServer (this=0x5555647e5a20, tick=..., check_regions=false) at src/map/zone_entities.cpp:1090
#2  0x00005555556b4b4b in CZone::ZoneServer (this=0x555564780b60, tick=..., check_regions=<optimized out>) at src/map/zone.cpp:806
#3  0x00005555556b5923 in zone_server (tick=..., PTask=<optimized out>) at src/map/zone.cpp:83
#4  0x0000555555591ab9 in CTaskMgr::DoTimer (this=0x555555ab7b10, tick=...) at src/common/taskmgr.cpp:78
#5  0x0000555555571440 in main (argc=1, argv=0x7fffffffdfa8) at src/common/kernel.cpp:267
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Jul 27, 2020 at 08:39:49_

----

https://github.com/project-topaz/topaz/pull/877
