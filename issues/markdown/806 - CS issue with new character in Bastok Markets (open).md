**Labels:**



<a href="https://github.com/Endymionls"><img src="https://avatars1.githubusercontent.com/u/67812950?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Endymionls](https://github.com/Endymionls)**
_Saturday Jul 04, 2020 at 02:28:29_
_Originally opened as: project-topaz/topaz - Issue 806_

----

I have:

- [X] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [X] checked the commit log to see if the issue has been resolved since my server was last updated

Additional Information (Steps to reproduce/Expected behavior) :

When starting a new character in Bastok and ending up with the cutscene in Bastok Markets, the opening cutscene does not complete and I'm presented with a black screen.  I can run around and bring up menus, interact with NPCs.  Shutting down and reloading the character starts the SOA cutscene for the zone.  After this point, the screen is normal for the character.





----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 04, 2020 at 03:21:31_

----

It is likely that Cs is looking for an npc it isn’t finding due to npc id shifts - meaning your client version and the version the server expects aren’t the same.
