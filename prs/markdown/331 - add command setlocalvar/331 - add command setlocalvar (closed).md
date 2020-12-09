**Labels:**



<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Jan 23, 2020 at 16:59:15_
_Originally opened as: project-topaz/topaz - Issue 331_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

add the commands to check and set local vars on any entity in normal field and in instanced zones


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:40:27_

----

Would `if zone:getType() == tpz.zoneType.INSTANCED then` work here? (And in `!setlocalvar` too)

(May need to change the `zone` declaration above from` getZoneID` to `getZone`)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:43:01_

----

Can save a line by breaking this outside after the end of the `if` check and deleting L68 below~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:44:33_

----

Left a debug `printf` in~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:52:02_

----

Since the "ID" field for this (and `setlocalvar` below) can double as a name field, should the description say `<name/ID>` instead of just `<ID>`?

@project-topaz I want to say the existing convention from other commands is listing optional variables inside curly brackets (ex: [addcurrency](https://github.com/project-topaz/topaz/blob/master/scripts/commands/addcurrency.lua#L14), [checkvar](https://github.com/project-topaz/topaz/blob/master/scripts/commands/checkvar.lua#L14)). Do we want to keep it that way (so `!checklocalvar <variable name> {'player', 'mob', or 'npc'} {name, or ID}`), or make optional vars explicit by using the word?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:54:18_

----

`<value>` instead of `<variable number>` is shorter and might be more clear~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:56:04_

----

Left a debug `printf` here too~! 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 18:03:41_

----

Might be able to make this a little more clear by bringing this up to form an `else` for the `arg2 == nil` check above:

```lua
    if arg2 == nil then
        targ = player:getCursorTarget()
        if targ == nil then
            error(player, "no target")
            return
        end
    elseif arg3 == nil then
        error(player, "no name or ID given for target")
        return
    end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 18:12:05_

----

I'm not too familiar with how instance functions work, but if `arg3` is defined as a string (`parameters = 'sss'`), does it need to be cast to a number before doing bitwise operations on it?

(And `dsp.` is now `tpz.`)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 18:15:35_

----

Can save _six_ lines by breaking this outside of the parent if (so below the `end` for the is-in-instance check) and cutting lines L72-L77 below~!


----
<a href="https://github.com/project-topaz"><img src="https://avatars0.githubusercontent.com/u/57245158?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [project-topaz](https://github.com/project-topaz)**
_Friday Jan 24, 2020 at 09:00:02_

----

Let's stick to existing convention for now. When we start the documentation project we might adopt another method for specifying optional variables. Staying consistent will help us find and update them later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:40:27_

----

Would `if zone:getType() == tpz.zoneType.INSTANCED then` work here? (And in `!setlocalvar` too)

(May need to change the `zone` declaration above from` getZoneID` to `getZone`)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:43:01_

----

Can save a line by breaking this outside after the end of the `if` check and deleting L68 below~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:44:33_

----

Left a debug `printf` in~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:52:02_

----

Since the "ID" field for this (and `setlocalvar` below) can double as a name field, should the description say `<name/ID>` instead of just `<ID>`?

@project-topaz I want to say the existing convention from other commands is listing optional variables inside curly brackets (ex: [addcurrency](https://github.com/project-topaz/topaz/blob/master/scripts/commands/addcurrency.lua#L14), [checkvar](https://github.com/project-topaz/topaz/blob/master/scripts/commands/checkvar.lua#L14)). Do we want to keep it that way (so `!checklocalvar <variable name> {'player', 'mob', or 'npc'} {name, or ID}`), or make optional vars explicit by using the word?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:54:18_

----

`<value>` instead of `<variable number>` is shorter and might be more clear~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 17:56:04_

----

Left a debug `printf` here too~! 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 18:03:41_

----

Might be able to make this a little more clear by bringing this up to form an `else` for the `arg2 == nil` check above:

```lua
    if arg2 == nil then
        targ = player:getCursorTarget()
        if targ == nil then
            error(player, "no target")
            return
        end
    elseif arg3 == nil then
        error(player, "no name or ID given for target")
        return
    end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 18:12:05_

----

I'm not too familiar with how instance functions work, but if `arg3` is defined as a string (`parameters = 'sss'`), does it need to be cast to a number before doing bitwise operations on it?

(And `dsp.` is now `tpz.`)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 23, 2020 at 18:15:35_

----

Can save _six_ lines by breaking this outside of the parent if (so below the `end` for the is-in-instance check) and cutting lines L72-L77 below~!


----
<a href="https://github.com/project-topaz"><img src="https://avatars0.githubusercontent.com/u/57245158?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [project-topaz](https://github.com/project-topaz)**
_Friday Jan 24, 2020 at 09:00:02_

----

Let's stick to existing convention for now. When we start the documentation project we might adopt another method for specifying optional variables. Staying consistent will help us find and update them later.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Friday Jan 24, 2020 at 13:01:53_

----

All looks good to me


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Friday Jan 24, 2020 at 18:35:13_

----

Tested and working . Approved 
