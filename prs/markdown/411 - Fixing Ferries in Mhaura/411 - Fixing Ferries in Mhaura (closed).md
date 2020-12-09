**Labels:**

merge ready



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Mar 12, 2020 at 04:53:24_
_Originally opened as: project-topaz/topaz - Issue 411_

----

* Offset was wrong and time at dock was also wrong. This was fixed.
* Issue with docking position for Ferries is still wrong, but pos in table is now retail accurate.
* NPC at dock in Mhaura now moves when ferry arrives and departs, also tells you about it,
not 100% retail accurate as it needs to rotate when it reaches final location. Leaving it as a TODO
for someone else to complete it.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:55:53_

----

Can probably shorten these; they're already in the `tpz.transport` namespace, so `Porter` is already implied. 😉 

```
tpz.transport.trigger.mhaura
tpz.transport.offset.mhaura
tpz.transport.interval.mhaura
tpz.transport.pos.mhaura
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:56:42_

----

Picky ibm: Could you make sure the `=` line up all pretty like~?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 22:02:00_

----

Here's a trick you could do to save some lines and space, since your "arriving" and "departing" are all even/odd:

```lua
if (triggerID % 2) == 0 then
    npc:pathThrough(-- arriving)
else
    npc:pathThrough(-- departing)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 22:07:50_

----

Not going to force you to globalize this _juuusstt_ yet, but you can save yourself a little effort later by:
```lua
tpz.transport.messages = {}
tpz.transport.messages.mhaura = function(npc, triggerID, messages)
```

(Later we can extend this to instead be just one function which takes a `dock`, and then pulls the appropriate tables based on the dock, but I realize right now that the focus is to fix the ferry)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 22:08:47_

----

And then your function call down here becomes: `tpz.transport.messages.mhaura(npc, triggerID, messages)`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:55:53_

----

Can probably shorten these; they're already in the `tpz.transport` namespace, so `Porter` is already implied. 😉 

```
tpz.transport.trigger.mhaura
tpz.transport.offset.mhaura
tpz.transport.interval.mhaura
tpz.transport.pos.mhaura
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 21:56:42_

----

Picky ibm: Could you make sure the `=` line up all pretty like~?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 22:02:00_

----

Here's a trick you could do to save some lines and space, since your "arriving" and "departing" are all even/odd:

```lua
if (triggerID % 2) == 0 then
    npc:pathThrough(-- arriving)
else
    npc:pathThrough(-- departing)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 22:07:50_

----

Not going to force you to globalize this _juuusstt_ yet, but you can save yourself a little effort later by:
```lua
tpz.transport.messages = {}
tpz.transport.messages.mhaura = function(npc, triggerID, messages)
```

(Later we can extend this to instead be just one function which takes a `dock`, and then pulls the appropriate tables based on the dock, but I realize right now that the focus is to fix the ferry)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 22:08:47_

----

And then your function call down here becomes: `tpz.transport.messages.mhaura(npc, triggerID, messages)`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 22:20:41_

----

~~Developer: I _was_ going to have this target the `transport` branch, but the commit history did _not_ like that, so I punted back to `release`. I'll have to see what's going on with the `transport` branch later.~~

`transport` is just quite a ways behind `release`, which is what this was based on. 
