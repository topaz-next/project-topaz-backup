**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Saturday Oct 10, 2020 at 12:40:58_
_Originally opened as: project-topaz/topaz - Issue 1308_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Wiki states the following.
https://www.bg-wiki.com/bg/Dark_Puppet
- Head to I-8 of the 1st floor map and you will find a ???.
- Trade the Darksteel Ingot to the ??? to spawn a NM: Gerwitz's Axe (NM). This will consume the ingot.

The SQL coordinates are wrong, as they are (H-12) in Ordelle's Caves MAP4. 
This is an outdated specification that was in place before the monster placement changes in the May 10, 2011 version of the game were taken into account.

```
INSERT INTO `npc_list` VALUES (17568176,'qm4','???',159,-51.779,27.694,-84.459,1,40,40,0,0,0,0,3,0x0000340000000000000000000000000000000000,0,NULL,0);
```

The spawn position of the mob "Gerwitzs_Axe" is also different.
```
INSERT INTO `mob_spawn_points` VALUES (17568135,'Gerwitzs_Axe','Gerwitz\'s Axe',46,-52,27,-81,255);
```


