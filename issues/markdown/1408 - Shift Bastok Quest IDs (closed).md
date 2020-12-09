**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Friday Oct 23, 2020 at 00:10:49_
_Originally opened as: project-topaz/topaz - Issue 1408_

----

added TRUST_BASTOK. I know it has its own branch but adding it here so it doesn't get lost

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 23, 2020 at 00:46:45_

----

Others:
Trust branch currently has Trust: Bastok as 91. kain is saying that there's a quest that _should_ have been there of Synergistic Support, which is 8 years old.

I'm hoping someone made a mistake when adding Trust Bastok.

If not, this could be quite bad for us.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 01:04:24_

----

@ibm2431[ its part of a "deleted" quest-line on retail.](https://ffxiclopedia.fandom.com/wiki/Synergistic_Pursuits) (removed on 3-27-12) its still in the dats but no longer can be flagged. Still shows in my "completed" list though:

![image](https://user-images.githubusercontent.com/6871475/96944718-9d899480-14a9-11eb-9500-7a5fd58c4c42.png)

Polutils shown to confirm it does come right before the trust quest in the index, though our IDs do not match that.

The Japanese shown just says "BS Quest 93           Requester" - placeholder entries for future things. I like to think some SE devs was like _"sigh.. Bull Sh--- quest 98..  Bull Sh-- Quest number 99.."_


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 01:06:13_

----

Support was a repeatable btw, The 2 that came right before are not.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Oct 23, 2020 at 03:12:08_

----

dunno if this got changed recently or if the quest was always flagged wrong for bastok. Would be good if someone had an old client. for like last year maybe?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Oct 23, 2020 at 04:49:50_

----

@TeoTwawki  @ibm2431 

No issue with progression. After further investigation it seems the issue is being cause by another issue will be open up.

This only fixes the missing questID.

@zach2good  tagging you so you merge this onto trust branch 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 23, 2020 at 04:54:15_

----

@TeoTwawki 

> Trial-size Trial by Earth
> Trial by Earth

> All By Myself

> The Naming Game

This just keeps looking worse. I was really hoping it was just Jeuno.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Oct 23, 2020 at 04:58:22_

----

Changed name of this PR as it only fixes the missing quests.

Issue with trusts quest progression in bastok can be explained in https://github.com/project-topaz/topaz/issues/1411


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 24, 2020 at 04:10:01_

----

If this just makes the quest in Bastok appear correctly in the logs, then this is fine to merge.
People _might_ get caught in a position where a GM has to use GM wizardry to fix their quest status, but it's so small on such minor quests that I think that's OK.
```
        SYNERGISTIC_SUPPORT             = 91,
        TRUST_BASTOK                    = 92,
```

This has unearthed a lof of evil that we should track outside of this PR.
