**Labels:**



<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [rude-jerk](https://github.com/rude-jerk)**
_Saturday Oct 24, 2020 at 05:17:05_
_Originally opened as: project-topaz/topaz - Issue 1422_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 24, 2020 at 05:44:07_

----

While the dyna yagudo may do this at a 100% rate, there has also always been a random chance for this to occur for other mobs doom's as well that has never been implemented in the project. It may be worth making the this a little less yag specific and having a way to define the chance. There is also a message "PlayerName narrowly escapes impending doom." (its msg basic id 359)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Oct 24, 2020 at 05:44:37_

----

Awesome work @rude-jerk  :smile: 

Something from FFXIcyclopedia that they should also receive a message when the status gets deleted:
```(when this occurs, "[Player] narrowly escapes impending doom" will be displayed in the chat log).```

Dunno if you have played with data inside ID.lua inside each zone. If that would be a textid that is the same on each dynamis zone that can be prompted. If it is then you would have to store the textID inside each ID.lua for each zone that the yagudo dynmis are =)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 24, 2020 at 05:47:10_

----

@kaincenteno its a messageBasic not a messageSpecial, so it'd go in the msg.lua global instead. :)


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Saturday Oct 24, 2020 at 05:47:25_

----

Whoops! Missed the message because it was in a different color than I was expecting in my reference video. 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Oct 24, 2020 at 05:51:27_

----

Awesome @TeoTwawki  that makes it even easier =)

But yeah @rude-jerk  i agree that you would have to keep track on WHICH yagudo uses it so the correct yagudo that casted it when killed can remove the effect of Doom (which is a technicality but would make it more accurate to retail =) )

But so far your work looks amazing =) thank you for spending some time on making our dear yagudo army great again =)


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Saturday Oct 24, 2020 at 06:55:59_

----

Generalized the mixin and allowed for removal chance to be set per-mob using local vars. Tracking the mob that applied the debuff can probably be added as a follow-up for mobs where that's of a concern. 
