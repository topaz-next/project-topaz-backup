**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Friday Nov 13, 2020 at 18:08:14_
_Originally opened as: project-topaz/topaz - Issue 1513_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

The goal of this PR was to fix the first time visiting events of classic Dynamis areas including Dreamland zones.
In the process there were a lot of things I stumbled upon and needed adjustments.

This fixes:
- being able to enter base zones with only VIAL_OF_SHROUDED_SAND
The requirements have been rewritten to be incremental and based on the PRISMATIC_HOURGLASS since it is impossible to legitimately obtain *any* of the subsequent key items without obtaining the hourglass first and the hourglass trade is locked behind the Vial of Shrouded Sand. Consequently it is impossible to legitimately obtain a HYDRA_CORPS_INSIGNIA *without* winning all the other areas. It is therefore perfectly reasonable to only check for the follow-up items. This applies to Dreamland also.
- use of incorrect legacy menus
The csid's for the menus were all wrong and called one of two legacy menus which did not work with the parameteres that were passed. Dialogues referred to legacy mechanics and put wrong output in wrong places and options plain would not work. I suppose everybody reading here knows what this refers to exactly, but just in case I made a [short video](https://streamable.com/ywju5a) on stock Topaz canary branch (Canaria server).
- bad usage of area bit
The player was getting the current areas bit set only by *calling* the menu even if he chose to cancel it. The bit was changed to be applied only after choosing to enter Dynamis.
- wrong default dialogues and incorrect usage of Hieroglyphics in Dreamland areas and incorrect usage of default dialogues of Trail Markings in classic areas
The deault dialogue [will](https://youtu.be/oI7jo-3EYZA?t=14) *[always](https://youtu.be/mD91QXsDvSM?t=707)* [print](https://www.youtube.com/watch?v=i6Sg1Q6fvYg) on every click except for the [winning cs](https://www.youtube.com/watch?v=pgksQI0IRKs) and the very first visit of [Dynamis Tavnazia](https://www.youtube.com/watch?v=QBgEgg0v3uo). This required some extra logic.
- obtaining RHAPSODY_IN_AZURE while on cooldown would not allow to enter Dynamis despite having the key item
An additional check for the key item allows to by-pass this behavior

This adds:
- all the first-visit cutscenes for all classic and all dreamland areas
logic had to be re-written because these cutscenes are [played](https://youtu.be/mD91QXsDvSM?t=707) *[after](https://youtu.be/qLxB7TxGQUY?t=2635)* [selecting](https://www.youtube.com/watch?v=pAI_9XDL9kc) "Ready!" from the menu event with the sole exception of Dynamis Tavnazia where the player simply [falls](https://youtu.be/qLxB7TxGQUY?t=4674) [unconscious](https://www.youtube.com/watch?v=t4Ph4daUwns) when clicking the Hieroglyphics there upon first visit.

Additional changes:
 • renamed `csSand` to `csVial` as it could be mistaken for having a relation to San d'Oria
 • renamed `csDyna` to `csMenu` to make it as descriptive as possible
 • outsourced the re-enter timeout into a local function because it gets used twice and clutters the legibiliity of later logics
*(Tavnazia first visit needs this individually)*

- [x] Tested extensivly locally working, probing all marks during every step
(with only vial ki, with hourglass ki, first-cs, winning-cs, access of subsequent zones, functionality of subjob in dreamland)
*(Made sure this time that I didn't accidentally watch Dyna [D] captures ;D)*

