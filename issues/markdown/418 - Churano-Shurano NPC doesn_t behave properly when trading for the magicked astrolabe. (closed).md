**Labels:**

bug



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Mar 12, 2020 at 21:38:57_
_Originally opened as: project-topaz/topaz - Issue 418_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Talk to Churano-Shurano without the magicked astrolabe key item in your inventory, and your char var "Astrolabe" == 0.  He will ask you if you want to buy it for 10k, if you select yes, nothing happens.  If you talk to him again, he gives the same event (it should be a diff one with diff dialogue), and may or may not sell the astrolabe to you correctly.  The current script doesn't clean up its unused char var, "Astrolabe", after the trade is completed either.
