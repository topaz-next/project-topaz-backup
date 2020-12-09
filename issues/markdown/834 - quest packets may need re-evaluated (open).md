**Labels:**

bug

help wanted

research needed



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:18:11_
_Originally opened as: project-topaz/topaz - Issue 834_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Our quest IDs for every region differ from the client dat index. I believe its likely we have an issue with the packet+blob structure. ID 157 in the dat is ID 170 in our current blob. 
[jeuno quests.xlsx](https://github.com/project-topaz/topaz/files/4907304/jeuno.quests.xlsx)

I have checked other regions. They do not match up either. We need to check and see if the ID we send matches what retail sends, because maybe retail does some strange thing to hide all their placeholder IDs:

`SDクエスト43    依頼者` = `SD[Quest] number [Client]`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 17:24:01_

----

To underline problem, our IDs don't match at all; and tend to go awry around intervals of 32. What sucks is that we also use these IDs as indexes for the blob where we store quest completion status.

Just so server admin don't freak out: _Player quest progress is currently safe_. The problem only extends so far as we're telling the client that the player is starting and completing the wrong quests. _But the player itself is still progressing the correct quest_; it's just the player's _quest log_ displaying wrong.

**However, once we fix the packet and IDs, you _must_ run our included migration, or your players' quest progress _will_ be corrupted.**


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 11, 2020 at 17:28:10_

----

:D


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:28:32_

----

its not necessarily displaying wrong in game: this is similar to how CoP had all wrong IDs all over that displayed correctly, but they had the wrong value  so some IDs were unreachable or were to high or to low. Our quest IDs are out of order, but most of them **_probably_** look OK in game right now (no promises tho).
