**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 16, 2020 at 08:48:12_
_Originally opened as: project-topaz/topaz - Issue 1375_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

You can play the cutscene while being attacked by a monster by clicking the point where the Cutscenes animation scene flows in the field or dungeon. And while the cutscene is playing, the monsters continue to attack and the player can't do anything. And by the end of the cutscene play, the player is already dead.
Is the above behavior the same as retail specifications?

In the retail specifications, the behavior of the cutscene types is as follows.
1. An Cutscenes that occurs when you choose an option or take a specific action (such as a warp).
A state in which the status icon is still displayed and interference from others is accepted. It will be forcibly terminated if it receives interference from others.
2. An Cutscenes with an animated scene.
The status icon disappears and no interference from others is accepted.

if you are hit by weak magic such as "Blind", or if the effects of "Utsusemi" and "Blink" are erased, the Cutscenes will be canceled even if it is not damaged.
Since the use of the warp device and the operation of opening the door are also treated as Cutscenes , they may be interrupted by external interference.
The OP teleport will end the Cutscenes immediately after selecting "Yes".
If you select "Yes" to track hostile monsters, the hostility disappears.
In the Cutscenes where the screen is completely switched (corresponding to the above two items), on the contrary, the interference of monsters is temporarily stopped and the hostility disappears.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 16, 2020 at 14:40:58_

----

the rules that covers most of this is:
 * if you are the target of an enmity/aggro action, and you didn't already make it to the fade out, you get "event skipped".
* if you made it to a fade out, the mob(s) forget you exist (example: changing floors in promy dem)



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 16, 2020 at 15:17:53_

----

@zach2good and I were talking about the need to implement this functionality. We were considering a new binding so we could distinguish between "safe" cutscenes and "stopable" cutscenes.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 16, 2020 at 15:44:59_

----

Thank you for comment.
I would appreciate your consideration.
