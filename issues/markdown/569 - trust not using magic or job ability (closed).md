**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 02, 2020 at 17:04:25_
_Originally opened as: project-topaz/topaz - Issue 569_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
just tested the canary branch to see the changes made by PR #454 . Kupipi doesn't cast magic and naji still doesnt provoke. (Curilla no casting either, didn't try shantoto)



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 02, 2020 at 18:53:02_

----

this is experienced when the server is built on ubuntu 18.04


----
<a href="https://github.com/brianmask"><img src="https://avatars2.githubusercontent.com/u/33399423?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [brianmask](https://github.com/brianmask)**
_Saturday May 02, 2020 at 20:45:09_

----

Seeing this as well on a fresh canary build. 
git rev-parse --short HEAD == 741211aade
Linux - Debian bullseye/sid 

Nothing odd seen in the logs. Will attempt to debug for more info.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 02, 2020 at 22:03:07_

----

I just checked and windows works well. thank for your feedback @brianmask 


----
<a href="https://github.com/brianmask"><img src="https://avatars2.githubusercontent.com/u/33399423?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [brianmask](https://github.com/brianmask)**
_Sunday May 03, 2020 at 03:19:35_

----

trustentity.h
`// Note: The default name is the lowercase spell script name, so we override GetName()
    // to return the packetName instead, which makes the behaviour consistant with other uses
    // of GetName()
    const int8* GetName() override;
`
trustentity.cpp
`const int8* CTrustEntity::GetName()
{
    return (const int8*)packetName.c_str();
}`

is the cause of this issue
with the current implementation GetName is returning the packet_name column from the database which is used for client formatting.  Normally GetName returns the name column which is what scripts are named by.

Windows don't care about file name casing, so it finds trust.lua when Trust.lua is given.  Linux does, it wants to find exactly what you told it to find so Trust.lua will not resolve to the file.... trust.lua.

I'm not sure if there is a reason for this override of the baseentity implementation, but this override is causing the issue in Linux.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:14:04_

----

Resolved on #576 
