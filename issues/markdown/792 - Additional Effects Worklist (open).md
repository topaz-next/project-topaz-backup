**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 01, 2020 at 23:36:53_
_Originally opened as: project-topaz/topaz - Issue 792_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

1. [ ] add item mods for all weapons that have an additional effect (formerly in the now deleted scripts)
2. [ ] retail verification of base power of item effect damages (this should be _**the most**_ it will hit for, and then resistance checks will reduce it). Related to point 1's completion.
3.  [ ] refactor the global to use less repeated code, less if/else towering, and be easier to add more onto. The types are arbitrary numbers, it should be trivial to make a new one as needed but the code needs to be clear at a glance what you should do. I want this to be easy for new people who've never even looked at this stuff before. 
4. [ ] testing of different types of add effect just to make sure all the types work as close to retail as they can be made.

plan:
 - **I am going to need lots of help filling in item_mods.sql before we can call this ready for canary/release.**
 - modifiers to control params, not static values in script
 - modular, call only functions we use instead of using if/elseif blocks
 - pave the way for eventually handling item spikes here as well (note 1)
 - pave the way for eventually migrating monster additional effect and spikes here as well (note 2)
 - need verification/correction of item's base power (note 3)

Note 1:
 - item spikes are currently hard coded into the core with very little that is adjustable

Note 2:
 - attacker/defender, NOT player/mob
 - structure of my current work in progress needs to change a bit so that mobs will be an easy find replace, I am working on it still

Note 3:
 - due to issues with the resistance functions, damage amounts and status effect rates will not look like they are retail accurate (low variance).



Sample of how to add an additional effect (damage type):
```sql
INSERT INTO `item_mods` VALUES (16564,431,1); -- Flame Blade: Addeffect Type
INSERT INTO `item_mods` VALUES (16564,499,1); -- subeffect fire
INSERT INTO `item_mods` VALUES (16564,500,10); -- effect damage 10
INSERT INTO `item_mods` VALUES (16564,501,10); -- effect chance 10%
INSERT INTO `item_mods` VALUES (16564,944,1); -- Addeffect element fire
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 20, 2020 at 01:25:21_

----

Additional to-do's I am currently handling:
 - [ ] Excalibur's slashing damage
 - [ ] Effects that only proc vs a specific kind of target (Like Bano Del Sol)
 - [ ] Rare items that actually factor in magic accuracy (Like "[Vampirism](https://www.ffxiah.com/item/20706/vampirism)" - this isn't typical)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 21:13:47_

----

Reminder about Twlight Knifes edge case:
https://github.com/project-topaz/topaz/pull/1390

I flip flopped on how I was handling this and forgot to take care of the subeffect. While I am unsure about the knife itself, I am sure we'll at least want independent control for the rate and power of differing effects that come form the same item as well, so that is now on my radar as well.
