**Labels:**

merge ready



<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 18:59:25_
_Originally opened as: project-topaz/topaz - Issue 608_

----

The current message players get when using OP teleporters is wrong with regards to ownership of regions (except the San d'Orian one, because that nation ID is 0 anyway).
This issue is also reported here with some examples: https://github.com/EdenServer/community/issues/827

[Test Video](https://www.youtube.com/watch?v=fM-lPnh9hmo) - Shows results both before and after the fix.

Basically they report any region under San d'Orian control as being under control of your home nation, even if you're in Windurst/Bastok, and any others as outside your home nation control.

Captured a few of the events on retail when talking with them:
* [Windurst teleporter - player from Windurst](https://github.com/project-topaz/topaz/files/4606529/op-warp-windy-windynation.log)
* [San d'Orian teleporter - player from San d'Oria](https://github.com/project-topaz/topaz/files/4606530/op-warp-sandy-sandynation.log)
* [Bastok teleporter - player from San d'Oria](https://github.com/project-topaz/topaz/files/4606531/op-warp-bastok-sandynation.log) - note that the region data is still sent in the first parameters, even though player is not allowed to teleport.

They all show that two of the bytes in Param 5 are set to the player and the teleporter nation, which in turn are used by the client to determine home nation ownership of regions, and if the player is allowed to teleport at all.

This PR changes Param 5 to be: `<zero byte> <teleporter nation byte> <player nation byte>`

_Note: The reason it works correctly for San d'Orians with the current topaz implementation, is because this param is just set to 0, which in turn is translated by the client as if both the player and the teleporter are San d'Orian._

In the current topaz implementation, Param 4 currently has some nation data sent in it, but I don't think this is correct. From the captures above this param is always `16777216 (0x01000000)`, and I also did a capture in the previous conquest week and it had the same value. I'm not sure what it is used for, if anything, so I've set it to 0 for now. Any ideas to what it could mean are welcome.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


