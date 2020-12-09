**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Nov 12, 2020 at 04:32:57_
_Originally opened as: project-topaz/topaz - Issue 1505_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

After getting access to Dynamis and having been instructed to go get a Prismatic Hourglass, any Dynamis currency goblin in Beadeaux, Davoi or Castle Oztroja will [talk to the player about the key item](https://youtu.be/mD91QXsDvSM?t=410) at this point. Once.
After that all goblins will introduce their currency to the player. Once.
After that they will all show the menu.

This PR adds the missing events and makes it so that:
• either of the goblins will introduce the hourglass. After doing so, the others won't.
• the player may skip this dialogue by trading 50k gil right away without talking to the goblin and receiving the hourglass
• before offering the dialogue menu each goblin will introduce the currency he trades once and then never again
• after all three goblins have introduced their currency to the player the charVar responsible for this is deleted
• the player may move freely between these three in any state of this logic without messing anything up

A lot of the lines in the commit are just parenthesis clean up. The important bit is the `onTrigger()` function in each goblins script and the resulting `onEventFinish()`.
