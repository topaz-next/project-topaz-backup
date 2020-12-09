**Labels:**

merge ready



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Tuesday Jul 28, 2020 at 23:39:42_
_Originally opened as: project-topaz/topaz - Issue 906_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

These abilities have improper flags, allowing them to be removed in various ways inappropriately:
![image](https://user-images.githubusercontent.com/37684138/88739875-84fb1f80-d0f0-11ea-830e-a0d068a038d8.png)

Thanks to Nireya@GoldSaucer for reporting this.



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 00:18:38_

----

I like how no one noticed Feint was never wearing off over multiple attacks.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 00:31:11_

----

Feint should wear on the [next _successful_ attack](https://ffxiclopedia.fandom.com/wiki/Feint). The behavior was implemented in https://github.com/DarkstarProject/darkstar/pull/5677, but the submitter must have assumed that the lose-on-attack effect flag was 2 instead of 4.

So Feint's effect flag should just be 32 (since I'm not finding evidence it can be dispelled)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 00:18:38_

----

I like how no one noticed Feint was never wearing off over multiple attacks.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 00:31:11_

----

Feint should wear on the [next _successful_ attack](https://ffxiclopedia.fandom.com/wiki/Feint). The behavior was implemented in https://github.com/DarkstarProject/darkstar/pull/5677, but the submitter must have assumed that the lose-on-attack effect flag was 2 instead of 4.

So Feint's effect flag should just be 32 (since I'm not finding evidence it can be dispelled)
