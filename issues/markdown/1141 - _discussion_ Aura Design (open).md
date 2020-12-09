**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 15, 2020 at 05:20:43_
_Originally opened as: project-topaz/topaz - Issue 1141_

----

I'm trying to get the ball rolling on integrating all of the GEO code, and the first step to that is getting aura handling into core. No content, just a single aura. This is a very heavy-weight mechanic which I don't want to populate with content until it's performant and working as well and as safely as we can get it.

Starting PR:
https://github.com/project-topaz/topaz/pull/1138

The areas in question:
https://github.com/project-topaz/topaz/pull/1138/files#diff-4fa3f9f67b44be17ddcfcbb83b337bfbR270
https://github.com/project-topaz/topaz/pull/1138/files#diff-0c15fa23f4c9823216f55fb835928c67R1517

The problem (in addition to what IBM mentioned) that I was going after in the next day or so - is that this first iteration targets anyone of the same allegiance to you, so it'll hit other parties. 

I'm just about to start work so I can't dig in now, but I'm forseeing a trip into "however curaga works" will yield me some answers.

@TeoTwawki @ibm2431 

EDIT:
These seem relevant to my interests:
https://github.com/project-topaz/topaz/blob/45c97efb1fdb128570a223b3bea8cb40ed281182/src/map/ai/helpers/targetfind.h#L41-L55


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 15, 2020 at 05:25:03_

----

From the PR:
ibm:
>allegiance.PLAYER is the wrong approach to the problem. Bubble types should be tagged as targeting aliies or enemies, and allegiance checks against potential targets done based on that.
>
> If this paradigm isn't corrected early, it will bite people in the ass the second they start trying to implement NMs with auras.

teo:
> Oops. Good catch tho, don’t want to repeat the player/mob paradigm that is a problem with skill/ability use atm.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 15, 2020 at 16:26:14_

----

> I'm just about to start work so I can't dig in now, but I'm forseeing a trip into "however curaga works" will yield me some answers.

now find myself wondering if there are any retail mobs that use curaga, and if so do we even do that right.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 16, 2020 at 05:18:40_

----

This is looking like a good place for the fabled `reverse enmity container`
