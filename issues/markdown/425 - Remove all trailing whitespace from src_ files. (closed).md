**Labels:**

merge ready



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Mar 14, 2020 at 23:20:02_
_Originally opened as: project-topaz/topaz - Issue 425_

----

This is a preemptive step for converting all tabs to spaces.

Commands used (on Mac):
```
  export LC_CTYPE=C
  export LANG=C
  find . -not \( -name .svn -prune -o -name .git -prune \) -type f -print0 | xargs -0 sed -i '' -E "s/[[:space:]]*$//"
```
