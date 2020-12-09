**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 14, 2020 at 14:06:21_
_Originally opened as: project-topaz/topaz - Issue 1359_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

After accepting the mission, it will occur by the following procedure.
1. Talk to the NPC "Iron Eater".
2.  Use the "Survival Guide" to go to "Beadeaux".
3.  Go to "Pashhow Marshlands".
4.  Plays a cutscene telling you that you haven't killed enough "Copper Quadav" (cs 10)
5.  Go to "Beadeaux".
6. . A cutscene is played instructing you to kill 20 "Copper Quadav" (cs 120)
cs10 and cs120 are in reverse order in the story.

I figured out how to fix it.
Conditions for the "Pashhow Marshlands" cutscene (cs10 or 11)
The "Beadeaux" cutscene (cs120) has been played in advance.
https://github.com/project-topaz/topaz/blob/d695c8061f371732b14849f6431dd09fdf9e92cf/scripts/zones/Pashhow_Marshlands/Zone.lua#L32-L39
```
        if missionStatus > 1 and missionStatus < 22 then
```
