**Labels:**



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Saturday Nov 14, 2020 at 23:30:11_
_Originally opened as: project-topaz/topaz - Issue 1524_

----

Issue:

Accessing the Profile Menu causes the client to crash.

Affected Client Versions:

`30201103_1`
`30201103_3`

Steps to Replicate:

Be on either of the above mentioned client versions.
Log in a character.
Open The Main Menu (- key) > Select Status > Select Profile
Client will crash.

Additional Notes:

This was tested against Canary `ea135512f18bc2e0da51d154883c9c0d8dc1b37c`
Client version `30201006_1` does not exhibit this behavior when tested against the above version of Canary.

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 




----
<a href="https://github.com/claywar"><img src="https://avatars1.githubusercontent.com/u/12447174?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [claywar](https://github.com/claywar)**
_Saturday Nov 14, 2020 at 23:31:08_

----

[2020-11-14_18-02.zip](https://github.com/project-topaz/topaz/files/5541582/2020-11-14_18-02.zip)
Attached retail captures for accessing status->profile.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 26, 2020 at 06:48:25_

----

Fixed by: https://github.com/project-topaz/topaz/commit/be34888ce2c2727bf233d8acbaf8c3e2d284a194
