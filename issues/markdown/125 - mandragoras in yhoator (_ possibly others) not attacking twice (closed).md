**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:33:07_
_Originally opened as: project-topaz/topaz - Issue 125_

----

<a href="https://github.com/eraffxi"><img src="https://avatars1.githubusercontent.com/u/6442410?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [eraffxi](https://github.com/eraffxi)**
_Wednesday Jun 01, 2016 at 20:21 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3207_

----

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30160427_0

**_Server Version_** (type `revision` in game) **:**

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
fight one




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:33:08_

----

<a href="https://github.com/HeavensSword"><img src="https://avatars0.githubusercontent.com/u/12627703?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [HeavensSword](https://github.com/HeavensSword)**
_Thursday Jul 21, 2016 at 00:38 GMT_

----

Did some quick debugging; these particular mob's main hand is set to Scythe instead of H2H.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:33:09_

----

<a href="https://github.com/HeavensSword"><img src="https://avatars0.githubusercontent.com/u/12627703?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [HeavensSword](https://github.com/HeavensSword)**
_Thursday Jul 21, 2016 at 05:44 GMT_

----

I notice all the mandragora are set to scythe. iirc they were set to that because of delay issues?

I set the mainhand of the Yhoator mandy to H2H in the sql and left the cmbDelay alone; everything seems fine to me.
Used : [https://www.youtube.com/watch?v=qFqktcqvIuE](https://www.youtube.com/watch?v=qFqktcqvIuE) as a reference for attack speed.

I can update the mandys to H2H if there aren't other issues i'm not aware of.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:33:10_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Wednesday Jul 27, 2016 at 18:54 GMT_

----

This issue fixed? HeavensSword 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:33:11_

----

<a href="https://github.com/HeavensSword"><img src="https://avatars0.githubusercontent.com/u/12627703?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [HeavensSword](https://github.com/HeavensSword)**
_Wednesday Jul 27, 2016 at 19:07 GMT_

----

Not yet; I'll take care of it tonight. I was holding off in case there was any reasons against me making the changes. Sounds like there are none. :)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:33:12_

----

<a href="https://github.com/HeavensSword"><img src="https://avatars0.githubusercontent.com/u/12627703?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [HeavensSword](https://github.com/HeavensSword)**
_Thursday Jul 28, 2016 at 17:51 GMT_

----

Update:
I think I'm going to make this a part of a larger Mandragora Family fix. Going through the DB, I'm seeing other issues like incorrect jobs and missing spell lists for certain NMs in the mandragora family.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:33:13_

----

<a href="https://github.com/abriasffxi"><img src="https://avatars1.githubusercontent.com/u/20671885?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [abriasffxi](https://github.com/abriasffxi)**
_Thursday Oct 06, 2016 at 18:08 GMT_

----

Any luck completing that?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:33:15_

----

<a href="https://github.com/HeavensSword"><img src="https://avatars0.githubusercontent.com/u/12627703?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [HeavensSword](https://github.com/HeavensSword)**
_Thursday Oct 06, 2016 at 18:28 GMT_

----

Sorry I've been very busy irl and had to take a break from darkstar
updates. I may not get to it in a few more weeks.

On Oct 6, 2016 12:08 PM, "Chuck" notificationsgithub.com wrote:

> Any luck completing that?
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> github/DarkstarProject/darkstar - Issue 3207Darkstar Issue issuecomment-252042909,
> or mute the thread
> github/notifications/unsubscribe-auth/AMCu9_yDhgO-4oD_VyIXG4XompLyqIKtks5qxTkMgaJpZM4Ir8A8
> .




----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Monday Mar 09, 2020 at 20:48:27_

----

Hello. Unable to reproduce this particular issue with said mobs on mast as of 03/09/2020 **but** it's related to some extent to https://github.com/project-topaz/topaz/issues/9, https://github.com/project-topaz/topaz/issues/94 and https://github.com/project-topaz/topaz/issues/134. Feel free to reopen an issue if this persists. Thank you.
