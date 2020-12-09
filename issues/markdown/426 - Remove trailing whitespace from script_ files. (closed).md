**Labels:**

merge ready



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Mar 14, 2020 at 23:32:50_
_Originally opened as: project-topaz/topaz - Issue 426_

----

Commands used (on Mac):
```
  export LC_CTYPE=C
  export LANG=C
  find . -not \( -name .svn -prune -o -name .git -prune \) -type f -print0 | xargs -0 sed -i '' -E "s/[[:space:]]*$//"
```
The script  also adds a newline to the end of the files where one is missing. This isn't strictly needed, but it seems reasonable since it's the POSIX standard:
https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206

> 3.206 Line
> A sequence of zero or more non- <newline> characters plus a terminating <newline> character.

This will also keep future diffs cleaner since some tools add the newline automatically.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 18, 2020 at 21:35:21_

----

Good to know. This one was pretty straightforward so fortunately not too bad.

But I'll keep that in mind going forward for any bulk changes.
