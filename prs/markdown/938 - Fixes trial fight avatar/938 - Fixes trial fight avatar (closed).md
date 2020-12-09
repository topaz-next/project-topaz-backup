**Labels:**

reviewed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Aug 13, 2020 at 20:08:19_
_Originally opened as: project-topaz/topaz - Issue 938_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR splits the original scripts for the primes into two--one for the mini trial/normal trial and one for the ASA mission that wasn't completed yet.  The ASA script is NOT linked to any of the primes in the mob_spawn_points from the database currently, so that will need to be adjusted when ASA is actually implemented.

Also level adjusts the primes for these fights to 20 for mini and 60 for regular (according to bgwiki and captures).

Also still to be done: each avatar should be immune to magic of its own element.  I'm unsure what the message is specifically when you use fire on ifrit, but that can be determined later, or added to this PR with further insight.
