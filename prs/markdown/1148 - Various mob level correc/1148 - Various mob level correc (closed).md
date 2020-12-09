**Labels:**

approved

reviewed



<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Nireya](https://github.com/Nireya)**
_Thursday Sep 17, 2020 at 07:51:42_
_Originally opened as: project-topaz/topaz - Issue 1148_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

All of this was done by using capture data provided in the captures discord by Wiggo, aether, ibm2431, and Jimmayus. Thanks to those 4 for providing the data. I've attached the .log data from their captures to make it easy for reviewers.

Synopsis of changes:
Fully audited and corrected mob levels for Rise of the Zilart missions (lacked data for the pot NM for a full completion).
Fully audited and corrected mob levels for all Chains of Promathia missions (including pop NMs and any I missed previously).
Fully audited and corrected mob levels for all Treasures of Aht Urhgan  missions.
Corrected many HNM mob levels.

Also a valuable source I used:
https://docs.google.com/spreadsheets/d/1YBoveP-weMdidrirY-vPDzHyxbEI2ryECINlfCnFkLI/edit#gid=1789487472

[The Celestial Nexus.log](https://github.com/project-topaz/topaz/files/5237136/The.Celestial.Nexus.log)
[Cape Teriggan.log](https://github.com/project-topaz/topaz/files/5237137/Cape.Teriggan.log)
[Al'Taieu2.log](https://github.com/project-topaz/topaz/files/5237138/Al.Taieu2.log)
[Misareaux Coast.log](https://github.com/project-topaz/topaz/files/5237139/Misareaux.Coast.log)
[Pso'Xja.log](https://github.com/project-topaz/topaz/files/5237140/Pso.Xja.log)
[Sacrarium.log](https://github.com/project-topaz/topaz/files/5237141/Sacrarium.log)
[Carpenters' Landing.log](https://github.com/project-topaz/topaz/files/5237142/Carpenters.Landing.log)
[Attohwa Chasm.log](https://github.com/project-topaz/topaz/files/5237143/Attohwa.Chasm.log)
[Dragon's Aery.log](https://github.com/project-topaz/topaz/files/5237144/Dragon.s.Aery.log)
[Jugner Forest [S].log](https://github.com/project-topaz/topaz/files/5237145/Jugner.Forest.S.log)
[Nyzul Isle2.log](https://github.com/project-topaz/topaz/files/5237146/Nyzul.Isle2.log)
[Nyzul Isle.log](https://github.com/project-topaz/topaz/files/5237147/Nyzul.Isle.log)
[Misareaux Coast2.log](https://github.com/project-topaz/topaz/files/5237148/Misareaux.Coast2.log)
[Bibiki Bay.log](https://github.com/project-topaz/topaz/files/5237149/Bibiki.Bay.log)
[Carpenters' Landing2.log](https://github.com/project-topaz/topaz/files/5237150/Carpenters.Landing2.log)
[Navukgo Execution Chamber.log](https://github.com/project-topaz/topaz/files/5237151/Navukgo.Execution.Chamber.log)
[Chamber of Oracles.log](https://github.com/project-topaz/topaz/files/5237152/Chamber.of.Oracles.log)
[The Ashu Talif.log](https://github.com/project-topaz/topaz/files/5237153/The.Ashu.Talif.log)
[Promyvion - Vahzl.log](https://github.com/project-topaz/topaz/files/5237154/Promyvion.-.Vahzl.log)
[Al'Taieu.log](https://github.com/project-topaz/topaz/files/5237155/Al.Taieu.log)
[Sacrificial Chamber.log](https://github.com/project-topaz/topaz/files/5237156/Sacrificial.Chamber.log)
[The Ashu Talif2.log](https://github.com/project-topaz/topaz/files/5237157/The.Ashu.Talif2.log)
[The Ashu Talif3.log](https://github.com/project-topaz/topaz/files/5237158/The.Ashu.Talif3.log)
[Behemoth's Dominion.log](https://github.com/project-topaz/topaz/files/5237159/Behemoth.s.Dominion.log)
[Periqia.log](https://github.com/project-topaz/topaz/files/5237160/Periqia.log)
[Jade Sepulcher.log](https://github.com/project-topaz/topaz/files/5237161/Jade.Sepulcher.log)
[Qu'Bia Arena.log](https://github.com/project-topaz/topaz/files/5237162/Qu.Bia.Arena.log)



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 17, 2020 at 10:39:59_

----

Wow, this is good work! I'll look through this at the weekend, thanks alot!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 17, 2020 at 15:54:25_

----

What did the person making the spreadsheet use for their source? I see some thing that don't jive with packet caps there. ..Some of it might come in ranges I guess..


----
<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Nireya](https://github.com/Nireya)**
_Thursday Sep 17, 2020 at 20:03:01_

----

> What did the person making the spreadsheet use for their source? I see some thing that don't jive with packet caps there. ..Some of it might come in ranges I guess..

I believe the creator of the sheet is Jimmayus, who also provided many of the retail captures on the capture discord that I used. Their data is from months of retail captures/monstrosity/HNM stat testing. I agree some of them likely have a few ranges that could use slight tweaking, but difficult as there was not a ton of people capturing to pull from and verify it with, plus a lot of the ffxiclopedia numbers are wrong as the captures show (Behemoth being level 80 for example).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 18, 2020 at 02:50:41_

----

k, I trust almost all of Jim's data. If we get some other data confirms later we can re-evaluate case by case whatever he has is likely to be far more accurate than other sources (let alone whats already in repository).
