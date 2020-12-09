**Labels:**



<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Thursday Jun 25, 2020 at 22:17:54_
_Originally opened as: project-topaz/topaz - Issue 773_

----

**This is meant for testing purposes only. It is not ready for use. Any server using this code does it at it's own risk.**

Setzor's fishing code, posted in FfxiPrivateServers Discord, adapted for Topaz and with the compile errors solved.
The code needs to be cleaned, but for now it does function.

- Skill ups work
- Zones up to Treasures of Aht Uhrgan have their pools with their fish and items and the correct info. Mostly.

*Disclaimer*
I did get Setzor's permission to PR his code to Topaz, originaly for DSP., so long as proper credit was given.
This was originaly coded by Setzor and used/tested in Eden server by it's players for a year.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

*Related Issues*
#763 #168 


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Friday Jun 26, 2020 at 15:53:02_

----

Dawnbreak is willing to test this as long as @Xaver-DaRed can confirm it's complete enough to run on a server.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jun 26, 2020 at 17:43:22_

----

@Lynnea1320 I'm not sure anyone can confirm that at this point, it's still WIP and if it were ready then this could be marked as non-draft. :)

Thanks for this though, both to Setzor originally and to Xaver for integrating! Look forward to taking a closer dive when I have time.


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Friday Jun 26, 2020 at 18:14:05_

----

Xaver DMed me and said it's ready to be tested for the most part, so I
merged it and he's on our server keeping an eye on issues that may arise.

On Fri, Jun 26, 2020 at 1:43 PM Kreidos <notifications@github.com> wrote:

> @Lynnea1320 <https://github.com/Lynnea1320> I'm not sure anyone can
> confirm that at this point, it's very much still WIP and if it were ready
> then this could be marked as non-draft. :)
>
> Thanks for this though, both to Setzor originally and to Xaver for
> integrating! Look forward to taking a closer dive when I have time.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/pull/773#issuecomment-650309931>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AJIPZIHJS5CLXIOHOMP7SYDRYTM4RANCNFSM4OIZGQWA>
> .
>



----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Friday Jun 26, 2020 at 18:47:16_

----

the act of fishing and any of its possible outcomes dont seem to make anything explode.
regarding other fishing related activities, i dont think the fishing guild is ready. havent tested that far yet


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jun 27, 2020 at 09:04:11_

----

Can remove the 2010-2015 DSP copyright from the _new_ source files too, as Setzor has sole copyright on the files (until we modify it). GPL3 boilerplate should remain.


----
<a href="https://github.com/Arklus"><img src="https://avatars1.githubusercontent.com/u/61334622?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Arklus](https://github.com/Arklus)**
_Sunday Jul 12, 2020 at 04:08:57_

----

Why wont this compile with linux 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Jul 12, 2020 at 04:18:02_

----

You'll have to be more specific, @Arklus. It seems to compile just fine on both my systems. (Debian 10 GCC 8.3 / Debian 9 GCC 7.4)


----
<a href="https://github.com/Arklus"><img src="https://avatars1.githubusercontent.com/u/61334622?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Arklus](https://github.com/Arklus)**
_Sunday Jul 12, 2020 at 04:46:49_

----

Clearly this thing isnt completely not working on my server it crashes my client when fishing . and my rod was missing 



----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Tuesday Jul 14, 2020 at 23:56:30_

----

As discussed in discord, whatever issue you had doesnt have to do with this code concretely. Lockstyle mechanics need to be revised though.

Also, to all the ppl pulling this PR, it would be helpfull if you provided feedback on it, so we can get this fixed, cleaned and ready.


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Monday Aug 24, 2020 at 08:39:21_

----

Setzor donated an updated version of his fishing system, making this one obsolete.
I will PR it soon, once its ready.
Im closing this PR in the meantime.
