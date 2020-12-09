**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Monday Aug 17, 2020 at 13:07:47_
_Originally opened as: project-topaz/topaz - Issue 965_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I got caught out a couple of weeks ago because I was working exclusively with 32bit Windows and a casting warning-as-error snuck in on the 64-bit build. I did a little digging and Travis's support for Windows and multi-OS builds is a little lacking, so I split everything out into GitHub Workflows.

**Note:**
I wasn't paying enough attention to notice that Appveyor covers the gap I got caught by, but then, why didn't it? Hmmm.
Still probably better to have all CI in one place

**Successful run:**
https://github.com/zach2good/topaz/runs/1041773878
![image](https://user-images.githubusercontent.com/1389729/91578155-79e71980-e952-11ea-9b08-6bebf95256f8.png)

**C++ Formatting Error**
![image](https://user-images.githubusercontent.com/1389729/91578271-9aaf6f00-e952-11ea-83a4-d5fbe2efeb38.png)

![image](https://user-images.githubusercontent.com/1389729/90402631-690feb80-e0a8-11ea-8f33-57049077bcff.png)
![image](https://user-images.githubusercontent.com/1389729/90404517-2b609200-e0ab-11ea-854a-0668cfe452c9.png)



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 05, 2020 at 14:22:47_

----

If someone likes this I'll merge it.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 05, 2020 at 14:23:02_

----

Say no more fam.
