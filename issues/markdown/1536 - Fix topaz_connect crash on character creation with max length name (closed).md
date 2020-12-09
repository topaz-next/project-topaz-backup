**Labels:**



<a href="https://github.com/claywar"><img src="https://avatars1.githubusercontent.com/u/12447174?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [claywar](https://github.com/claywar)**
_Saturday Nov 28, 2020 at 16:34:30_
_Originally opened as: project-topaz/topaz - Issue 1536_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Client allows for character creation with up to a 15 character name.  Issue occurred due to limiting length of some char arrays being limited to 15 characters, and therefore not containing null termination, which would result in a connect server crash on character creation.

Fix was tested against min-length and max-length character creation and load from previously-created; in addition, basic function for interaction (AH, trade, combat, and communication channels).
