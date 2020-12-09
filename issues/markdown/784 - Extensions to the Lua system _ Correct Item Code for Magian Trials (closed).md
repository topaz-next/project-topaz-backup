**Labels:**

approved



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Tuesday Jun 30, 2020 at 04:38:42_
_Originally opened as: project-topaz/topaz - Issue 784_

----

These were developed as a required part of the Magian system which @Apocarypse is working on, but I will PR it separately for comment, and so those who voiced a desire to use it from the discord may start putting it to work sooner! This fixes the Trial Number code for items + includes Lua hooks for reading them. As well it allows the creation of ephemeral item objects in Lua from just an item number. This allows full access to the item lua lookup functions without possessing the actual item. I feel this has wide-reaching potential for use.

### New Lua Functions:
```
GetItem(ITEM#)                              // Returns a default item object of the specified type
player:getEquippedItem(SLOT)                // Returns the item object from specified slot
item:getBasePrice()                         // Returns the base price of the item
item:getTrialNumber()                       // Returns the Trial Number on the item
item:getReqLvl()                            // Returns the lvl required to wear an item
item:getILvl()                              // Returns the item's ilvl
```
### Considerations
The item objects returned by GetItem() do not exist in-game. They are pointers to the global default item array and are intended to be used to READ ONLY and should not be modifiable. Currently there is only one item function which can modify lua item objects: `addMod()`. A method now exists to identify these item pointers and I've modified `addMod()` as an example of how any future 'writing' functions should check for and refuse to write to these kinds of objects. I can't think of any reason anyone would have cause to modify an item that doesn't exist in-game but never hurts to be cautious.
