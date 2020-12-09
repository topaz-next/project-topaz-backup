**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday May 28, 2020 at 15:40:40_
_Originally opened as: project-topaz/topaz - Issue 663_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
This has been getting a lot of discussion lately in the discord so I am making an issue (didn't see an existing one) so people can find this info easily and be aware of it - it has been a longstanding known quirk that the system for making pets use their skills is riding off the mobskills system in places that retail doesn't do this. They work, except when the skill doesn't exist in the monster version of the list (Siren) and certain 3rd party addons expected the retail version of the packet.

> [2:39 PM] Teo: the person you are quoting is mostly correct that it is done wrong using monster moves
[2:40 PM] Teo: the core has this weirdness where the pet "ability" is connected with a mob move and shouldn't be (hence why ppl had problems adding siren's moveset)
[2:40 PM] Teo: real pet skills are in the player ability list in rom\181\72.dat
[2:43 PM] Teo: player ws, ability, avatar, and monstrosity stuff all there
[2:44 PM] Teo: monsters skills are in rom\24\80.dat
the way is coded right now the pet's ability had to exist in both dats for us to use it, and its the mob version firing off.

![](https://media.discordapp.net/attachments/639659267003252748/715585087072108655/0x28-2.png?width=432&height=426)


----
<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [EpicTaru](https://github.com/EpicTaru)**
_Thursday May 28, 2020 at 17:38:59_

----

Also per Thorny in the Ashita discord, the accepted work around (until this is fixed in Topaz) is:

![bp workaround 1](https://user-images.githubusercontent.com/26195580/83174484-17c31200-a0e0-11ea-8d86-35978bfb2f7c.png)
![bp workaround 2](https://user-images.githubusercontent.com/26195580/83174495-198cd580-a0e0-11ea-9753-26017ed18710.png)
![bp workaround 3](https://user-images.githubusercontent.com/26195580/83174502-1a256c00-a0e0-11ea-806a-d33468aa82ca.png)



----
<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [EpicTaru](https://github.com/EpicTaru)**
_Thursday May 28, 2020 at 17:42:05_

----

The above snippet is from my SMN Ashitacast profile so set names probably won't be the same for what others use in their SMN Ashitacast profile.  Adjust accordingly, ofc.


----
<a href="https://github.com/Sinnersslayer"><img src="https://avatars2.githubusercontent.com/u/33654112?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Sinnersslayer](https://github.com/Sinnersslayer)**
_Monday Jun 01, 2020 at 07:40:41_

----

Thing is that if you define it like this, you won't be able to swap BP delay set before using BP dmg.
I have found another solution.
I have removed all BPs names defined under ``ad_name``  in ``<petskill>`` and used ``<else><equip set="BP-Physical" /></equip>`` at the end of ``<petskill>`` section.
That way, Ashitacast swapping **BP-Physical** set for every undefined BP.
Works on v1.58 since yesterday, no issues so far.
