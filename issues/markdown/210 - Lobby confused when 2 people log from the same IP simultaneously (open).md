**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:21_
_Originally opened as: project-topaz/topaz - Issue 210_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Monday Feb 12, 2018 at 17:39 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4555_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30171223_0


**_Server Version_** (type `!revision` in game) **:** fae4c89


**_Source Branch_** (master/stable) **:** master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
1. Grab a buddy
2. Start up FFXI from your FFXI "man cave" at the same time your buddy does and on the same IP.
--- you may either---
3. Laugh when you get to char select because you now have the option to select your buddy's characters and he has the option to select yours.
--- or ---
4. Log on as normal because lobby doesn't get 'confused' 100% of the time. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:22_

----

<a href="https://github.com/Cryptexx"><img src="https://avatars1.githubusercontent.com/u/33128434?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Cryptexx](https://github.com/Cryptexx)**
_Tuesday Feb 13, 2018 at 09:15 GMT_

----

Here are my experiences with the Login Server and Game Server as far as character login goes:

1. Confirm Wiggo's issue - this happens all the time. Especially if you're dual-boxing and you logout properly. You will not go to your account's char selection, you'll go to your last logged in account's char selection.
2. Sometimes if you shutdown the client without properly logging off/shutting down/etc, you will be unable to login on subsequent attempts. Not sure if the session data isn't being deleted fast enough...or? 
3. Get a lot of 'invalid login attempt from what.ever.ip. Looking at it, I'm guessing related to session data from above, seeing existing entries.
4. This one happens a lot: "login_parse:" CL_WHITE"<%s>" CL_RESET" has logged in %i times! Removing older logins.\n" It resolves the error, but breaks from the switch. So, people have to try again. It would be better if it resolved the error, then re-attempted login, so it's transparent to users and they're not confused (why can't I login?).

All in all, I think the login server just needs a few tweaks for better user experience.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:23_

----

<a href="https://github.com/stevomatic"><img src="https://avatars3.githubusercontent.com/u/26309049?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [stevomatic](https://github.com/stevomatic)**
_Wednesday May 02, 2018 at 19:42 GMT_

----

I usually play with between 3-6 characters and have always had problems with windower's send addon. Whichever character I'm controlling my party with has to be logged in last, if I try and control my party with a character I logged in first there's a good chance send won't work. I've just gotten used to it but it's annoying. I wonder if it's related to this. 

