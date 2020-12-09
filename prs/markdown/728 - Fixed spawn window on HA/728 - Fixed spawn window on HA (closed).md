**Labels:**



<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Lynnea1320](https://github.com/Lynnea1320)**
_Monday Jun 15, 2020 at 16:46:55_
_Originally opened as: project-topaz/topaz - Issue 728_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixed spawn window (was 1 hr when it should have been 1-3 hrs)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jun 16, 2020 at 21:02:15_

----

I think since this is a lottery spawn then it only needs the minimum time value.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 16, 2020 at 21:46:30_

----

as presently in release branch, it'd just have a 10% shot at popped after the 1hr cooldown passes, which could be 1 spawn cycle or 500 spawn cycles. Some other NMs have a variable randomly chosen window open point, but there's been no decided standard thus far for how to deal with wiki's purely anecdotal accounts of "it took me 6 hours to pop this guy!" and we do not know if an upper limit even exists (if an upper limit does exist, we shoudl be forcing them to spawn next cycle when that window ends)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jun 16, 2020 at 22:21:24_

----

Are there any lottery mobs we do this with? I know we do it with some timed mobs like Fafnir, but imo all lottery mobs should just have their minimum time, everything else is just bad luck.


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Wednesday Jun 17, 2020 at 01:10:21_

----

Okay the wiki showed 1-3 so I was thinking that the spawn window was not
guaranteed after one hour, I thought it was determined by a time in the
window. I wasn't sure how it if this is not how we do it, you can close the
pr

On Tue, Jun 16, 2020, 6:21 PM Corey <notifications@github.com> wrote:

> Are there any lottery mobs we do this with? I know we do it with some
> timed mobs like Fafnir, but imo all lottery mobs should just have their
> minimum time, everything else is just bad luck.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/pull/728#issuecomment-645041532>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AJIPZIHNAEWMODSS4K5ADNLRW7V7DANCNFSM4N6LHWGQ>
> .
>



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jun 17, 2020 at 17:32:23_

----

> 
> 
> Are there any lottery mobs we do this with? I know we do it with some timed mobs like Fafnir, but imo all lottery mobs should just have their minimum time, everything else is just bad luck.

Several, but I think we _should not._
https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/scripts/zones/Beaucedine_Glacier/mobs/Tundra_Tiger.lua#L15
