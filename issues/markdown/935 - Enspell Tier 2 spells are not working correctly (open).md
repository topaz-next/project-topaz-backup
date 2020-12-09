**Labels:**



<a href="https://github.com/neosatus"><img src="https://avatars2.githubusercontent.com/u/17725395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neosatus](https://github.com/neosatus)**
_Tuesday Aug 11, 2020 at 18:23:29_
_Originally opened as: project-topaz/topaz - Issue 935_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Enspell 2 spells are supposed to only proc on main hand, first attack of the round. All other hits should be capable of proccing other effects. This is currently not the case. The issue lies in the logic in BattleUtils::HandleEnspell where any enspell mod logically prevents all other procs from happening when this should only be the case for Enspell 1 spells.

