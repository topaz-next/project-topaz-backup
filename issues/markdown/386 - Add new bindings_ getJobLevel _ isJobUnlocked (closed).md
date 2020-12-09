**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Feb 23, 2020 at 15:28:30_
_Originally opened as: project-topaz/topaz - Issue 386_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

As spoken about in discord, I added these to more easily support the Rhapsodies-style unlocking of the subjob with Gilgamesh's key item.

**Tested with:**
```lua
    print("Subjob Level: "..player:getJobLevel(0))
    print("WAR Level: "..player:getJobLevel(1))
    print("MNK Level: "..player:getJobLevel(1))
    print("DRG Level: "..player:getJobLevel(14))
    print("Subjob Unlocked: "..player:isJobUnlocked(0))
    print("WAR Unlocked: "..player:isJobUnlocked(1))
    print("MNK Unlocked: "..player:isJobUnlocked(1))
    print("DRG Unlocked: "..player:isJobUnlocked(14))
```

```
[23/Feb] [17:22:38][LUA Script] Subjob Level: 0
[23/Feb] [17:22:38][LUA Script] WAR Level: 99
[23/Feb] [17:22:38][LUA Script] MNK Level: 99
[23/Feb] [17:22:39][LUA Script] DRG Level: 0
[23/Feb] [17:22:39][LUA Script] Subjob Unlocked: 1
[23/Feb] [17:22:39][LUA Script] WAR Unlocked: 1
[23/Feb] [17:22:39][LUA Script] MNK Unlocked: 1
[23/Feb] [17:22:39][LUA Script] DRG Unlocked: 0
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 23, 2020 at 17:56:42_

----

`isJobUnlocked`, `jobUnlocked`, or `unlockedJob`?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Feb 23, 2020 at 18:19:12_

----

Whatever you prefer? 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 23, 2020 at 18:54:47_

----

I am _horrible_ at deciding on function names.

I want to say that `unlockedJob` is the closest to natural English:
`player:unlockedJob(tpz.job.WAR)` -> "Player unlocked (the) job Warrior?"

But then it'd only be two characters different from `unlockJob`. I don't know if this is a good or bad thing.

Let's see if anyone else has very strong opinions on what it should be called!

(Bindings themselves look fine.)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 23, 2020 at 18:58:07_

----

how about `hasJob()` ?  `hasJobUnlocked()`?

also technically speaking, we could just check that the job has levels. its zero if not unlocked isn't it?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Feb 23, 2020 at 20:42:54_

----

The reason I ended up doing two bindings is that you can't query for the level of job NON to find out if subjob is unlocked, you have to get the corresponding bit from jobs.unlocked. It felt dirty to check if the player has a subjob of any level to fulfil that condition 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 23, 2020 at 20:53:56_

----

I honestly would not have thought to check eithr of these at all to find out if sub was available. Just did not cross my mind. I was like "why's his example saying subjob level when we have a binding for getting sj level?" (which is for current sj and thus not what you wanted or meant). 

tl;dr I didn't get it :)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 17:27:04_

----

I like `hasJob`.
