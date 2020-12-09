**Labels:**



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Feb 22, 2020 at 03:22:45_
_Originally opened as: project-topaz/topaz - Issue 373_

----

Command applied:
find . -type f -name "*.lua" | xargs -d '\n' sed -i 's/;//g'

Semicolons are not appropriate in Lua per the style guidelines:
https://github.com/project-topaz/topaz/blob/master/CONTRIBUTING.md

This change is just a style change, no functionality has been changed.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
