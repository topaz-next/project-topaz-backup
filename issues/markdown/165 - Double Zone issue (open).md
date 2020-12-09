**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:35_
_Originally opened as: project-topaz/topaz - Issue 165_

----

<a href="https://github.com/whateversclever1215"><img src="https://avatars1.githubusercontent.com/u/26280208?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [whateversclever1215](https://github.com/whateversclever1215)**
_Monday Mar 13, 2017 at 04:54 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3798_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30161227_1

**_Server Version_** (type `revision` in game) **:**
Revision is: Unknown (ERA)

**_Source Branch_** (master/stable) **:**


**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
I multibox. It leads to me doing things others might not do.
I ran into another bug.
On its own this sounds like it would never matter however, I am again documenting this one because it may provide some hint to a more serious issue.

When I am feeling lazy and I want to warp one of my characters, I might just type
//send all //warp2 <charactername>
I may have 2-4 black mages try to warp that character, but at most two will go off, and it's easier than typing a more individualized command.

Well, as it turns out this creates a 100% reproducible error which was not how retail behaved.

If you multibox, and you have 2 black mages cast warp2 on the same target at the same time,

that target will have one black screen/loading...
show up where he was before being warped, load the zone for a second,
and then have a second black screen/loading screen,
and THEN end up at home point

this is reproducible and this happens either every time or most of the time when 2 warp2's land on the same target

hopefully this gives more insight into any remaining issues with homepointing/warping behavior


