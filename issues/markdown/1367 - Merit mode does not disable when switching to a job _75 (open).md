**Labels:**



<a href="https://github.com/GanimanSwift"><img src="https://avatars1.githubusercontent.com/u/13344227?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [GanimanSwift](https://github.com/GanimanSwift)**
_Thursday Oct 15, 2020 at 20:21:50_
_Originally opened as: project-topaz/topaz - Issue 1367_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

On a level 75 capped server, switch to a level 75 job. Go to the Status menu and enable merit mode. Switch to a job under level 75. Check status. Job is "locked" and colored blue. XP is greyed out.

I have not tested if you actually earn merit points with a job under level 75, but you cannot switch modes back to exp without first switching back to a level 75 job.

Edit: This effect persists after zoning.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 15, 2020 at 20:43:46_

----

does it persist even after your newly set job changes zones? I ask because my hunch is we fail to send an update packet or something silly like that


----
<a href="https://github.com/GanimanSwift"><img src="https://avatars1.githubusercontent.com/u/13344227?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [GanimanSwift](https://github.com/GanimanSwift)**
_Thursday Oct 15, 2020 at 20:57:49_

----

> does it persist even after your newly set job changes zones? I ask because my hunch is we fail to send an update packet or something silly like that

Yes, it persists after zoning. Forgot to mention, had confirmed before submitting.
