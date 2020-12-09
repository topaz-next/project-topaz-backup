**Labels:**

focus

help wanted

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Wednesday Jul 22, 2020 at 08:20:22_
_Originally opened as: project-topaz/topaz - Issue 877_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Working on stability before forging ahead to finish gambits and positioning. There were rare crashes on zone after BCNM and I think the rate has shot up since messaging was added.

**Absolutely** looking for help with this


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Jul 22, 2020 at 08:30:40_

----

There is another much rarer crash reported by Canaria after BCNMs with Trusts, but there are many many more since messaging came in, so the messaging crash should be fixed first. 

If you're suffering with crashes since the messaging update, you can comment out the guts of messaging inside `trust.lua`: 
```lua
tpz.trust.message = function(mob, message_offset)
    --[[
         ...comment out everything in here...
     ]]--
end
```
and reload the file with `!reloadglobal trust` without a restart (or do a restart, same effect).


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Jul 22, 2020 at 08:33:51_

----

In this case, Trusts rely on their master to get a reference to the party that they're a member of. During zoning, a Char's party is set to `nullptr` until they've entered their destination zone and the reference is restored. I've tried wrapping up sensitive-looking areas with `if (PChar->loc.zoning) {...}` but it hasn't helped. 

**Braindump**
Could the PTrust's PMaster be nullptr? Is the lua running after the Trust is deleted in core?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 25, 2020 at 20:20:24_

----

~~Hold off on merging, found a bug where ClearTrusts() misses one trust, allowing you to sneak trusts into BCNMs and other places they shouldn't be in. Good news though didn't get any crashes around zoning.~~

OK to merge, those bugs are already present in current trust branch, stability work is unaffected and can go ahead! Fixed the bug where trusts can sneak into your BCNM, the orphaned trusts bug is still there but hasn't caused any problems since trust went into canary, so is fine to leave for a while.
