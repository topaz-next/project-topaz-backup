**Labels:**

bug

crafting



<a href="https://github.com/SirGouki"><img src="https://avatars3.githubusercontent.com/u/11664236?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [SirGouki](https://github.com/SirGouki)**
_Thursday Feb 20, 2020 at 02:38:06_
_Originally opened as: project-topaz/topaz - Issue 359_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

Branch: master

Client version: 30200217_0

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
go to zone: Bastok Markets
head to the goldsmithing guild.
talk to Visala.  She will have a shorter inventory than she should have.  If you attempt to sell her something she's supposed to stock, like Mythril Ore, she just outright wont buy it.
Also, she will buy up more than she's supposed to of items she does stock (I was able to sell her 10 zircon) but still only stocks the minimum for whatever her current maximum stock is (mine was 3 since I just started the server)
Source for what she is supposed to stock: https://www.bg-wiki.com/bg/Visala



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Feb 20, 2020 at 03:40:44_

----

cause at least in large part by SE changes:
Teerth uses the new style guild shop (see shop.lua), and Visala needs an updated stocklist of the old style

