**Labels:**

exploit



<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zircon-tpl](https://github.com/zircon-tpl)**
_Tuesday Jul 14, 2020 at 21:00:39_
_Originally opened as: project-topaz/topaz - Issue 849_

----

Project Topaz was recently informed of an exploit in which any player using a widely available client plugin may create a situation in which they may duplicate items. **This duplication exploit allows players to bazaar items without losing them, and also allows duplication of any item which may be traded.**

This is a resolution which will prevent the exploit and display notices that a player is attempting it.

**As far as we are aware, this exploit is possible on all servers derived from Darkstar Project. It is not an exploit unique to Project Topaz.**

We have already informed the operators for all servers derived from Darkstar Project of which we are aware. These servers have had advanced notice to apply this patch, and servers that have applied it will receive notifications in their server logs should a player attempt the now-patched exploit.

**As of this time Project Topaz will not be revealing the exact instructions for how to reproduce this exploit to the broader public.** This is to give server operators who we have not contacted additional time to apply the patch from this Pull Request. Should you have theories as to how this exploit was produced, please do not publicly speculate as to the method.

**Project Topaz will disclose the exact reproduction steps for the exploit within the next few days.**

Should you operate a server, please be aware that we did reveal the exact reproduction steps to the servers we contacted so that they may confirm the issue affects their server. **As we increase the number of people who are aware of the exploit -- and now provide this patch publicly -- Project Topaz can not guarantee that those who might take advantage of this exploit will not learn how to reproduce it.**

If your server does not currently address this exploit, we recommend updating as soon as possible.

Discussion on this Pull Request will be locked. Should you wish to provide input or additional knowledge regarding this exploit -- or any other exploit -- we ask that you please contact an official Staff member of Project Topaz in private. These members may be discovered through the following group: @project-topaz/staff.


----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Tuesday Jul 21, 2020 at 01:07:52_

----

**We will now disclose the exploit.**

Upon receiving a "trade update" packet from a client, the server attaches a "reserve" to the item. This is intended to prevent the "reserve amount" from being used elsewhere. When the server receives a "trade update" packet with an item quantity of zero -- sent by normal clients to indicate that the trade slot should be emptied -- this "reserve" is removed.

The exploit this patch addressed had two aspects, and involved usage of Ashita's Bellhop, which is designed to simplify trade transactions. When Bellhop updates items in a trade window, it does not first send a "zero quantity" update to the server -- instead it informs the server that a new item is in the trade slot. We believe this capability is accurate to retail, and that any addon may also achieve this.

As the server previously operated, should an update packet of quantity zero never be received the "reserve" on the previous item was never removed. This was instrumental in replicating the exploit, and has been remedied. Items which have been placed in a trade window will have their "reserve" removed when a new item is placed in the same slot.

Servers with the patch in this Pull Request will receive the following message in their server log should this be attempted:
> [Error] SmallPacket0x034: Player <name> trying to update quantity of a RESERVED item! [Item: <id> | Trade Slot: <number>]

**As we believe it to be accurate to retail behavior, the server takes no action to prevent the "trade update". Server administrators may choose to modify this detection to take action on the player.**

The second aspect of the exploit involves checks for if an item has a "reserve amount". Many aspects of the server check the "reserves" of an item before interacting with them -- for example, NPCs will not purchase items that are marked as reserved. Previously, bazaars were not one of these aspects. A player could place a "reserved" item in their bazaar to sell it. The item would not be removed from their inventory upon sale. This has also been remedied. Should another exploit be found which creates a leftover "reserve" amount, the items may not be added to a bazaar and duplicated through one.

The following is a video demonstration prior to these remedies. We provided this video to server administrators so that they may know replication steps and could confirm their server was affected.

<https://youtu.be/8m1qL8NRask>

**As Project Topaz has now publicly disclosed the exploit with its exact replication steps, we strongly encourage patching any server you operate have you not already done so.**
