**Labels:**



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Monday Oct 05, 2020 at 17:29:59_
_Originally opened as: project-topaz/topaz - Issue 1256_

----

This still maintains support for showing the player's Spark amount and giving/removing spark currency (In case any server wants alternate ways to obtain them or custom usage.)

Summary of fail-out conditions when RoE Disabled:
- Client RoE packets won't be replied to (Take record, Remove record, Quest Log.) RoE client menu will be blank.
- RoE Events bail-out immediately.
- No RoE writes to DB

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 05, 2020 at 17:33:05_

----

Smart!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 05, 2020 at 17:34:19_

----

No space after ! please


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 05, 2020 at 17:35:04_

----

Space after for
Brackets around the statement


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Oct 05, 2020 at 17:39:49_

----

This line actually pre-dates this commit. I didn't modify it. and both lines really represent a singular command, as the questLog must **always** be as a set of 4.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Oct 05, 2020 at 17:41:10_

----

Are we averse to having it all on one line? It will never change as it's concrete in its required function.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 05, 2020 at 17:45:41_

----

The end result I meant was:
```cpp
for (int i = 0; i < 4; i++)
{
    PChar->pushPacket(new CRoeQuestLogPacket(PChar, i));
}
```

I think the only thing I like for single line ifs are returns.

Maybe it wouldn't be such a bad thing to just have these 4 lines without a loop?
```cpp
PChar->pushPacket(new CRoeQuestLogPacket(PChar, 0));
PChar->pushPacket(new CRoeQuestLogPacket(PChar, 1));
PChar->pushPacket(new CRoeQuestLogPacket(PChar, 2));
PChar->pushPacket(new CRoeQuestLogPacket(PChar, 3));
```


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Oct 05, 2020 at 17:50:52_

----

...I will put the brackets... I just hate how bloated single-line braced sections look. :unamused: 

My preference would to avoid bracing would be:
```c++
for (int i = 0; i < 4; i++) PChar->pushPacket(new CRoeQuestLogPacket(PChar, i));
```
(If this looks offensive, then don't throw stones unless you've never use lambdas! :joy: )

But I didn't want to unroll it, since the compiler will be doing that anyway, and I suspected it's possible that SE may expand the record system in the future; there's clear evidence that's why this multi-packet situation already exists.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 05, 2020 at 17:33:05_

----

Smart!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 05, 2020 at 17:34:19_

----

No space after ! please


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 05, 2020 at 17:35:04_

----

Space after for
Brackets around the statement


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Oct 05, 2020 at 17:39:49_

----

This line actually pre-dates this commit. I didn't modify it. and both lines really represent a singular command, as the questLog must **always** be as a set of 4.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Oct 05, 2020 at 17:41:10_

----

Are we averse to having it all on one line? It will never change as it's concrete in its required function.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 05, 2020 at 17:45:41_

----

The end result I meant was:
```cpp
for (int i = 0; i < 4; i++)
{
    PChar->pushPacket(new CRoeQuestLogPacket(PChar, i));
}
```

I think the only thing I like for single line ifs are returns.

Maybe it wouldn't be such a bad thing to just have these 4 lines without a loop?
```cpp
PChar->pushPacket(new CRoeQuestLogPacket(PChar, 0));
PChar->pushPacket(new CRoeQuestLogPacket(PChar, 1));
PChar->pushPacket(new CRoeQuestLogPacket(PChar, 2));
PChar->pushPacket(new CRoeQuestLogPacket(PChar, 3));
```


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Oct 05, 2020 at 17:50:52_

----

...I will put the brackets... I just hate how bloated single-line braced sections look. :unamused: 

My preference would to avoid bracing would be:
```c++
for (int i = 0; i < 4; i++) PChar->pushPacket(new CRoeQuestLogPacket(PChar, i));
```
(If this looks offensive, then don't throw stones unless you've never use lambdas! :joy: )

But I didn't want to unroll it, since the compiler will be doing that anyway, and I suspected it's possible that SE may expand the record system in the future; there's clear evidence that's why this multi-packet situation already exists.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 05, 2020 at 18:21:44_

----

`clang-format` has been disabled as a check for a while, mysteries continue
