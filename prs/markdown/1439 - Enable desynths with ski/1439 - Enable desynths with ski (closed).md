**Labels:**

crafting



<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Tuesday Oct 27, 2020 at 16:43:08_
_Originally opened as: project-topaz/topaz - Issue 1439_

----

Continuing the work of #1306, This is the first step of verifying excluded recipes following the synthesis database rewrite. Per [IBM2431's comment](https://github.com/project-topaz/topaz/pull/1306#issuecomment-717001439), I have activated and assigned levels to recepies with the following criteria:

1. Desynth with FFXIAH listing the skill level as 255
2. BGWiki lists a specific level (no approximations or verification needed flags)
3. Recipe and results match

No assumptions were made based on similar recipes (various gem rings and earrings for example), and no other data was considered.

Recipes with a specific BGWiki skill level but a mismatch in yield or recipe had their skill level set, but remained commented out and had comment added at the end of the line.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:24:21_

----

HQ2: Darksteel Nugget x6


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:25:40_

----

HQ2: Mythril Nugget x4 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:28:44_

----

HQ1: Parchment x1


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:30:38_

----

HQ1: Iron Ingot x1


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:37:05_

----

BGWiki seems confused about HQ yields on their page; I'm fine with these.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:40:02_

----

[BGWiki is claiming this Scorpion Ring desynth is 60](https://www.bg-wiki.com/bg/Scorpion_Ring). Both [FFXIAH](https://www.ffxiah.com/recipes/555) and BGWiki say the _synth_ is 60.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:44:44_

----

Hrm. BGWiki is claiming HQ3 of Mythril Ingot x2, while the current quantity came from [FFXIAH claiming Mythril Ingot x3](https://www.ffxiah.com/recipes/423). Dunno how we want to proceed, or if we want to keep excluding the recipe for further verification.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:50:05_

----

For _yield_ mismatches (_not ingredients_), I'd be okay with going with just BGWiki unless FFXIAH deliberately contradicts.

FFXIAH only recorded what it saw and I don't think it recorded/displays different HQ tiers properly. So if it only saw an [HQ of Bronze Ingot x3](https://www.ffxiah.com/recipes/3199), _I'd_ be okay with [BGWiki's claims that the Bronze Ingot x3 is HQ3, and filling in their claimed HQ1 and HQ2 as appropriate](https://www.bg-wiki.com/bg/Aspis).

But in this case, FFXIAH doesn't _deliberately_ contradict BGWiki by having all tiers filled out with conflicting information. It only has two tiers filled out with mislabeled "tier levels".


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:53:26_

----

I suspect you're going to do another PR for yields, so I won't comment on those further, and just stick to levels for excluded recipes~

(So people who _aren't_ the two of us know what's on BGWiki)

Smithing 79


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:53:55_

----

Smithing 95


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 19:00:38_

----

Leathercraft 90


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 19:01:06_

----

Leathercraft 7


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 19:04:07_

----

Props for _not_ falling for the "Bonecraft Kit 30" trap that some BGWiki editor did for the synth. 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 19:06:30_

----

BGWiki is claiming 52.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Wednesday Oct 28, 2020 at 00:15:05_

----

Seems reasonable to wait until we have retail confirmation or at least some more sources.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Wednesday Oct 28, 2020 at 00:16:49_

----

In that case, that's the course I'll take on the next PR.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:24:21_

----

HQ2: Darksteel Nugget x6


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:25:40_

----

HQ2: Mythril Nugget x4 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:28:44_

----

HQ1: Parchment x1


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:30:38_

----

HQ1: Iron Ingot x1


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:37:05_

----

BGWiki seems confused about HQ yields on their page; I'm fine with these.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:40:02_

----

[BGWiki is claiming this Scorpion Ring desynth is 60](https://www.bg-wiki.com/bg/Scorpion_Ring). Both [FFXIAH](https://www.ffxiah.com/recipes/555) and BGWiki say the _synth_ is 60.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:44:44_

----

Hrm. BGWiki is claiming HQ3 of Mythril Ingot x2, while the current quantity came from [FFXIAH claiming Mythril Ingot x3](https://www.ffxiah.com/recipes/423). Dunno how we want to proceed, or if we want to keep excluding the recipe for further verification.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:50:05_

----

For _yield_ mismatches (_not ingredients_), I'd be okay with going with just BGWiki unless FFXIAH deliberately contradicts.

FFXIAH only recorded what it saw and I don't think it recorded/displays different HQ tiers properly. So if it only saw an [HQ of Bronze Ingot x3](https://www.ffxiah.com/recipes/3199), _I'd_ be okay with [BGWiki's claims that the Bronze Ingot x3 is HQ3, and filling in their claimed HQ1 and HQ2 as appropriate](https://www.bg-wiki.com/bg/Aspis).

But in this case, FFXIAH doesn't _deliberately_ contradict BGWiki by having all tiers filled out with conflicting information. It only has two tiers filled out with mislabeled "tier levels".


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:53:26_

----

I suspect you're going to do another PR for yields, so I won't comment on those further, and just stick to levels for excluded recipes~

(So people who _aren't_ the two of us know what's on BGWiki)

Smithing 79


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 18:53:55_

----

Smithing 95


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 19:00:38_

----

Leathercraft 90


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 19:01:06_

----

Leathercraft 7


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 19:04:07_

----

Props for _not_ falling for the "Bonecraft Kit 30" trap that some BGWiki editor did for the synth. 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 19:06:30_

----

BGWiki is claiming 52.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Wednesday Oct 28, 2020 at 00:15:05_

----

Seems reasonable to wait until we have retail confirmation or at least some more sources.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Wednesday Oct 28, 2020 at 00:16:49_

----

In that case, that's the course I'll take on the next PR.
