**Labels:**

exploit



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 09, 2020 at 07:33:57_
_Originally opened as: project-topaz/topaz - Issue 1293_

----

Exact explanation at a later date.

Most servers are already aware of this, and have had a chance to apply this fix. If you're a public server owner who isn't, message zach2good on Discord.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 22, 2020 at 21:04:34_

----

When a player interacts with a Burning Circle, they trigger (or trade to) it. They then select various options to identify which battlefield they want to undertake. This initiates a series of responses between the client and the server in the form of eventUpdates.

When the server "finds" a valid, empty battlefield, it then gives the player - and their party members - the battlefield status with the ID of the battlefield they're about to enter. This status is what allows party members to enter the same battlefield as you.

Unfortunately, the orb used to initiate this process wasn't marked as "used" at this point. It was only marked as used when the client sent the final eventFinish back to the server, saying that the player was done with any animations of entering the battlefield. By preventing this final eventFinish from reaching the server, a player could give their party members the battlefield status without "consuming" the entry item. This would allow their party to enter the BC an infinite number of times on the same orb.
