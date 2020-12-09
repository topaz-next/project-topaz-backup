**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 19:20:04_
_Originally opened as: project-topaz/topaz - Issue 1179_

----

This commit adapts the outdated timeout of "until next server day" mentioned in #1163 and turns it into a timeout between 10 and 40 seconds. `math.random(10,40)` was chosen to not have this be a fixed 40s neither an instant return. This is in line with what is said in the current game guides.

The commit also optimizes the functions for this script, corrects erroneous quest naming and reduces the overall usage of variables from 3 hard triggered locals and 2 charVars to 1 conditioned local and 1 charVar.

It is unclear to me though how flushing charVar "needs_crawler_blood" (from previous steps) to 0 means "being unable to start next quest" (see comment original file). Also it is not explicitly commented what quest is being referred to. I tested my commit and if the "next quest" was meant to be RDM AF3 (Peace for the Spirit [same starter NPC]) I can say that it's perfectly working as expected.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code **extensively**_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 22, 2020 at 19:28:30_

----

does this work without having `require("scripts/globals/npc_util")` header? 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 22, 2020 at 19:29:07_

----

I know this is not on you but please add an empty line at the end (i know it's just a guideline thing)


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 19:37:42_

----

Funny you mention it, because I tested this extensively. Yes it seems so. Should I rather include it anyways?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 22, 2020 at 19:43:55_

----

@TeoTwawki  what u think? 


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 19:48:45_

----

Btw the parentheses were removed because I shortened the superfluity of `:hasKeyItem() == true`


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 22, 2020 at 20:03:35_

----

no need for all if ( ) parenthesis even if it has an `and` or `or` unless it is really needed for order of resolution

if (something) then <- not good accourding to styleguide should be
if something then
^dont get mad at me, get mad at the styleguide xD


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 20:08:38_

----

Sorry, what do you refer to? Should I just resolve them all? I'll gladly do so! (I read the style guide but mostly referred to the original file) I happily get rid of any parentheses where applicable :> (Done)


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 20:30:27_

----

Since I couldn't find any file where npc_util is not explicitly required I also added it accordingly. Marking all of this as resolved then.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 22, 2020 at 22:20:09_

----

It wasn't a prob in testing was because something else happened to be loaded that already required it, putting it in memory for this script by chance. Always require teh things you use :+1:  (and only the ones you use - have seen ppl just add the kitchen sink before lol)



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 24, 2020 at 13:46:37_

----

repeat because for the life of me I cannot type correctly the example in one try >.< so sorry


as for parentheses what kain means is the outmost ones are usually not needed:
```lua
if (condition1 and condition2) then
```
vs:
```lua
if condition1 and condition2 then
```
If things get complicated we'll wrap things in parentheses but otherwise they only are involved in function calls: `entity:doStuff(arguments)`




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 22, 2020 at 19:28:30_

----

does this work without having `require("scripts/globals/npc_util")` header? 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 22, 2020 at 19:29:07_

----

I know this is not on you but please add an empty line at the end (i know it's just a guideline thing)


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 19:37:42_

----

Funny you mention it, because I tested this extensively. Yes it seems so. Should I rather include it anyways?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 22, 2020 at 19:43:55_

----

@TeoTwawki  what u think? 


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 19:48:45_

----

Btw the parentheses were removed because I shortened the superfluity of `:hasKeyItem() == true`


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 22, 2020 at 20:03:35_

----

no need for all if ( ) parenthesis even if it has an `and` or `or` unless it is really needed for order of resolution

if (something) then <- not good accourding to styleguide should be
if something then
^dont get mad at me, get mad at the styleguide xD


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 20:08:38_

----

Sorry, what do you refer to? Should I just resolve them all? I'll gladly do so! (I read the style guide but mostly referred to the original file) I happily get rid of any parentheses where applicable :> (Done)


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 20:30:27_

----

Since I couldn't find any file where npc_util is not explicitly required I also added it accordingly. Marking all of this as resolved then.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 22, 2020 at 22:20:09_

----

It wasn't a prob in testing was because something else happened to be loaded that already required it, putting it in memory for this script by chance. Always require teh things you use :+1:  (and only the ones you use - have seen ppl just add the kitchen sink before lol)



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 24, 2020 at 13:46:37_

----

repeat because for the life of me I cannot type correctly the example in one try >.< so sorry


as for parentheses what kain means is the outmost ones are usually not needed:
```lua
if (condition1 and condition2) then
```
vs:
```lua
if condition1 and condition2 then
```
If things get complicated we'll wrap things in parentheses but otherwise they only are involved in function calls: `entity:doStuff(arguments)`




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 22, 2020 at 22:14:47_

----

> math.random(10,40) was chosen to not have this be a fixed 40s neither an instant return

We know its not going to be random, so I'd rather we guessed at the time with a good ballpark figure we can adjust later rather than doing a random call. On retail it's _probably_ the length of an in game minute give or take some fraction from lag. The wiki's disagree with each other about the actual conditions now. A consistent 30 seconds seems pretty reasonable compared to JP midnight if you ask me even if we're not positive.

Just thinking here but: We could potentially refactor this to use localvar instead of CharVar as well, since the time period is short and logging back in or zoning would be enough time in the event that didn't clear the wait condition anyway (BG wiki is instruction people to zone instead of wait).



----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 23:42:08_

----

I heard the "we can use localVar" comment from so many people now to the extent that I got confused at first (for I am pretty new to the backend of this project). But by now I think I can safely argue that we can not. This is merely a minimal required wait time. The player can turn in the key items (thereby activating the timer), then walk away from the quest for weeks, log out, log in, log out again, wait for some server restarts and not come back until he feels like it. Have to have the flag when that day comes he decides to come back for his shiny RDM AF boots.

I can do that a fixed +30s no problem. I thought it would be actually most adequate (referring to the "up to 40s") to randomize it a bit. My first change used `os.date("%M")` which can result in anywhere from 1 to 59s which I find even more off, but is probably what SE actually uses. Personally I feel it's pretty useless anyways, would be way less resource expensive to just remove all that crap and return the friggin boots right away...(no big difference to retail anyways when the wiki says "up to 40s" [which sounds like "next minute" indeed]). I'd bet my RDM AF boots that the SE dev at the time simply changed `%j` to `%M` like we are discussing and was off with it to not even bother with rewriting anything (prioritization of [time]investment instead of resources).

Please tell me how to proceed with the exact timeout and I'll happily commit accordingly 😀 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Sep 23, 2020 at 03:02:35_

----

> This is merely a minimal required wait time. The player can turn in the key items (thereby activating the timer), then walk away from the quest for weeks, log out, log in, log out again, wait for some server restarts and not come back until he feels like it. Have to have the flag when that day comes he decides to come back for his shiny RDM AF boots.

that doesn't necessarily mean it can't be the other type of var. if we make the condition to continue being our stored value less than something we're comparing it to - maybe not this instance of it but I just want you to know in many cases we can still avoid saving to the database, by checking other requirements and making changing the logic of what exactly our variable is intended to hold.

> Please tell me how to proceed with the exact timeout and I'll happily commit accordingly grinning

I'd just use 30 seconds where you have math.random and call it a day till someone runs through it on retail and tells us exactly what it did (maybe they already did - I have not looked in the [captures discord](https://discord.gg/XSNJnUE) to see)


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Sep 23, 2020 at 03:30:42_

----

Well I'd really like to see this very example with a localVar to be honest, cause everybody keeps saying. Sadly this is what I can do ^^; I wouldn't mind an edit/comment here. If anything, I'll change to fix 30s and call it a day for today :)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Sep 23, 2020 at 22:04:55_

----

> Well I'd really like to see this very example with a localVar to be honest, cause everybody keeps saying. Sadly this is what I can do ^^; I wouldn't mind an edit/comment here. If anything, I'll change to fix 30s and call it a day for today :)

looks good to me as it is, if someone wants to change it to use a localVar, they can after it gets merged :smile_cat: 
