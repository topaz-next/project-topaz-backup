**Labels:**

discussion



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Aug 25, 2020 at 08:21:16_
_Originally opened as: project-topaz/topaz - Issue 1001_

----

I like this format for discussion so things don't get lost in Discord.

===

**What?**

You may have poked around in Core's `common` area, or looked in `map/lua` and seen literally a billion bindings. These are what is required in order to register these Core functions for use in Lua. These have all been working fine _forever_. My issue comes with when I'm trying to create a nice flexible and extensible object in Lua and pass it back into the Core for use. 

**Example from Trust Advanced Gambits:**

https://github.com/project-topaz/topaz/pull/780/files#diff-89a95d61edadcc18eafd55b82089169eR12426

Having to take `lua_State* L` and manipulate it by hand is fine when you're just saying: If there is a number at argument 1, give me that, otherwise die. But for my use case, this is prohibitively difficult.

===

**Proposal**

Replace the small single header `lunar.hpp` with the single-header distribution for Sol2 (Sol3) and patch everything up.  It has support for everything we currently do, and enables much easier interaction with the Lua state.

I still need to investigate the state of debugging, but currently - it's nest to impossible to debug whats going on on the Lua stack (at least to me).

**Dealing with tables:**

```cpp
sol::state lua;
lua.safe_script("conf.lua");
sol::table conf_table = lua["conf"];

for (const auto& key_value_pair : conf_table ) {
     sol::object key = key_value_pair.first;
     sol::object value = key_value_pair.second;

     // inspect key/value, manipulate as you please
}
```

===

**Edit additional note:**

Sol2/3 can exist alongside any current Lua/C/C++ wrapper system.  It can create a view around a Lua_state which will then provide all the cool tricks. It isn't a "quick, do the switchover! Oh no, a million conflicts" transition process.

===

**What about FFI?**

That's a discussion for a different day.

===

**Sol2 (Sol3) Examples**

https://github.com/ThePhD/sol2/tree/develop/examples/source


Basics

https://github.com/ThePhD/sol2/blob/develop/examples/source/basic.cpp

Custom Usertype

https://github.com/ThePhD/sol2/blob/develop/examples/source/usertype_basics.cpp

Interacting with Tables

https://github.com/ThePhD/sol2/blob/develop/examples/source/tables.cpp

Calling Lua Functions

https://github.com/ThePhD/sol2/blob/develop/examples/source/calling_lua_functions.cpp

===

**Links**

**Lunar**

http://lua-users.org/wiki/CppBindingWithLunar

**Sol2 (Sol3)**

https://github.com/ThePhD/sol2

===


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Tuesday Aug 25, 2020 at 12:37:05_

----

It will likely be a ton of work but I think this is a really good plan. Especially since it will allow us to use coroutines which would really help us when writing certain scripts.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Aug 25, 2020 at 12:40:24_

----

Updated my original post with this:
```
Sol2/3 can exist alongside any current Lua/C/C++ wrapper system.  It can create a view around a Lua_state* which will then provide all the cool tricks. It isn't a "quick, do the switchover! Oh no, a million conflicts" transition process.
```


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Aug 30, 2020 at 00:28:35_

----

Sol3 looks like a great system, I think this would be a solid win. As Zach rightly points out, new segments can use Sol while still maintaining Lunar for legacy code!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 08:00:45_

----

I may continue with this in a few weeks, I want to see if I can hijack the existing binding macros.
