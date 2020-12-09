**Labels:**

reviewed



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Sunday Oct 11, 2020 at 04:54:14_
_Originally opened as: project-topaz/topaz - Issue 1319_

----

![Screenshot - 101020 - 09:55:16 PM](https://user-images.githubusercontent.com/12466395/95670686-51526200-0b43-11eb-8c7d-5de428f7956d.png)
(Relax Zach, 2000 of these lines are just moving records into their own file. :wink: )

Phase 3 mostly adds support for Timed/Daily records, as well as performance improvements/code cleanup.

##### Features: ####
- Timed 4-hour Records (All except magic/physical kills)
- Daily Records (Just Vanquish 30 implemented)
- Add last logout timestamp to chars table (last online time/date)
- Performance improvements + Reduced DB writes (Often significantly)
- Records now kept in separate lua file
- API + code quality Improvements
- Delicious miscellany 

#### Fixes: ####
- Kill credit now counts for party/alliance
- Mob Kill XP now given before Record completion XP (Cases for double-level-ups now in-line with retail behaviour)
- Notification thresholds for all deal/take dmg type records


~~Expect a few follow-up commits if Win32 CI screams bloody murder...~~
Let the record show I have at last submitted a PR which passed CI on the first try. :sunglasses:

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 05:08:10_

----

![image](https://user-images.githubusercontent.com/1389729/95670812-c0a67100-0b98-11eb-9abe-0bcf0a0edb7e.png) ![meebs1](https://user-images.githubusercontent.com/1389729/95670818-c9974280-0b98-11eb-8deb-9a8db8465f29.png)



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 05:23:34_

----

@zach2good lien change/add/remove count greatly inflated by github due to breaking out a function that had a fat a-- from one file into its own new file. the 2 files "too large to display" are this.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Oct 15, 2020 at 20:21:50_

----

Oopsie, looks like this merged into release since there was no more `feature/roe` branch to target anymore. Hopefully everything is A-OK!
