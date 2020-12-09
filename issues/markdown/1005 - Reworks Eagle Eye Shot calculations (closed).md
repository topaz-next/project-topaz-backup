**Labels:**

hold



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Wednesday Aug 26, 2020 at 00:51:55_
_Originally opened as: project-topaz/topaz - Issue 1005_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This is a WIP, and I'd like input or suggestions.

Some of this might only be properly handled in source.  
Still todo:

- add TP per weapon delay - confirmed by rudejerk with two chars on retail: rudejerk08/25/2020
"TP return is based on weapon delay"
- adjust enmity value to "mimimum amount": Nyu08/25/2020 https://forum.square-enix.com/ffxi/threads/23295-May-16-2012-%28JST%29-Version-Update Eagle Eye Shot: Enmity incurred by ranged attacks made with this ability has been lowered to the minimum possible value.
- fix calculation?  it should be 5x a ranged attack (from wiki: Damage of Eagle Eye Shot = Damage of 1 ranged attack * 5.00.), not based specifically on your ranged weapon damage.
- factor in crit hit rate and +% crit damage -- EES can crit, from wikipedia as well... assume it can crit as often as a normal ranged attack after factoring in mods.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Wednesday Aug 26, 2020 at 04:13:57_

----

can you cite sources?

my feedback would be to get the math down, this mechanic will hopefully be changing in the next few months.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Aug 27, 2020 at 21:29:01_

----

> 
> 
> can you cite sources?
> 
> my feedback would be to get the math down, this mechanic will hopefully be changing in the next few months.

sources cited


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 26, 2020 at 05:54:56_

----

The sources you've cited:

```
Eagle Eye Shot
Enmity incurred by ranged attacks made with this ability has been lowered to the minimum possible value.

[dev1119] The following job abilities have had their effective range extended:
Eagle Eye Shot / Shadowbind / Bounty Shot / Quick Draw
```

Any updates on the ideas behind these changes?

Also, @TeoTwawki ?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 28, 2020 at 04:58:58_

----

Tank has stepped away from the project and we don't have any evidence that this is the correct way to go for damage calcs, so closing the PR


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 28, 2020 at 06:50:13_

----

should be fairly easy for a retail ranger to sort out the actual math. if its really 5x the final damage and not 5x some step along the way, then the final damage can only ever be a multiple of 5. no 2001 or 1503 dmg amounts for example would ever be possible. "5x a ranged attack" is pretty ambiguous as to how the multiplier is applied. SE's own phrasing says "five-fold" which they usually reserve for multihit, leading me to think _maybe_ they calculated acc once but calculated 5 damages and added them, rather than a straight 5x(original value) or _maybe_ they did a 5x multiplier on a step prior to the final dmg. I could locate no official sources on the 1,5x multiple being reference either. In teh event we do need to just take a standard ranged attack and 5x the final damage value, we should _just bind the function that already does ranged attacks_  and make use of that.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 28, 2020 at 07:11:48_

----

I've always wanted to level ranger... Guess now I have an excuse


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Sep 28, 2020 at 16:13:52_

----

Is there a difference between ranged attack damage * 5 and a single-hit ranged weaponskill with a ftp multiplier of 5?
