**Labels:**

bug

good first issue



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Sep 11, 2020 at 18:06:39_
_Originally opened as: project-topaz/topaz - Issue 1099_

----

Glenne.lua

```
function onTrade(player, npc, trade)
    if (player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.A_SENTRY_S_PERIL) == QUEST_ACCEPTED and
        trade:hasItemQty(601, 1) and count == 1) then
            player:startEvent(513)
            npc:wait()
    end

end
```

Even when I traded "Ointment Case" to Glenne, there was no response.
There is a "count == 1" condition, but the "count" variable appears to be undefined.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Sep 11, 2020 at 18:17:05_

----

Welcome! Thanks for reporting this, @eyes-and-brain 


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Sep 11, 2020 at 18:54:14_

----

I always like to find what exactly happened in these cases... for this NPC a long time ago there used to be a local variable declared in the onTrade function, ``local count = trade:getItemCount();``

Mystery solved.. this just needs to be given some 2020 attention.
