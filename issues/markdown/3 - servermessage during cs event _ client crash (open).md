**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:14_
_Originally opened as: project-topaz/topaz - Issue 3_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 04, 2014 at 18:02 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 518_

----

There are several onZoneIn cs that can change depending on a parameter, you can see this in the Starting WotG scenes at the Cavernous Maws and also in the early ASA missions.

I started to do the work needed for this, and found I need packet info from retail - can't just recycle the startEvent coding since this is happening in CZoneInPacket and I don't know the correct hex offsets. Should be fairly simple work once the offsets are known.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:15_

----

<a href="https://github.com/gedads"><img src="https://avatars1.githubusercontent.com/u/5845173?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gedads](https://github.com/gedads)**
_Tuesday Oct 21, 2014 at 12:51 GMT_

----

yes please. let me know which packets you need. (but you can't have the wotg packets since the gob replays the first part in the present the other in the past but not onzonein).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:16_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 22, 2014 at 02:24 GMT_

----

Gedads and I spoke on irc but putting this here so anyone else looking at this issue is aware of whats up:

If retail really does this in the zone in packet like Darkstar is doing, a capture of a zone in cs should reveal the parameter fields. The ones that take params that I know of all require a new char to reach lv10 and trigger for the first time ever (replaying the cs will not use the same event type). This has made it difficult to get a packet capture.

CS I know of using params:

"A Shantotto Ascension" scene existing Windurst in which you are told to fetch 1 of several enfeeble kits.

"A Crystalline Prophecy" opening scene. (unsure what the params are, but likely its what nation missions player has cleared).

The first set of Cavernous Maw CSs for "Wings of the Goddess".




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:17_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Oct 22, 2014 at 03:09 GMT_

----

i have like 4 characters that are 99 and haven't done any of those




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:18_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 24, 2014 at 05:51 GMT_

----

Think you can capture one and pick out where the params are sometime soonish then?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:19_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 22, 2015 at 05:05 GMT_

----

gedads  starlightknight
github/DarkstarProject/darkstar/commit/48dcf3726207d13abb6e4fb28e4649e6d4d21e01
When I saw that commit I had an idea and we now have a solution, using updateEvent() in the zone scripts works, 

``` lua
-----------------------------------
-- onEventUpdate
-----------------------------------

function onEventUpdate(player,csid,option)
   -- printf("CSID: %u",csid);
   -- printf("RESULT: %u",option);
   if (csid == 0x02BC) then
      player:updateEvent(2, 0, 0, 0, 0, 0, 0, 0);
   end
end;
```

I just tested a little while ago and was able to get all effected WotG cs to display correct stuff by doing that. Should be the same for the ASA cs that was unable to display the other KI names before.

teschnei gedads and I were unable to pick out the param in the zone in packet before..I guess we were looking in the wrong place. :)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:21_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 22, 2015 at 05:08 GMT_

----

edited last comment, I R not gooder with engrish tonight




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:22_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Feb 22, 2015 at 06:48 GMT_

----

i dont think that was from a 0x60.. would have always worked (0x60 is from
updating an event using a string)

On Sat, Feb 21, 2015 at 10:08 PM, TeoTwawki notificationsgithub.com
wrote:

> edited last comment, I R not gooder with engrish tonight
> 
> —
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 518Darkstar Issue issuecomment-75420170
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:23_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 22, 2015 at 06:53 GMT_

----

I meant that it made me think of trying it, which was why I had to edit that comment. Up to now we've never had any updateEvent() uses inside a zone script.

I am all kinds of derpy from not sleeping without being woken back repeatedly with less than 2hrs rest.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:24_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Monday Apr 06, 2015 at 14:38 GMT_

----

i take it this isnt needed then? since you managed to get it to display correctly using updateEvent()




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:25_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 06, 2015 at 22:04 GMT_

----

Reopen please, because gedads discovered updateEvent() would crash him out if triggered in a zone In CS that he tripped by logging in and then never mentioned here.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:26_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Apr 06, 2015 at 22:05 GMT_

----

Is that even possible?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:28_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Apr 06, 2015 at 22:33 GMT_

----

Oh yes, it is. Maybe my friend hasn't started ASA yet and I can get her to
cap it (think there is one at the start)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:29_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 06, 2015 at 22:38 GMT_

----

teschnei unless using afterZoneIn turns out to not have issues (he told me he didn't try that) and is acceptable?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:30_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Apr 06, 2015 at 22:40 GMT_

----

It's not, unless that's how retail does it (which I doubt). The main
blocker here is I don't know which cs have to be capped to fix this, so
I've not bothered to try




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:31_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 06, 2015 at 23:02 GMT_

----

the cs for "A Shantotto Ascention" exiting windurst (where you are told which trap kit to fetch) will use a paramter, and so will the WotG misison cs triggered at the maws cs in sauramogue, rolanberry, and battallia. The opening (very first) cs of "A Crystiline Prophecy" also uses a parameter, but nobody know wtf the change  in the cs is actually dependent on (is theorized to be nation mission status).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:32_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Sunday Apr 12, 2015 at 12:49 GMT_

----

it's crashing cause of the broken /smes
seems to be caused when /smes is sent anywhere other than immediately after logging in (with the default server message)
set the server message to "message" and it works fine, though

haven't really tested to see exactly what it is causing the crash




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:33_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Monday Apr 27, 2015 at 07:39 GMT_

----

gedads cutscenes on login shouldn't crash the client anymore - get scripting




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:34_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday May 02, 2015 at 04:17 GMT_

----

not resolved. Still seeing client implode on login if cs event and server message both try and go.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:35_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2015 at 14:43 GMT_

----

Its seems to be (am not 100% on this) related to the menu prompts that soem cs (like mog house home point crap). Triggers a memory violation client side.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:37_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Thursday Jun 21, 2018 at 08:57 GMT_

----

TeoTwawki Are we still violating people's memory here? If so, do you have any reproduce steps? I am unable to reproduce.

