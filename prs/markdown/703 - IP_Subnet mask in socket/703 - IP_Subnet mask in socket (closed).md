**Labels:**

approved



<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ShelbyZ](https://github.com/ShelbyZ)**
_Wednesday Jun 10, 2020 at 02:59:02_
_Originally opened as: project-topaz/topaz - Issue 703_

----

- Fixes #686
- ntohl changes from network byte order to host byte order
- Mask was swapped, IP was not swapped

Test on win/nix, but not for every mask combination

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


