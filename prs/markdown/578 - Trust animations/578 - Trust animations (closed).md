**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday May 03, 2020 at 18:42:09_
_Originally opened as: project-topaz/topaz - Issue 578_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**The aim of this PR:**
- Get a bunch of animation caps



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 13:43:18_

----

Did aern skills get moved?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 13:47:24_

----

[Looks like this got changed in Windower's resources lib in June](https://github.com/Windower/Resources/commit/979184450747ea2efdd03f2f5df0843584eebaeb#diff-06d2dc9b9cf47e05842a393d97098171)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 11, 2020 at 15:51:06_

----

![image](https://user-images.githubusercontent.com/1389729/87228067-75b56b80-c3a7-11ea-9589-63f8321cf8cc.png)



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 11, 2020 at 15:52:26_

----

I guess they must have gone somewhere else, probably need to re-cap those aern skills


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 16:30:21_

----

I'm concerned about the mob skill lists which currently use these IDs:
3412 and 3413 are currently tied to skill list 3, Aern

3414 is tied to Sekhmet; I remember that @tankfest changed its ID for Charged Whisker back in #553 , so maybe _all_ of its IDs have changed.

@TeoTwawki have _skill IDs_ ever _changed_ before? This prospect scares me, because I don't think we have _any_ mechanism for dealing with _skill shifts_.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:44:04_

----

@ibm2431 they have but its super rare - when it happenes it usually means the mobIDs also had a shift, some mob getting added or removed from zone in the middle of other mobs in the index.

Its much more likely there was a prior mistake here honestly.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:48:43_

----

Those look like 2hrs on the Aerns, I suspect someone saw the blanks and assumed the aern 2hrs belong wshere when they really do not, and then later SE filled in the blanks with these.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 13, 2020 at 15:27:59_

----

May want to ask @project-topaz/researcher to go let Sekhmet get some TP moves in so its existing skill list can be adjusted. If these skill IDs are getting replaced with those for trusts, we don't want to end up with a coeurl using Combo. 😉 

On the aern front, here are all the pools using that skill list ID:
![image](https://user-images.githubusercontent.com/13112942/87322615-242eed00-c51d-11ea-9574-6370b6613cc1.png)

Truth be told, I take aerns as being broken in general, and wouldn't mind simply removing those IDs from their lists. But if someone _really_ wants to hunt down what happened to those skills, there's a list of potential targets~



----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Monday Jul 13, 2020 at 20:15:49_

----

re: sekhmet: https://github.com/project-topaz/topaz/pull/553#issuecomment-624654846



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jul 13, 2020 at 23:05:03_

----

iirc certain coeurl nm won't use whisker unless struck by magic 1st or it matches another condition like day. I think you have to thundaga sek or it needs lightning day before he'll use it. camped his drop on retail, only remember tripping it one time and then just avoided the trigger. don't remember what the trigger was exactly.


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Thursday Jul 16, 2020 at 16:59:31_

----

I tried with multiple possibilities to make him use Charged Whisker, no success.

First time I pulled him with Frazzle (no damage), let him hit me for a good 15 minutes without casting anything else on him. It was during darksday through firesday, lasting more than an hour. Then I started casting Thunder on him until he went under 25% then under 20%. Still nothing.

I went back during lightningday then I tried to use Shock, Shock Spikes, Thundaga, Dia and multiple magic debuffs on him, even warping back because he was low on HP. Went back again and tried to melee him with low damage weapon. As far as being below 5% HP still during lightningday and... no trace of Charged Whisker. All of this lasted more than an hour too so he had time building up TPs hitting me, etc.

I checked on YouTube, ZAM, BGWiki and FFXIclopedia. Beside FFXIclopedia and ZAM stating the same thing ("He rarely use it."), nothing can confirm it.

On a side note what can be confirmed about Sekhmet:

He is immune to Bind, Break, Gravity, Silence and Sleep (FFXIclopedia had Silence listed only). He doesn't link with other Coeurls and his Enaspir occurs at a really low rate (5-10% seems accurate).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 18:00:51_

----

we should assume he has no skill at this point till someone proves he does (and how they got him to go)

I think its more likely everyone (incl me) mixed up their kitties than SE just spontaneously removing it.

And you forgot to tell them you tried to shock spikes to show kitty how to zap ppl. :wink: 

Conspiracy theory: SE accidentally gave poor this NM negative regain instead of positive.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 18:08:34_

----

P.S. the list entries near here that the PR does not change, are also wrong just like blaster was. These are howling First and Dragon Kick.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 13:43:18_

----

Did aern skills get moved?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 13:47:24_

----

[Looks like this got changed in Windower's resources lib in June](https://github.com/Windower/Resources/commit/979184450747ea2efdd03f2f5df0843584eebaeb#diff-06d2dc9b9cf47e05842a393d97098171)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 11, 2020 at 15:51:06_

----

![image](https://user-images.githubusercontent.com/1389729/87228067-75b56b80-c3a7-11ea-9589-63f8321cf8cc.png)



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 11, 2020 at 15:52:26_

----

I guess they must have gone somewhere else, probably need to re-cap those aern skills


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 16:30:21_

----

I'm concerned about the mob skill lists which currently use these IDs:
3412 and 3413 are currently tied to skill list 3, Aern

3414 is tied to Sekhmet; I remember that @tankfest changed its ID for Charged Whisker back in #553 , so maybe _all_ of its IDs have changed.

@TeoTwawki have _skill IDs_ ever _changed_ before? This prospect scares me, because I don't think we have _any_ mechanism for dealing with _skill shifts_.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:44:04_

----

@ibm2431 they have but its super rare - when it happenes it usually means the mobIDs also had a shift, some mob getting added or removed from zone in the middle of other mobs in the index.

Its much more likely there was a prior mistake here honestly.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:48:43_

----

Those look like 2hrs on the Aerns, I suspect someone saw the blanks and assumed the aern 2hrs belong wshere when they really do not, and then later SE filled in the blanks with these.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 13, 2020 at 15:27:59_

----

May want to ask @project-topaz/researcher to go let Sekhmet get some TP moves in so its existing skill list can be adjusted. If these skill IDs are getting replaced with those for trusts, we don't want to end up with a coeurl using Combo. 😉 

On the aern front, here are all the pools using that skill list ID:
![image](https://user-images.githubusercontent.com/13112942/87322615-242eed00-c51d-11ea-9574-6370b6613cc1.png)

Truth be told, I take aerns as being broken in general, and wouldn't mind simply removing those IDs from their lists. But if someone _really_ wants to hunt down what happened to those skills, there's a list of potential targets~



----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Monday Jul 13, 2020 at 20:15:49_

----

re: sekhmet: https://github.com/project-topaz/topaz/pull/553#issuecomment-624654846



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jul 13, 2020 at 23:05:03_

----

iirc certain coeurl nm won't use whisker unless struck by magic 1st or it matches another condition like day. I think you have to thundaga sek or it needs lightning day before he'll use it. camped his drop on retail, only remember tripping it one time and then just avoided the trigger. don't remember what the trigger was exactly.


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Thursday Jul 16, 2020 at 16:59:31_

----

I tried with multiple possibilities to make him use Charged Whisker, no success.

First time I pulled him with Frazzle (no damage), let him hit me for a good 15 minutes without casting anything else on him. It was during darksday through firesday, lasting more than an hour. Then I started casting Thunder on him until he went under 25% then under 20%. Still nothing.

I went back during lightningday then I tried to use Shock, Shock Spikes, Thundaga, Dia and multiple magic debuffs on him, even warping back because he was low on HP. Went back again and tried to melee him with low damage weapon. As far as being below 5% HP still during lightningday and... no trace of Charged Whisker. All of this lasted more than an hour too so he had time building up TPs hitting me, etc.

I checked on YouTube, ZAM, BGWiki and FFXIclopedia. Beside FFXIclopedia and ZAM stating the same thing ("He rarely use it."), nothing can confirm it.

On a side note what can be confirmed about Sekhmet:

He is immune to Bind, Break, Gravity, Silence and Sleep (FFXIclopedia had Silence listed only). He doesn't link with other Coeurls and his Enaspir occurs at a really low rate (5-10% seems accurate).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 18:00:51_

----

we should assume he has no skill at this point till someone proves he does (and how they got him to go)

I think its more likely everyone (incl me) mixed up their kitties than SE just spontaneously removing it.

And you forgot to tell them you tried to shock spikes to show kitty how to zap ppl. :wink: 

Conspiracy theory: SE accidentally gave poor this NM negative regain instead of positive.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 18:08:34_

----

P.S. the list entries near here that the PR does not change, are also wrong just like blaster was. These are howling First and Dragon Kick.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday May 04, 2020 at 03:39:42_

----

If this is just going to be SQL (and maybe minor .h changes), do _me_ a favor and target release~

That way you can do _Wiggo_ a favor and define the zoneFlags for Adventuring Fellow too, and then we can merge release into both `trust` and `adventuringfellow` while updating the animations in `release`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jun 06, 2020 at 22:35:27_

----

We may need to give the nameless TP moves names. A naming convention eludes me at the moment, but I believe some of these might need scripts.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 23:47:58_

----

@ibm2431 Sometimes the packet will have a name even if the dat does not. In the cases where its the entities melee animations (tp skill as special melee) I have been using `mobname_special_melee` in all lowercase. Legion had done up a ton of these but I think the server shut down without anyone sharing them back. Accurate animations on most of them. :(


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Jul 27, 2020 at 08:47:07_

----

Since I'm greedy and I want these caps for my next trust feature PR, I've wiped out the (possibly) incorrect skill list entries for Sekhmet and the Aern skills. I think the impact will be nearly unnoticeable and if someone flags them up then that gives us a chance to fix them _for reals_ 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 28, 2020 at 01:21:43_

----

[I had sole hold~!](https://github.com/project-topaz/topaz/wiki/Staff-Meeting-022-Summary)
