**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:38_
_Originally opened as: project-topaz/topaz - Issue 4_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Dec 03, 2014 at 02:36 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 607_

----

Since forever basically, there has been a bug where your inventory count gets stuck until you hit sort, which causes the game to think your inventory is full (which it likely IS, and you just can't see it). This has side effects like invisible items and stackable items not stacking automatically so the player looks at their inventory and think they have however many slots free while their treasure pool hits the dirt.

If this has already got a github issue, its buried farther back than I care to browse. I was just talking to someone about this and was reminded it still wasn't fixed, and its a really old bug now so I thought I'd give it some attention here as its beyond my knowledge to fix




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:39_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Dec 03, 2014 at 05:31 GMT_

----

would like to see at least some sort of hint on how to reproduce




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:40_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Dec 03, 2014 at 06:10 GMT_

----

I honestly don't know how you've been unable to reproduce it. Any time people have a lot of loot dropping fast, it happens quickly and easily.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:41_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Dec 03, 2014 at 07:01 GMT_

----

i don't see it happen because i don't play on darkstar servers
if you can find a reliable way to make it happen, i can fix it easily




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:42_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Dec 03, 2014 at 07:07 GMT_

----

This is like the auto homepoint bug - it just happens a lot, but nobody can say for sure WHY it happens. :/ 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:43_

----

<a href="https://github.com/Scavenge"><img src="https://avatars2.githubusercontent.com/u/9778206?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Scavenge](https://github.com/Scavenge)**
_Wednesday Dec 03, 2014 at 09:55 GMT_

----

i can confirm this, a common scenario that it's probably noticed most easily being you are 79/80 and you will see that you obtained something but not see it in your inventory, which is still reporting 79/80 like before.  hit sort and it updates to showing things correctly.  or the opposite where you can't buy something due to full inv but it shows 79/80 until you sort.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:44_

----

<a href="https://github.com/Novah1"><img src="https://avatars2.githubusercontent.com/u/7852285?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Novah1](https://github.com/Novah1)**
_Wednesday Dec 03, 2014 at 17:18 GMT_

----

Similarly, there are times when you'll receive an item through trade or via additem, and it won't appear in your inventory, until you sort it. I don't know if this is related




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:46_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Dec 03, 2014 at 19:37 GMT_

----

novah1 thats from the trade or additem happening after this bug has already triggered.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:47_

----

<a href="https://github.com/Vivitarut"><img src="https://avatars2.githubusercontent.com/u/9279896?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Vivitarut](https://github.com/Vivitarut)**
_Thursday Dec 04, 2014 at 17:15 GMT_

----

I just reproduced the problem in Giddeus by killing Yagudos, a bunch of gear and bard spells dropped but not in inventory until sorted.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:48_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Dec 14, 2014 at 03:18 GMT_

----

So far the only thing I can consistently say when this triggers, is I've been killing mobs for at least 30 min and the closer my inventory is to 80, the more likely to see it I am (at 72/80 items and 30 min playtime, every single drop does it for me).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:49_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Dec 14, 2014 at 03:37 GMT_

----

i suppose i should be more clear: steps to reproduce _FROM LOGIN_ make this a lot easier

if you can log in with 72/80 and it doesn't work, then we have issues




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:50_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Dec 14, 2014 at 03:50 GMT_

----

FROM LOGIN its random. If anyone knew a precise trigger you'd be seeing a pull request instead of a bug report. 

Edit: but even first kill of the day has a pretty high chance of seeing it, but there is no single thing I can point to and for certain say AHA! THERE IT IS!




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:51_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Dec 14, 2014 at 03:55 GMT_

----

I want to say reducing total inventory back down is reducing the chances, but I can't prove that - I may just be being lucky -_-




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:52_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Dec 19, 2014 at 07:19 GMT_

----

Ok, I can now say theories about it being related to time or inventory free space are now both debunked. At least :/ 

Still no idea why its happening my own chat just has it happening form the moment he logged it today every item that drops to me from loot pool not showing in my inventory till I sort, even if I empty inventory. Re-logged character and still happened, which begs the question why so many other times it doesn't happen at all for many hours. >.< and you know its going to randomly go away and then not happen when I'm trying to find a cause >.<




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:53_

----

<a href="https://github.com/Cloudef"><img src="https://avatars2.githubusercontent.com/u/480330?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Cloudef](https://github.com/Cloudef)**
_Sunday Mar 29, 2015 at 12:27 GMT_

----

Could this be dropped packets?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:55_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Mar 29, 2015 at 19:52 GMT_

----

dropped packets aren't really a thing in DSP - it'll keep resending the
packet until you get it

On Sun, Mar 29, 2015 at 6:27 AM, Jari Vetoniemi notificationsgithub.com
wrote:

> Could this be dropped packets?
> 
> —
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 607Darkstar Issue issuecomment-87404427
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:56_

----

<a href="https://github.com/Ma77o"><img src="https://avatars2.githubusercontent.com/u/13141216?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Ma77o](https://github.com/Ma77o)**
_Thursday Jul 02, 2015 at 16:40 GMT_

----

I'm going to finish setting up my local environment and will get to testing on this.The only thing I'm seeing that looks strange so far is below:

Free Slots is determined below

```
uint8 CItemContainer::GetFreeSlotsCount()
{
    return m_size - m_count;     (Max Size - Inventory Count)
}
```

m_count is incremented in the CItemContanier::InsertItem function
/src/map/item_container.cpp - Line: 179

```
else if(m_ItemList[SlotID] != nullptr && SlotID != 0)  m_count--; (If the itemList in that slot isn't null, reduce count)
```

I can understand NOT increasing the inventory count if an item was already accounted for, but decreasing it in this situation doesn't seem correct. I'm not sure what anomaly may cause this situation, perhaps the other instance of CItemContainer::InsertItem accounted for that item already. (it assigns m_itemList[SlotID]) It seems very random an sporadic as to when this happens to my inventory in game.

To expand on this, if it's going into this else statement it was never incremented in the original if statement. Perhaps this dev was under the impression he was incrementing it a second time mistakenly, and as such reduced it if the item was indeed accounting for. Whereas he should simply leave it as accounted.

I'll test a few changes out and report my findings soon.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:57_

----

<a href="https://github.com/Ma77o"><img src="https://avatars2.githubusercontent.com/u/13141216?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Ma77o](https://github.com/Ma77o)**
_Thursday Jul 02, 2015 at 17:02 GMT_

----

I have auto sort enabled through all of this, so I'm going to review that code and others to find out which function is being called. The prior instance of InsertItem has 
`DSP_DEBUG_BREAK_IF(PItem == nullptr);`
But the second instance of the function does not. There's simply an if statement making sure it's not null, but further in the script (outside of this if) it assigns the item to the SlotID  (even if it were a nullptr).

So invisible/missing items may not be the case here, it may be incrementing m_count because the slot is null, and then when it assigns the item (potentially null) it remains null and we've effectively increased our inventory count without any new items.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:58_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Friday Jul 03, 2015 at 10:54 GMT_

----

edited your comments so it's easier to see the code :)
(use three backticks before the code, and three after it to make it easier to tell code apart from regular text)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:59_

----

<a href="https://github.com/Ma77o"><img src="https://avatars2.githubusercontent.com/u/13141216?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Ma77o](https://github.com/Ma77o)**
_Saturday Jul 04, 2015 at 07:17 GMT_

----

Thank you! Still getting used to this site. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:01_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Mar 20, 2016 at 00:54 GMT_

----

Darkstar Issue 2876 definitely sounds like the same thing happening when crafting adds to inventory.


