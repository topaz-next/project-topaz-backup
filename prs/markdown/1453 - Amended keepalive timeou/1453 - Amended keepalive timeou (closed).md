**Labels:**



<a href="https://github.com/Bizzle-Dapp"><img src="https://avatars0.githubusercontent.com/u/36421291?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Bizzle-Dapp](https://github.com/Bizzle-Dapp)**
_Thursday Oct 29, 2020 at 15:26:18_
_Originally opened as: project-topaz/topaz - Issue 1453_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR will go unnoticed by all except those that use a separate machine for the DB and Server Client. 
From my testing (MariaDB on AWS, Server Client on local machine at home) I've found that DB's hosted separately will sever TCP/IP read and writes if they are silent for more than 2 hours. 

This change should mean Server Client and DB will work "Out of the box" when hosted on separate machines. 



----
<a href="https://github.com/Bizzle-Dapp"><img src="https://avatars0.githubusercontent.com/u/36421291?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Bizzle-Dapp](https://github.com/Bizzle-Dapp)**
_Thursday Oct 29, 2020 at 15:32:41_

----

Typo in PR name, Its from 8 hours to 2 hours, not 2 minutes. Apologies! 🤦‍♂️


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 18:29:56_

----

> 
> 
> Typo in PR name, Its from 8 hours to 2 hours, not 2 minutes. Apologies! man_facepalming

theres an edit button :)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 29, 2020 at 18:30:18_

----

I would have been fine with the title being wrong, but it's also in the commit message, please change it 🙏 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 18:30:22_

----

for the commit message you'd need to use git amend


----
<a href="https://github.com/Bizzle-Dapp"><img src="https://avatars0.githubusercontent.com/u/36421291?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Bizzle-Dapp](https://github.com/Bizzle-Dapp)**
_Thursday Oct 29, 2020 at 19:09:13_

----

Haha, I've sorted it. Commit message was automatically used as PR title


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 30, 2020 at 04:52:06_

----

We were aiming for you to amend and overwrite your original commit, instead of adding 2 over the top of it ;)
I've taken your first commit as a patch and pushed it into release: https://github.com/project-topaz/topaz/commit/8573c78f9a67744da0893feeaef9ef9cca9c7d66
