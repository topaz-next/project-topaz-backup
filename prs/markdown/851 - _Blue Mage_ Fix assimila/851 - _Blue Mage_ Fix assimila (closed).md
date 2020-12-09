**Labels:**

focus

reviewed



<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Wednesday Jul 15, 2020 at 19:12:04_
_Originally opened as: project-topaz/topaz - Issue 851_

----

Assimilation Blue Mage merit now works. It properly raises the amount of blue points per merit assigned.
From my testing, it doesnt seem to break anything.

Credits to Devi for decompiling the game and to Caelic for the actual code.
Permission to PR this was granted by Caelic.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 20, 2020 at 20:50:13_

----

Does retail only set these bits when the character is on BLU, or is the merit point value _always_ sent but just not usable?


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Monday Jul 20, 2020 at 21:21:07_

----

asimilation is a job specific merit, they can only be set while the main job is blu


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 25, 2020 at 01:35:23_

----

Whoever wants to investigate, see the capture "Wings of the Goddess: WOTG 10 (Part 1)".

At 06:12:44 (system time - always viewable in the top-right corner of a character's screen) she enters a Mog House and changes from WHM to BLU. This is at around 28:52 on the video.

Here's the excerpt of her incoming 0x063 packet log around that time:
[WHM_to_BLU_0x063.log](https://github.com/project-topaz/topaz/files/4974746/WHM_to_BLU_0x063.log)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 20, 2020 at 20:50:13_

----

Does retail only set these bits when the character is on BLU, or is the merit point value _always_ sent but just not usable?


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Monday Jul 20, 2020 at 21:21:07_

----

asimilation is a job specific merit, they can only be set while the main job is blu


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 25, 2020 at 01:35:23_

----

Whoever wants to investigate, see the capture "Wings of the Goddess: WOTG 10 (Part 1)".

At 06:12:44 (system time - always viewable in the top-right corner of a character's screen) she enters a Mog House and changes from WHM to BLU. This is at around 28:52 on the video.

Here's the excerpt of her incoming 0x063 packet log around that time:
[WHM_to_BLU_0x063.log](https://github.com/project-topaz/topaz/files/4974746/WHM_to_BLU_0x063.log)
