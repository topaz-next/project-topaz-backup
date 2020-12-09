**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Friday Oct 09, 2020 at 23:24:57_
_Originally opened as: project-topaz/topaz - Issue 1300_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Closes #179

Follow up to #459.  Implements all remaining items I am aware of:

* Kam'lanaut and Eald'narch are now facing the battlefield entrance.
* When using an en-spell TP move, Kam'lanaut will thereafter absorb elemental damage of that element.
* When using a non-en-spell TP move, Kam'lanaut can chain up to three attacks.
* Give Eald'narch bonus EVA and MDEF.

Per convo below,

* Uses en-skills on a timer, which doesn't consume TP.
* When using TP, does not select en-skills.  Instead, can use up to three skills from its remaining list of two moves.

With these items done, I'm turning on the battlefield in bcnm.lua.  I believe this branch can now merge into release.

~~edit: Hold this PR, per additional work in conversation below~~ Ready!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 10, 2020 at 00:29:09_

----

I know this is the Apocalypse Nigh version, and the video below is for the Return to Delkfutt version, but while seeing if the Return Delkfutt version has the multi-WS behavior (it doesn't, but if it did I was curious if it's the same WS 3x or if random 3), I noticed Delkfutt version uses the Blade moves an awful lot for someone who whiffs so often.
<https://www.youtube.com/watch?v=bIMUspfzKeY&t=7m5s>

At first I thought he must have Regain and TPs at 1000, but it's _only_ the elemental blade moves he's spamming while I'm pinging for status effects. He never used Light Blade or Great Wheel until after I started dealing damage, and it looks a little like hitting him didn't cause him to "WS" more often. We seem to have [already implemented this behavior for the Delkfutt version](https://github.com/project-topaz/topaz/blob/release/scripts/zones/Stellar_Fulcrum/mobs/Kamlanaut.lua), but I'm wondering if the Apocalypse Nigh version should have it or not.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Oct 10, 2020 at 01:04:32_

----

Interesting.  In that video, it looks to me like he's using the en-spell move on a set ~20 second timer, regardless of TP.

He probably only uses his TP for Light Blade and Great Wheel.

I'll implement this timer behavior on the Apoc Nigh version, and remove the en-spell TP moves from the skill list for both Apoc Nigh and Return to Delkfutt Tower versions, since they shouldn't be selecting them when using TP.



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 10, 2020 at 01:15:11_

----

Jimmay has a couple captures for Apoc Nigh in the Capture Discord, but it's a little hard to see the action in them and say for certain what the TP behavior is.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Oct 10, 2020 at 01:24:15_

----

I watched a few of them.  Looks like it's still a constant timer between en-spell moves, but a longer interval than the Return to Delkfutt version.  I estimate ~20sec for Delkfutt version, and ~28-30sec for Apoc Nigh version.


----
<a href="https://github.com/ghost"><img src="https://avatars3.githubusercontent.com/u/10137?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ghost](https://github.com/ghost)**
_Saturday Oct 10, 2020 at 03:29:25_

----

Please remove me guys I un subbed like ten times and am still getting
emails from all. Sorry thanks

On Fri, Oct 9, 2020, 7:25 PM wrenffxi <notifications@github.com> wrote:

> *I affirm:*
>
>    - that I agree to Project Topaz's Limited Contributor License Agreement
>    <http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md>, as
>    written on this date
>    - that I've *tested my code* since the last commit in the PR, and will
>    test after any later commits
>
> Follow up to #459 <https://github.com/project-topaz/topaz/pull/459>.
> Implements the all remaining items I am aware of:
>
>    - Kam'lanaut and Eald'narch are now facing the battlefield entrance.
>    - When using an en-spell TP move, Kam'lanaut will thereafter absorb
>    elemental damage of that element.
>    - When using a non-en-spell TP move, Kam'lanaut can chain up to three
>    uses of the TP move.
>    - Give Eald'narch bonus EVA and MDEF.
>
> With these items done, I'm turning on the battlefield in bcnm.lua. I
> believe this branch can then merge into release.
> ------------------------------
> You can view, comment on, or merge this pull request online at:
>
>   https://github.com/project-topaz/topaz/pull/1300
> Commit Summary
>
>    - [apoc nigh] adjust mobs' rotations to face battlefield entrance
>    - Kam'lanaut: absorb element of last en-spell TP move
>    - [apocalypse nigh] Add Kam'Lanaut ability: "Can perform three TP
>    attacks upon reaching 100%+ TP, giving very little rest for healers."
>    - [apocalypse nigh] Eald'narch: Highly evasive, Very high magic defense
>    - Unlock Apocalypse Nigh battlefield by default
>
> File Changes
>
>    - *M* scripts/globals/bcnm.lua
>    <https://github.com/project-topaz/topaz/pull/1300/files#diff-dcf2d879d1e21241f3802bb49c255700>
>    (2)
>    - *M* scripts/zones/Empyreal_Paradox/mobs/Ealdnarche.lua
>    <https://github.com/project-topaz/topaz/pull/1300/files#diff-fb491cf626f04b67893fa762300c3ca6>
>    (9)
>    - *M* scripts/zones/Empyreal_Paradox/mobs/Kamlanaut.lua
>    <https://github.com/project-topaz/topaz/pull/1300/files#diff-1e55e9e2e711e8570febc72dfdcddd5a>
>    (59)
>    - *M* sql/mob_spawn_points.sql
>    <https://github.com/project-topaz/topaz/pull/1300/files#diff-8bf2abcc09265d742efa1975527d09f8>
>    (12)
>
> Patch Links:
>
>    - https://github.com/project-topaz/topaz/pull/1300.patch
>    - https://github.com/project-topaz/topaz/pull/1300.diff
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/pull/1300>, or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAHCYJFNDZ6ICHKY47TSSQTSJ6LVRANCNFSM4SKUI7VA>
> .
>



----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Saturday Oct 10, 2020 at 04:48:22_

----

Hello @nuzor !

We are unable to change another user's subscription and notification settings on GitHub -- these settings must be managed by the user who wishes to modify them!

You may find this GitHub documentation helpful in unsubscribing from a repository:
https://docs.github.com/en/free-pro-team@latest/github/managing-subscriptions-and-notifications-on-github/viewing-your-subscriptions

https://docs.github.com/en/free-pro-team@latest/github/managing-subscriptions-and-notifications-on-github/managing-your-subscriptions

As you have participated in this Pull Request, you may now be automatically be subscribed to it. You may unsubscribe from individual Pull Requests by clicking the Unsubscribe button near the top right box for this Pull Request.
![unsubscribe](https://user-images.githubusercontent.com/60901633/95646010-f6543880-0a78-11eb-9df7-76e762984239.png)



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 05:47:56_

----

Before I start reviewing: Don't worry about the CI - if you're targeting or working from an older branch (like `project-topaz:feature/apoc-nigh`) which doesn't have bleeding-edge CI, it'll get a little screwy.
