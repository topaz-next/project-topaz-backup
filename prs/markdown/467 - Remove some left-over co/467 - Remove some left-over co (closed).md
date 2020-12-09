**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Apr 04, 2020 at 08:42:12_
_Originally opened as: project-topaz/topaz - Issue 467_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

~edit: **Hold review on this**.  I found some other left-over merit stuff and will fix where needed.~

bio: adjust DoT potency to known buckets
http://wiki.ffo.jp/html/1954.html

bio ii: adjust DoT potency to known buckets
http://wiki.ffo.jp/html/1954.html

bio iii: merit no longer affects duration. adjust DoT potency to known buckets
http://wiki.ffo.jp/html/1954.html

blind ii, paralyze ii, slow ii: merits no longer affects potency

dia iii: merit no longer affects duration

phalanx and phalanx ii: adjusted formula from bgwiki.  phalanx ii merit no longer does anything.

shellra v: removed unused variable

ninjustu san-tier nukes: spell-specific merits no longer do anything.

saboteur: when enfeebling NMs, only grant a +25% duration, rather than a +100% duration.

**Ready for review!**


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 09:23:06_

----

[old wiki is claiming](https://ffxiclopedia.fandom.com/wiki/Bio_II):
```
    290~ skill: 8 HP/3 seconds
    251~290 skill: 7 HP/3 seconds
    211~250 skill: 6 HP/3 seconds
    171~210 skill: 5 HP/3 seconds
    131~170 skill: 4 HP/3 seconds
    0~130 skill: 3 HP/3 seconds
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 09:27:22_

----

[Dia III might be a straight 180 seconds now along with Bio III](https://forum.square-enix.com/ffxi/threads/55751-August.-6-2019-%28JST%29-Version-Update?p=618448&viewfull=1#post618448)
> The duration of the white magic spell Dia III has been adjusted to 180 seconds.

I don't know if that means it floors at 180 though, might go below. Pinging @project-topaz/researcher if they feel like casting Dia III on an ilvl mob while naked.

edit: Commented on the wrong line, but I mean it might always be 180 without the duration calculation that's occurring above in the file.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Apr 08, 2020 at 18:15:21_

----

Adjusted all bio calcs to match JP wiki, which has the most complete set of breakpoints (and agrees with the data you linked)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Apr 08, 2020 at 18:19:15_

----

For enfeebling magic, the calculateDuration() will

* apply saboteur bonus (+25% vs NMs, otherwise +100%)
* apply bonus from ENFEEBLING_MAGIC_DURATION merit.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 19:57:31_

----

D:
[Alignment spaces inside the conditional are the devils styling!](https://tenor.com/view/mermaidman-evil-gif-10846836)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 23:52:45_

----

Oh I see; I was mentally linking Bio and Dia, and saw Bio didn't use the function (retrospect: because it's not enfeebling), so thought calculateDuration was for the purpose of taking resistances into play or something.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 09:23:06_

----

[old wiki is claiming](https://ffxiclopedia.fandom.com/wiki/Bio_II):
```
    290~ skill: 8 HP/3 seconds
    251~290 skill: 7 HP/3 seconds
    211~250 skill: 6 HP/3 seconds
    171~210 skill: 5 HP/3 seconds
    131~170 skill: 4 HP/3 seconds
    0~130 skill: 3 HP/3 seconds
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 09:27:22_

----

[Dia III might be a straight 180 seconds now along with Bio III](https://forum.square-enix.com/ffxi/threads/55751-August.-6-2019-%28JST%29-Version-Update?p=618448&viewfull=1#post618448)
> The duration of the white magic spell Dia III has been adjusted to 180 seconds.

I don't know if that means it floors at 180 though, might go below. Pinging @project-topaz/researcher if they feel like casting Dia III on an ilvl mob while naked.

edit: Commented on the wrong line, but I mean it might always be 180 without the duration calculation that's occurring above in the file.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Apr 08, 2020 at 18:15:21_

----

Adjusted all bio calcs to match JP wiki, which has the most complete set of breakpoints (and agrees with the data you linked)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Apr 08, 2020 at 18:19:15_

----

For enfeebling magic, the calculateDuration() will

* apply saboteur bonus (+25% vs NMs, otherwise +100%)
* apply bonus from ENFEEBLING_MAGIC_DURATION merit.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 19:57:31_

----

D:
[Alignment spaces inside the conditional are the devils styling!](https://tenor.com/view/mermaidman-evil-gif-10846836)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 23:52:45_

----

Oh I see; I was mentally linking Bio and Dia, and saw Bio didn't use the function (retrospect: because it's not enfeebling), so thought calculateDuration was for the purpose of taking resistances into play or something.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Apr 08, 2020 at 18:14:24_

----

Adjusted Saboteur duration vs NMs.
Adjusted Bio calcs per JP wiki.
Believe Dia III duration is correct.
