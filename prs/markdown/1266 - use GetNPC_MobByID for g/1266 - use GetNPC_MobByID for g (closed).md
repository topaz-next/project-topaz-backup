**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Oct 06, 2020 at 17:09:46_
_Originally opened as: project-topaz/topaz - Issue 1266_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

We fixed GetMobByID [#642] and GetNPCByID [#668] a while back, so let's use those for getting instanced entities, rather than instance:getEntity + bit.band + objType (which may confuse and deter new contributors)

