**Labels:**

bug

good first issue



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 04:09:59_
_Originally opened as: project-topaz/topaz - Issue 541_

----

Grauberg [S] has a lot of duplicated mob groups; specifically everything in the 10938+ block.

```sql
INSERT INTO `mob_groups` VALUES (45,3148,89,'Pixie',330,0,2001,0,0,51,56,0);
INSERT INTO `mob_groups` VALUES (46,1698,89,'Goblin_Pioneer',330,0,1138,0,0,62,64,0);
INSERT INTO `mob_groups` VALUES (47,1688,89,'Goblin_Mine',0,128,0,0,0,59,59,0);
INSERT INTO `mob_groups` VALUES (48,2654,89,'Migratory_Hippogryph',0,128,0,0,0,74,78,0);
INSERT INTO `mob_groups` VALUES (49,3276,89,'Quadav_Transporter',0,128,2061,0,0,60,60,0);
INSERT INTO `mob_groups` VALUES (50,3274,89,'Quadav_Guard',0,128,2061,0,0,60,60,0);
```

```sql
INSERT INTO `mob_groups` VALUES (10973,3148,89,'Pixie',240,0,0,3000,9999,56,59,0);
INSERT INTO `mob_groups` VALUES (10974,1688,89,'Goblin_Mine',240,0,0,500,9999,56,59,0);
INSERT INTO `mob_groups` VALUES (10975,1698,89,'Goblin_Pioneer',240,0,0,5000,9999,62,64,0);
INSERT INTO `mob_groups` VALUES (10976,2654,89,'Migratory_Hippogryph',240,0,0,2000,9999,60,62,0);
INSERT INTO `mob_groups` VALUES (10977,3276,89,'Quadav_Transporter',240,0,0,500,9999,56,59,0);
INSERT INTO `mob_groups` VALUES (10978,3274,89,'Quadav_Guard',240,0,0,2500,9999,65,68,0);
```

But their information isn't exactly the same (some have differing levels), so:

- Correct information needs to be determined, and made the actual information in the lower-end group
- Ensure that mob spawns use the lower end group
- And delete the higher end group


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 28, 2020 at 11:16:46_

----

Note that higher numbered groups are higher numbered **because** nothing in mob_spawn_points related to them.  That's why they weren't reassigned a new, low number during the group rework.

`select max(groupid) from mob_spawn_points`
`337`

None of those high numbers after the break are used, in any of the zones.  They were just left in there, I'm guessing, in case they contained useful data for fixing assigned groups or adding future content.



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Saturday May 02, 2020 at 06:55:11_

----

Some of the higher group numbers are still used for instanced allies as well (Prishe, Selhteus, Karababa, Trion, Volker, Ajido-Marujido, maybe more).
