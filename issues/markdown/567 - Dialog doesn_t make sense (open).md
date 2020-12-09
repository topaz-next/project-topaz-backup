**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 02, 2020 at 05:04:08_
_Originally opened as: project-topaz/topaz - Issue 567_

----

https://github.com/project-topaz/topaz/blob/c52431e2c48516954aa2f5ebbb331238f43cc3d8/scripts/zones/Southern_San_dOria/npcs/Taumila.lua#L35

If your fame happens to be  < 3 in sandoria he will  say:

        {
          "id": 571,
          "dialogue": [
            {
              "id": 7957,
              "string": "1\u0000\u0007Bring me three more, and I'll be happy to take them. You just drop by and we'll do business, eh?"
            }
          ]

as if you have already completed the quest.

Most likely the dialog when PC is lower equal 2 sandoria fame is:

              "id": 7949,
              "string": "1\u0000\u0007Dear, dear me. If only an adventurer would help me..."

though i'm not sure, it's just an assumption. But def his default dialog when fame is lower than 3 is bad.

This was brought up by Kaede at the Canaria server.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Saturday May 02, 2020 at 05:23:35_

----

I'm guessing if you don't have enough fame you get message 7959 `I am Taumila, the owner of this establishment. Talk to the lady behind the counter if you wish to make a purchase.≺Prompt≻` Looking at the event IDs I'm guessing 571 = after completion, 572 = quest completion, 573 = try trading less than 3 fangs, 574 = first time accepting the quest, 575 = quest already accepted. 571 looks like it might reset back to maybe 574 or 575 after zoning.
