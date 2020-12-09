**Labels:**

merge ready



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Thursday May 14, 2020 at 21:44:02_
_Originally opened as: project-topaz/topaz - Issue 621_

----

Game server has long had major issues where it won't exit cleanly for various reasons. Specifically topaz_game will hang permanently and need kill -9 in order to be closed. This was caused when calling zContext.close() on certain versions of zmq.hpp. We shouldn't be reliant on a possibly-buggy local versions wherever it's avoidable, so this bundles in our own known-good v4.3.0 of zmq.hpp. This mostly affected *nix hosts, as we're already bundling a version of zmq.hpp for Win32 which didn't have these issues.

~~While I'm confident this shouldn't pose any problems for Win32 builds, I don't run Windows and haven't been able to test. I'm marking this as draft until someone on Windows platform can confirm it still builds normally. (Or at least until Travis shows green?).~~ Reports from Windows look good.

Fixes #248

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 14, 2020 at 21:48:49_

----

I think Appveyor is currently configured to build for just generic any CPU instead of actual 32bit/64bit debug/release builds (ie: only one build instead of four since the intention is to make sure contributors aren't breaking the build with a stray syntax error).

I'll squeeze in a pull and build myself.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 14, 2020 at 22:05:17_

----

Builds and boots for Win32/Debug, Win32/Release, x64/Debug, and x64/Release


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday May 15, 2020 at 06:27:47_

----

Awesome work @Kreidos 
I'm tired of having to kill the app instead of ctrl+c it lol.

Would be awesome if the app running can have console-like commands (like be able to run search commands on topaz-search, kickout players on topaz-connect/topaz-game)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday May 15, 2020 at 19:42:32_

----

I dug into why the Login server had *its* issues with quitting gracefully and got them rolled into this PR.  On top of the zmq update, it wasn't closing threads/resources properly and the signal handlers were getting stuck in a loop trying to close already-freed resources. These have all been fixed and signal/exit handing should be correctly 'handled' now. 

I rolled that fix in here as it's also dependent on the same zmq update which fixes the game server.

Going forward we should have nice clean exits from all 3 core executables!
