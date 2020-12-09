**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Oct 28, 2020 at 06:14:16_
_Originally opened as: project-topaz/topaz - Issue 1446_

----

added zone.lua to make it easier to understand what this is doing.
added missing zones.
commented zones that do not teleport directly to leader but to
other specific locations.
Nexus cape still needs to check for zones visited by PC before
teleporting away as seen on https://ffxiclopedia.fandom.com/wiki/Nexus_Cape
No mention of this is seen on https://www.bg-wiki.com/bg/Nexus_Cape
Researcher would be appreciated on this, but its out of scope for this
quick fix only focused on missing areas and get rid of magic numbers

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits
(marking as done since it was done by @MarianArlt 



----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 28, 2020 at 06:51:12_

----

Kain asked me to test this. It seems to work fine.
I successfully tried the following:
Party leader zoned after successful use, then party member would use Nexus Cape to catch up.

1. From Ru'Aun Gardens to Ru'Aun Gardens
2. From Ru'Aun Gardens to Bhafleau Thickets
3. From Bhafleau Thickets to Xarcabards [S]
4. From Xarcabard [S] to Fort Karugo-Narugo [S]

- [x] Tested working locally for kain


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Oct 28, 2020 at 07:32:18_

----

I have added a check that should fix cheaters using it to go to unvisited zones.
Need a test b̶u̶n̶n̶y̶ canary to try and see if that fixes that issue.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 28, 2020 at 08:13:40_

----

Tested bb9f2ab27340079c3446dbf82331b4c297d1bc3a working (again) for lazykain.

After this commit new character now could not use Nexus Cape to warp to areas which he had not visited before. Areas he had been to before, could be accessed as expected.
Tried to catch up to a party leader in Grauberg [S], Jugner Forest [S] and Norg, all failing.
Tried to catch up to a party leader in Ru'Aun Gardens (accessed from before) with success.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 03:11:43_

----

Back when I added the cape, I vaguely recall having someone check for me on retail about the needing to have been in the zone (because I assumed that you'd have to have been there before, and someone argued to the contrary). But recheck would def be appreciated, as I did not check this myself and had to take someones word for it.

Also appreciate updating it to use the human readable zone names, we didn't have those available back then.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Oct 29, 2020 at 05:08:24_

----

wonder no more @TeoTwawki  as from the Bible of Altana says "(http://www.playonline.com/pcd/topics/ff11us/detail/5005/detail.html):
```*Characters may teleport only to areas they have previously visited.```
Amen


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 12:36:35_

----

Yay sources!

(Shows how much I look at the old playoneline.com site)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Oct 29, 2020 at 16:13:16_

----

> Yay sources!
> 
> (Shows how much I look at the old playoneline.com site)

i love sources <3 try to always add as many as i can find =)
