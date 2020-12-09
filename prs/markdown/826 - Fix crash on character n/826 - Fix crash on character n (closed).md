**Labels:**

merge ready



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Wednesday Jul 08, 2020 at 21:29:41_
_Originally opened as: project-topaz/topaz - Issue 826_

----

Does what it says on the tin! Fixed evil memcpy with assumptive byte-lengths.

Fixes #825 
<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Jul 09, 2020 at 02:39:04_

----

Thanks Kreidos, this is what kept crashing our connect server!  Meant to submit an issue for this.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 11, 2020 at 20:25:04_

----

Pinging @bope12, who had some similar fix pending on SuperNova.  I recall Bope changed a couple more things, so he might have some input here.


----
<a href="https://github.com/bope12"><img src="https://avatars0.githubusercontent.com/u/2702250?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [bope12](https://github.com/bope12)**
_Sunday Jul 12, 2020 at 00:23:14_

----

> 
> 
> Pinging @bope12, who had some similar fix pending on SuperNova. I recall Bope changed a couple more things, so he might have some input here.

I can't comment on this fix as I changed it a different way to stop the crashing, but line 194 
`                        memcpy(CharList + 12 + 32 + i * 140, strCharName, 15);`
can be changed to 16 at the end to make the names display correctly in the character select



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Jul 12, 2020 at 00:38:35_

----

Confirmed. The null wasn't being included in the character select packet, so the world name was being appended to the displayed character name. Changing to 16 makes sure the null is grabbed.

Adjusted to 16 as per @bope12. Thanks for the tip, bope12!
