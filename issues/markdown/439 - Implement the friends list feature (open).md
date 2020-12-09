**Labels:**

feature

research needed



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 25, 2020 at 03:26:16_
_Originally opened as: project-topaz/topaz - Issue 439_

----

We should be able to implement a custom implementation of the friends list, but probably needs some packet sniffing.

The request for the `Communication > Friend List > To List` option appears to be packet 119 `SmallPacket0x119`.

The `/befriend <name>` command issues a search. 

`/search friend` also issues a search.

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 25, 2020 at 11:44:59_

----

similarly the gm call feature on retail is just basically forming an email via packet. we could custom that too.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Nov 10, 2020 at 07:03:20_

----

I wouldn't be against filling out the packet information for these (GM Call and FList) and maybe forwarding the call out into a utils file of sorts, with the functionality stubbed out. Then if people want to add a backend, discord hooks etc. then that's on them. 

