**Labels:**

discussion



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Aug 25, 2020 at 14:08:06_
_Originally opened as: project-topaz/topaz - Issue 1003_

----

Talkin' about modules in Discord, @m241dan, @TeoTwawki .

**Basic Idea**

A _huge_ amount of content is kept within the `tpz.` namespace. It's very easy to override all of it or parts of it at launch, or at runtime. Consider `!reloadglobal x`; it just validates the file and loads it, replacing the contents of x.

If we formalise a location to keep modules, we can have mods for anything.

**Consider:** 
- Era-specific dynamis
- Swapping out loot tables
- Check modules on startup, only load certain modules on certain days (holidays, events etc.)
- Check modules every hour and see if anything needs to be unloaded, reloaded or hot-loaded in

**Easy/small possible modules for testing:**
- Changing droplists for mobs
- Restore behaviour changes in some fights to certain eras
- Holiday & event modules

**Larger ideas:**
- Land king popping

@m241dan's example module: 

https://github.com/project-topaz/topaz/pull/651/commits/7f2c967115b844a20988b2215ba6b6267cc09905

Module loading: 

https://github.com/project-topaz/topaz/pull/651/commits/6711d7d481f786a965e2d8ffe675efe22af4e7f7

**Considerations**
This will already work nicely for the things that live in the `tpz.` namespace. Things that are currently "hot-reloadable" would need a way of being overridable without a performance hit. Consider:

```cpp
    int32 OnPlayerLevelUp(CCharEntity* PChar)
    {
        lua_prepscript("scripts/globals/player.lua");
        if (prepFile(File, "onPlayerLevelUp"))
            return -1;

        CLuaBaseEntity LuaBaseEntity(PChar);
        Lunar<CLuaBaseEntity>::push(LuaHandle, &LuaBaseEntity);

        if (lua_pcall(LuaHandle, 1, 0, 0))
        {
            ShowError("luautils::onPlayerLevelUp: %s\n", lua_tostring(LuaHandle, -1));
            lua_pop(LuaHandle, 1);
            return -1;
        }

        return 0;
    }
```

How do we handle this?

**Hot-reloading**

I've had great success in other projects that have a filesystem watchdog, keeping an eye out for when you change scripts and then validating and loading them in when you do. Enabling this for debug builds or hiding behind a flag could be an option.

**Custom content**

My dream is that this allows servers to put in their era-balance changes and random custom things, keeping them exclusively in the modules subfolder. This would allow them to pull from upstream more easily without conflicts - and hopefully contribute back more because they haven't had to gut everything in-place to get the changes they want.

**Workflow**

If designed and implemented correctly, a good module system would be able to constantly be merged into release and downstream servers wouldn't notice. 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Tuesday Aug 25, 2020 at 15:27:34_

----

Side-car work: we make a lot of manual calls to SQL. We should not do this. We should have a database interface that we define are specific tasks for. This object could be then be exposed to lua in order for modules to make database changes. It would also support (for whatever reason) someone wanted to run their own database setup. The code would use the generic interface, and the actual implementation would extend whichever version they wanted to use.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 25, 2020 at 20:35:13_

----

There are a few things I would want to see core side done so that we could use them in lua after, but I struggle to adequately describe atm. Think about extending/adding more of the current hooks* that mixins use. I've also mentioned before that I'd like more things for the player object for the script end - presently we only have level up and level down to act on, and I think we'll want something that activates on players 2hrs so that we can do AV proper without editing every single 2hr script or trying to run a constant check in every tick of AV's battle script.

onAllTheThings(stuff) :+1: 


There is bound to be something people want to add that can't or shouldn't be done purely in lua for various reasons, and I've very much wanted to make a section of the core people could freely add new functionality to without polluting the other stock files. such a section could be attached to the lua end. I'm not sure trying to pure-lua a module system would be the best approach, but its better than the zilch we have currently that invites everyone to modify all the stock files to get anything cool done, then endure the MyFirstEditConflict training course, flunk it, and blame git for deleting their work/blame the project for "updates breaking my server" that I have seen these past 6 yrs or so.

Edit:
*Listeners. I forgot wtf they were actually called and keep calling them hooks coz thats what they DO.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Tuesday Aug 25, 2020 at 20:40:57_

----

Unfortunately, I'm of the mind that pure lua modules may be the only way to go. The core just isn't designed to support modules... though in saying that, we could "redesign" it to.

I think it is best at this point if we consider the core the orchestrator and the lua is the details. I'm sure there is a way we could make this done efficiently or at a minimal performance lost.

There's a lot to be explored by upgrading to sol2 v3 and changing the core to an event based orchestrator. My understanding is that the core does a lot of "let me iterate through everything in the zone even though there is a good chance it has done nothing." But that could be my ignorance.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 25, 2020 at 21:18:12_

----

I think if we fleshed out bindings a lot more or added more listeners to the core for it and weren't shy about adding more of both/either as we go retail use case or not (or did the FFI) we could do much more in lua. The previous project considered the bindings excessive and bloat so people who wanted to customize had to modify the core and would often just do the whole thing there, rather than have lua do the base logic and then the core carry the heavy lifting/repetitive parts at the binding.

> iterate through everything in the zone even though there is a good chance it has done nothing

some parts do this, and they either a)have no other way to get it done even if you moved it to lua or more often b)need to be purged with fire.

We also do some things that way in lua, which are also in need of rewriting. There are 4 things that if you see happen, is a good indication it should be changed:
1. If you iterate or loop through a massive pile of things just to find one that matches a condition you should see if you can use a keyed table instead
2. If you are asking every entity game wide whats its id or its name is you should probably be passing its entity along as a parameter instead so that you already have that object to work with
3. Checking if someone has something equipped is a good sign it should have been a modifier on the item
4. If you have to edit multiple scripts, for example ALL the weaponskill luas, to have something happen one a single mob and not any other mobs in the entire game world, that should probably just be a listener or in onWeaponskillHit at that one mob.
5. I forgot by the time I finished typing the 1st 4 but thats ok you get the idea, ima go with 4, these all have the same principles to them: doing way to much work to get the job done or not using inputs to do it
