**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Saturday Jul 11, 2020 at 20:33:38_
_Originally opened as: project-topaz/topaz - Issue 837_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_:** 

Kreidos's overhaul for zone_weather provided fantastic optimization for the server, but it eliminated ability to customize weather for each zone.  Before the optimizations, customizing weather was a bit of a chore, but still possible.  Can we provide the best of both worlds somehow?




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jul 11, 2020 at 20:39:32_

----

Maybe a weather generator script would help with that?


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Jul 11, 2020 at 20:42:18_

----

Agreed with that, possibly able to package it with topaz or added as a resource?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Jul 11, 2020 at 21:06:14_

----

The previous weather table meant editing 2160 SQL rows if you wanted to change 1 zone's weather. I'd argue it was no more user-friendly before, ha ha.

But the new format is well documented and easy to work with through scripting / python. A weather tool was something I hoped might eventually be made.
