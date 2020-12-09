**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Sep 27, 2020 at 00:40:50_
_Originally opened as: project-topaz/topaz - Issue 1197_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

When trying to buy any EXP ring from a gate guard, and one is already found in possession of the player it can not be obtained by default. An error message is shown (see example for Port Windurst below): "**You cannot obtain the [x] band. Come back after sorting your inventory.**" This error message seems extremely inadequate. Is this retail accurate to tell the player to sort his inventory when checked for possession of another item?!
https://github.com/project-topaz/topaz/blob/249b7e54ede2c6cfae73c7c3ce7df83e408567b9/scripts/globals/conquest.lua#L836
https://github.com/project-topaz/topaz/blob/249b7e54ede2c6cfae73c7c3ce7df83e408567b9/scripts/zones/Port_Windurst/IDs.lua#L39

Just as weird appears the message printed when the current conquest tally is not yet reset and the player wants to buy another ring (which he can not):
https://github.com/project-topaz/topaz/blob/249b7e54ede2c6cfae73c7c3ce7df83e408567b9/scripts/globals/conquest.lua#L844
I don't know where to find these ID strings (would be 11952 in this case; are they client side?) but it simply prints:
"**You do not meet the requirements to purchase the [x] band**"
Which also is extremely uninformative and does not seem like something you would experience on retail.


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

- Try to buy an EXP ring from a gate guard while already owning another/same one; I have no idea what the expected message would be, but I doubt it's the one generated.
- Also try to buy an EXP ring directly after dropping one during the same conquest tally period; again same as before.




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Sep 27, 2020 at 01:13:00_

----

@MarianArlt these stringIDs are client side.

You can look at them and extract them using polutils =)

No need to rebuild there should be already a current one under releases:

https://github.com/Windower/POLUtils

#theMostLuxuriousFFXIutils


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Sep 27, 2020 at 03:15:23_

----

It would seem the one for the conquest tally period error may be correct after looking through tons of strings extracted with POLUtils...but I can not be sure without looking at retail. I mean the guard dialogue for the purchase does mention it can only be purchased and recharged once per tally, so I guess that's fair enough to just print "requirements not met". Weird move from SE, but whatever.

The first one regarding the possession of another ring could be changed to:
`player:messageSpecial(text.ITEM_CANNOT_BE_OBTAINED - 1)`
which would call: **You cannot obtain any more.**
or
`player:messageSpecial(text.ITEM_CANNOT_BE_OBTAINED - 2, item)`
which would call: **You cannot obtain the [item].**
Either way a lot less confusing than saying "Come back after sorting your inventory".

Still, in all cases I can not confirm whether this would reflect retail or not. Would be super easy to test though.
