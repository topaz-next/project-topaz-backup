**Labels:**

improvement



<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [59blargedy](https://github.com/59blargedy)**
_Wednesday May 06, 2020 at 17:41:59_
_Originally opened as: project-topaz/topaz - Issue 589_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated
Need some way of cleanly applying temporary resistances and removing them. can currently addmobmod PIERCERES etc, but then need calls to remove.

reference: https://github.com/project-topaz/topaz/pull/561#discussion_r420708141
this could also affect mobs like Jailer of Temperance, Gladiatoral Weapons in Die By the Sword BCNM, wamouracampa, to name a few.  





----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday May 06, 2020 at 20:43:09_

----

yeah the current way we could do this in script result sin a lot of repeated messy code..Could def use utils function to clean it up and bake in handling of related things.

Edit: _if anyone doubts the pain of doing it with current methods, I have a custom mob that rotates weaknesses and winds up many many lines long you can witness and then regret looking at ^^; table/array inputs for what resistances to manipulate would be super._
