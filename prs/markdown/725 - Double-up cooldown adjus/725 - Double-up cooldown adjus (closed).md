**Labels:**

approved



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Monday Jun 15, 2020 at 01:45:39_
_Originally opened as: project-topaz/topaz - Issue 725_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Removes the cooldown added to double-up after a corsair uses a roll.  Also reduces the cooldown on double-up in line with the retail change to 5 seconds.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Wednesday Jun 17, 2020 at 18:56:27_

----

> 
> 
> I'm assuming the recast for Phantom Roll itself is added by core... somewhere.
> 
> If you want to go the extra mile:
> 
> ```lua
>     if (checkForElevenRoll(caster)) then
>         action:recast(action:recast()/2)
>     end
> ```
> 
> Is wrong. An 11 roll should instantly cause Phantom Roll to be available again, not at half the current recast time.

So does only the _next_ phantom roll get 0 cooldown, or do all phantom rolls while under the effects of an 11 give 0 cooldown?

edit: it's on wiki -- Rolling a total of 11 will immediately reset the Phantom Roll ability timer. While under the effect of an 11-valued roll, your Phantom Roll recast timer will be reduced by 50%. In addition, any rolls of 12+ will still remove the roll's effect, but you will not suffer a Bust penalty and may re-roll freely once your recast timer is up. 
