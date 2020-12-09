**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Monday Sep 14, 2020 at 13:37:09_
_Originally opened as: project-topaz/topaz - Issue 1137_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Left over from https://github.com/project-topaz/topaz/pull/1084
@kaincenteno 

### I've stripped out @UynGH 's notes about what is still left to do:

> **Prelude to Puissance**
>https://youtu.be/usNZOGDq5c0?t=256 (ibm's video), even if he trade unwanted items with the Seasoning Stone, the Moogle will accept said Stone and complete the quest. On canary (with your PR in) you can only trade Stone only if you want him to accept it. **Still present.**
> https://youtu.be/usNZOGDq5c

> **Beyond Infinity (limit break 10)**
> No "Obtained key item: Soul gem clasp." message (https://youtu.be/usNZOGDq5c0?t=644) but still listed in temporary key items. **Still present.**
> Also, by comparing with the above video, the cutscene upon defeating him should start right away when his HPs reach 0 (currently it starts when his name disappear). **Still present.**
> I got a Kindred Seal from him, I guess I shouldn't. He drops nothing. **Still present.**
> Missing the "If all party members' HP are still zero after 3 minutes, the party will be removed from the battlefield." message if you fail. **Still present.**

**Olde Rarab Tail mini-quest - Degenhard**

Dialog when checking him a second time after he asked for the materials should be the same as the one he gives you after you traded your stuff once (https://youtu.be/usNZOGDq5c0?t=788), currently he's repeating the first one only.
Repeating the quest quest - OKAY.
Same "multi trade" issue (https://youtu.be/usNZOGDq5c0?t=797) as in the Prelude to Puissance quest, quoted from my message above.
Using an Olde Rarab Tail on other mobs should do nothing: https://youtu.be/usNZOGDq5c0?t=1071. Currently I can use it on random mobs (it does nothing but still).

**BCNM**

There's two different versions of the BCNM if you're comparing with YouTube videos.
The old one has different messages, an Hundred Fists animation and when using an Olde Rarab Tail, Atori-Tutori used to run around the arena.
THIS IS NOT THE TARGETED VERSION.
https://forum.square-enix.com/ffxi/threads/22099-March-27-2012-(JST)-Version-Update

[dev1095] Limit Break Quest "Beyond Infinity" Adjustments
The effect of the Olde Rarab Tail item has been altered.
Effect duration has been extended.
Your opponent will be inflicted with Terror during this time.
Your opponent will not unleash weapon skills immediately after the effect wears off.

I'm losing the Soul gem clasp key item upon entry but no message stating it/no record message/no party limitation message: https://youtu.be/usNZOGDq5c0?t=1510), should be seen if you retry too. instead I'm getting this:
0
Which is not present on retail.

Atori-Tutori use H2H animation when hitting, wearing a red glowing H2H weapon. There's no additional effect when he's hitting, missing the additional effect on hit he has on retail, which is really potent: https://youtu.be/0AhtvL9nRQw?t=118.
Atori-Tutori used no WSs at all. On retail he use them pretty often, even after a few hits and he does skillchains by using them back to back: https://youtu.be/Q7ncfLXEPNE?t=396. This make it impossible to see if the WSs messages are working.
No message saying he used Hundred Fists but I got one when it wore off, while it should be the other way around: https://youtu.be/usNZOGDq5c0?t=2783. Not having any animation is good tho!

**BCNM retry**

I didn't lose the merit point needed when I tried to pay with it (https://youtu.be/usNZOGDq5c0?t=1636 ibm went from 12 to 11) but I was still able to select a location to teleport to.

In both cases I got the "Obtained key item: Soul gem clasp." message correctly when refusing to teleport directly (choosing "Nowhere yet." https://youtu.be/usNZOGDq5c0?t=1440) so you might take a look here to get the message where's it's missing above.

Bonus: Typos for Horlais Peak and Waughroon Shrine!



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Sep 14, 2020 at 18:04:48_

----

Thank you @zach2good  for creating this, and thank  you @UynGH for writing it so well documented.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Sep 14, 2020 at 23:36:43_

----

[Possesses some form of innate Sekkanoki and can self-SC without ability use or gaining TP between WS](https://www.youtube.com/watch?v=usNZOGDq5c0&feature=youtu.be&t=48m)

[Possesses either innate Regain or an insane amount of Store TP - was able to WS after landing only 5 punches](https://www.youtube.com/watch?v=usNZOGDq5c0&feature=youtu.be&t=25m45s)
