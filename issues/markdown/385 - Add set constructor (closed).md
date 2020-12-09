**Labels:**



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 23, 2020 at 15:08:09_
_Originally opened as: project-topaz/topaz - Issue 385_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

@zach2good I'm coming for your Rhapsodies PR~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 26, 2020 at 21:21:44_

----

So currently, a lot of scripts do something like this:
```lua
good_things =
{
    "cookies",
    "cake",
    "pie"
}

giveToNPC = function (player, npc, item)
    local gave_good = false
    for _, thing in pairs(good_things) do
        if thing == item then
            gave_good = true
            break
        end
    end
    if gave_good then
        player:showText(npc, I_LIKE_THIS)
    else
        player:showText(npc, I_DO_NOT_WANT)
    end
end
```

The above is quite silly. Every time a player gives an item to an NPC, you have to loop through the entire table every time - up to the number of items in the table if they did not give a good thing - and do your comparisons on every item until you find (or don't) the thing you're looking for.

So instead, with a set constructor - which builds a table of `true` values, with keys based on what you intend to compare against - you can check if something is a member of that "set" of items with a single operation. A key in the resulting table will return `true`, and if a key isn't in the table, the lookup will result in `nil`, evaluating to `false`:
```lua
good_things = set{
    "cookies",
    "cake",
    "pie"
}

giveToNPC = function (player, npc, item)
    if good_things[item] then
        player:showText(npc, I_LIKE_THIS)
    else
        player:showText(npc, I_DO_NOT_WANT)
    end
end
```

This results in code that's easier to follow, _and_ saves processing time when your script is running later.

The astute reader might say, "but with the constructor, you're always going to loop through the entire table when you build the set". This is true - but if the set is being defined as part of a global which is then loaded via `require`, it will only be stepped through once. When Lua loads a script/package through `require`, it will keep it in memory (until an event happens which triggers garbage collection).

The end result is you go through all items in the set when initially creating the key->`true` table, but when your functions are called later, checking is just a single operation.
