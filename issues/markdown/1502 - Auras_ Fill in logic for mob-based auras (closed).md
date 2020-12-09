**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Wednesday Nov 11, 2020 at 18:13:15_
_Originally opened as: project-topaz/topaz - Issue 1502_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Not yet tested, will have time at the weekend.

Side note; iterating a mob's enmity container suuuuuucks.
```cpp
            for (auto [idx, entry] : *PMob->PEnmityContainer->GetEnmityList())
            {
                CBattleEntity* PTarget = entry.PEnmityOwner;
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Nov 11, 2020 at 18:42:43_

----

Wondering if some genericism with var names / loops might result in us being able to combine the logic for the four branches into one, with the if check just determining which list is getting iterated.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Nov 11, 2020 at 18:56:23_

----

I was thinking the same thing, maybe a "generate lists" section, and then "iterate lists" after


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 06:01:50_

----

Another option is for me to make `EnmityList` iterable, but I'm sure I'll fight `EnmityContainer` and friends another time
