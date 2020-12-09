**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday May 25, 2020 at 22:01:12_
_Originally opened as: project-topaz/topaz - Issue 654_

----

… Added `charset` option to editorconfig to force saving as this format in the future so JP contributors can actually build.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

A few cases if trimmed whitespace happened as a result of touching all src files, and a couple edited comments when I had to fix some Cyrillic (my converted trashed the Russian comments, some of which I simply put back - if it doesn't make sense after google translate, I leave it alone)
```patch
- return std::min<uint8>(num, 8); // не более восьми ударов за одну атаку
+ return std::min<uint8>(num, 8); // No more than eight hits per attack
```
