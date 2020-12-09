**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 14, 2020 at 11:12:50_
_Originally opened as: project-topaz/topaz - Issue 1357_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

For THF AF feet quest "Hitting the Marquisate" in Garlaige Citadel:

When clicking a ??? and it's the right one in order, the player should receive the proper event which asks him/her whether or not to use the Bomb Incense key item. After choosing yes that ??? should become unusable for this purpose and the player can search for the next one. This way the player gets a proper clue on which ??? is the next.

Also the bomb NM should spawn with a certain delay or else it will most probably instantly self-destruct (since the only way to avoid this is to know this mechanic and run instantly after the CS into the correct corner), in which case the player won't get the necessary item dropped. Guides, and even the event's dialogue suggest this behavior.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Oct 16, 2020 at 04:54:53_

----

So luckily I found [a video from 2016](https://www.youtube.com/watch?v=X3Ou2nm5qCI) specific to this quest. There were even more messages missing. I added those, for which there were no JSON dumps and manually searching through the scenes in game didn't yield anything, so I used `messageSpecial`. The spawn seems to be around 5 seconds after the cutscene. I think that's a fair value.

- [x] Tested working locally

Doesn't build with various connection errors to OpenSuse..., is that from my end?
