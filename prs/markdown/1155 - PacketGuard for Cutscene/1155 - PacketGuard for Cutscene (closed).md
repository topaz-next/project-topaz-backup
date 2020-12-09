**Labels:**

exploit



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 13:37:21_
_Originally opened as: project-topaz/topaz - Issue 1155_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**Summary**
It's an allow-list for packets, validated with a non-modified retail client. If you're not on the list, you're not coming in.

**OFF BY DEFAULT**

I've opened this early because it **doesn't expose any specific exploits**. Rather, it showcases how we can stamp out a good number of current exploits. **It is not a silver bullet and will not stop bad actors from trying to mess with your server**, but it does narrow the vector that they can work with.

Once applied to trading, bazaar-ing, auction house use etc. a bunch of exploits will hopefully disappear.

**Workflow**
If enabled, when a player enters a CS their new `substate` is set to `in_cs`. While in this state, packets they send will be checked against an allow-list. Invalid packets will be dropped and reported.

In the future new states will be captured for trading/bazaaring etc. A player can only have a single state active at a time.

A player is destroyed and rebuilt on zone, so their `substate` will be reset. I don't see this as a problem, but I'm open to suggestions.

If the server is built with `PACKETGUARD_CAP_ENABLED` defined as 1, the allow-list logic will be switched off, and in its place will be a logger that collects valid packets for a given state and prints them to the console. This is hidden behind a compile definition because it is _hiddeous_ and only meant for dev machines. This is how I generated the current allow-list.

**I have tried:**
- SOA CS where you're teleported to a new zone and a cutscene starts straight away
- Cutscenes with multiple branches/options, which will call Update while they're going
- Cutscenes with different options from trades
- Transport events like teleporters
- Sending most types of messages while in CS
- Most commands while in CS (https://ffxiclopedia.fandom.com/wiki/Category:Commands)

**PERFORMANCE**
No longer used `unordered_set` because:
```
unordered_set (hash set) .find()
Average case: constant.
Worst case: linear in container size.
```

Not good enough for a lookup affecting all (or the majority of) packets. I've gone with a double `unordered_map` lookup and double checked that calls to non-existant keys don't result in keys being populated with anything strange:

```cpp
    std::unordered_map<int, bool> empty_map;
    std::cout << "Contents of non-existant key: " << empty_map[0] << std::endl;
    std::cout << "Contents of non-existant key (again): " << empty_map[0] << std::endl;

  // Contents of non-existant key: 0
  // Contents of non-existant key (again): 0
```

I wonder, should I just bite the bullet and set all of these up as vectors to avoid the hashing at lookup time?

**Rate Limiter**
Now that we're not trusting the client for _anything_, we should be rate-limiting duplicate packets from the client.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Sep 18, 2020 at 16:23:14_

----

```
0x0B6 // Tell
```

I'm _fairly_ certain party commands are allowed during CS too. These would be [0x06E through 0x078](https://github.com/Windower/Lua/blob/dev/addons/libs/packets/fields.lua#L740-L791).

But I do play on retail with `autoinvite` and `autojoin`, so my memory may be influenced through packet injections as opposed to vanilla commands. Someone may want to check with a vanilla client on retail if you can `/pcmd add`, `/join`, `/pcmd leader`, and `/pcmd leave` during a CS event (Eternal Flame in Western Adoulin counts as a CS).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Sep 18, 2020 at 16:40:09_

----

Will need one of these in server-outgoing [0x52 (NPC Release)](https://github.com/project-topaz/topaz/blob/release/src/map/packets/release.cpp) too, for event skips (hit during CS) and the !release command.

There's another packet to potentially look into too, but I'll hit you up on Discord about it.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 18:19:42_

----

I did try `/pcmd add` I think, but I will double check all of these that you mentioned, thanks!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 11:29:52_

----

Confirmed: `/pcmd leave` is `You cannot use that command at this time.`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 11:31:14_

----

Same with `/join` and all the others


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Sep 18, 2020 at 16:23:14_

----

```
0x0B6 // Tell
```

I'm _fairly_ certain party commands are allowed during CS too. These would be [0x06E through 0x078](https://github.com/Windower/Lua/blob/dev/addons/libs/packets/fields.lua#L740-L791).

But I do play on retail with `autoinvite` and `autojoin`, so my memory may be influenced through packet injections as opposed to vanilla commands. Someone may want to check with a vanilla client on retail if you can `/pcmd add`, `/join`, `/pcmd leader`, and `/pcmd leave` during a CS event (Eternal Flame in Western Adoulin counts as a CS).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Sep 18, 2020 at 16:40:09_

----

Will need one of these in server-outgoing [0x52 (NPC Release)](https://github.com/project-topaz/topaz/blob/release/src/map/packets/release.cpp) too, for event skips (hit during CS) and the !release command.

There's another packet to potentially look into too, but I'll hit you up on Discord about it.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 18:19:42_

----

I did try `/pcmd add` I think, but I will double check all of these that you mentioned, thanks!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 11:29:52_

----

Confirmed: `/pcmd leave` is `You cannot use that command at this time.`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 11:31:14_

----

Same with `/join` and all the others


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Sep 18, 2020 at 17:11:01_

----

> I wonder, should I just bite the bullet and set all of these up as vectors to avoid the hashing at lookup time?

Can add in a check to see if the char is in a sub-state before the call to valid packet list (same line as if guard enabled), to skip the look-up attempt entirely unless the character is in a substate we care about.

`if (PChar->m_Substate != CHAR_SUBSTATE::SUBSTATE_NONE)`

Not entirely certain how many cycles, if any, that _might_ save. Could potentially add cycles 🤷 .


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 18:21:23_

----

I'm imagining there will be packets we want to block, even in the default state. (trade close etc.), so I'll leave it as it is. Given how the rest of the project is, I think I've done my due diligence (so far) in saving cycles.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Sep 18, 2020 at 18:46:45_

----

Good call on blocking some packets even in default state. I hadn't considered~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Sep 20, 2020 at 15:34:26_

----

I wonder if it should be on a more minute scale, so some packets can be adjusted to be quicker without disabling rate limiting all together.

Ex: Each time a player adds an item to a player-to-player trade window, it's a new packet. I can imagine a situation in which a vanilla player could potentially add items to the window in sub-second rates (especially with controller/keyboard). But at the same time, you don't want an injector to be able to outright flood 10+ in a single second. Although, admittedly, a vanilla player adding 2 items to a trade window in a second would be pretty hard to do.

Some servers are more lenient with GearSwap too, and might want to allow sub-second swaps without completely turning the rate limiter for the packet off.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 21, 2020 at 05:29:04_

----

Then I wonder, should I tune this to work with the most common and accepted plugins that affect packet flow?
I think packets-per-minute is a good idea, but should exist alongside the outright cooldown timer. 
+1 for people operating very quickly using a controller.

I'm somewhat reluctant to break out the fine-grained control of this into a settings file, or and existing settings file.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Sep 21, 2020 at 08:57:50_

----

I think you're fine without a settings file; servers that really care about allowing/disallowing addons should be able to edit and recompile directly. Can always put the definitions in a standalone header if people are worried about git poisoning.

Default timings based on popular addons might be a source of contention. We'd have room to give just about any timing that we'd prefer to let certain addons work out of the box (like GearSwap) - there's the ultimate argument of "it works on retail".

But then someone might come along and claim that retail doesn't have this packetguard system at all, making the whole thing non-retail (maybe?), so why not "take it further" to prevent "cheating elitist gearswapers" from having an advantage... etc etc. You might be surprised how contentious GearSwap can be among the "era" community (_actual retail_ players... not so much).

My opinion is that if an addon is in Windower's default addon list, it should probably work on Topaz by default. GearSwap, Organizer, Treasury, etc. If a server admin wants to make their players' gameplay experience worse, they can deal with editing a header and recompiling.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 21, 2020 at 10:00:22_

----

> My opinion is that if an addon is in Windower's default addon list, it should probably work on Topaz by default. GearSwap, Organizer, Treasury, etc. If a server admin wants to make their players' gameplay experience worse, they can deal with editing a header and recompiling.

Agree on all of this


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Sep 23, 2020 at 03:26:06_

----

Opinions: 

1. def don't add to our existing settings for it, either give it a new one or let people eat header file edits. This stiff isn't for the average newbie and they shouldn't try to mess with it till they know what they are doing. I think if it looks to easy to set up, they'll do things they shouldn't and not understand why the "server is broken".

2. As far as retailness..
> someone might come along and claim that retail doesn't have this packetguard system at all, making the whole thing non-retail (maybe?),  

Retail does a ton of dumb client trusting and has a lot of exploits/cheats that still work to this day. They only patch them when something serious makes waves and they can't ignore it (dynamis D medal dupes) and most of the ones they are aware of, they just log and ban later. A select few just drop you instantly to Mordion at the NPC GM\*. Private servers don't have the manpower to run their own version of the STF to poor through logs constantly - screw that I do too much of that already and I loves me some some automation. 

> You might be surprised how contentious GearSwap can be among the "era" community

Those ppl and the arguments they have make me a sad Teo. But yeah that's a.. a thing.. Let the defaul stuff through and anything you deem sane. And don't forget a lot of us are on Ashita instead of windower, thanks.

###### .

\*Btw that NPC GM:
> Your character has been jailed due to prohibited activities. Your account will soon be suspended due to this violation.
Dependant upon the outcome of the investigation, your account may also be banned. We will not be accepting any GM calls from this account at this point in time.
Once your suspension has been processed and lifted, login and place a GM call to be removed from jail. You will automatically be transferred back to your home point.

That's it's full dialog. It's the only thing in the room they drop you in. When you try to leave by any means, including if you happen to get zoned in while poison/bio/whatever and die, you rubber banded right back where you "exited" at and receive this message:
> Any attempt at escape is futile!




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 26, 2020 at 05:50:02_

----

Update (as I go through my weekly rounds of the recent PRs): 
Been working on other stuff, no progress here, will probably come back next week (important to keep the scope to _just_ CS blocking. The rate limiting is nice, but there's a lot of risk, so it'll be off for everything by default in this PR.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 04, 2020 at 08:25:08_

----

Since this is "off-by-default" I'm going to merge it and leave it on for all of my local testing for other things. I'll also ask some more experimental servers to turn it on after the next release and see how much it breaks...
