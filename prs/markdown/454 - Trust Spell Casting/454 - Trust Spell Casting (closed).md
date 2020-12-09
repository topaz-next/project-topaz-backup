**Labels:**

focus

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Mar 31, 2020 at 13:42:16_
_Originally opened as: project-topaz/topaz - Issue 454_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**Since all the SQL changes were moved into another PR, I'll re-work this PR into being:**
- Trust spell list loading
- Trust spell selection
- Trust recast tracking
- A little ground work for Trust magic bursting

**As always, I have inflated the scope of this PR because I hate myself, and this now includes:**
- The bones of the ibm's gambit system, a basic behaviour definition system for trusts


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 12:03:45_

----

![image](https://user-images.githubusercontent.com/6871475/78782098-71744f00-796f-11ea-89b3-94ed8cb1f919.png)



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 16:01:13_

----

at this point maybe we should just debug break if its somehow an NPC lol


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Apr 10, 2020 at 10:17:24_

----

_it is done_


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Apr 17, 2020 at 05:56:44_

----

why is there two behaviors for CURE? shouldnt the one for HPP_LTE, 75 be enough? (sorry for my blunt question, just trying to provide feedback :cat: )


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Apr 17, 2020 at 06:00:16_

----

Useful question!

These behaviours are looked at in order behind the scenes, so if you wanted to weight a certain behaviour to be more important, you would put it higher on the list, or add another copy of it with different parameters. 

In this case, if someone in the party is critically low, Kupipi will try and drop a heal on them above all else. If not, she'll try to wake people up with Cure I, then she'll go to her regular type healing checks of 75% and all the other things in the list. 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Apr 17, 2020 at 16:07:30_

----

Awesome that makes sense @zach2good  :smile_cat: :  can't wait to try it out :smile_cat: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 07:58:28_

----

Or at least outside of the gambit checks which happen on every tick 😉 

Clarity edit: The resonance check obviously needs to happen on every gambit check, but at the moment the resonance _vector_ is being defined on each gambit tick


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:00:36_

----

Can pop a break in here


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:02:15_

----

This would be a good spot for those spell families~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:09:24_

----

Are line breaks required here?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:28:52_

----

Does Kupipi dispel?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:50:27_

----

"Hey in the future we should only search lists that would have the appropriate spell."
"I know; that's why I want to give spell families parent families."


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:53:11_

----

I know there's a check in getHighest, but are there checks for selectSpecific for if the trust has enough MP?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:54:01_

----

Arrr... thar be global here!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday May 02, 2020 at 12:40:06_

----

Nope! I think I got confused when trying to put in as much functionality as possible. She does -na though, so I'll swap those in


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 12:03:45_

----

![image](https://user-images.githubusercontent.com/6871475/78782098-71744f00-796f-11ea-89b3-94ed8cb1f919.png)



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 16:01:13_

----

at this point maybe we should just debug break if its somehow an NPC lol


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Apr 10, 2020 at 10:17:24_

----

_it is done_


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Apr 17, 2020 at 05:56:44_

----

why is there two behaviors for CURE? shouldnt the one for HPP_LTE, 75 be enough? (sorry for my blunt question, just trying to provide feedback :cat: )


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Apr 17, 2020 at 06:00:16_

----

Useful question!

These behaviours are looked at in order behind the scenes, so if you wanted to weight a certain behaviour to be more important, you would put it higher on the list, or add another copy of it with different parameters. 

In this case, if someone in the party is critically low, Kupipi will try and drop a heal on them above all else. If not, she'll try to wake people up with Cure I, then she'll go to her regular type healing checks of 75% and all the other things in the list. 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Apr 17, 2020 at 16:07:30_

----

Awesome that makes sense @zach2good  :smile_cat: :  can't wait to try it out :smile_cat: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 07:58:28_

----

Or at least outside of the gambit checks which happen on every tick 😉 

Clarity edit: The resonance check obviously needs to happen on every gambit check, but at the moment the resonance _vector_ is being defined on each gambit tick


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:00:36_

----

Can pop a break in here


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:02:15_

----

This would be a good spot for those spell families~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:09:24_

----

Are line breaks required here?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:28:52_

----

Does Kupipi dispel?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:50:27_

----

"Hey in the future we should only search lists that would have the appropriate spell."
"I know; that's why I want to give spell families parent families."


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:53:11_

----

I know there's a check in getHighest, but are there checks for selectSpecific for if the trust has enough MP?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 02, 2020 at 08:54:01_

----

Arrr... thar be global here!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday May 02, 2020 at 12:40:06_

----

Nope! I think I got confused when trying to put in as much functionality as possible. She does -na though, so I'll swap those in


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Mar 31, 2020 at 16:19:57_

----

Pretty sure you know of the duplicate spells for Zeid causing travis to not complete, just leaving this here as a note.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 09:52:25_

----

Yell at me when you want to remove the WIP label~

(Any of us would work, Nyu and aether have the power too.)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Apr 10, 2020 at 10:18:24_

----

**Note:**
Because I want/need the new db column, I've rebased off this PR:
#482

Until that goes in, this will be un-reviewable
