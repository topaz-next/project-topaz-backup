**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:46:17_
_Originally opened as: project-topaz/topaz - Issue 195_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [takhlaq](https://github.com/takhlaq)**
_Sunday Nov 12, 2017 at 23:10 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4224_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 


**_Server Version_** (type `!revision` in game) **:** 
8417380cd6b0b104cee5b9efa404eee09f9305f5

**_Source Branch_** (master/stable) **:** 
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
dsconnect / lobby send the correct id, xiloader receives the uint32 id, something fucky happens and only 2 bytes are written to memory




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:46:18_

----

<a href="https://github.com/NiQ1"><img src="https://avatars3.githubusercontent.com/u/23407689?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [NiQ1](https://github.com/NiQ1)**
_Sunday Nov 03, 2019 at 00:00 GMT_

----

After some checks, seems the client seems to be copying that data somewhere, it doesn't seem to modify the original memory and also if I overwrite the the char id in g_CharacterList with random crap it still sends the original.
Doesn't solve the issue but at least we know where it is _not_.

