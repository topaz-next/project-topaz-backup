**Labels:**

reviewed



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Thursday May 28, 2020 at 23:04:27_
_Originally opened as: project-topaz/topaz - Issue 664_

----

<img align="right" src="https://user-images.githubusercontent.com/12466395/83200195-aabb7680-a0f7-11ea-9e20-050828a91235.png"/>

No longer can zone_weather be the butt of jokes. She's lean and fast and remembers how you laughed when she was big; so she's not giving you her number.

In seriousness, zone_weather is big. 237,000 rows of daily weather data that takes a long time to import, and a lot of space to store. It's the largest DB table by a wide margin. This switches the inefficient existing storage to just one neatly packed bit pattern per zone. Those interested in technical specs can see the comment above loadZoneWeather() where it's detailed for you.

### Gains
```
SQL File Size:              83% reduction
SQL Import time:            97% reduction
Server weather load:        55% reduction
Raw table Size:             40% reduction
```
This will be especially welcome to those who aren't running on high end hardware, or those trying to run on Raspberry Pi's where SQL transaction IO can be limiting.

### Considerations
The table will no longer be in human-readable form, though I would argue it was far from human-friendly before, and the weather table has generally gone untouched for quite some time so I consider it essentially static. That said, the fixed-length data format was designed to be easy to work with, and a tool or script could be made to make editing zones easier than was even possible previously.

The new weather blobs ~~live in a new table which~~ needs to be imported or the server will display errors that the user should "Import zone_weather.sql". I don't believe any migrate step is needed at this time, as the table is new and shares nothing in common with the old one. 

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Jun 01, 2020 at 08:06:57_

----

Would like some spaces in here:
`if (...`
`i = 1;`
etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Jun 01, 2020 at 08:08:01_

----

Thanks for the excellent comment explaining the bit shifting witchcraft :)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Jun 01, 2020 at 13:47:37_

----

Updated to give you some space!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Jun 01, 2020 at 08:06:57_

----

Would like some spaces in here:
`if (...`
`i = 1;`
etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Jun 01, 2020 at 08:08:01_

----

Thanks for the excellent comment explaining the bit shifting witchcraft :)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Jun 01, 2020 at 13:47:37_

----

Updated to give you some space!


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Friday May 29, 2020 at 04:35:04_

----

RIP thicc zone_weather
hello slimfast weather!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 02, 2020 at 00:41:25_

----

> _gotta go fast_

![](https://media.giphy.com/media/6bt7096m6fy1i/giphy.gif)

