**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 02, 2020 at 15:15:29_
_Originally opened as: project-topaz/topaz - Issue 1233_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

https://github.com/project-topaz/topaz/blob/50e64bd5fa324a22e260b5c79a3213fb3510d186/scripts/globals/missions.lua#L1072-L1081

The csid "1004" and "2004" are cutscenes to occur when the mission "Save the Children" is completed at least twice.
I think the correct initial csid is "2026" and "2027".

If the mission "Save the Children" is received a second time and thereafter, the guard's request will cause a cutscene in which "Tedimout" is abducted again.
"Arnau", "Pieuje" and "Shamonde" cutscenes will occur again.
This is a mistake.

If the mission "Save the Children" is received a second time or later, the guard's cutscene should be different because "Tedimout" is not kidnapped, and the cutscenes of "Arnau", "Pieuje" and "Shamonde" should not occur again.
(The cutscene in the Hut Door where the child is rescued correctly causes a cutscene for the second and subsequent cutscenes.)




