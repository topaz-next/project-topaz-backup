**Labels:**

approved

focus



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Jul 10, 2020 at 22:07:42_
_Originally opened as: project-topaz/topaz - Issue 833_

----

Now that I've had some sleep, see updated comment below

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jul 11, 2020 at 00:12:48_

----

awesome, samba needed some debuffs :dancers: 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 11, 2020 at 07:30:39_

----

So, it was reported that trusts weren't getting any drain from a monster that was under the effect of drain daze (from drain samba). 

I dug in, and there is a section that skips over anything that has a master: (`PAttacker->PMaster == nullptr`). This was fine, according to the wiki:

```
Characters outside of the Dancer's party will not benefit from this effect, nor will non-party members of the Dancer's alliance. Likewise, Puppetmaster automatons, Dragoon wyverns, Beastmaster pets (Jugs or Natural), and NPC fellows will not benefit from a Drain Daze effect.
```

But I went and tested on retail and Trusts _DO_ get the benefit from drain daze.

This PR cleans up the relevant section in core by extracting the daze checking into its own lambda and then checking the relevant configurations of party/master's party/self for the samba's presence.

To clarify, this is just to allow Trusts to get samba effects, no balancing.
