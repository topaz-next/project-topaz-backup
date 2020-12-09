**Labels:**

bug



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Friday May 08, 2020 at 21:45:38_
_Originally opened as: project-topaz/topaz - Issue 598_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I'm unsure what the specific trigger for causing this glitch is... but sometimes (rarely) when a player leaves their mog in a city, they will be put in a wall or in the air, or underground.  This is an example of one time it happened to me, zoning from Bastok Mines mog back outside normally:
![image](https://user-images.githubusercontent.com/37684138/81451960-809b1800-913a-11ea-86d9-c75678a322ce.png)

I got stuck in the air above the alleyway in mines.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 08, 2020 at 21:47:32_

----

Have seen this. Server dropped a player at 0, 0, 0, pos which should have been caught by the zone lua conditional. The player then fell because that pos was mid-air and off map in port windurst. 


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday May 08, 2020 at 22:03:19_

----

I get reports from various players occasionally on my server.  I've also seen it happen on other servers and heard reports of it.

Happens with dualboxers and soloboxers alike.
