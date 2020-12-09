**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:54:57_
_Originally opened as: project-topaz/topaz - Issue 226_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [helixhamin](https://github.com/helixhamin)**
_Friday May 25, 2018 at 03:02 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4896_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_** Checked the status.lua, and found modid has gaps, and has some duplicate ids assigned to different mods

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**  N/A


**_Source Branch_** (master/stable) **:** Master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Check status.lua modids for the following:
Missing modids (possibly can be used as reserve IDs):
53
74-79
123-126
138-143
152-159
190-223
239
256
260-287
290
297
796-825
830
888

Duplicate modid:
ROLL_TACTICIANS | 873
AUGMENTS_FEINT | 873


ROLL_ALLIES | 874
SNEAK_ATK_DEX | 874

873 is not associated with anything in the item_mods file yet, but 874 is associated with:
raiders_armlets_+2
raiders_armlets_+1
skulkers_armlets
skulkers_armlets_+1

So I don't think it will interfere with anything yet, but may in the future, since these will use the SNEAK_ATK_DEX (Unless these are modding an ability somewhere?)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:54:58_

----

<a href="https://github.com/nfaletra"><img src="https://avatars1.githubusercontent.com/u/11480851?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nfaletra](https://github.com/nfaletra)**
_Friday May 25, 2018 at 04:52 GMT_

----

Use modifier.h as your guide instead of status.lua. status.lua should match modifier.h.

Also: 
`
// Weaponskill %damage modifiers
// The following modifier should not ever be set, but %damage modifiers to weaponskills use the next 255 IDs (this modifier + the WSID)
// For example, +10% damage to Chant du Cygne would be ID 570 + 225 (795)
WEAPONSKILL_DAMAGE_BASE   = 570,
`



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:00_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Friday May 25, 2018 at 07:16 GMT_

----

nfaletra 

Modifier.h shows:
AUGMENTS_FEINT            = 873, // Feint will give another -10 Evasion per merit level
ROLL_TACTICIANS           = 873, // Tracks totals
SNEAK_ATK_DEX             = 874, // % DEX boost to Sneak Attack (if gear mod, needs to be equipped on hit)
ROLL_ALLIES               = 874, // Tracks totals

status.lua shows:
AUGMENTS_FEINT                  = 873, -- Feint will give another -10 Evasion per merit level
ROLL_TACTICIANS                 = 873,
SNEAK_ATK_DEX                   = 874, -- % DEX boost to Sneak Attack (if gear mod, needs to be equipped on hit)
ROLL_ALLIES                     = 874,

Duplicates match.
I have not tested for all missing, but some random checks seem to match (aka, the missing values seem to also be missing in the modifier.h file)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:01_

----

<a href="https://github.com/nfaletra"><img src="https://avatars1.githubusercontent.com/u/11480851?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nfaletra](https://github.com/nfaletra)**
_Friday May 25, 2018 at 15:21 GMT_

----

Sorry, didn't mean to make it sound like I was saying you were wrong. The duplicates are definitely there. I was just mentioning that we do specific ws damage mods by using WEAPONSKILL_DAMAGE_BASE + WSID. So 571-795 are actually being used.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:02_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Monday May 28, 2018 at 01:57 GMT_

----

No, I understand, that is why I just listed what I did not see. I notice that the status.lua actually states the values are part of ws stuff. Basically, I am just trying to do some quick checks of items (excel spreadsheet), and that was just the numbers I noted. Every skipped number might be used by something else for all I know, I have not really had a chance to dig deeper. Just using this topic as a reference (I will change the original and remove those wsid numbers though)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:04_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday May 28, 2018 at 14:20 GMT_

----

even having to question it is a sign we need better documentation in there while ensuring both files mirror each other's mod lists fully. it being non sequential makes it harder to spot the gaps but organizing things into groups makes it easier on finding related mods, its really a mess. And re-sequencing is out of the question - we'd have to redo the entire item mods sql. So we'll just have to fix it once and then make dang sure any new changes are good and reviewed.

