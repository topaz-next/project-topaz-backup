**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 13, 2020 at 04:55:50_
_Originally opened as: project-topaz/topaz - Issue 1347_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Got a report of there being lingering entries in PNotorietyContainer, meaning you'd have to zone to clear it.
This makes player:hasEntity() wrongly return true, when the player isn't in trouble
It was in Castle O [S], so I'm guessing it has something to do with the broken giant beastmen parties.

Repro'd in canary by running around in Castle O [S] and killing Yagudos, and then trying to summon trusts -> rejected

Proven fixed by merging this branch into canary, doing the same, then being able to summon trusts when I've killed everything around me and I have no obvious aggro.

Also put a breakpoint on the `remove()` call to make sure invalid mobs were being taken out of the container


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 13, 2020 at 08:04:11_

----

Each tick seems a little overkill for what's probably a bug elsewhere (the wrong mob got on the list somehow). Could we safely lighten the load by calling tryClear inside checks for notoriety (ie: hasEnmity)?

```
Do I have enmity?
Remove any invalid mobs from my list
Mobs remaining? Return Yes
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 13, 2020 at 08:12:25_

----

Now I'm getting crazy thoughts like the iterator for the container always checking for the player in the mob's enmity container, and removing the entry from the notoriety container if there's no corresponding match, so that the notoriety container is always "self cleaning" as its stepped through.

But feel free to ignore the mad science.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 13, 2020 at 11:11:37_

----

> Could we safely lighten the load by calling tryClear inside checks for notoriety (ie: hasEnmity)?

This is the exact use case that the bug appears in (so far), so this makes a lot of sense! This is also the _only_ place that the container is iterated by.
