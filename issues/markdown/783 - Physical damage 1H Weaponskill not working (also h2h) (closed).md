**Labels:**



<a href="https://github.com/dleeshus"><img src="https://avatars3.githubusercontent.com/u/67570273?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [dleeshus](https://github.com/dleeshus)**
_Monday Jun 29, 2020 at 03:43:38_
_Originally opened as: project-topaz/topaz - Issue 783_

----

<!-- place 'x' mark between square [x] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
- latest canary build

I was playing around with dagger skillchains and noticed that dancing edge was not doing any damage while cyclone was.
 Shark Bite was also not working.  I say not working because the logs say the weapon skill is readied and then there is no message for miss or 0 damage, it is just blank as if it never happened 

Also tested combo and shoulder tackle which both don't work for H2H.

Shining Strike dealt some damage while Brainshaker does not work for club.

We reverted commit 743dc2f53c5cb146336e69f55e375d5524dcd594 " Add var and binding for isDualWielding + remove presumptuous granting" and the damage is working again.






----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jun 29, 2020 at 04:03:50_

----

Did you recompile core?


----
<a href="https://github.com/dleeshus"><img src="https://avatars3.githubusercontent.com/u/67570273?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [dleeshus](https://github.com/dleeshus)**
_Monday Jun 29, 2020 at 04:51:27_

----

I will check with the server admin but if I had to guess, probably not.

I'll have him recompile and confirm.

Thanks for the prompt reply.


----
<a href="https://github.com/dleeshus"><img src="https://avatars3.githubusercontent.com/u/67570273?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [dleeshus](https://github.com/dleeshus)**
_Monday Jun 29, 2020 at 07:41:41_

----

not recompiling the core was the issue.

sorry and thanks!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jun 30, 2020 at 08:36:46_

----

👍 
