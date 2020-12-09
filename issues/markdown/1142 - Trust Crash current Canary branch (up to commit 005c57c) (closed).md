**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 15, 2020 at 19:48:37_
_Originally opened as: project-topaz/topaz - Issue 1142_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Debug log can be find below. 

```
[15/Sep] [12:33:09][Info] parse: 011 | 0002 0001 04 from user: Steelia
[15/Sep] [12:33:09][Info] parse: 01A | 1050 104F 0E from user: Macncheese
[15/Sep] [12:33:09][Action Info] CLIENT Macncheese PERFORMING ACTION 07
[15/Sep] [12:33:11][Info] parse: 00C | 0003 0002 06 from user: Steelia
[15/Sep] [12:33:11][Info] parse: 061 | 0003 0002 04 from user: Steelia
[15/Sep] [12:33:11][Info] parse: 118 | 0003 0002 04 from user: Steelia
[15/Sep] [12:33:11][Warning] parse: Unhandled game packet 118 from user: Steelia
[15/Sep] [12:33:11][Info] parse: 11B | 0003 0002 04 from user: Steelia
[15/Sep] [12:33:11][Warning] parse: Unhandled game packet 11B from user: Steelia
[15/Sep] [12:33:11][Info] parse: 053 | 0003 0002 44 from user: Steelia
[15/Sep] [12:33:11][Info] parse: 01A | 0003 0002 0E from user: Steelia

Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
CTrustSyncPacket::CTrustSyncPacket (this=0x555586659380, PChar=0x0, PTrust=0x555585c2a150)
    at src/map/packets/trust_sync.cpp:45
45          ref<uint16>(0x0C) = PChar->targid;
40          ref<uint8>(0x04) = 0x03;
41          ref<uint8>(0x05) = 0x05;
42
43          ref<uint16>(0x06) = PTrust->targid;
44          ref<uint32>(0x08) = PTrust->id;
45          ref<uint16>(0x0C) = PChar->targid;
46
47          packBitsBE(data + (0x04), (0x18) + PTrust->packetName.size(), 0, 6, 10); // Message Size
48          memcpy(data + (0x18), PTrust->packetName.c_str(), PTrust->packetName.size());
49
#0  CTrustSyncPacket::CTrustSyncPacket (this=0x555586659380, PChar=0x0, PTrust=0x555585c2a150)
    at src/map/packets/trust_sync.cpp:45
#1  0x00005555556c5287 in CZoneEntities::SpawnTRUSTs (this=<optimized out>, PChar=0x5555865aebc0)
    at src/map/zone_entities.cpp:570
#2  0x00005555556562cb in SmallPacket0x01A (session=<optimized out>, PChar=0x5555865aebc0, data=...)
    at src/map/packet_system.cpp:827
#3  0x00005555556301ce in parse (buff=0x555586493340 "\003", buffsize=buffsize@entry=0x7fffffffdd28, 
    from=from@entry=0x7fffffffdd40, map_session_data=map_session_data@entry=0x5555864f9640) at src/map/map.cpp:607
#4  0x0000555555630868 in do_sockets (rfd=<optimized out>, next=...) at src/map/map.cpp:388
#5  0x0000555555571a8b in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:268
   0x555555644209 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+153>:        lea    0x4(%rax),%edi
   0x55555564420c <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+156>:        mov    %edx,0x8(%rax)
=> 0x55555564420f <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+159>:        movzwl 0xc(%r13),%edx
   0x555555644214 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+164>:        mov    %dx,0xc(%rax)
   0x555555644218 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+168>:        xor    %edx,%edx
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```



Also we have experienced some were server hangs, topaz_game still running but everyone R0s and nobody can connect to topaz_game anymore. No debug provided for this as none can be given. This was experienced since Saturday/Sunday Release.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Oct 05, 2020 at 16:03:36_

----

haven't seen this crash in 20 days, it looks almost exactly the same. This happened on current canary C202010-01

```
[05/Oct] [07:22:00][Info] parse: 01A | 28DF 28D0 0E from user: Remode
[05/Oct] [07:22:00][Action Info] CLIENT Remode PERFORMING ACTION 03
[05/Oct] [07:22:01][Navmesh Error] CPathFind::FindPath Entity (17203447) could not find path
[05/Oct] [07:22:01][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-421.681671, -0.149128, 514.043274) (35)
[05/Oct] [07:22:01][Navmesh Error] CPathFind::FindPath Entity (16920597) could not find path

Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
CTrustSyncPacket::CTrustSyncPacket (this=0x555587d94c90, PChar=0x0, PTrust=0x555587af6460) at src/map/packets/trust_sync.cpp:45
45          ref<uint16>(0x0C) = PChar->targid;
40          ref<uint8>(0x04) = 0x03;
41          ref<uint8>(0x05) = 0x05;
42
43          ref<uint16>(0x06) = PTrust->targid;
44          ref<uint32>(0x08) = PTrust->id;
45          ref<uint16>(0x0C) = PChar->targid;
---Type <return> to continue, or q <return> to quit---
46
47          packBitsBE(data + (0x04), (0x18) + PTrust->packetName.size(), 0, 6, 10); // Message Size
48          memcpy(data + (0x18), PTrust->packetName.c_str(), PTrust->packetName.size());
49
#0  CTrustSyncPacket::CTrustSyncPacket (this=0x555587d94c90, PChar=0x0, PTrust=0x555587af6460) at src/map/packets/trust_sync.cpp:45
#1  0x00005555556c9267 in CZoneEntities::SpawnTRUSTs (this=<optimized out>, PChar=0x555587c67f10) at src/map/zone_entities.cpp:570
#2  0x0000555555648ec3 in SmallPacket0x015 (session=<optimized out>, PChar=0x555587c67f10, data=...) at src/map/packet_system.cpp:561
#3  0x000055555562d722 in parse (buff=0x555587b097d0 "J\005I\005$\002", buffsize=buffsize@entry=0x7fffffffdd28, from=from@entry=0x7fffffffdd40,
    map_session_data=map_session_data@entry=0x555587b7a590) at src/map/map.cpp:612
#4  0x00005555556301a8 in do_sockets (rfd=<optimized out>, next=...) at src/map/map.cpp:393
#5  0x0000555555571dfb in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:268
   0x555555644bd9 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+153>:        lea    0x4(%rax),%edi
   0x555555644bdc <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+156>:        mov    %edx,0x8(%rax)
=> 0x555555644bdf <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+159>:        movzwl 0xc(%r13),%edx
   0x555555644be4 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+164>:        mov    %dx,0xc(%rax)
   0x555555644be8 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+168>:        xor    %edx,%edx
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Oct 22, 2020 at 01:55:14_

----

Crash happened again on this weeks canary release (C202010-03)

[21/Oct] [18:31:15][Info] parse: 061 | 0855 0853 04 from user: Gharm
[21/Oct] [18:31:16][Info] parse: 05B | 0BCE 0BCD 0A from user: Raist
[21/Oct] [18:31:16][Debug]  5b 0a ce 0b cd 42 07 01 52 00 00 80 cd 02 00 00
[21/Oct] [18:31:16][Debug]  74 00 3d 00

```
Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
CTrustSyncPacket::CTrustSyncPacket (this=0x5555862af290, PChar=0x0, PTrust=0x5555862ad640) at src/map/packets/trust_sync.cpp:45
45          ref<uint16>(0x0C) = PChar->targid;
40          ref<uint8>(0x04) = 0x03;
41          ref<uint8>(0x05) = 0x05;
---Type <return> to continue, or q <return> to quit---
42
43          ref<uint16>(0x06) = PTrust->targid;
44          ref<uint32>(0x08) = PTrust->id;
45          ref<uint16>(0x0C) = PChar->targid;
46
47          packBitsBE(data + (0x04), (0x18) + PTrust->packetName.size(), 0, 6, 10); // Message Size
48          memcpy(data + (0x18), PTrust->packetName.c_str(), PTrust->packetName.size());
49
#0  CTrustSyncPacket::CTrustSyncPacket (this=0x5555862af290, PChar=0x0, PTrust=0x5555862ad640) at src/map/packets/trust_sync.cpp:45
#1  0x00005555556cfbd7 in CZoneEntities::SpawnTRUSTs (this=<optimized out>, PChar=0x555585e13050) at src/map/zone_entities.cpp:571
#2  0x000055555564dd83 in SmallPacket0x015 (session=<optimized out>, PChar=0x555585e13050, data=...) at src/map/packet_system.cpp:577
#3  0x00005555556321b1 in parse (buff=0x555585ce6440 "\316\v\315\vF\003", buffsize=buffsize@entry=0x7fffffffdcf8, from=from@entry=0x7fffffffdd10, map_session_data=map_session_data@entry=0x555585e217c0)
    at src/map/map.cpp:632
#4  0x00005555556327e8 in do_sockets (rfd=<optimized out>, next=...) at src/map/map.cpp:397
#5  0x0000555555571eab in main (argc=3, argv=0x7fffffffdf68) at src/common/kernel.cpp:268
   0x555555648879 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+153>:        lea    0x4(%rax),%edi
   0x55555564887c <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+156>:        mov    %edx,0x8(%rax)
=> 0x55555564887f <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+159>:        movzwl 0xc(%r13),%edx
   0x555555648884 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+164>:        mov    %dx,0xc(%rax)
   0x555555648888 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+168>:        xor    %edx,%edx
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 16:15:58_

----

This should be fixed with:
https://github.com/project-topaz/topaz/commit/eb646ef2b0c306e15c26dceb084a754716e10bd6
(coming this week)
