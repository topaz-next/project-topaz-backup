**Labels:**



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 04:45:11_
_Originally opened as: project-topaz/topaz - Issue 379_

----

This is a prerequisite for DarkstarProject/xiloader#7.

This change adds support for a new command in the login code to support
changing a users password. It simply verifies the users login similarly
to the existing flow, and then makes another request over the socket for
the new password. Then it updates the SQL.

Tested locally. Have a set of changes ready for xiloader as well, but
this work is required first.

NOTE: There is definitely some refactoring that could be done in this
file to reduce the amount of nested braces and to reduce duplicated code.
I tried to touch as little existing code as possible in this change to
reduce the risk of introducing a regression.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 05:03:33_

----

Technically this warning can be triggered on either the account not existing _or_ a password mismatch


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 05:10:57_

----

Is there no need for a memset like with [during the login flow](https://github.com/project-topaz/topaz/blob/821bcfe6b8db045a03694d032bde530e8152585f/src/login/login_auth.cpp#L165-L170)?


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:37:38_

----

It shouldn't be needed since I'm resizing the `wdata` (which is a `std::string`). Per the documentation:

http://www.cplusplus.com/reference/string/string/resize/

> If n is smaller than the current string length, the current value is shortened to its first n character, removing the characters beyond the nth.

So the code resizes the string to a single byte, then we set that byte value to `LOGIN_ERROR_CHANGE_PASSWORD`.

So there's no bytes that contain garbage or need to be copied over with memset.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:38:21_

----

This pattern is used elsewhere in the code as well: https://github.com/project-topaz/topaz/blob/821bcfe6b8db045a03694d032bde530e8152585f/src/login/login_auth.cpp#L97-L98


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:39:38_

----

Fair point. Let me adjust the wording of this error to be more clear.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:44:56_

----

For context, this was copied from this line: 
https://github.com/project-topaz/topaz/blob/821bcfe6b8db045a03694d032bde530e8152585f/src/login/login_auth.cpp#L205

It suffers from the same ambiguity problem.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:46:57_

----

A lot of code in this file can be cleaned up and optimized. I tried to make as minimal changes as possible to reduce the risk of introducing a regression bug.

When I get some time I can try to clean up this file and provide a bit more structure and better organization for maintainability.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 06:47:11_

----

Alright, just curious since I saw a memset was being used for bans later on, and I'm not gonna pretend I'm very familiar with the login server~! 😅 


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:47:48_

----

Updated the wording here. Please take another look and let me know what you think.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 06:48:14_

----

New wording looks good~! 👍 


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:50:59_

----

As I mentioned in the other thread. A lot of this code can be pulled into helper functions and consolidated for better readability and maintainability. However there's a lot of copy/paste style code blocks throughout here that I didn't wanna mess with for the sake of this change.

A more solid rewrite of this file should be done with care and tested thoroughly. 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 05:03:33_

----

Technically this warning can be triggered on either the account not existing _or_ a password mismatch


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 05:10:57_

----

Is there no need for a memset like with [during the login flow](https://github.com/project-topaz/topaz/blob/821bcfe6b8db045a03694d032bde530e8152585f/src/login/login_auth.cpp#L165-L170)?


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:37:38_

----

It shouldn't be needed since I'm resizing the `wdata` (which is a `std::string`). Per the documentation:

http://www.cplusplus.com/reference/string/string/resize/

> If n is smaller than the current string length, the current value is shortened to its first n character, removing the characters beyond the nth.

So the code resizes the string to a single byte, then we set that byte value to `LOGIN_ERROR_CHANGE_PASSWORD`.

So there's no bytes that contain garbage or need to be copied over with memset.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:38:21_

----

This pattern is used elsewhere in the code as well: https://github.com/project-topaz/topaz/blob/821bcfe6b8db045a03694d032bde530e8152585f/src/login/login_auth.cpp#L97-L98


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:39:38_

----

Fair point. Let me adjust the wording of this error to be more clear.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:44:56_

----

For context, this was copied from this line: 
https://github.com/project-topaz/topaz/blob/821bcfe6b8db045a03694d032bde530e8152585f/src/login/login_auth.cpp#L205

It suffers from the same ambiguity problem.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:46:57_

----

A lot of code in this file can be cleaned up and optimized. I tried to make as minimal changes as possible to reduce the risk of introducing a regression bug.

When I get some time I can try to clean up this file and provide a bit more structure and better organization for maintainability.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 06:47:11_

----

Alright, just curious since I saw a memset was being used for bans later on, and I'm not gonna pretend I'm very familiar with the login server~! 😅 


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:47:48_

----

Updated the wording here. Please take another look and let me know what you think.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 06:48:14_

----

New wording looks good~! 👍 


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 06:50:59_

----

As I mentioned in the other thread. A lot of this code can be pulled into helper functions and consolidated for better readability and maintainability. However there's a lot of copy/paste style code blocks throughout here that I didn't wanna mess with for the sake of this change.

A more solid rewrite of this file should be done with care and tested thoroughly. 
