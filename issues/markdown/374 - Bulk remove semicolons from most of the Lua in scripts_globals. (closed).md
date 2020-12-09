**Labels:**



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Feb 22, 2020 at 04:14:42_
_Originally opened as: project-topaz/topaz - Issue 374_

----

Command applied:
find . -type f -name "*.lua" | xargs -d '\n' sed -i 's/;//g'

Semicolons are not appropriate in Lua per the style guidelines:
https://github.com/project-topaz/topaz/blob/master/CONTRIBUTING.md

NOTE: I skipped /globals/weaponskills for now, since many files have
a valid use of semicolons (for multiple statements on the same line).
I'll audit those separately.

This change is just a style change, no functionality has been changed.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Feb 22, 2020 at 04:40:31_

----

PR is reporting an error on continuous build from Travis. Will investigate.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Feb 22, 2020 at 05:02:45_

----

The issue has been addressed. Turns out tables need a delimiter.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Feb 22, 2020 at 05:05:00_

----

Generally a comma is used instead of a semicolon for table delimiters


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Feb 22, 2020 at 05:09:55_

----

Is that preferable? I can update it to use a comma instead.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Feb 22, 2020 at 05:13:15_

----

I updated it to use commas. It's a bit strange, the odd numbered indexes are ever needed. Despite being a combination of inner tables and integers, only the inner table are used -- simulating a 2D array.

But idk how to test Limbus because I'm a FFXI noob, so I didn't wanna mess with it within this PR.

https://github.com/project-topaz/topaz/blob/2943fab983cc1457ce75f15dd9dca9d3bfa21b05/scripts/globals/limbus.lua#L65-L75

Could easily be:

```
MIMICPOSITION =
{
    {-363, 0, -282};
    {-359, 0, -277};
    {-326, 0, -301};
    {-331, 0, -330};
    {-340, 0, -330};
    {-345, 0, -311};
    {-339, 0, -300};
    {-335, 0, -281};
}
```

Although then you'd need to update the index values here:
https://github.com/project-topaz/topaz/blob/2943fab983cc1457ce75f15dd9dca9d3bfa21b05/scripts/globals/limbus.lua#L603-L616


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 22, 2020 at 20:59:41_

----

best would be not to touch limbus as its a work in progress, any changes to that area can cause un needed rebasing, merge conflicts


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 03:29:19_

----

In that case I'll just revert that file. Its only a few lines and can easily be cleaned up later once the limbus.lua is more finalized. 


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 03:39:44_

----

Amended the commit to drop the changes to limbus.lua.
