**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Saturday Oct 10, 2020 at 14:01:58_
_Originally opened as: project-topaz/topaz - Issue 1310_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

A treasure chest needs to be added to the cutscene.
The relevant cutscene is event ID "14" (L46)

https://github.com/project-topaz/topaz/blob/c2aa517599909fa0473f9739861ea8feb432d9ac/scripts/zones/Middle_Delkfutts_Tower/Zone.lua#L43-L50

A warning was output to the log.
```
[10/Oct] [22:44:09][Warning] Server need NPC <17420665>
```

If you add the following records, a treasure chest will appear in the cutscene.
```
INSERT INTO `npc_list` VALUES (17420665,'NOT_CAPTURED','     ',0,0.000,0.000,0.000,0,50,50,0,0,0,0,0,0x0000C00300000000000000000000000000000000,0,NULL,0);
```

