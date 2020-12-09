**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 02, 2020 at 17:07:34_
_Originally opened as: project-topaz/topaz - Issue 1235_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

https://github.com/project-topaz/topaz/blob/50e64bd5fa324a22e260b5c79a3213fb3510d186/scripts/zones/La_Theine_Plateau/npcs/Augevinne.lua#L14-L32

The messages in "L26" and "L29" are wrong.
(L26) player:showText(npc, ID.text.RESCUE_DRILL + 6)
(L29) player:showText(npc, ID.text.RESCUE_DRILL + 33)

https://github.com/project-topaz/topaz/blob/50e64bd5fa324a22e260b5c79a3213fb3510d186/scripts/zones/La_Theine_Plateau/npcs/Yaucevouchat.lua#L14-L32

The messages in "L26" and "L29" are wrong.
(L26) player:showText(npc, ID.text.RESCUE_DRILL + 7)
(L29) player:showText(npc, ID.text.RESCUE_DRILL + 34)

https://github.com/project-topaz/topaz/blob/50e64bd5fa324a22e260b5c79a3213fb3510d186/scripts/zones/La_Theine_Plateau/npcs/Vicorpasse.lua#L15-L39

The messages in "L31" and "L36" are wrong.
(L31) player:showText(npc, ID.text.RESCUE_DRILL + 29, tpz.ki.RESCUE_TRAINING_CERTIFICATE)
(L36) player:showText(npc, ID.text.RESCUE_DRILL + 38)

https://github.com/project-topaz/topaz/blob/4a40c5f10cb7421c578cfa1a6370b483c81fada3/scripts/zones/La_Theine_Plateau/npcs/Galaihaurat.lua#L14-L46

The messages in "L41" are wrong.
(L41) player:showText(npc, ID.text.RESCUE_DRILL + 39)

https://github.com/project-topaz/topaz/blob/4a40c5f10cb7421c578cfa1a6370b483c81fada3/scripts/zones/La_Theine_Plateau/npcs/Equesobillot.lua#L14-L44

The messages in "L41" are wrong.
(L41) player:showText(npc, ID.text.RESCUE_DRILL + 31)

https://github.com/project-topaz/topaz/blob/4a40c5f10cb7421c578cfa1a6370b483c81fada3/scripts/zones/La_Theine_Plateau/npcs/Deaufrain.lua#L14-L44

The messages in "L41" are wrong.
(L41) player:showText(npc, ID.text.RESCUE_DRILL + 32)

https://github.com/project-topaz/topaz/blob/4a40c5f10cb7421c578cfa1a6370b483c81fada3/scripts/zones/La_Theine_Plateau/npcs/Laurisse.lua#L14-L34

The messages in "L31" are wrong.
(L31) player:showText(npc, ID.text.RESCUE_DRILL + 36)

https://github.com/project-topaz/topaz/blob/4a40c5f10cb7421c578cfa1a6370b483c81fada3/scripts/zones/La_Theine_Plateau/npcs/Narvecaint.lua#L14-L34

The messages in "L31" are wrong.
(L31) player:showText(npc, ID.text.RESCUE_DRILL + 37)







