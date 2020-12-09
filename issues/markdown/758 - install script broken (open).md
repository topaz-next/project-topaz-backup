**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Monday Jun 22, 2020 at 21:40:08_
_Originally opened as: project-topaz/topaz - Issue 758_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

This script will install Project Topaz.
Supported Operating Systems: Debian, Ubuntu, Raspbian

1. Install Topaz & Dependencies
2. Update Configurations Only
3. Restart Topaz Server
4. Shutdown Topaz Server & Disable Auto Start
5. Start Topaz Server & Enable Auto Start
6. Exit

topaz_install_script.sh: 27: read: Illegal option -n
topaz_install_script.sh: 28: [: unexpected operator

topaz_install_script.sh: 143: [: unexpected operator
topaz_install_script.sh: 143: [: unexpected operator
topaz_install_script.sh: 163: [: unexpected operator
topaz_install_script.sh: 163: [: unexpected operator
topaz_install_script.sh: 168: [: unexpected operator
topaz_install_script.sh: 176: [: unexpected operator
topaz_install_script.sh: 176: [: unexpected operator

Exiting



bash --version
GNU bash, version 4.4.20(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.





----
<a href="https://github.com/dynisor"><img src="https://avatars1.githubusercontent.com/u/4257244?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [dynisor](https://github.com/dynisor)**
_Thursday Jul 02, 2020 at 07:58:23_

----

`read -n` is a bash extension. Did you perhaps run `sh topaz_install_script.sh`?

Try:
```
chmod +x topaz_install_script.sh
./topaz_install_script.sh
```

or:
```
sudo bash topaz_install_script.sh
```
