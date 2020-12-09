**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Mar 27, 2020 at 09:20:31_
_Originally opened as: project-topaz/topaz - Issue 445_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Purely selfishly, I'm fighting with this file all the time while I'm switching branches, rebasing, merging etc. So moving the default into `conf/default`, updating core to look for it in `conf` and adding an entry for it in the `.gitignore` for `conf`

Also, historically a file that people new to the project, or git, try to submit with their PRs


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 27, 2020 at 21:01:11_

----

@ibm2431 I _want_ to say whatever reason I had for putting it where I did is no longer valid. But I don't remember. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 27, 2020 at 21:02:49_

----

only thing that will be annoying about this is we'll have to manually update our file to reflect version updates.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 27, 2020 at 21:06:13_

----

request: lets rename it to a proper conf since its going subfolder there now, and make sure the core defaults to allow all versions in the event the file isn't found. (I do not know the current default behavior, it was changed more than once since created)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Mar 27, 2020 at 21:18:18_

----

Good point on the rename.

Do we want to change the default ver_lock to 2? (In the file itself, also agreed with Teo for 2 default for instances where file isn't found)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 27, 2020 at 21:25:17_

----

I only mean if the core doesn't see a file -at all- and not the default value in the file itself. A standard behavior for it like the other confs have.  The in file value (or even the default behavior for no file found) being 2 would make sense - already have warnings for players with a client newer than their server.

```
#0 - disabled (every version allowed)
#1 - enabled - strict (only exact CLIENT_VER allowed, default)
#2 - enabled - greater than or equal  (matching or greater than CLIENT_VER allowed)
VER_LOCK: 1
```
I just don't want file missing to be "1" because that will be annoying when I forget to copy it for quick testing a pr
