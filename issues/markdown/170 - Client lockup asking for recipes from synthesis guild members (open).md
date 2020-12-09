**Labels:**

bug

crafting



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:11_
_Originally opened as: project-topaz/topaz - Issue 170_

----

<a href="https://github.com/Trystanosaurus"><img src="https://avatars3.githubusercontent.com/u/25745474?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Trystanosaurus](https://github.com/Trystanosaurus)**
_Tuesday Mar 21, 2017 at 07:53 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3815_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30170304_1

**_Server Version_** (type `revision` in game) **:**
65a52ae

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
When asking an NPC in a guild for "information on synthesis materials" the client locks up. You can still move the camera and talk in chat but movement and access to the menu are prevented.

The server log doesn't show any errors that I can see, the last instruction it get when trying to ask about amateur synthesis materials from Anillah in the weavers guild of Windhurst Woods are:
[21/Mar] [08:50:52][1;36m[Debug][0m [1;36mCLIENT Client PERFORMING ACTION 00
[0m[21/Mar] [08:50:53][1;37m[Info][0m parse: 016 | 0157 0156 04 from user: Client 
[21/Mar] [08:52:20][1;37m[Info][0m parse: 058 | 0226 0225 0A from user: Client

