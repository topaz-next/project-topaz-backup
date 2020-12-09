**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 25, 2020 at 00:47:31_
_Originally opened as: project-topaz/topaz - Issue 886_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 25, 2020 at 14:10:09_

----

Just a heads up, both name columns are completely unused _except_ for instanced entities like pets, trusts, and Battlefield helpers.

The original name column only existed for human readability, and the 2nd one was added not knowing that when instanced entities needed a way to name them that didn't alter the script name (since many of them have named that need sent in the packet that are impossible to use as a file name).

So if desired, we could get rid of the 1st one that has the underscores in the future.
