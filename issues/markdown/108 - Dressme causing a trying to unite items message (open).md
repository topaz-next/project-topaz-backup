**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:18_
_Originally opened as: project-topaz/topaz - Issue 108_

----

<a href="https://github.com/dacrybabysuck"><img src="https://avatars3.githubusercontent.com/u/8637673?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [dacrybabysuck](https://github.com/dacrybabysuck)**
_Saturday Mar 19, 2016 at 23:40 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2924_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30160203_0

**_Server Version_** (type `revision` in game) **:**
6a943ead49e6bf05bad52f546f4ca2f8bdac184c

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
I believe since the introduction of mogsafe 2 this has been going on but I can't be certain of that.  I'm not entirely sure what the logic is intending to do here, however when doing a little troubleshooting, the following block seems to be the culprit.

packet_system.cpp:951

```
   if (ToSlotID < 82) // 80 + 1
    {
        ShowDebug("SmallPacket0x29: Trying to unite items\n", FromLocationID, FromSlotID);
        return;
    }
```

If I comment out the return, everything appears to continue to function properly when using Dressme to move items around.  I'm also able to split stacks, combine stacks and move items from any storage location to another manually.  Could someone shed some light on what this is actually checking for?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:19_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Saturday Mar 19, 2016 at 23:50 GMT_

----

Does this still happen if you remove anything to do with Mog Safe 2 from your Dressme script? Mog Safe 2 wasn't intentionally/properly implemented AFAIK.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:20_

----

<a href="https://github.com/dacrybabysuck"><img src="https://avatars3.githubusercontent.com/u/8637673?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dacrybabysuck](https://github.com/dacrybabysuck)**
_Sunday Mar 20, 2016 at 00:12 GMT_

----

Negative.  During my testing I had tried with and without bank2 in the configuration.  When the bank2 is enabled however and the early return is removed, dressme is successful in moving items into bank2.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:21_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Mar 20, 2016 at 01:04 GMT_

----

When moving items around, ToSlotID doesn't seem to be used for anything
except debug messages.  It appears that the client always specifies some
nonsense number and lets the server decide the new slot value.  It could be
modified to use the supplied slot ID (and check that the slot is empty or
the same item ID for stacks), and use the auto-generated slot ID if the
supplied one was higher than the container's size.

I don't use dressme and I'm not really sure how the stacking/sorting
functions work on the client, so I won't make that change right now.

On Sat, Mar 19, 2016 at 6:12 PM, dacrybabysuck notificationsgithub.com
wrote:

> Negative. During my testing I had tried with and without bank2 in the
> configuration. When the bank2 is enabled however and the early return is
> removed, dressme is successful in moving items into bank2.
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 2924Darkstar Issue issuecomment-198812781


