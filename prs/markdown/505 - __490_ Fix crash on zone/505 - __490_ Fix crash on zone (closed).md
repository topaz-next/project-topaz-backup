**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Apr 18, 2020 at 06:51:02_
_Originally opened as: project-topaz/topaz - Issue 505_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #490 

Not yet tested, but given @Kreidos did some digging and it looks like this check will guard against looking at `loc.zone` while it's `nullptr`. Will try and get set up to do some testing later, unless someone else gets to it first.

The existing guarding getter:
```
uint16 CBaseEntity::getZone()
{
    return loc.zone != nullptr ? loc.zone->GetID() : loc.destination;
}
```


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Apr 18, 2020 at 10:03:05_

----

I did some testing and unfortunately I was still able to reproduce the crash. I have updated #490 with details.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 18, 2020 at 10:28:01_

----

So, there are now two crashes in here that are fixed:
If you were running a debug build and teleported with a Trust in your party, it would try and teleport the trust and check to see if the trust had the right key item. This triggered a debug break. Letting the trust through is fine, because it will try and fail to cast the entity into a char, and return false anyway. It's a little hacky, but is probably fine as a quick fix.

The second bug was trying to access the PLeader in a party while zoning and they weren't available. This check was needed to see if the party definition packets that have information about trusts needed to be sent. I did a little cleanup of that interface and the whole flow is a little better now. 

Hopefully those crashes are squashed now.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 18:34:03_

----

I rebased from canary back onto trust~

I wonder if we're falling into a trap re: the key item checking. While `hasKeyItem` returning false for trusts _is_ a valid answer to the explicit question the programmer is asking, letting trusts through might obscure causes of problems later - for example, what will happen if a player with trusts tries to enter content where everyone requires a KI?

Potentially outside of the scope of this PR, but the subject of teleports has me thinking: What happens if a player casts Warp II on a trust? Retrace? Escape?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 00:48:23_

----

> I rebased from canary back onto trust~
> 
> I wonder if we're falling into a trap re: the key item checking. While `hasKeyItem` returning false for trusts _is_ a valid answer to the explicit question the programmer is asking, letting trusts through might obscure causes of problems later - for example, what will happen if a player with trusts tries to enter content where everyone requires a KI?
> 
> Potentially outside of the scope of this PR, but the subject of teleports has me thinking: What happens if a player casts Warp II on a trust? Retrace? Escape?

when they first came out, just to see wtf happened I tried it. with most spells I could not target them. AoEs like teleport-dem -did- hit them tho, and after a few tries saw my trusts despawn before I myself got zoned. SO I think they answer is they despawn.

As far as non spell teleport pads, if there is a zone change they get left behind and then despawn. if there is not a zone change, they get re-positioned around you as if you ran really far at high speed. occasionally one gets left behind and lost (stop being a ditz kupipi, get up here and heal me!) which I think was because my new position wasn't far enough from her old position or another position update hit her just prior and the AI got confused. I had to go use the despawn all /command and recast to get my ducklings in a row again.
