**Labels:**

merge ready



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 26, 2020 at 04:32:18_
_Originally opened as: project-topaz/topaz - Issue 394_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Moved them to a new subdirectory and added the original location to ignore list. Put a read me file in the original location to tell new people how to use the confs. Perhaps a afutture update can auto-copy any "missing" file from the default directory.

Also: adjusted some settings to be modern retail in the defaults. Existing servers will be retaining modified confs, this won't affect them. 

**Left speed settings alone** because while modern retails base has moved from 40 to 50, the database has a mix of the 2 for mobs and NPCs. And I think for players the base for what "0" is should be modified before changing the default setting here. Right now 0 = 40 and we I feel should either make that 50 or make 0 actually be 0 and set the default setting to 50. 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 20:09:49_

----

```suggestion
skillup_chance_multiplier: 1.0
craft_chance_multiplier: 1.0
```
Is this the current chance on retail?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 26, 2020 at 20:14:07_

----

See the commit comment. Settings should be for adjusting _from_ retail, but I have my personal doubts as to the retail accuracy of what should be the baseline stock retail level. As far as I know every server has this above 1.0


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 20:09:49_

----

```suggestion
skillup_chance_multiplier: 1.0
craft_chance_multiplier: 1.0
```
Is this the current chance on retail?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 26, 2020 at 20:14:07_

----

See the commit comment. Settings should be for adjusting _from_ retail, but I have my personal doubts as to the retail accuracy of what should be the baseline stock retail level. As far as I know every server has this above 1.0
