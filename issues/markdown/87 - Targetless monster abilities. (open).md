**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:37_
_Originally opened as: project-topaz/topaz - Issue 87_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [dazusu](https://github.com/dazusu)**
_Friday Jan 29, 2016 at 18:04 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2692_

----

On retail, certain monsters have offensive abilities which are targetless.

These abilities should be used, and complete animation without interruption even if all viable targets are out of range.

**Dark Ixion**:
[Acheron Kick](http://ffxiclopedia.wikia.com/wiki/Acheron_Kick), [Trample](http://ffxiclopedia.wikia.com/wiki/Trample), [Wrath of Zeus](http://ffxiclopedia.wikia.com/wiki/Wrath_of_Zeus), [Rampant Stance](http://ffxiclopedia.wikia.com/wiki/Rampant_Stance)

Also note, a small "pre-charge" animation is played before **Wrath of Zeus** or **Lightning Spear** is used. The regular orange charge bars do not appear before these abilities are used. Currently, I believe there is no support for this either.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:38_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Friday Jan 29, 2016 at 18:08 GMT_

----

The pre-charge animation is probably just another skill without a name. Easily supported right now.  Targetless shouldn't be too hard to get in, it's just that every mobskill currently always adds its primary target first before checking aoe (and there are a ton of skills that don't work right because of that, every wyrm breath, etc..)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:40_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Friday Jan 29, 2016 at 18:09 GMT_

----

from irc:

```
<MalRD> Zeus should be self targeting!
```

should be able to just self-target and set findflags to players (also change the distance for valid targets)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:41_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Friday Jan 29, 2016 at 18:12 GMT_

----

Just watched a video on YouTube to clarify some points, as I was miss-remembering:
1. Ixion spins to a random direction (360 degrees) - remains facing this direction for duration of ability use
2. The pre-animation "tell" is head down, horn sparkle.
3. A couple of seconds later, he does a regular ability charge and uses the ability

Ref: https://youtu.be/mqBDwpn5rbc?t=160




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:42_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Friday Jan 29, 2016 at 18:13 GMT_

----

it would still add the first target (itself) I think unless it's looked into.  Actually, all cones and self-centered aoes should be self-target, since they don't rely on the target to find the stuff to add.  Shouldn't be too hard to do, but would require some targetfind changes


