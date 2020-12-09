**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:13_
_Originally opened as: project-topaz/topaz - Issue 138_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Saturday Sep 17, 2016 at 03:47 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3371_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [ x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [ x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **Not a client issue**

**_Server Version_** (type `revision` in game) **f8175463415d4964d3deb2492d73a1bd03b548c6**

**_Source Branch_** (master/stable) **Master**

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

Certain mobs are immune to bind, but not shadowbind. Examples include Jailer of Temperance, Tiamat, and Absolute Virtue. Currently on DSP a bind immunity is blanket to both, and the only way to produce retail accurate behavior is to add family exceptions into half a dozen bind spell/ws lua.

Certain mobs are immune to both (Grah and I believe fire/ice elementals) and when the JA is used on such a mob it returns a message indicating it has missed. Currently on DSP it will say it has landed even though it has not.

Shadowbind is more sensitive than regular bind, if any damage is dealt at all (regardless of mob to player level ratio) it will break.

Unlike regular bind, Shadowbind should not be susceptible to erase the way it currently is.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:15_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 20, 2016 at 02:26 GMT_

----

Its amazingly rare, but once in a while the lucky dice roll and shadowbind remains unbroken on a single attack. Just putting that out there so whoever edits the code doesn't think its 100% (just very, very close to it). I'm unsure how best to separate the bind types. A couple ways come to mind: a dummy effect with a separate immunity?  Use a value in the status itself and if its non magical bind, run alternate code in our core bind checks?


