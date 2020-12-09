**Labels:**

feature



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Mar 14, 2020 at 20:09:41_
_Originally opened as: project-topaz/topaz - Issue 423_

----

I imagine this might be implemented to match retail behavior, which has some merit. But we should allow for a configuration that removes the search request cap.

It's a bit annoying that commands such as`/sea all` doesn't actually return the full player list for servers with a lot of players.

This could be a useful configuration to enable on some servers.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Mar 14, 2020 at 21:12:52_

----

Its actually just missing handling not retail behavior. So its more a bug to be fixed really.

Retail will split the packet when its “to big”.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Mar 21, 2020 at 19:47:26_

----

On retail, it seems to cap the results at 40.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Mar 21, 2020 at 20:30:06_

----

Playing around locally, it seems we can include more than 20 results in a single packet. Tested `21` and it worked fine without any other modifications.

Specifically I just upped the count here:
https://github.com/project-topaz/topaz/blob/820f822c271b91d6a55ed015a75d544d3604d2b9/src/search/data_loader.cpp#L321

Which in turn appends more results to the packet, here:
https://github.com/project-topaz/topaz/blob/820f822c271b91d6a55ed015a75d544d3604d2b9/src/search/search.cpp#L581-L583


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Mar 21, 2020 at 20:33:33_

----

It's unclear if we can get the same result by just sending multiple packets of size 20 each. Without sniffing the retail behavior it may be hard to test that, but I can try playing around with it locally on Topaz to see.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Mar 21, 2020 at 20:39:14_

----

Naively breaking this into two packets does not seem to work. I get a "receive error".

Will try to test >40 results in a single packet to see if it can handle that, or if the 40 shown in retain is a hard limit.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Mar 21, 2020 at 21:01:22_

----

Its not going to work by just sending multiple - the split is different than what you are thinking. If nasomi is willing to talk about it they’ve got some info on this.
