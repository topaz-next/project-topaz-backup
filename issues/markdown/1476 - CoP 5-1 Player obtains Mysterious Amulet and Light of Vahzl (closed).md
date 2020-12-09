**Labels:**

reviewed



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Nov 04, 2020 at 08:30:39_
_Originally opened as: project-topaz/topaz - Issue 1476_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

These slipped my attention in #1433 With this they should be complete. See the spoiler if you're curious :)
- In [Mission 5-1 (Capture)](https://youtu.be/yfBfXpeosFg?t=2196), before getting warped to Promyvion-Vahzl, Prishe returns the drained amulet from Selh'teus to the player. After waking up in Promyvion, the player obtains the amulet key item and the light of Vahzl key item and gets both printed with a special message. This was missing.
<details>
  <summary>Spoiler</summary>
This was a key moment for me because in 6-3 all of a sudden Prishe appears again with an amulet but now you already have one and she got another one. Apparently when Prishe becomes sick in 3-5 and wakes up without her amulet, it was actually Eshan'tarl (formerly known as Cardinal Mildaurion) who "stole" the amulet from her. She tells Prishe though that she only needs to lend it and in 6-3 it becomes clear that she returned Prishe her original amulet. From here on the player has his and Prishe has hers. In 7-5 Nag'molada actually takes the one that legitimately belongs to Prishe, and the one from Selh'teus hold by the player, already weak, now shatters. (Has to be removed at this point, was also missing)
</details>

- In Mission 5-2 the Tarus try to steal the amulet again but get caught and return it to the unconscious player immediately
This cutscene was missing the key item as argument

- [x] Tested working locally.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Nov 06, 2020 at 06:47:46_

----

To passers-by: Normally, we'd want to use: 
https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L299
for assigning key items etc, but it isn't possible to get to these stages while having the key item, and the messages are custom when you DO get them. 

We could MAYBE expand `function npcUtil.giveKeyItem(player, keyitems)` to take some params to tell it to be silent, or to tell it to use custom messages, or something. But, that is out of the scope of this PR.
