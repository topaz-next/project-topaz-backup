**Labels:**

approved

reviewed



<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [rude-jerk](https://github.com/rude-jerk)**
_Friday Aug 21, 2020 at 03:50:31_
_Originally opened as: project-topaz/topaz - Issue 990_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 21, 2020 at 11:52:30_

----

these should be updated, not removed. this is also going to conflict with the multiple other prs dealing with mods. Staff needs to sort these out and get a process going where these stay accurate at least on a pr-by-pr basis (conflicts are inevitable, but we shouldn't have inaccurate spares in branch everyone bases PRs on!)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 21, 2020 at 12:09:58_

----

should be battleentity, not charentity. Also unsure if the static cast prevents the possibility that the base entity had a legit pointer but the battleentity still was invalid (we should probably explicitly check the battleentity exists after casting it, this also saves us from checking if it was an NPC someone mistakenlyaimed this at)

Side note: we have mixed of using static cast and dynamic cast all over core, I'm no expert and both seem to work just fine but I thought we're supposed to use dynamic casts for derived classes..and all the other entity types are derived from baseentity ¯\\\_(ツ)\_/¯ can somebody clarify what we -should- be doing and why?


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Friday Aug 21, 2020 at 12:10:18_

----

I removed only the two that are actually not spares. I agree with you that the current situation is not ideal, but I'm not sure why you'd advocate against removing a comment that something that is not a spare is one. I feel like auditing the list in order to find more spares to update two of the three spare comments is outside of the scope of this, though I'm willing to look into it separately. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 21, 2020 at 13:17:07_

----

we maintain 3 spares. we don't remove them we just update the numbers.


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Friday Aug 21, 2020 at 13:17:13_

----

CharEntity was a goof when I rearranged my original bodged test code, whoops.

I think you're probably right on dynamic vs static cast here. Dynamic with a nullptr check should be the safest option. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 21, 2020 at 11:52:30_

----

these should be updated, not removed. this is also going to conflict with the multiple other prs dealing with mods. Staff needs to sort these out and get a process going where these stay accurate at least on a pr-by-pr basis (conflicts are inevitable, but we shouldn't have inaccurate spares in branch everyone bases PRs on!)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 21, 2020 at 12:09:58_

----

should be battleentity, not charentity. Also unsure if the static cast prevents the possibility that the base entity had a legit pointer but the battleentity still was invalid (we should probably explicitly check the battleentity exists after casting it, this also saves us from checking if it was an NPC someone mistakenlyaimed this at)

Side note: we have mixed of using static cast and dynamic cast all over core, I'm no expert and both seem to work just fine but I thought we're supposed to use dynamic casts for derived classes..and all the other entity types are derived from baseentity ¯\\\_(ツ)\_/¯ can somebody clarify what we -should- be doing and why?


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Friday Aug 21, 2020 at 12:10:18_

----

I removed only the two that are actually not spares. I agree with you that the current situation is not ideal, but I'm not sure why you'd advocate against removing a comment that something that is not a spare is one. I feel like auditing the list in order to find more spares to update two of the three spare comments is outside of the scope of this, though I'm willing to look into it separately. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 21, 2020 at 13:17:07_

----

we maintain 3 spares. we don't remove them we just update the numbers.


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Friday Aug 21, 2020 at 13:17:13_

----

CharEntity was a goof when I rearranged my original bodged test code, whoops.

I think you're probably right on dynamic vs static cast here. Dynamic with a nullptr check should be the safest option. 


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Aug 28, 2020 at 03:50:47_

----

looks like this one just needs an additional pass @project-topaz/developer  @project-topaz/reviewer 


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 05:00:11_

----

@rude-jerk do you mind resolving the conflicts in mods and rebasing? got the other ones prior to yours merged in and now there are conflicts. almost done! (and thank you)


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Thursday Sep 10, 2020 at 13:50:42_

----

@59blargedy done!
