**Labels:**

bug

crafting



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:50:34_
_Originally opened as: project-topaz/topaz - Issue 201_

----

<a href="https://github.com/Rigginit"><img src="https://avatars2.githubusercontent.com/u/34630701?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Rigginit](https://github.com/Rigginit)**
_Sunday Dec 17, 2017 at 20:01 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4395_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [] checked the commit log to see if my issue has been resolved since my server was last updated
^Fresh install less than 12 hours ago

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **.**   30171103_1


**_Server Version_** (type `!revision` in game) **:** f643501963854f1b763aec94c9ee730d1812b1c7


**_Source Branch_** (master/stable) **:** master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Try to buy something from Guild vendors and "Buy" button gives error tone or a blank sales window. Not all vendors, and I could only narrow it down to find the problematic NPCS have the 4 digit guild ID in the script/zone/****/NPC.  Not all 4 digit NPCs have errors (Cooking Guild NPCs work for example) 

NPCs Ive found (not a complete list, just the few Ive checked):
Northern San d'Oria    - Woodworking Guild    - Chaupire
Windurst Woods         - Clothcraft Guild            -Kuzah Hpirohpon
Windurst Woods         - Bonecraft Guild            -Retto_Marutto









----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:50:35_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Dec 17, 2017 at 20:25 GMT_

----

Is it any guild ID over 255, perhaps?  Maybe it was broken by one of the
commits to remove warnings

Is there any message in the log?  We have a debug message for not being
able to find a guild ID

On Sun, Dec 17, 2017 at 1:01 PM, Rigginit <notificationsgithub.com> wrote:

> *I have:*
>
>    - searched existing issues (http://github.com/darkstarproject/darkstar/
>    issues/ <github/darkstarproject/darkstar - Issue >) to see
>    if the issue I am posting has already been addressed or opened by another
>    contributor
>    - [] checked the commit log to see if my issue has been resolved since
>    my server was last updated
>    ^Fresh install less than 12 hours ago
>
> *Client Version* (type /ver in game) *.* 30171103_1
>
> *Server Version* (type !revision in game) *:* f643501
> <github/DarkstarProject/darkstar/commit/f643501963854f1b763aec94c9ee730d1812b1c7>
>
> *Source Branch* (master/stable) *:* master
>
> *Additional Information* (Steps to reproduce/Expected behavior) *:*
>
> Try to buy something from Guild vendors and "Buy" button gives error tone
> or a blank sales window. Not all vendors, and I could only narrow it down
> to find the problematic NPCS have the 4 digit guild ID in the
> script/zone/****/NPC. Not all 4 digit NPCs have errors (Cooking Guild NPCs
> work for example)
>
> NPCs Ive found (not a complete list, just the few Ive checked):
> Northern San d'Oria - Woodworking Guild - Chaupire
> Windurst Woods - Clothcraft Guild -Kuzah Hpirohpon
> Windurst Woods - Bonecraft Guild -Retto_Marutto
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 4395>, or mute the
> thread
> <github/notifications/unsubscribe-auth/ABGI_6Ed_M6Dn3nzPW99w2gmi-TqvZ0_ks5tBXMWgaJpZM4RExoI>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:50:36_

----

<a href="https://github.com/Rigginit"><img src="https://avatars2.githubusercontent.com/u/34630701?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Rigginit](https://github.com/Rigginit)**
_Sunday Dec 17, 2017 at 20:39 GMT_

----

Sorry, I'm still new. if by the log you mean DSGame-Server window then no error is shown.  
The scripts for the NPCs are where I'm seeing the ID. I may have called it by the wrong name earlier but its this line:
if (player:sendGuild(5142,8,23,3)) then ...  
the working NPC for the guild has "514" and the other "5142" again not even sure this is where the problem lies. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:50:37_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Dec 17, 2017 at 21:29 GMT_

----

Yep, dsgame window is the log (also the log file which is the same thing)

If 514 works then my guess was wrong, guess we'll have to look into it more

On Sun, Dec 17, 2017 at 1:39 PM, Rigginit <notificationsgithub.com> wrote:

> Sorry, I'm still new. if by the log you mean DSGame-Server window then no
> error is shown.
> The scripts for the NPCs are where I'm seeing the ID. I may have called it
> by the wrong name earlier but its this line:
> if (player:sendGuild(5142,8,23,3)) then ...
> the working NPC for the guild has "514" and the other "5142" again not
> even sure this is where the problem lies.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 4395Darkstar Issue issuecomment-352283673>,
> or mute the thread
> <github/notifications/unsubscribe-auth/ABGI_6jlY6TYzhbvm2KKFMgdld_YFr0vks5tBXvpgaJpZM4RExoI>
> .
>


