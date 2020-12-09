**Labels:**

approved



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Saturday Jun 13, 2020 at 01:44:38_
_Originally opened as: project-topaz/topaz - Issue 718_

----

No more putting it off.

Convention is as follows:
- Spaces replaced with underscore
- Hyphens replaced with underscore. Lua does allow hyphens in table keys, but they need to be defined `['like-this'] =` and can't be defined `like-this =`. This also matches our [current hyphen handling in Core](https://github.com/project-topaz/topaz/blob/release/src/map/spell.h#L502-L508) 
- `'` and `:` were dropped
- Abbreviations were spelled out. We are not currently [consistent](https://github.com/project-topaz/topaz/blob/release/src/map/spell.h#L867) on [this](https://github.com/project-topaz/topaz/blob/release/src/map/spell.h#L888). Consistency on abbreviation with core will have to be addressed later. (Core typically uses the raw spell ID from the spell object as assigned by the DB _anyway_)
- Gaps in IDs are represented by an empty line for visual distinction that there is supposed to be a gap
- I'll want consistency with file names as well in the future, but that's outside the scope of finally getting an enum table in Lua for `trust`, `geo`, and wherever else we've been putting it off

@zach2good 

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 13, 2020 at 15:45:36_

----

if it must be done, at least its got its own home now instead of making magic or status globals astronomical proportions (I has a sadness anytime we have to enum the same IDs in all 3 of core lua and sql)
