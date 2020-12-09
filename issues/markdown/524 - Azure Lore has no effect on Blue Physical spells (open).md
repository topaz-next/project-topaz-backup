**Labels:**

bug

focus



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 25, 2020 at 01:26:14_
_Originally opened as: project-topaz/topaz - Issue 524_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**tl;dr:** https://github.com/project-topaz/topaz/blob/release/scripts/globals/bluemagic.lua#L61

**edit (for some reason submitted when I tried to insert line break):**

Currently in various blue magic scripts they [define a "azuretp" field as part of their params](https://github.com/project-topaz/topaz/blob/release/scripts/globals/spells/bluemagic/cannonball.lua#L34). There are currently 38 spells that do so.

This params table is then [sent off to BluePhysicalSpell](https://github.com/project-topaz/topaz/blob/release/scripts/globals/spells/bluemagic/cannonball.lua#L44).

The `azuretp` param is never used. There are no references to it in the [entire Blue Magic global](https://github.com/project-topaz/topaz/blob/release/scripts/globals/bluemagic.lua) except for the comment.

**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated




