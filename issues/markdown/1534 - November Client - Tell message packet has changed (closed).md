**Labels:**



<a href="https://github.com/claywar"><img src="https://avatars1.githubusercontent.com/u/12447174?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [claywar](https://github.com/claywar)**
_Thursday Nov 26, 2020 at 16:46:43_
_Originally opened as: project-topaz/topaz - Issue 1534_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

■ Occurrence Rate: 5 out of 5
■ Precondition:
1. Two characters are logged in to the server

■ Procedure:
1. Send tell from first character to second
2. Send tell from second character to first

■ Observations:
- Expected Result
1. Tell should be received successfully by the intended recipient

- Actual Result
1. Tell is not received by the intended recipient

■ Fault Recovery:
None



----
<a href="https://github.com/claywar"><img src="https://avatars1.githubusercontent.com/u/12447174?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [claywar](https://github.com/claywar)**
_Thursday Nov 26, 2020 at 16:47:32_

----

Creating this issue for tracking purposes.  Need to collect retail data for incoming chat to verify changes in addition to outgoing.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Nov 26, 2020 at 18:54:45_

----

the previous update removed a null byte that was sent with the name in chat packets. now, I believe the name has been shifted over and a new byte added preceding it for the purposes of displaying an icon. This may be the cause of the issue. That byte would likely not be used by all forms of chat (I think its only the new assiste/assistj channels) but the packet probably still expects the name moved over and a placeholder byte at a minimum. Worth trying and seeing what happens.


----
<a href="https://github.com/claywar"><img src="https://avatars1.githubusercontent.com/u/12447174?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [claywar](https://github.com/claywar)**
_Saturday Nov 28, 2020 at 16:47:41_

----

Shifting the start bytes for name and message resolved the immediate issue.  Working now to confirm the function of this additional byte, document, and ensure that non-null values will not disrupt function.


----
<a href="https://github.com/claywar"><img src="https://avatars1.githubusercontent.com/u/12447174?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [claywar](https://github.com/claywar)**
_Thursday Dec 03, 2020 at 22:01:31_

----

Closing issue after #1538 merge.
