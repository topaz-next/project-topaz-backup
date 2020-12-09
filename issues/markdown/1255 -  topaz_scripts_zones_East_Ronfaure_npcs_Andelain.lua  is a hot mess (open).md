**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 05, 2020 at 17:04:04_
_Originally opened as: project-topaz/topaz - Issue 1255_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Related: #669

cs event 19 isn't even a valid cs event for that zone. it will lock up your client till you hit escape or are otherwise released from the non-existent event. Those showText commands shouldn't be there either. The correct cs event ID will likely account for all of those messages. Running the messages with messageSpecial loses the NPC name, which is a strong indicator those shouldn't be forced text messages at all.

```json
    <field name="index">7412</field>
    <field name="text">My name is Andelain. As part of my devotions, I come here each day to pray.≺Prompt≻

    <field name="index">7413</field>
    <field name="text">During this time, I may eat only three ≺Possible Special Code: 01≻≺Possible Special Code: 05≻%≺BAD CHAR: 8280≻≺BAD CHAR: 80≻≺BAD CHAR: 80≻ a day for nourishment. No more, no less. And no other food may I eat.≺Prompt≻

    <field name="index">7414</field>
    <field name="text">Thanks be to the Goddess in her benevolence!≺Prompt≻

    <field name="index">7415</field>
    <field name="text">I am currently undergoing devotions, and as such, am not allowed to take alms from those on the road. I am sorry, but I cannot accept this.≺Prompt≻

    <field name="index">7416</field>
    <field name="text">May the Gates of Paradise open to all...≺Prompt≻

    <field name="index">7417</field>
    <field name="text">I appreciate your offer, but I only need one ≺Possible Special Code: 01≻≺Possible Special Code: 05≻#≺BAD CHAR: 8280≻≺BAD CHAR: 80≻≺BAD CHAR: 80≻. Thank you for your kindness.≺Prompt≻
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 05, 2020 at 17:10:11_

----

https://github.com/KnowOne134/FFXI_Events/blob/master/east_ronfaure.json#L1831

event 19 may be one of those ones we could not extract and do not handle properly,


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Oct 10, 2020 at 07:26:25_

----

Tested this earlier this evening.  Event 19 is the animation where Andelain raises his arms in the air.  No associated text appears when it plays.

I searched events 1 through 1000 and couldn't find any that played Andelain's dialogs, so it's probably a very large event ID that will need retail capping --  @project-topaz/researcher -- or possibly not an event, and we gotta keep doin' it how we are (but with updated and IDs.lua'ed numbers)

edit to add: I also tried passing various parameters into event 19, but the ones I tried didn't do anything.
