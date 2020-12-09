**Labels:**



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jun 17, 2020 at 08:21:29_
_Originally opened as: project-topaz/topaz - Issue 740_

----

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Putting this here before it's forgotten:
The children spawned by Progenerator during the Ancient Flames Beckon fight in Promyvion Dem aren't added to the battlefield, and therefore, can't be attacked by players.

There may also be an issue where they are being erroneously spawned prior to Progenerator engaging.

The skill script which spawns them, Fission, puts them at exactly the same position as Progenerator, which may render the Progenerator unable to be targeted if idle. (And maybe there should be a little bit of buffer space added to the script).

I attempted to resolve these myself, but for some reason I can't get it to trigger skills on my machine. So, free PR to anyone who wants to put this in `bcnm_battlefield` and then test the fight to make sure everything is working okay (and that it's not spawning them pre-engage).
```
INSERT INTO `bcnm_battlefield` VALUES (800,1,16855041,3); -- ancient_flames_beckon (dem)
INSERT INTO `bcnm_battlefield` VALUES (800,1,16855042,0);
INSERT INTO `bcnm_battlefield` VALUES (800,1,16855043,0);
INSERT INTO `bcnm_battlefield` VALUES (800,1,16855044,0);
INSERT INTO `bcnm_battlefield` VALUES (800,1,16855045,0);
INSERT INTO `bcnm_battlefield` VALUES (800,2,16855046,3);
INSERT INTO `bcnm_battlefield` VALUES (800,2,16855047,0);
INSERT INTO `bcnm_battlefield` VALUES (800,2,16855048,0);
INSERT INTO `bcnm_battlefield` VALUES (800,2,16855049,0);
INSERT INTO `bcnm_battlefield` VALUES (800,2,16855050,0);
INSERT INTO `bcnm_battlefield` VALUES (800,3,16855051,3);
INSERT INTO `bcnm_battlefield` VALUES (800,3,16855052,0);
INSERT INTO `bcnm_battlefield` VALUES (800,3,16855053,0);
INSERT INTO `bcnm_battlefield` VALUES (800,3,16855054,0);
INSERT INTO `bcnm_battlefield` VALUES (800,3,16855055,0);
```

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated


----
<a href="https://github.com/Altalus"><img src="https://avatars1.githubusercontent.com/u/194725?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Altalus](https://github.com/Altalus)**
_Tuesday Jun 23, 2020 at 02:42:03_

----

For what is worth, I was able to confirm this behavior this evening as I got into the battlefield the Progenitor was spawned but I was unable to target it, and it did not attack.

I was able to target an Offspring, but not attack, so, at the moment, this fight cannot be won (or lost, except on time out).


----
<a href="https://github.com/Altalus"><img src="https://avatars1.githubusercontent.com/u/194725?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Altalus](https://github.com/Altalus)**
_Tuesday Jun 23, 2020 at 02:55:52_

----

Updating the SQL fixed the targeting and the fight, but I was unable to get any spawn in my test (only ran once, sorry).
