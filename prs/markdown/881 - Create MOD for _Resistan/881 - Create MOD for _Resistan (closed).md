**Labels:**

approved



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Thursday Jul 23, 2020 at 22:16:02_
_Originally opened as: project-topaz/topaz - Issue 881_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Creates MOD 958 - STATUSRES for "Resistance to All Status Ailments".
Removes Death Resistance from Items with "All Status Ailments" (see: related BG Thread with justification - https://www.bluegartr.com/threads/108199-Random-Facts-Thread-Other?s=c66ef360f8f47cb9a568306781e9a045&p=6981981&viewfull=1#post6981981 )
Replaces Individual Resist MODS (240-255) on existing "All Status Ailment" Items with a single 958 with relevant value.
Adds math check in magic.lua to combine specific resistance values with the newly created All Status Ailments MOD.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 23, 2020 at 22:43:31_

----

can you do me the favor of making sure modifier.h has the same "spares" as well?

 the fact you had to jump the 1st spare id all the way to 964 tells me the 2 files have come unsynchornised in their lists again.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 23, 2020 at 22:44:39_

----

not your fault you just happen to be in prime position to fix it



----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Thursday Jul 23, 2020 at 22:53:29_

----

https://github.com/neuromancerxi/topaz/blob/003425b91d553a271fd4237119def041b4cf3be0/src/map/modifier.h#L804

modifier.h already has next spare as 964.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 00:17:28_

----

but I looked and it doesn't have 1:1 for all 3.

```cpp
    // The spares take care of finding the next ID to use so long as we don't forget to list IDs that have been freed up by refactoring.
    // 570 through 825 used by WS DMG mods these are not spares.
    // SPARE = 964, // stuff
    // SPARE = 965, // stuff
};
```
both files should have all matching id's, for everything, even the spares. it helps prevent future editors from mistakenly thinking an ID is used/not used


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 17, 2020 at 16:43:13_

----

note to self: come back later and murder this giant if/else tower with great fury.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 23, 2020 at 22:43:31_

----

can you do me the favor of making sure modifier.h has the same "spares" as well?

 the fact you had to jump the 1st spare id all the way to 964 tells me the 2 files have come unsynchornised in their lists again.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 23, 2020 at 22:44:39_

----

not your fault you just happen to be in prime position to fix it



----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Thursday Jul 23, 2020 at 22:53:29_

----

https://github.com/neuromancerxi/topaz/blob/003425b91d553a271fd4237119def041b4cf3be0/src/map/modifier.h#L804

modifier.h already has next spare as 964.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 00:17:28_

----

but I looked and it doesn't have 1:1 for all 3.

```cpp
    // The spares take care of finding the next ID to use so long as we don't forget to list IDs that have been freed up by refactoring.
    // 570 through 825 used by WS DMG mods these are not spares.
    // SPARE = 964, // stuff
    // SPARE = 965, // stuff
};
```
both files should have all matching id's, for everything, even the spares. it helps prevent future editors from mistakenly thinking an ID is used/not used


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 17, 2020 at 16:43:13_

----

note to self: come back later and murder this giant if/else tower with great fury.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Aug 17, 2020 at 06:33:42_

----

is this the MOD for the ribbon equipment? :smile: 


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Monday Aug 17, 2020 at 11:56:45_

----

> is this the MOD for the ribbon equipment? smile

Yep. Ribbons, Hearty Earring, and others with the "Resistance to All Status Ailments" listed on the item.
