**Labels:**



<a href="https://github.com/CLSIO"><img src="https://avatars3.githubusercontent.com/u/48628726?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [CLSIO](https://github.com/CLSIO)**
_Tuesday Jul 14, 2020 at 07:16:49_
_Originally opened as: project-topaz/topaz - Issue 847_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

When on multi server setup party members do not show up in party list between different servers. Only shows correctly for party leader. 

This seems to only be an issue on canary, release appears to work fine so maybe issue with trust implementation. 


----
<a href="https://github.com/CLSIO"><img src="https://avatars3.githubusercontent.com/u/48628726?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [CLSIO](https://github.com/CLSIO)**
_Tuesday Jul 14, 2020 at 18:38:27_

----

Not sure where this issue is in party.cpp but replacing party.cpp/.h in canary with the party.cpp/.h in release this issue goes away.  Right now we have trusts disabled so this is our solution for now. 


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Wednesday Jul 15, 2020 at 11:39:15_

----

![Party cpp](https://user-images.githubusercontent.com/60053999/87540736-777d7880-c6a0-11ea-9b67-e2bd23c2de2b.png)

Something tells me that this is the problem, considering party leader doesnt have this problem
