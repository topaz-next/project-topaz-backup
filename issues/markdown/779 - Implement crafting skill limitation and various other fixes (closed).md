**Labels:**

merge ready



<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Sunday Jun 28, 2020 at 02:51:03_
_Originally opened as: project-topaz/topaz - Issue 779_

----

Among other things, this implements the limit imposed by retail in wich you can only have a certain amount of levels over level 70 in crafts.

**Main changes**
- *Implements "Craft Sepecialization" System*
   Retail only allows up to 40 levels across all main craft skills combined starting from level 70.
   This makes it imposible to have all skills maxed, forcing players to specialize on 1.

- *New configurable option:* Maximum amount of specialization points.
   This allows server to configure how many crafts can a character maximize.
   By default, 400 points are needed per craft.

- *New configurable option:* Maximum level of crafts before using the Specialization System.
   This is shared across all 8 crafts involved. It cannot be individualy set per craft.
   Retail = 700; Level 75 era = 600; Opt out of the system entirely = 1100;

**Other bugfixes**

- *Limit skill up gains amounts (not the chance of it happening) to 0.1 per level above level 70*
   As per https://www.bluegartr.com/threads/57123-Before-you-ask-a-stupid-crafting-question-read-this!
   This needs confirmation from a more recent era. It may have changed after the raise in level cap.
   For now I made this cap the same as the skill common cap, before the specialization system activates, becouse it made
   sense to me. (Level 70)

- *Fixes a badly placed random call*
   The place it was coded in undesirebly lowered the actual chance of 0.2+ skill ups from happening.

- *Removes crafting myths*
   As per discussion in discord.

- *Fixed skill up chance configuration variable*
   It actually works as a multiplier now and skill ups happen when set at 1.0

- *Lower skill up chance of desynths*

- *Cleaned up coments*

**Related Issues**
#66 #401 

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Jun 28, 2020 at 02:58:24_

----

Nice, thanks Xaver! Would definitely like that config flag for something like this; I'm sure it would be a somewhat 'divisive feature' with some servers. :laughing: 

You may also want to mark this PR as draft, then nobody may merge it until you mark it as ready!


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Sunday Jun 28, 2020 at 03:00:53_

----

I will
It does work, from my testing. that is... 1 hour -2


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 28, 2020 at 03:05:05_

----

Similarly some people are very insistent about their myths not being myths in spite of SE confirmation, which is why there were settings for those (altho I can’t speak to if they even still work)


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Sunday Jun 28, 2020 at 03:11:05_

----

the way it was coded, one of those myths didnt even work.
I did ask in topaz discord before removing them


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Jun 28, 2020 at 03:14:12_

----

Could just pull a page from Square's book... If they were removed would anyone even know? :wink: 

I do believe there was some discussion on the discord about that; if someone were really serious about it they could revert these changes. I haven't heard from Consul but I expect the number of servers who would even want/use the myths is very small.


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Sunday Jun 28, 2020 at 03:33:04_

----

If SE states they're myth and our goal is to be as retail accurate as possible, I don't see any other outcome. If we ever get a custom code section up and running, the myths can go in that pile and be configurable.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 28, 2020 at 03:47:53_

----

@xaver-dared I’m surprised any of them still work.

@Apocarypse I’m the one that settingified them, used to be just hard coded on. While I disagree with you logic as no setting is a retail accurate thing, I did want these gone since the outset. But ppl didn’t like that so they became setting instead.

I wasn’t making a “no don’t do that” post. It was a history lesson to laugh about. Coz people still believe this stuff is more than random numbers. Fake news lord Odin wants my craft to HQ!


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Sunday Jun 28, 2020 at 04:39:07_

----

Hello!

What Apocarypse said. It's clearly a customization thing, not an era setting. If people got accomodated to a bug for years, we wouldn't make a setting for it in the fixing PR. Let's take the recent Treasure Hunter values revealed by S-E for example, if people got used to the old ones and we fix them, we won't make a setting out of the old ones. Same goes here, this is not like Neo Dynamis or the old fishing system, etc.

Edit:

I hope I didn't misunderstood (wouldn't be the first time tho...), I'm sorry if it felt like I was reacting to anyone's message, I wasn't. Just my thoughts about a setting!

Thanks!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 28, 2020 at 04:43:38_

----

I would say most of our settings aren’t era settings and are custom i would also say thats irrelevant seeing how busted up the crafting code has been for ages while trying to accommodate it


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 28, 2020 at 04:49:46_

----

@UynGH if its not clear i’m saying axe the myths and code related but don’t mistake “its not era” or “not retail” as a reason because then your logic applies to almost everything else too. Kill it coz its both broken and silly instead!


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Sunday Jun 28, 2020 at 14:57:51_

----

Sorry for the late response, Dawnbreak doesn't use the ridiculous crafting myths. We will be pulling this later in the week to test it.


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Tuesday Jul 14, 2020 at 03:48:58_

----

If this gets merged to canary, server owners should be noticed that skill up rate config now works correctly at 1.0 and that they should check it


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 16:33:11_

----

Just linking this on #831 so it's not forgotten~
