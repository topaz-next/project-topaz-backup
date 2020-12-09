**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Oct 03, 2020 at 14:07:26_
_Originally opened as: project-topaz/topaz - Issue 1241_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Uses _maths_ to determine where trusts should stand.

**DONE**
Different "types" of movement will run to valid positions and stay there until conditions change
1-2 Trusts that use this type of movement
A sane way of attaching these movement styles to trusts (Lua, DB etc.)
Update `feature/trust` with the fix commit that's lurking in here, because we're changing branch permissions and I got impatient.

![image](https://user-images.githubusercontent.com/1389729/94993694-7d963d80-059b-11eb-8a8d-595af8bb4c51.png)



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 04, 2020 at 13:45:19_

----

Like I mentioned in Discord, this is literally the most checking I can be doing to see if a new position is valid:

```cpp
        // Validate position
        if (POwner->PAI->PathFind->ValidPosition(potential_position) &&
            POwner->loc.zone->m_navMesh->raycast(PTarget->loc.p, potential_position) &&
            !POwner->loc.zone->m_navMesh->findPath(POwner->loc.p, potential_position).empty())
```

Without updated navmeshes, there will always be problems with pathing 🤷 
