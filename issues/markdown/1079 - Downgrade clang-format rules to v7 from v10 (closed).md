**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 08, 2020 at 16:08:07_
_Originally opened as: project-topaz/topaz - Issue 1079_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

@Kreidos made a very good point that not everyone has access to bleeding-edge v10 clang-format and the associated rules, so it's safer to stick to an older version.

Tested locally with v10, still works.



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 08, 2020 at 16:18:20_

----

Ah, so thats why v6 is in my mind


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 08, 2020 at 17:35:20_

----

what choo talking about @Kreidos 

18.04 LTS is running v7
```
bananarama@topaz:~$ gcc --version
gcc (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Sep 08, 2020 at 17:37:33_

----

> what choo talking about @Kreidos
> 
> 18.04 LTS is running v7

Sorry, Clang-format, not GCC. :)
https://packages.ubuntu.com/search?suite=default&section=all&arch=any&keywords=clang-format&searchon=names

