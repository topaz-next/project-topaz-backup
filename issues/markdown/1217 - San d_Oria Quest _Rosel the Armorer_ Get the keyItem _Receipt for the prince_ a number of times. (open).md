**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Sep 29, 2020 at 21:22:21_
_Originally opened as: project-topaz/topaz - Issue 1217_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

https://github.com/project-topaz/topaz/blob/2bbdf369d86335c4610bb9b2587b31ebd7da11ec/scripts/zones/Southern_San_dOria/npcs/Rosel.lua#L19-L56

The same event ID "524" is called before and after the receipt of the quest (L25, L30).

As a result, in L46, Get the keyItem "Receipt for the prince" a number of times.




----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Sep 30, 2020 at 00:07:57_

----

Perhaps after receiving the quest.
It would be correct to display the following message.

If the recipient is a Pieuje
player:showText(npc, 7782);


If the the recipient is Trion
player:showText(npc, 7783);

