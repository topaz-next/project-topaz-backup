**Labels:**

improvement



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:32_
_Originally opened as: project-topaz/topaz - Issue 144_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Tuesday Nov 15, 2016 at 23:09 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3544_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [X] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [X] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
current

**_Server Version_** (type `revision` in game) **:**
b8a258559e8178b7924e43a95805e1d4992609bf

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
When I was looking through synthutils.cpp for a recent pull request, I noticed that it's hardcoded to decrease the success rate for synths using a lightning element crystal. Not all such synths are desynths (ie. the alchemy ones to make Mercury from various fish), and not all desynths use a lightning element crystal (I can't think of one offhand). The synth_recipes table does not have a column for desynth. I did notice there is a column named Type, however it does not appear to even be read from judging by the query (if I'm reading it correctly). It looks like it has a value of either 0 or 1, though I didn't look at all of the entries closely.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:34_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Nov 15, 2016 at 23:11 GMT_

----

moblin armor (leathercraft) is a desynth that uses wind




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:35_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Nov 16, 2016 at 08:16 GMT_

----

Quadav backplate desynth with a wind crystal




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:36_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 16, 2016 at 21:05 GMT_

----

Quadav Backplates (and a ton of others) have multiple desynth recipes, 1 wind 1 lightning.

If that column is unused, lets rename it to make it obvious, and then use it to tell if a recipe is a desynth.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:37_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Feb 11, 2017 at 16:36 GMT_

----

I've QCed two craft recipe lists so far (alchemy and bonecraft) and the `type` column is consistently 1 for synths and 0 for desynths, so I believe we can reliably use this column to distinguish.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:38_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Saturday Feb 11, 2017 at 16:39 GMT_

----

We will use it, but I'm almost positive at least some of the recipes in the
db are marked incorrectly. Appreciate you verifying them.

On Feb 11, 2017 11:37 AM, "wrenffxi" <notificationsgithub.com> wrote:

> I've QCed two craft recipe lists so far (alchemy and bonecraft) and the
> type column is consistently 1 for synths and 0 for desynths, so I believe
> we can reliably use this column to distinguish.
>
> —
> You are receiving this because you were assigned.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 3544Darkstar Issue issuecomment-279157950>,
> or mute the thread
> <github/notifications/unsubscribe-auth/AGPFUZFzcgC7Lak8qnHw8X_AgV9Glza0ks5rbeOsgaJpZM4KzI7O>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:40_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 11, 2017 at 16:40 GMT_

----

Should that column be renamed from `type` to something more informative?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:41_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Saturday Feb 11, 2017 at 16:45 GMT_

----

I mean 'type' is a pretty accurate description for what it is, I think most
of the confusion around it rose from the fact it was never referenced in
the code

On Feb 11, 2017 11:40 AM, "ibm2431" <notificationsgithub.com> wrote:

> Should that column be renamed from type to something more informative?
>
> —
> You are receiving this because you were assigned.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 3544Darkstar Issue issuecomment-279158181>,
> or mute the thread
> <github/notifications/unsubscribe-auth/AGPFUYWUk86YPJ3-1LR57HW28QsYgVYrks5rbeRzgaJpZM4KzI7O>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:42_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 11, 2017 at 17:44 GMT_

----

Just floating the idea of flipping the two values, and renaming the column from `type` to `is_desynth` ~!



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:43_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Feb 11, 2017 at 17:53 GMT_

----

I almost did something with that last night..I almost named it isDesynth while I was at it (no underscore, underscores in field names just feel wrong to me, dunno why they just do) but then decided to leave it alone. I didn't finish though. We should absolutely use 0 for normal synths and 1 for desynths, though we do not right now. All the older recipes have a 1. Some of the newer ones use zero. and all the desynths currently use zero.

maxtherabbit the fact that the craft container is a recycled trade container broke my sleep deprived brain when I realized it when I was looking to try and store the field someplace instead of using a query every time you craft..wtf should I be doing with that. Or should I just leave it alone for now.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:44_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Sunday Feb 12, 2017 at 00:38 GMT_

----

I'd leave it be IMO

On Feb 11, 2017 12:53 PM, "TeoTwawki" <notificationsgithub.com> wrote:

> I almost did something with that last night..I almost named it isDesynth
> while I was at it (no underscore, underscores in field names just feel
> wrong to me, dunno why they just do) but then decided to leave it alone. I
> didn't finish though. We should absolutely use 0 for normal synths and 1
> for desynths, though we do not right now. All the older recipes have a 1.
> Some of the newer ones use zero. and all the desynths currently use zero.
>
> maxtherabbit <github/maxtherabbit> the fact that the craft
> container is a recycled trade container broke my sleep deprived brain when
> I realized it when I was looking to try and store the field someplace
> instead of using a query every time you craft..wtf should I be doing with
> that. Or should I just leave it alone for now.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 3544Darkstar Issue issuecomment-279163380>,
> or mute the thread
> <github/notifications/unsubscribe-auth/AGPFUc5OZBq5WY-4c134WVbMmB62eL_Tks5rbfWWgaJpZM4KzI7O>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:45_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Sunday Feb 12, 2017 at 17:08 GMT_

----

"We should absolutely use 0 for normal synths and 1 for desynths" I just noticed this was backwards from how it is now... why would we reverse it? 1 seems to be a more intuitive value for a "constructive" synth and 0 for a "destructive" one



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:47_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 12, 2017 at 17:22 GMT_

----

So it can be directly used as a bool when checking if its a desynth. We don't need to ask "is it a normal synth" when thats the majority situation, so we're going to be asking if its a desynth right? 1=true, 0=false. Since a bunch need changed *anyway* I'd rather just set them all in one go and use a bool. We'll never have a 3rd "type" there anyway.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:48_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Sunday Feb 12, 2017 at 17:24 GMT_

----

I don't feel terribly strong about this either way but...

My opinion - using a more intuitive value for DB contributors is more 
valuable than saving the use of a single ! in the core

On 2/12/2017 12:22 PM, TeoTwawki wrote:
>
> So it can be directly used as a bool when checking if its a desynth. 
> We don't need to ask "is it a normal synth" when thats the majority 
> situation, so we're going to be asking if its a desynth right? 1=true, 
> 0=false. Since a bunch need changed /anyway/ I'd rather just set them 
> all in one go and use a bool. We'll never have a 3rd "type" there anyway.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub 
> <github/DarkstarProject/darkstar - Issue 3544Darkstar Issue issuecomment-279233347>, 
> or mute the thread 
> <github/notifications/unsubscribe-auth/AGPFUZunr3JRtuo0Zfp11TdKybiW886Hks5rbz_VgaJpZM4KzI7O>.
>





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:49_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 12, 2017 at 17:27 GMT_

----

I don't see how zero is more intuitive, feels completely backward to me. it feels like someone will make the wrong assumption and exactly why I didn't want to do a ! or a == 0 to it. When I see it I am already thinking its an on/off for it being a desynth. /shrug



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:50_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 12, 2017 at 17:29 GMT_

----

Maybe my way of thinking of it is because I am oriented on the "default" state. Oh well.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:51_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Sunday Feb 12, 2017 at 17:33 GMT_

----

I think it's because in your mind you've already named the field `isDesynth` lol. If you think of it as `type` 1 feels like a more intuitive value for a synth that creates v. destroys, no?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:52_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Sunday Feb 12, 2017 at 17:38 GMT_

----

if you guys think it is more intuitive to contributors to rename the field and invert the values, by all means do it - I'm really just discussing this because I find the differences in perception to be interesting



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:53_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 12, 2017 at 17:39 GMT_

----

>I think it's because in your mind you've already named the field isDesynth

sort of? I think of it how I plan to use it. Which is basically the core asking the sql "is it a desynth?" And I think of positive "answers" as being 1 so..Circle of biased logic. 😄  never really thought of it in terms of create/destroy. *sploding magical crystals confuse me*



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:55_

----

<a href="https://github.com/Aethermage"><img src="https://avatars0.githubusercontent.com/u/25830539?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Aethermage](https://github.com/Aethermage)**
_Thursday Feb 16, 2017 at 21:24 GMT_

----

isDesynth makes sense because isSynth doesn't remove ambiguity any more than Type does.  

The reason you would use Synth to be 0 and Desynth to be 1 is because if we're going to use it as a flag, the flag has to refer to the name of the column. If the flag refers to a "Type" you now refer to the context of the data itself. We have two types of synthesis, one of which bears the name of the entity itself that clearly comes first to mind when considering the two types, and the second of which wasn't even a game mechanism until many years later. The only way you would consider the 0/1 false/true on/off dichotomy is if any of those made sense. They don't. It has entirely to do with what's more colloquial. The first type of synthesis is a regular synth, and the secondary type is a desynth. We don't start counting from one, we start counting from zero.

The only way around that is to name it isSynth, which technically they all are.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:56_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Thursday Feb 16, 2017 at 21:58 GMT_

----

whatever just split them into their own tables for 0 ambiguity



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:57_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Feb 16, 2017 at 22:05 GMT_

----

not going to swap the existing values - can you imagine if someone had started on a PR before and then didn't notice they were swapped while they were working on it?
to be honest, i had entertained the idea of using two tables instead of one, but i think it's more work than it's worth.  thus, the best path is just renaming "type" to something that makes more sense (and as aethermage pointed out, isSynth is out because it doesn't make any more sense)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:58_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Feb 16, 2017 at 23:31 GMT_

----

> not going to swap the existing values - can you imagine if someone had started on a PR before and then didn't notice they were swapped while they were working on it?

The values we have aren't fully consistent, has to be fixed anyway. So doesn't matter one whit whether you use zero or one there, several PRs already merged with them at zero when the older entries were one. Yeah if only there was some kind of review process.. Oh wait. 👅 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:59_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Feb 16, 2017 at 23:36 GMT_

----

2 outa 3 devs so far want zero for desynth. I don't care enough let this keep going so I'll stfu now that I've said my piece.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:00_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 17, 2017 at 00:02 GMT_

----

"We made the decision last week to flip the values of type so they're more clear, could you run a quick regex on the rows you're adding to match up?"

This assumes that there is currently someone out there in the world working on a PR for this table, right now, which realistically speaking, is low odds. And on the chance there is, it'd take them all of two minutes to flip the values to match master.

And really, it's a bit silly to make design decisions because someone might be working with something we want to change. We'd never be able to fix something that's broken!



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:02_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Friday Feb 17, 2017 at 00:11 GMT_

----

No, the concern is that, if it slips by, it goes unnoticed because the mistake is completely valid data for this table.  This is very different from changing the API of something that would no longer compile, or the structure of the table that would make it no longer insert cleanly.

And this isn't something that just happens for a week or so after.  What if someone imports some data they found on someone else's forums from years back?  Obviously we have code review, but if someone adds 3000 recipes and 100 of them have type flipped, will a reviewer notice?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:03_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Friday Feb 17, 2017 at 00:20 GMT_

----

I think demo might be right with the separate table honestly

On Feb 16, 2017 7:11 PM, "Tyler Schneider" <notificationsgithub.com> wrote:

No, the concern is that, if it slips by, it goes unnoticed because the
mistake is completely valid data for this table. This is very different
from changing the API of something that would no longer compile, or the
structure of the table that would make it no longer insert cleanly.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub
<github/DarkstarProject/darkstar - Issue 3544Darkstar Issue issuecomment-280507814>,
or mute the thread
<github/notifications/unsubscribe-auth/AGPFUYbarjOgIsVM55wHmTcm-baBgxGcks5rdOXIgaJpZM4KzI7O>
.




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 09:18:34_

----

Turns out that this [got slipped in](https://github.com/project-topaz/topaz/blob/release/sql/synth_recipes.sql#L28) two years after this issue was originally created!

See: https://github.com/DarkstarProject/darkstar/pull/6128
