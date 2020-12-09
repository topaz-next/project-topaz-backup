**Labels:**

hold

reviewed



<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 01:51:30_
_Originally opened as: project-topaz/topaz - Issue 1101_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Tested abilities on the deoffset abilities. recreated sql to have offset. more information is in the deoffset list which i have saved for when ever that is pushed to branches. I have tested these in game only issues ive come across are with a few of the animations. May want to create or pull into a testing branch incase my server missed something.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 12, 2020 at 20:29:06_

----

I'm gonna put a hold tag on this until I can sit down and give this a really thorough review. This is good stuff, there's just loads of it. 


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 23:08:33_

----

I spent 30 minutes looking over this PR last night and I barely feel I've scratched the surface lol


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:15:29_

----

Specifically _because_ this is such a massive PR, I would ask you to set up your editor to honour our editorconfig file (https://github.com/project-topaz/topaz/blob/release/.editorconfig).

If you're like me and you edit your Lua in VSCode, `Lua Helper` formats everything nicely (I'm not sure if it's using the editorconfig file, but the output looks good).

This'll handle: spacing out args, newline at end of file, indentation, etc. etc. etc.

I'm not gonna comment on style until you've ran a tool over everything, because I'm a human and I'll let mistakes through!


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 17:01:18_

----

I grabbed a styling tool and ran it over all my changes. Looks good now thanks, I had no idea there was one and it makes life much easier!

I still need to check everywhere for extra sets of parens where they aren't needed.

I checked all of the comments at the top and adjusted where necessary.

I don't really like DNC part either I went thru what was already scripted for flourish n step abilities to get them to do what they should. They test ok in game just still trying to get animations found.


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 23:12:27_

----

I think I took care of all the extra sets of parens where they aren't needed


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 15, 2020 at 06:13:44_

----

Thanks for all your hard work tidying this up! I promise I'll sit down this weekend and in-depth review everything 👍 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 12:21:43_

----

I've sat down and done about 5 partial reviews of this this week, and I think it's totally fair to drop this into a feature branch and into canary since it's 99.9% additive. It isn't going to break anything that wasn't already broken 👍 

Thanks for the gargantuan effort!
