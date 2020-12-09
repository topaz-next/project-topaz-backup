**Labels:**



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Wednesday Sep 09, 2020 at 20:00:32_
_Originally opened as: project-topaz/topaz - Issue 1088_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Now that we have some RoE quests that give large amount of exp, like 5K:
If this happens while you are low level, you will gain more than 1 level in a single quest complete bonus.
Retail behavior is that you should be limited to 1 level up (for instance if you are level 1 you should get level 2 + all the exp to get level 3 minus 1)



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Sep 09, 2020 at 21:06:33_

----

Is this not already the case? This is how it's written in `release`. :thinking: 

https://github.com/project-topaz/topaz/blob/release/src/map/utils/charutils.cpp#L3768

```c++
if (PChar->jobs.exp[PChar->GetMJob()] >= GetExpNEXTLevel(PChar->jobs.job[PChar->GetMJob()] + 1))
{
        PChar->jobs.exp[PChar->GetMJob()] = GetExpNEXTLevel(PChar->jobs.job[PChar->GetMJob()] + 1) - 1;
}
        PChar->jobs.job[PChar->GetMJob()] += 1;
```


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Wednesday Sep 09, 2020 at 23:24:07_

----

Testing via adding xp with GM command confirms that this limit is functioning, have you seen this behavior specifically with RoE?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Sep 09, 2020 at 23:45:37_

----

RoE simply uses the existing AddExperiencePoints code, same as mobs/quests/missions/all other sources of XP.I confirmed by cranking the RoE exp way up that it doesn't give you multiple levels. :confused: Not sure if I'm missing something. 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Sep 09, 2020 at 23:48:26_

----

Hmm, Unless; it is theoretically possible that the mob kill gave you X exp points, which were enough to give you a level, and then a Record gives you Y exp points which is enough for a second? Exp from 2 different sources would allow you to go up 2 levels, but I assume retail would *have* to work the same way so that should be accurate.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Thursday Sep 10, 2020 at 10:07:18_

----

Indeed maybe it was a rare case where both the mob kill and the end of RoE "kill 200 mobs" gave 2 consecutive level up.
In which case we can safely close this issue.
