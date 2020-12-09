**Labels:**

reviewed



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Oct 08, 2020 at 06:27:56_
_Originally opened as: project-topaz/topaz - Issue 1279_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Players are now able to teleport directly to the BCNM. The Lower Delkfutt Tower cutscene should be optional.
To be honest I don't know how I feel about this one. Different guides say different things about this and most don't even mention the cutscene in the Lower Tower. Tokenr says it is optional by now. Maybe others can confirm this too.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 08, 2020 at 07:21:31_

----

Without looking too deeply, I would imagine this CS would only become optional once you've progressed beyond the mission.`ZilartStatus >= 0` seems like a catch-all while you're on that mission. Would the logic to skip the CS be this instead?
```lua
if player:getCurrentMission(ZILART) > tpz.mission.id.zilart.RETURN_TO_DELKFUTTS_TOWER then
... skip cs ...
```


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Oct 09, 2020 at 03:47:24_

----

>  [...] I would imagine this CS would only become optional once you've progressed beyond the mission.

Nope. It's also not really catch-all, since it also checks for currentMission. But while on that mission yes, that is correct and is what's desired in this specific case. The event that sets the 2 is now an optional CS while being on this very mission. There are two cutscenes before zoning into Stellar Fulcrum (BCNM zone):

1. Aldo in Lower Jeuno (has always been optional since 2003; sets ZilartStatus to 1)
2. When zoning into Lower Delkfutt's Tower from Qufim (this could not be avoided back in the day anyways, so some guides don't even mention it; sets ZilartStatus 2)

Today Stellar Fulcrum has a home point so players can just HP to the BCNM fight. With the current logic in place the player is hard pressed to get the CS from lower tower nevertheless because Stellar Fulcrum checks for a 2 on zoneIn. I do not know how this is handled on retail, that's why I said I'm kinda unsure about this PR, but if SE put a home point up there, it sure was not to make the player zone into Lower Delkfutt's first.
`>=0` would just mean that the player may or may not watch either of the above and still get the Stellar Fulcrum event even if he didn't came from Qufim.
Does that make sense?
