**Labels:**

improvement



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:06_
_Originally opened as: project-topaz/topaz - Issue 227_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 27, 2018 at 20:48 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4921_

----

we currently have quit a few "special" npcs and other entries where the pol_name field is empty (intentionally).

I propose a default placeholder entry of an underscore just to prevent having to manually maintain a bunch of blank spaces on redump/copypaste to keep the `'` apart. 

By default I mean a change to the sql column default and the batch tools output to stop doing `''` and do `'_'` instead.

```patch
-INSERT INTO `npc_list` VALUES (17908242,'_7o0','     ',0,900.000,95.000,200.000,1,50,50,9,0,0,0,6147,0x0200000000000000000000000000000000000000,0,'SOA',0);
+INSERT INTO `npc_list` VALUES (17908242,'_7o0','',0,900.000,95.000,200.000,1,50,50,9,0,0,0,6147,0x0200000000000000000000000000000000000000,0,'SOA',0);
````
^ example.

'','', ..........',',',',',',',''',,',,,',,',','''
or we can keep ppl counting punctuation and giving me eyestrain, I guess.. 

![mew](https://user-images.githubusercontent.com/6871475/40590483-0d89a380-61ef-11e8-9b55-5e3f27ab3013.gif)

Darkstar Issue Darkstar Issue Darkstar Issue Darkstar Issue Darkstar Issue Darkstar Issue  yes yes I know, I didn't use the template. "omgzords guyz teo hypocrite!"



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:07_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday May 29, 2018 at 19:48 GMT_

----

We need to add ```'_'``` as a discord emote.

