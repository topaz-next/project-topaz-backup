**Labels:**



<a href="https://github.com/claywar"><img src="https://avatars1.githubusercontent.com/u/12447174?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [claywar](https://github.com/claywar)**
_Sunday Nov 29, 2020 at 15:06:51_
_Originally opened as: project-topaz/topaz - Issue 1538_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Latest client changed the outgoing tell packet (0x0B6) start locations for Recipient and message by one byte.  In addition, a maximum length recipient name has the potential to no longer be null-terminated.  The latter issue only impacts logging, as strictly 15 bytes are read from the data to determine RecipientName.

Note: This fix only corrects tells not functioning, and does not implement the new outgoing 0x05 value.
