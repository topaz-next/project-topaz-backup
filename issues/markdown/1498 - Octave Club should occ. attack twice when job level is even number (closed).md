**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Nov 11, 2020 at 00:59:35_
_Originally opened as: project-topaz/topaz - Issue 1498_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

This is not merged yet but I'm opening this because I can't figure out a way to handle this well in #1490
#1490 will already come with the multiplier of 8 activated but:

The concrete issue is that Octave Club sets a modifier value once when the Players main job level is a multiple of 8 and another value when the level is even (multiple of 2).

Problem is that apparently *all* levels that are multiples of 8 are *also* even, and the current logic will try to apply both mod values at the same time. There needs to be a check made somewhere when adding the latents to give preference to either the latent that gives the higher modifier, or to the latentid that has the higher value.

This could maybe become its own function in `latent_effect_container.cpp` where job level divisors are structured in order of priority from highest to lowest: `void CLatentEffectContainer::CheckLatentsJobMultiple()` or something along those lines.
Say: for each latentlist latentid that is JOB_MULTIPLE get value. Add only the mod of item in list with highest value.

Maybe there's a way easier solution though? 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 11, 2020 at 01:01:13_

----

use 2 rows in latent table, and remember that the modifier will stack

so 2+6 = 8


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Wednesday Nov 11, 2020 at 01:07:46_

----

> use 2 rows in latent table, and remember that the modifier will stack
> 
> so 2+6 = 8

Came here to say mostly this as well. Use Latent Cases since you're planning on moving this to a MOD anyway.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Nov 11, 2020 at 02:09:44_

----

Thank you very much both of you! I didn't realize that they *add* up.
