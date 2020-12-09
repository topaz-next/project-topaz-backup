**Labels:**

bug

feature



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday May 27, 2020 at 13:34:50_
_Originally opened as: project-topaz/topaz - Issue 660_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Until the correct adjustments are made to packets that display item data evoliths are unable to display their augments and synergy augmenting cannot be implemented. Once this is corrected the way synergy evolith augmentation works is the evolith is consumed and the augment it carried is cloned onto the matching socket of the augmented item (which in the current methods is a new copy of that item with the old being destroyed, so technically 2 items are consumed).

I had intended to capture said packets to get the socket data on the evoliths and get those working but leave it to someone else to implement the matching sockets on various equipment. But I derped my captures during free week :x

I've put in a request on the captures discord and will see I can still take a crack at getting this partially done.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday May 29, 2020 at 00:58:38_

----

Magian TrialIDs are part of the augment status, and they aren't working in the item packets either. But I already fixed that and merged it into @Apocarypse Magian branch to support his magian work. I can PR that here separately as well if desired.
