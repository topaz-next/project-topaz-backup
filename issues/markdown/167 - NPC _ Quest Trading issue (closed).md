**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:38_
_Originally opened as: project-topaz/topaz - Issue 167_

----

<a href="https://github.com/whateversclever1215"><img src="https://avatars1.githubusercontent.com/u/26280208?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [whateversclever1215](https://github.com/whateversclever1215)**
_Tuesday Mar 14, 2017 at 21:20 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3804_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30161227_1

**_Server Version_** (type `revision` in game) **:**
Revision is: Unknown (ERA)

**_Source Branch_** (master/stable) **:**


**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

I ran into this issue while raising fame on an alt.
I was doing the quest:
http://ffxiclopedia.wikia.com/wiki/Only_the_Best
involving the NPC Melyon in Selbina but I don't believe the quest or npc are important details.

I have capped fame on many many many alts on retail, so I am aware of how trading items to NPCs works.

On retail, when you trade a stack of 12(or really anything beyond the 3 millioncorn Melyon asks for), what happens is it will take 3 out of the stack, finish the quest, and the rest will just still be in your bag.

On era, when you trade a stack of 12, or any number except for the exact 3, the trade simply fails to go through.

This is another issue that is extremely unlikely to affect people too badly, but it is not working like retail, and this may give clues to any other issues people have so I am reporting it.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:39_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Mar 14, 2017 at 21:28 GMT_

----

It's an issue with the way the trades are handled in scripts. We do have
the functionality to do it correctly (used in like.. two places), but every
single script that uses trades would have to be rewritten to use it

On Mar 14, 2017 3:20 PM, "whateversclever1215" <notificationsgithub.com>
wrote:

> *I have:*
>
>    - searched existing issues (http://github.com/darkstarproject/darkstar/
>    issues/ <github/darkstarproject/darkstar - Issue >) to see
>    if the issue I am posting has already been addressed or opened by another
>    contributor
>    - checked the commit log to see if my issue has been resolved since my
>    server was last updated
>
> *Client Version* (type /ver in game) *:*
> 30161227_1
>
> *Server Version* (type revision in game) *:*
> Revision is: Unknown (ERA)
>
> *Source Branch* (master/stable) *:*
>
> *Additional Information* (Steps to reproduce/Expected behavior) *:*
>
> I ran into this issue while raising fame on an alt.
> I was doing the quest:
> http://ffxiclopedia.wikia.com/wiki/Only_the_Best
> involving the NPC Melyon in Selbina but I don't believe the quest or npc
> are important details.
>
> I have capped fame on many many many alts on retail, so I am aware of how
> trading items to NPCs works.
>
> On retail, when you trade a stack of 12(or really anything beyond the 3
> millioncorn Melyon asks for), what happens is it will take 3 out of the
> stack, finish the quest, and the rest will just still be in your bag.
>
> On era, when you trade a stack of 12, or any number except for the exact
> 3, the trade simply fails to go through.
>
> This is another issue that is extremely unlikely to affect people too
> badly, but it is not working like retail, and this may give clues to any
> other issues people have so I am reporting it.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 3804>, or mute the
> thread
> <github/notifications/unsubscribe-auth/ABGI_8VedNfzgU0wCb1KdM2LJizLKlv5ks5rlwSUgaJpZM4MdK2g>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:41_

----

<a href="https://github.com/whateversclever1215"><img src="https://avatars1.githubusercontent.com/u/26280208?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whateversclever1215](https://github.com/whateversclever1215)**
_Tuesday Mar 14, 2017 at 21:29 GMT_

----

So there's trading behavior different from retail and a bunch of people using custom trading scripts to take advantage of the difference? ok then, I didn't know scripting trades was possible in the first place, maybe this change made that possible?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:42_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Mar 14, 2017 at 21:39 GMT_

----

Sorry, the problem is in our NPC scripts with how they handle the trade.  When you trade an NPC, the NPC only checks exactly what you have placed into the trade container.  We do have some Lua bindings to support the proper way of doing it (I wrote them), but most NPCs don't use those bindings.  So fixing this would mean rewriting the Lua script for every NPC that accepts trades (ie. would take a long time).



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:43_

----

<a href="https://github.com/whateversclever1215"><img src="https://avatars1.githubusercontent.com/u/26280208?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whateversclever1215](https://github.com/whateversclever1215)**
_Tuesday Mar 14, 2017 at 21:40 GMT_

----

Oh, so just not worth it. Got you.
I was only ticketing this in the event it gave insight into an unsolved issue.
I will close, this isn't an issue really.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:44_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Mar 14, 2017 at 21:53 GMT_

----

It's still a bug that we should fix - it's just a lot of work.  Perhaps someone will see this who has a lot of free time and can ask on IRC what the converted functions are so that they can be used.  It should be pretty simple, but would probably have to be manual.  And even then, just converting some at a time is probably still worth it.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:45_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Wednesday Mar 15, 2017 at 01:33 GMT_

----

If you can let me know what to do, I can try to work on it little by little



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:46_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 15, 2017 at 12:46 GMT_

----

It is important to note that not every NPC behaves this way (on retail). This mainly applies to when you're able to present the NPC with multiple options: which trophies you trade Sanraku, trading in AF3+2 materials with multiple pieces of armor, which Skirmish parts are used when constructing a simulacrum, etc.

There might be other exceptions outside of these types of trades, but nothing immediately comes to mind. And on the other hand, there are NPCs which will be happy to take differing item IDs: Reisenjima stone storers will take all types of stone at once. But Shami won't take multiple kinds of seals at once, go figure.

You'll have to make judgment calls which trades should be "I'll only remove these" and which should remain "exact trade only".



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:48_

----

<a href="https://github.com/Altalus"><img src="https://avatars1.githubusercontent.com/u/194725?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Altalus](https://github.com/Altalus)**
_Wednesday Mar 15, 2017 at 12:58 GMT_

----

My 2c but I think Shami could be modified to be like Reisenjima without impacting the “retail” feel. A little like the fact that chocobos does not “refuse” to go in dungeons but simply zone the player.

________________________

Guillaume Gingras

 

From: ibm2431 [mailto:notificationsgithub.com] 
Sent: Wednesday, March 15, 2017 8:46 AM
To: DarkstarProject/darkstar <darkstarnoreply.github.com>
Cc: Subscribed <subscribednoreply.github.com>
Subject: Re: [DarkstarProject/darkstar] NPC / Quest Trading issue (Darkstar Issue 3804)

 

It is important to note that not every NPC behaves this way (on retail). This mainly applies to when you're able to present the NPC with multiple options: which trophies you trade Sanraku, trading in AF3+2 materials with multiple pieces of armor, which Skirmish parts are used when constructing a simulacrum, etc.

There might be other exceptions outside of these types of trades, but nothing immediately comes to mind. And on the other hand, there are NPCs which will be happy to take differing item IDs: Reisenjima stone storers will take all types of stone at once. But Shami won't take multiple kinds of seals at once, go figure.

You'll have to make judgment calls which trades should be "I'll only remove these" and which should remain "exact trade only".

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub <github/DarkstarProject/darkstar - Issue 3804Darkstar Issue issuecomment-286730720> , or mute the thread <github/notifications/unsubscribe-auth/AAL4pW95kajHFdsXo7BT1RO_f_LYxTYKks5rl92XgaJpZM4MdK2g> .  <github/notifications/beacon/AAL4pT6mCkR4p6I6juJCOWghaKvpklcuks5rl92XgaJpZM4MdK2g.gif> 



---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:49_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Mar 28, 2017 at 16:26 GMT_

----

> A little like the fact that chocobos does not “refuse” to go in dungeons but simply zone the player.

Retail actually does this with the mounts now. Only the old rented/whistle spawned egg raised chocobos still give that error :) They also seem to ignore that annoying zoneflag that would keep you from calling a ride in outdoor zones you normally can't take a chocobo into (like glacier) which is nice.



----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Thursday Mar 19, 2020 at 07:14:03_

----

Hello. I'm unable to reproduce this issue on canary as of 03/19/2020, I traded 12 Millioncorn to Melyon in Selbina and he just took the 3 he needed. Feel free to reopen an issue if you come across something new regarding this. Thank you.
