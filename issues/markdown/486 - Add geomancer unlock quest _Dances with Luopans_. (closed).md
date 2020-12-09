**Labels:**

merge ready



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Apr 11, 2020 at 06:18:18_
_Originally opened as: project-topaz/topaz - Issue 486_

----

The only TODO left here is to handle the cutscene 37
which happens after you have geomancer unlocked. It
allows the user to re-buy the Matre Bell. It needs
more research to determine how to handle the
`player:updateEvent(....)` during `onEventUpdate`.

Also I only implemented one of the /heal areas. I
found conflicting documentation, but seems like
you can rest at any of the Ergon Locus locations.
However I only implemented the one commonly used
in the unlock quest and mentioned in most of the
online wiki guides.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Apr 11, 2020 at 06:19:35_

----

I wasn't sure the best way to handle the resting. I feel a bit icky about pulling quest info into `scripts/globals/effects/healing.lua`, but it seemed to be the only place I could find to track the user while they are using `/heal`.

I'm open to other suggestions.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Apr 11, 2020 at 07:09:51_

----

Made a few tweaks and re-tested everything.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 01:01:52_

----

Resolved a handful of comments. Will look into applying the changes sent over by @Omnione next.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 04:24:07_

----

Applied the timer idea and added the other 2 areas that you can rest within.

Did some thorough testing and the timer idea works great.

The only thing I wish we had was the ability to keep a reference to the timer and cancel it immediately if the rest state ends. As of now it continues and just acts like a no-op on execution in that case.

But the core doesn't seem to support this and I didn't have time to look into adding that for a small optimization. 


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Apr 21, 2020 at 17:06:07_

----

https://youtu.be/3NL-h8TGReM
https://www.dropbox.com/s/4nqthprth9wdaxq/matre%20bell.rar?dl=0
for matre bell dropping and reacquisition


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Apr 21, 2020 at 18:12:19_

----

Thank you for this! Very helpful. I'll update the pull request to handle this case as well.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Apr 22, 2020 at 04:58:41_

----

Adjusted the final comment. And added logic for the matre bell repurchase.

I thoroughly tested out every edge case I could think of. So hopefully it's pretty bug-free now.

Please take another look.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Apr 23, 2020 at 03:04:49_

----

Updated the params and rewrote the logic to be more straightforward for `onEventUpdate`.
