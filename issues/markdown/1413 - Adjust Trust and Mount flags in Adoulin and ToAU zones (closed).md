**Labels:**

reviewed



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Friday Oct 23, 2020 at 10:51:59_
_Originally opened as: project-topaz/topaz - Issue 1413_

----

Missing mount flag in some Adoulin open fields
Removed mount flag in Adoulin dungeons
Adding trust flag in ToAU event zones

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Oct 31, 2020 at 18:57:17_

----

ouch wasn't aware that people were able to use mounts in dungeons lol. Glad this fixed it


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 31, 2020 at 21:16:58_

----

May wanna go over these again; SOA dungeons are losing Escape and Fellow.

Mazurka might be okay; [Omni deliberately didn't touch SOA zones when he was adjusting Mazurka flags last](https://github.com/project-topaz/topaz/pull/539).

![flags](https://user-images.githubusercontent.com/13112942/97790106-b5ee6300-1bbd-11eb-909b-31dd5af34d6d.png)



----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Sunday Nov 01, 2020 at 09:37:53_

----

Escape is intended, release branch does not have it either, because it takes more work to allow escape (need to define escape zones).
I will add back fellow


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Sunday Nov 01, 2020 at 09:54:33_

----

did a quick test on retail, you can use mazurka in SOA dungeons


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Sunday Nov 01, 2020 at 19:39:01_

----

Ok flag FELLOW added for dungeons, even though this flag is not consistent across all zones, which has never been detected as an issue since... fellow is not implemented :-)
