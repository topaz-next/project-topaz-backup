**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Sep 12, 2020 at 07:24:41_
_Originally opened as: project-topaz/topaz - Issue 1103_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

![image](https://user-images.githubusercontent.com/1389729/93587563-c56d7000-f9b2-11ea-995e-fa9bf390734d.png)

It's been asked a few times, so I've extracted the most basic elements needed to do PVP into its own PR.
Originally from my dead ballista branch: https://github.com/project-topaz/topaz/compare/release...zach2good:ballista_v2

**How it works:**
- You run `!setallegiance 2`
- A "friend" runs `!setallegiance 3` (or you run: `!setallegiance 3 Target`)
- You are now able to fight to the death.

I changed the targeting and tested my results using this table:
```
**Original Results**

ALLEGIANCE_MOB vs ALLEGIANCE_MOB: false
ALLEGIANCE_MOB vs ALLEGIANCE_PLAYER: true
ALLEGIANCE_MOB vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_MOB vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_MOB vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_MOB vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_MOB vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_PLAYER vs ALLEGIANCE_MOB: true
ALLEGIANCE_PLAYER vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_PLAYER vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_PLAYER vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_PLAYER vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_PLAYER vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_PLAYER vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_MOB: false
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_BASTOK: true
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_BASTOK vs ALLEGIANCE_MOB: false
ALLEGIANCE_BASTOK vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_BASTOK vs ALLEGIANCE_SAN_DORIA: true
ALLEGIANCE_BASTOK vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_BASTOK vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_BASTOK vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_BASTOK vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_WINDURST vs ALLEGIANCE_MOB: false
ALLEGIANCE_WINDURST vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_WINDURST vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_WINDURST vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_WINDURST vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_WINDURST vs ALLEGIANCE_WYVERNS: true
ALLEGIANCE_WINDURST vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_WYVERNS vs ALLEGIANCE_MOB: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_WINDURST: true
ALLEGIANCE_WYVERNS vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_GRIFFONS vs ALLEGIANCE_MOB: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_GRIFFONS: false
```

```
**New Results**

ALLEGIANCE_MOB vs ALLEGIANCE_MOB: false
ALLEGIANCE_MOB vs ALLEGIANCE_PLAYER: true
ALLEGIANCE_MOB vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_MOB vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_MOB vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_MOB vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_MOB vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_PLAYER vs ALLEGIANCE_MOB: true
ALLEGIANCE_PLAYER vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_PLAYER vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_PLAYER vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_PLAYER vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_PLAYER vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_PLAYER vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_MOB: false
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_BASTOK: true
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_WINDURST: true
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_SAN_DORIA vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_BASTOK vs ALLEGIANCE_MOB: false
ALLEGIANCE_BASTOK vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_BASTOK vs ALLEGIANCE_SAN_DORIA: true
ALLEGIANCE_BASTOK vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_BASTOK vs ALLEGIANCE_WINDURST: true
ALLEGIANCE_BASTOK vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_BASTOK vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_WINDURST vs ALLEGIANCE_MOB: false
ALLEGIANCE_WINDURST vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_WINDURST vs ALLEGIANCE_SAN_DORIA: true
ALLEGIANCE_WINDURST vs ALLEGIANCE_BASTOK: true
ALLEGIANCE_WINDURST vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_WINDURST vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_WINDURST vs ALLEGIANCE_GRIFFONS: false

ALLEGIANCE_WYVERNS vs ALLEGIANCE_MOB: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_WYVERNS: false
ALLEGIANCE_WYVERNS vs ALLEGIANCE_GRIFFONS: true

ALLEGIANCE_GRIFFONS vs ALLEGIANCE_MOB: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_PLAYER: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_SAN_DORIA: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_BASTOK: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_WINDURST: false
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_WYVERNS: true
ALLEGIANCE_GRIFFONS vs ALLEGIANCE_GRIFFONS: false
```


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Sep 18, 2020 at 17:44:00_

----

The fact this line is going away pleases me greatly.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Sep 18, 2020 at 17:53:31_

----

Took some thinking to understand what this section does. I'm not super familiar with how allegiances work, but are there cases where a player with Nation Allegiance would need to fight a Mob? That would seem to not be covered by any of these cases.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 18:17:12_

----

I'm going under the assumption that those are only for ballista, and that campaign battles have their own thing going on. Since none of that is anywhere close to anyone implementing, I think these are safe.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Sep 18, 2020 at 17:44:00_

----

The fact this line is going away pleases me greatly.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Sep 18, 2020 at 17:53:31_

----

Took some thinking to understand what this section does. I'm not super familiar with how allegiances work, but are there cases where a player with Nation Allegiance would need to fight a Mob? That would seem to not be covered by any of these cases.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 18:17:12_

----

I'm going under the assumption that those are only for ballista, and that campaign battles have their own thing going on. Since none of that is anywhere close to anyone implementing, I think these are safe.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 08:07:29_

----

**TODO**
Check this section still fires:
```
    if ((targetFlags & TARGET_SELF) && (this == PInitiator || (PInitiator->objtype == TYPE_PET &&
        static_cast<CPetEntity*>(PInitiator)->getPetType() == PETTYPE_AUTOMATON && this == PInitiator->PMaster)))
    {
        return true;
    }
```

**EDIT:** Yeah, it will, target flags are a thing
