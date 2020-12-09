**Labels:**

reviewed



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Wednesday Nov 11, 2020 at 22:22:56_
_Originally opened as: project-topaz/topaz - Issue 1504_

----

Needed for @kaincenteno and his in-progress work on Login Points. Simple Lua hook to return the Unix timestamp of the last online time.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 05:54:58_

----

`static_cast` forces the cast without any checking, so if debug breaks are off and a mob is passed in here, this check will still pass. Granted, it'll get caught by `PChar->objtype == TYPE_PC`, but it's a practice we shouldn't be relying on;

```cpp
if (auto* PChar = dynamic_cast<CCharEntity*>(m_PBaseEntity))
{
    ....
}
```

will honour nullptr, and check that the pointer is in the same inheritance tree, rather than hard-casting the pointer by virtue of them being the same size.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 06:19:15_

----

Almost, after `dynamic_cast`, these checks are redundant; as they're implied by `dynamic_cast`: `PChar && PChar->objtype == TYPE_PC`

All you need is:
```cpp
if (auto* PChar = dynamic_cast<CCharEntity*>(m_PBaseEntity))
{
...
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 06:34:06_

----

Ah, just saw your comment:

> TYPE_PC check needs to stay, since lua_baseentities could be other types and only PCs have valid online times.

`dynamic_cast<CCharEntity*>` will only return a 'usable' pointer if the target has vtable entries and memory allocated for the type it's trying to cast to, otherwise it will fail. Like you mention; `static_cast` will just smush the pointer into the new type and hope for the best. It would have the base class available, but would fail when it tries to get anything from `CharEntity`.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Nov 12, 2020 at 06:41:36_

----

Good to know


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 05:54:58_

----

`static_cast` forces the cast without any checking, so if debug breaks are off and a mob is passed in here, this check will still pass. Granted, it'll get caught by `PChar->objtype == TYPE_PC`, but it's a practice we shouldn't be relying on;

```cpp
if (auto* PChar = dynamic_cast<CCharEntity*>(m_PBaseEntity))
{
    ....
}
```

will honour nullptr, and check that the pointer is in the same inheritance tree, rather than hard-casting the pointer by virtue of them being the same size.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 06:19:15_

----

Almost, after `dynamic_cast`, these checks are redundant; as they're implied by `dynamic_cast`: `PChar && PChar->objtype == TYPE_PC`

All you need is:
```cpp
if (auto* PChar = dynamic_cast<CCharEntity*>(m_PBaseEntity))
{
...
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 06:34:06_

----

Ah, just saw your comment:

> TYPE_PC check needs to stay, since lua_baseentities could be other types and only PCs have valid online times.

`dynamic_cast<CCharEntity*>` will only return a 'usable' pointer if the target has vtable entries and memory allocated for the type it's trying to cast to, otherwise it will fail. Like you mention; `static_cast` will just smush the pointer into the new type and hope for the best. It would have the base class available, but would fail when it tries to get anything from `CharEntity`.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Nov 12, 2020 at 06:41:36_

----

Good to know
