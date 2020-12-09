**Labels:**



<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [59blargedy](https://github.com/59blargedy)**
_Thursday Jul 02, 2020 at 16:51:40_
_Originally opened as: project-topaz/topaz - Issue 798_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [] checked the commit log to see if the issue has been resolved since my server was last updated

it appears that mobskills that gain the effect dsp.effect.BOOST simply wear off before the action, so the attp bonus is never realized
can confirm by going to zhayolm and giving trolls tp, watching as the boost effect wears right before hit and seeing no increase in their damage. 
https://github.com/project-topaz/topaz/blob/08fcc59f5fc1a5a929037ca24b13ce9cec8f287f/scripts/globals/mobskills/quake_stomp.lua#L28
https://github.com/project-topaz/topaz/blob/release/scripts/globals/effects/boost.lua
the only mention i can find of boost in cpp is this, which is player only:
https://github.com/project-topaz/topaz/blob/08fcc59f5fc1a5a929037ca24b13ce9cec8f287f/src/map/lua/luautils.cpp#L1451




----
<a href="https://github.com/Taruecho"><img src="https://avatars0.githubusercontent.com/u/22431344?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Taruecho](https://github.com/Taruecho)**
_Thursday Jul 09, 2020 at 20:42:57_

----

This is happening on players as well using boost ability as MNK. It wears before the effect does anything to attk power
