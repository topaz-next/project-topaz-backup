**Labels:**

merge ready



<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [InoUno](https://github.com/InoUno)**
_Thursday Jun 18, 2020 at 11:21:14_
_Originally opened as: project-topaz/topaz - Issue 744_

----

This PR fixes a bug where BRDs are able to keep up many more than the allowed max amount of songs.

With the current implementation, if BRD A overwrites a song of the same tier/type from BRD B, the check for maximum amount of songs allowed for BRD A is never performed, since it just overwrites it immediately.
This leaves BRD B free to sing a new song, since he doesn't own that active song anymore. Rinse and repeat, and you can get as many songs active as the casting time allows with just 2 BRDs.

Example:
```
A sings March1
A sings March2
B sings Minuet1
B sings Minuet2
A overwrites Minuet1
A overwrites Minuet2
[at this point there's 4 songs up, all owned by BRD A]
B sings Madrigal1
B sings Madrigal2
[at this point there's 6 songs up between 2 BRDs]
[rinse and repeat, with BRD A overwriting songs and BRD B singing new songs]
```

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


