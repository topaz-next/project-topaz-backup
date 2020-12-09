**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 08, 2020 at 17:40:15_
_Originally opened as: project-topaz/topaz - Issue 931_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Long ago, past me had to do this : 
https://github.com/project-topaz/topaz/blob/37f47a657bd3a2fe67790a3eab68543942af0c01/src/map/utils/battleutils.cpp#L4427

I know for a fact my work is not retail accurate there. Let us not go into detail as to why I knowingly did non accurate things, other than to say an argument was had and the man in charge said to do it like this, so I did.

Retails bind break rates are not known and I highly doubt it is as simple every mob in the game having one rate that is only level corrected and nothing else. I dunno what. Someone will need to gather some retail data. And by some I mean a lot. And I do not even know in what way or by how much the correction should be, level per level.

More important than the rate being accurate is the possibility* that some things do not even run the check at all. This is quickly and easily fixed but highly exploitable, so I am asking the project lead before I start saying where.


*Person who brought it to my ATTN then told me they weren't sure how old the server was, after I posted this.
