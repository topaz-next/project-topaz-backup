**Labels:**



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Friday Sep 11, 2020 at 14:27:51_
_Originally opened as: project-topaz/topaz - Issue 1096_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

With client version 30200904_2 it appears that text sent from client to server (and potentially other areas) has changed.

while on client version 30200904_2:

- Attempting to create new character, will fail with error 3322 when entering character name.
- Text sent via client will appear to be correct client side e.g. /l hi will echo `<charactername> hi` on local client side. 
- Messages received from the server will appear on other receiving clients as `<charactername> `.

This may extend to other forms of text (/s /p SERVERMESSAGE, etc).


----
<a href="https://github.com/fishytheuppity"><img src="https://avatars3.githubusercontent.com/u/20100339?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [fishytheuppity](https://github.com/fishytheuppity)**
_Sunday Sep 13, 2020 at 15:59:39_

----

I am having a similar issue.  players on the 30200904_2 cannot receive the text of /tell.

Players on a previous version work correctly.
