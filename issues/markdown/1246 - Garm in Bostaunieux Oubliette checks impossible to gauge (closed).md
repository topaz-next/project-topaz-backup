**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Oct 03, 2020 at 22:48:18_
_Originally opened as: project-topaz/topaz - Issue 1246_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Go to Bostaunieux Oubliette and find any Garm. Check it. See the log.
Should check a difficulty level in relation to players level.
Checks "impossible to gauge".

I tried to simply set the `mobType` flag to `0` (is currently 16) which did not work.
Most mobs that check "incredibly easy prey" do not seem to have this issue, this is the first occurrence of this type I encountered.
Seems the latest commit including this mob was just yesterday 56fa1ac85f822b2816944634469597ea3104838b
Apparently the poolid of the Garm is being constantly changed.
