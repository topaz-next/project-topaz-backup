**Labels:**

hold



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Wednesday Oct 14, 2020 at 18:08:53_
_Originally opened as: project-topaz/topaz - Issue 1360_

----

Zones: Kuftal / Gustav Tunnel

(I confirmed the changes by doing to random checks in both zones on retail)

Cf #1190 for discussion about this.

With the introduction of Ground of Valor, SE reduced all respawn rates
to 5 minutes for normal mobs in GoV dungeons.Happened  around 2011, as
mentioned here:
https://forum.square-enix.com/ffxi/archive/index.php/t-10269.html?s=4e177444d020fa7d4d45328406c31160

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 16, 2020 at 18:19:07_

----

This (and the other PRs) are big sets of changes to fundamental groups of mobs. I'm starting to worry that _random checking_ isn't enough to justify these sorts of changes. Especially if you're planning on doing this sort of blanket adjustment on every GOV zone. There is a balance issue here, if respawns are too low they'll destroy historical exp camps etc.

I'm gonna put a hold on this until I have time to check the mobs in this PR. Sorry!


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Saturday Oct 17, 2020 at 16:48:04_

----

There is really no other way for you to believe this besides checking by yourself on retail?
I can check all of the mobs if you really want, but would that be enough?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 00:21:24_

----

In Kuftal Tunnel, the Sand Lizard, Robber Crab, Cave Worm, Fire Elemental, Sabotender Sedieno, Recluse Spider, Ovinnik, Greater Cockatrice, Ladon, Kuftal Delver, Deinonychus, Goblin Mercenary, Alchemist, Bandit and Tamer respawned after 5 minutes.

The Haunt and Diplopod did not. I do not know their exact respawn time, but the Haunt was greater than 10 minutes, and the Diplopod was greater than 16. I did confirm that both did eventually respawn. I was the only person in the zone.

I did not check Gustav Tunnel.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Sunday Oct 18, 2020 at 12:31:07_

----

I checked on Asura, and Haunt are indeed 20 minutes.
Diplopod is more tricky: it does respawn after 5 minutes but it uses shared spawn with the 3 IDs:
17490077 / 17490090 / 91.
i saw the upper level 77 respawn once as 5 min. And the next time, it didnt respawn at all while the 90 had spawn.
So i think here its the same kind of issue that we have with Monastic Cavern and such: SE is not spawning everything contrary to us, hence the overpopulation is some areas.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Oct 27, 2020 at 19:50:05_

----

I edited Haunt to move it to 20min.
Do you want me to remove Gustav zone edits entirely, so that we can merge Kuftal (so that IBM time checking everything does not go to waste)?
Or I can check all Gustav mobs if you wish.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 23, 2020 at 01:08:16_

----

I did eventually witness the Diplopod I killed respawn. As I was the only person in the zone, I'm not convinced on the potential "shared spawn" explanation - if the respawn time were 5 minutes, it spawned in a different slot, and I was the only person killing mobs, what later caused it to respawn in the slot I used?

I reverted the Diplopod in Kuftal. Since the Antares in Gustav was also a scorpion, absent concrete evidence of it being lowered, I reverted that back as well. Since the Erlik in Gustav is a Haunt, and the corresponding Haunt in Kuftal was confirmed to be on a 20 minute timer, I also set the Erlik to 20 minutes.

Based on the "similar mobs" in Kuftal being confirmed to have been lowered, I'm willing to presume that the other mobs in Gustav have been lowered, and left them as you set them.

[The branch this was originally merged to is now merged into release.](https://github.com/project-topaz/topaz/commit/a20caebabe360cec2b1bc2a0e640ee3ecf2e3d81)
