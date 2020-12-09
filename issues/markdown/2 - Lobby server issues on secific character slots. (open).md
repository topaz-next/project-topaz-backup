**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:09_
_Originally opened as: project-topaz/topaz - Issue 2_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 23, 2014 at 02:09 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 497_

----

I didn't notice til I needed to create a bunch of alts to test my attempts at nexus cape with but I verified this is not a multi boxing issue and tested with a clean dsp pull & build (no modifications) before opening the issue on github.

Remember the old bug that crashed servers if you tried to log in certain characters? That was fixed a long time ago, but I think the recent client updates changed something again. 

I'm seeing certain character slots unable to log in with pol-0001 after 5+ characters are created on the account. 

If I move the effected characters to a different account they can log in, but at the risk of a different character on the previous account suffering the pol-0001 error. 

The weird thing is, its not always the same slot across accounts. I loaded up 2 accounts to test it. account ID 1000 had slot 4 get perma stuck after creating the 5th character. Account 1001 had slot 3 get stuck instead. All other characters on both accounts are able to log in. Very interestingly, logging in directly from character creation will work. By this I mean if you delete "stuck" character and then make a new one that occupies that slot the initial zone in from char creation works (IF you don't get the invalid key crap that is) but then re-logging you see pol-0001 again.

These are NOT problems that can be fixed by resetting the character, they don't even touch the map server at all. There are no server log errors or crashes, ports and IPs are correctly set.

I'm pretty sure recent one of the client updates did it. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:10_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Sep 23, 2014 at 02:14 GMT_

----

could be that something changed for lobby packets, anything in lobby server log?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:11_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 23, 2014 at 02:18 GMT_

----

That was my guess. Nothing in log at all abnormal for lobby or map, acts like client isn't there when affected chars try to log in.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:13_

----

<a href="https://github.com/atom0s"><img src="https://avatars2.githubusercontent.com/u/1422090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [atom0s](https://github.com/atom0s)**
_Thursday Jan 22, 2015 at 18:20 GMT_

----

Before I recoded the boot loader, every slot past 6? or something did not work. Which I found the bug causing that and fixed it. However, in the attempt to fix that, the bug you are explaining here came about. It is not a new bug that happened recently. It is a known issue with the boot loader / lobby server that 2 out of the 16? slots have problems logging in when you create a character in every slot. I have not been able to pinpoint the problem, granted I stopped looking into it a while ago. 

Now that I wrote polpackets to dump the packet flow from PlayOnline, someone could dump the retail POL communications again and check into it. It's mainly needing to see if anything changes when you log into an account in a higher end slot. And what the packets look like if anything has changed. I doubt they have since POL has not been updated in years now.




----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Monday May 11, 2020 at 18:32:59_

----

stupid git, i cant use hashes, cos it tags stuff like this lol


----
<a href="https://github.com/dwardlow"><img src="https://avatars1.githubusercontent.com/u/21171687?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [dwardlow](https://github.com/dwardlow)**
_Saturday May 16, 2020 at 13:33:43_

----

I don't know enough about how the POL client actually communicates with darkstar/topaz to fix it, but I made a workaround for this on my own private server.

There's an issue with how the lobby server communicates with POL for character slots slots 4, 8 and 12 (at least it's those slots on the first account id 1000). You can see this clearly if you reorder the character list returned by the Lobby Server to the POL client. (e.g. Look at the SQL statement [which begins on line #132 of lobby.cpp](https://github.com/project-topaz/topaz/blob/release/src/login/lobby.cpp#L132) - and stick either _"ORDER BY charid ASC \\"_ or _"ORDER BY charname ASC \\"_  on a new line just _after "WHERE accid = %i \\"_) The listed order of the account's characters on the client's POL screen can be changed around... but unless you make any further changes, whichever characters end up in slots 4, 8 and 12 on that screen will give POL-0001 errors and refuse to load!

If you look deeper inside lobby.cpp [there's a loop that begins](https://github.com/project-topaz/topaz/blob/release/src/login/lobby.cpp#L169): "while (Sql_NextRow(SqlHandle) != SQL_NO_DATA)" where the server iterates through that loaded character list from SQL (adding 1 to "i" each time) and adds each character into memory. If you rework this loop with an extra counter so that _whenever i would equal 3, 7 and 11 (the problematic character slots) it instead adds an extra one to i_... then you skip over those problematic character slots and the POL-0001 errors go away. The client's screen will show an unbroken list of characters, and all of them will load without errors. 

Although doing this lowers the maximum character limit from 16 to 13, at least they all load!

e.g.

            int i = 0;
            int charOffset = 0;            
            while (Sql_NextRow(SqlHandle) != SQL_NO_DATA)
            {
                // Ridiculously Stupid Fix for the Loading Screen Bug.
                if (charOffset == 3) { i++; }
                if (charOffset == 7) { i++; }
                if (charOffset == 11) { i++; }

                [BLAHBLAHBLAH... DO REGULAR LOOP STUFF...]

                ++i;
                ++charOffset;
            }


Obviously this is a bit too simplistic if the borked slots differ from Account ID to Account ID _(although the testing I've done so far seems to show it's ALWAYS those same three character slots. At least whenever that first SQL statement in lobby.cpp is returning an ordered list!)_ however at least it helps point out where the problem is actually coming from - it's whenever character data is stored in specific locations within that memory array (uList? CharList?) that POL throws a wobbler trying to load it. However the list of characters that the user actually ends up seeing on their screen can be made to display a lot more than 4 characters without them getting any loading errors.
