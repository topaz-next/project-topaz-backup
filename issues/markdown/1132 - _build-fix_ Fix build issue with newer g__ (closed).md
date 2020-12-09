**Labels:**

approved

reviewed



<a href="https://github.com/pacampbell"><img src="https://avatars3.githubusercontent.com/u/3587094?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [pacampbell](https://github.com/pacampbell)**
_Sunday Sep 13, 2020 at 23:14:33_
_Originally opened as: project-topaz/topaz - Issue 1132_

----

Fixed an issue where world_pass.gcc failed to compile
on newer gcc due to -Werror=format-truncation=.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 14, 2020 at 05:12:21_

----

Hello @pacampbell! 
Welcome to the project! Our build system is a horrible Frankenstein's monster of scripts and legacy voodoo, so sadly you'll have to include `fmt` using a relative path from where you're including it. We also have our own assert as `TPZ_DEBUG_BREAK_IF`, please swap to using that.

Otherwise looks sane, thanks for the contribution!


----
<a href="https://github.com/pacampbell"><img src="https://avatars3.githubusercontent.com/u/3587094?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [pacampbell](https://github.com/pacampbell)**
_Monday Sep 14, 2020 at 05:44:57_

----

Hopefully got it right this time. Make sure to double check the assert condition. I also added a memset to the data before copying the string into it. It's unclear to me currently if this memory would always be zeroed so I was being safe.


----
<a href="https://github.com/pacampbell"><img src="https://avatars3.githubusercontent.com/u/3587094?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [pacampbell](https://github.com/pacampbell)**
_Monday Sep 14, 2020 at 05:50:14_

----

> As a side note, there is no need to assume uint32_MAX is 10 digit, it is: 4294967295

I feel kinda dirty about this, even though it should be true on all sane platforms. I just wanted to be explicit for someone looking at the code later since it took me a few moments to figure out what was happening here. I can remove the comment if you think it was redundant.

> EDIT: Also, don't worry about the clang-format check, it's been playing up recently :(

Ah, I was wondering what was happening with this. I ran the command a few times and it wasn't changing anything :)

