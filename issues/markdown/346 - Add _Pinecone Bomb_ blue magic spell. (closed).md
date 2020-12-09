**Labels:**

focus

merge ready

research needed



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 16, 2020 at 08:50:17_
_Originally opened as: project-topaz/topaz - Issue 346_

----

Now that the order of operations has been cleaned up for spells,
Pinecone Bomb can be properly implemented. It does damage to the mob
(which may wake it up from a previous slept state), but then can reapply
sleep as described here: https://ffxiclopedia.fandom.com/wiki/Pinecone_Bomb



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 10:25:25_

----

Hello, @mrhappyasthma! Thank you for contributing to Project Topaz!

So that we don't use our parent project's brand, we've changed some function and table names to reflect adopting a new brand. I remember seeing that this PR was started prior to Topaz and originally submitted to our parent project - I took the liberty of updating these references for you; you don't need to sweat over them!

Although, I realize after I submitted the push that I should have asked first to make sure I didn't step on your toes. I'm sorry if I did! My intent was to make your contribution experience as painless as possible! 😅 

That said, I haven't had the chance to take a look at the code yet. We try to be relatively swift with reviews though, so I look forward to working with you soon!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 16, 2020 at 23:25:12_

----

No worries. I look forward to your review.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 09:30:01_

----

Tagging #269 


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 15:52:57_

----

Question: Do you want me squashing these commits? Or do the mergers handle that for this repo?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 16:03:37_

----

We can go ahead and squash for you~!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 16:04:43_

----

Awesome. Just wanted to verify! :)


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:50:10_

----

Rebased and closed out some of the outstanding comments.

This PR is still waiting on a more accurate TP-based sleep duration.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 04:01:59_

----

Corrected the attackType to be `RANGED`.

Still need to do a bit of research for the TP-based sleep. Been crazy with work and will be having more travel over the coming weeks. Whenever I can find some downtime I can plot some of the values from the captures and find a reasonable equation.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 21, 2020 at 14:24:19_

----

Compiled a spreadsheet from the two captures in which Chain Affinity was used:
[Pinecone-Bomb.zip](https://github.com/project-topaz/topaz/files/4363102/Pinecone-Bomb.zip)



----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Mar 28, 2020 at 02:29:07_

----

BTW I still haven't forgotten about this. Just a crazy time we live in these days... Whenever I get some time I'll dig into those spreadsheets and compile any other data that is needed.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Apr 09, 2020 at 20:34:03_

----

Wow thanks for digging so deeply into this. I know my contributions have been sporadic and irregular. So I really appreciate you doing all this work on behalf of this PR.
