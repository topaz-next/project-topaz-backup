**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Saturday Sep 05, 2020 at 06:06:41_
_Originally opened as: project-topaz/topaz - Issue 1060_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #1034 

Howl (behemoth) was given to all beastmen.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Saturday Sep 05, 2020 at 08:59:56_

----

from wiggo's actionview, this is actually dynamis divergence quadav only. there are a ton of different howls with same animation id. 

        ['Ruby Quadav-17129595'] = {
            [11] = {
                [762]  = {['name']="Howl",                           ['category']=11, ['id']=762,  ['animation']=354,  ['message']=194, },
        ['Yagudo Abbot-17129600'] = {
            [11] = {
                [764]  = {['name']="Howl",                           ['category']=11, ['id']=764,  ['animation']=354,  ['message']=194, },
            },
my guess is 760 or 766 have the same animation id and are the one for orcs. 
So: 
update howl 762 and 764 with correct animation id. assign correct howl to mob skill lists based on it.
pick 760 or 766 for orcs (gonna troll through captures, or maybe @project-topaz/researcher  can help grab a regular orc and prove it) and update accordingly.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Sep 10, 2020 at 04:55:11_

----

Is `mob_prepare_time` of 4 intended?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Sep 10, 2020 at 05:13:19_

----

omg welcome back @ibm2431  :heart_eyes_cat: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 10, 2020 at 23:25:57_

----

@ibm2431 that looks like `mob_valid_targets` is 4 there, prepare time the 1500 next to it. both look to be preexisting copypaste values (which are unlikely to be correct for most skills)

[in this case](https://github.com/project-topaz/topaz/blob/8c722838094c1aac0887eb3f13a3eb3168926933/src/map/entities/battleentity.h#L358)
```cpp
 TARGET_ENEMY = 0x04,
```
so that Quadav will buff me instead of itself! COME AT ME TURTLE MAN!


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Sep 11, 2020 at 00:01:21_

----

> @ibm2431 that looks like `mob_valid_targets` is 4 there, prepare time the 1500 next to it. both look to be preexisting copypaste values (which are unlikely to be correct for most skills)
> 
> [in this case](https://github.com/project-topaz/topaz/blob/8c722838094c1aac0887eb3f13a3eb3168926933/src/map/entities/battleentity.h#L358)
> 
> ```c++
>  TARGET_ENEMY = 0x04,
> ```
> 
> so that Quadav will buff me instead of itself! COME AT ME TURTLE MAN!

lol i love your comments @TeoTwawki  they always cheer up my day =)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 11, 2020 at 18:15:08_

----

@kaincenteno I have invented a new sport. I call it turtle tipping. to play, turn off mob despawning. go deep into palborough mines, build up tp. anger a turtle on the other side of the gates where Zi'gi Boneeater spawns. he'll have to run all the way around to get to you. while you wait, anger a turtle on your side till he howls at you. All his friends will arrive just in time to eat a big pile of howl boosted aoe ws to the face.

forget exp per hr, turtles per hr is where its at Kain!


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Saturday Sep 05, 2020 at 08:59:56_

----

from wiggo's actionview, this is actually dynamis divergence quadav only. there are a ton of different howls with same animation id. 

        ['Ruby Quadav-17129595'] = {
            [11] = {
                [762]  = {['name']="Howl",                           ['category']=11, ['id']=762,  ['animation']=354,  ['message']=194, },
        ['Yagudo Abbot-17129600'] = {
            [11] = {
                [764]  = {['name']="Howl",                           ['category']=11, ['id']=764,  ['animation']=354,  ['message']=194, },
            },
my guess is 760 or 766 have the same animation id and are the one for orcs. 
So: 
update howl 762 and 764 with correct animation id. assign correct howl to mob skill lists based on it.
pick 760 or 766 for orcs (gonna troll through captures, or maybe @project-topaz/researcher  can help grab a regular orc and prove it) and update accordingly.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Sep 10, 2020 at 04:55:11_

----

Is `mob_prepare_time` of 4 intended?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Sep 10, 2020 at 05:13:19_

----

omg welcome back @ibm2431  :heart_eyes_cat: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 10, 2020 at 23:25:57_

----

@ibm2431 that looks like `mob_valid_targets` is 4 there, prepare time the 1500 next to it. both look to be preexisting copypaste values (which are unlikely to be correct for most skills)

[in this case](https://github.com/project-topaz/topaz/blob/8c722838094c1aac0887eb3f13a3eb3168926933/src/map/entities/battleentity.h#L358)
```cpp
 TARGET_ENEMY = 0x04,
```
so that Quadav will buff me instead of itself! COME AT ME TURTLE MAN!


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Sep 11, 2020 at 00:01:21_

----

> @ibm2431 that looks like `mob_valid_targets` is 4 there, prepare time the 1500 next to it. both look to be preexisting copypaste values (which are unlikely to be correct for most skills)
> 
> [in this case](https://github.com/project-topaz/topaz/blob/8c722838094c1aac0887eb3f13a3eb3168926933/src/map/entities/battleentity.h#L358)
> 
> ```c++
>  TARGET_ENEMY = 0x04,
> ```
> 
> so that Quadav will buff me instead of itself! COME AT ME TURTLE MAN!

lol i love your comments @TeoTwawki  they always cheer up my day =)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 11, 2020 at 18:15:08_

----

@kaincenteno I have invented a new sport. I call it turtle tipping. to play, turn off mob despawning. go deep into palborough mines, build up tp. anger a turtle on the other side of the gates where Zi'gi Boneeater spawns. he'll have to run all the way around to get to you. while you wait, anger a turtle on your side till he howls at you. All his friends will arrive just in time to eat a big pile of howl boosted aoe ws to the face.

forget exp per hr, turtles per hr is where its at Kain!


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Sep 08, 2020 at 21:14:23_

----

[766]  = {['name']="Howl",                           ['category']=11, ['id']=766,  ['animation']=354,  ['message']=194, },
Orc!!!! (THANKS TO @UynGH )


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Sep 09, 2020 at 22:17:48_

----

```sql

-- INSERT INTO `mob_skills` VALUES (757,501,'howl',0,7.0,2000,1500,4,0,0,0,0,0,0);
-- INSERT INTO `mob_skills` VALUES (758,502,'howl',0,7.0,2000,1500,4,0,0,0,0,0,0);
-- INSERT INTO `mob_skills` VALUES (759,503,'howl',0,7.0,2000,1500,4,0,0,0,0,0,0);
-- INSERT INTO `mob_skills` VALUES (760,504,'howl',0,7.0,2000,1500,4,0,0,0,0,0,0);
-- INSERT INTO `mob_skills` VALUES (761,505,'howl',0,7.0,2000,1500,4,0,0,0,0,0,0);
-- INSERT INTO `mob_skills` VALUES (762,354,'howl',0,7.0,2000,1500,4,0,0,0,0,0,0);
-- INSERT INTO `mob_skills` VALUES (763,507,'howl',0,7.0,2000,1500,4,0,0,0,0,0,0);
-- INSERT INTO `mob_skills` VALUES (764,354,'howl',0,7.0,2000,1500,4,0,0,0,0,0,0);
-- INSERT INTO `mob_skills` VALUES (765,509,'howl',0,7.0,2000,1500,4,0,0,0,0,0,0);
INSERT INTO `mob_skills` VALUES (766,354,'howl',1,20.0,2000,1500,1,0,0,0,0,0,0); -- Orc
-- INSERT INTO `mob_skills` VALUES (767,511,'bow',0,7.0,2000,1500,4,0,0,0,0,0,0);
```
that is a lot of howls.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Sep 10, 2020 at 03:54:28_

----

Updated all of the family howls with your guys' findings <3
