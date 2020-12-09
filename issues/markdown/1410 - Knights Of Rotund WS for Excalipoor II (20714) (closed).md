**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 02:48:41_
_Originally opened as: project-topaz/topaz - Issue 1410_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Now you too can make Light at level one for amazingly gimp damage.

###### Excalipoor+1 not included. Not responsible for side effects that may include sudden weight gain, a rash, sneezing, itchy red eyes, incontinence, lost or misdirected mail, or an urge to _/yell I haaaave the powerrrrrr!_



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 23, 2020 at 06:28:37_

----

I might be able to get you the information for excalipoor for the db so this can be an all-in-one PR, please hold for a day or so 👍 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 06:35:54_

----

Okies


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 23, 2020 at 20:06:28_

----

When I added Nihility for reference;
https://github.com/project-topaz/topaz/commit/13984d847277c7dfce6eb45649954bdd000af6bf#diff-1ae46b4dec5f3da0b65d817c19f83b927d563bd5afa95ebc6d6c5f82787fe2eeR10654
```
item_basic:
	(20713, 0, 'excalipoor', 'excalipoor', 1, 30784, 0, 1, 0),
	(20714, 0, 'excalipoor_ii', 'excalipoor_ii', 1, 30784, 0, 1, 0),
item_equipment:
	(20713, 'excalipoor', 1, 0, 4194303, 729, 0, 0, 3, 0),
	(20714, 'excalipoor_ii', 1, 0, 4194303, 729, 0, 0, 3, 0),
item_weapons:
	(20713, 'excalipoor', 3, 0, 0, 0, 0, 2, 1, 240, 1, 0),
	(20714, 'excalipoor_ii', 3, 0, 0, 0, 0, 2, 1, 233, 2, 0),
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 22:44:16_

----

@zach2good so turns out all 6 of those rows already exist with those exact values. I've now added the item mod row, which was all that was left.

I could have sworn I already added all of this back in DSP but when I saw the weaponskill row and script missing thought I must have been mistaken. Its half there half not there, only git blame knows for sure now.
