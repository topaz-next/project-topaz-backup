**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Sep 30, 2020 at 01:16:27_
_Originally opened as: project-topaz/topaz - Issue 1218_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

https://github.com/project-topaz/topaz/blob/c52431e2c48516954aa2f5ebbb331238f43cc3d8/scripts/zones/West_Ronfaure/npcs/Phairet.lua#L11-L37

Wrong message (L29)
The Right Message
player:startEvent(127, 4367)

If you trade anything other than Supplies Order
player:startEvent(117)

If you lose Batagreens, you should be able to get Batagreens by trading 50 gil to Phairet.
