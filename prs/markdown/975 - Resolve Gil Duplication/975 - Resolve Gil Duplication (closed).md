**Labels:**

exploit



<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zircon-tpl](https://github.com/zircon-tpl)**
_Wednesday Aug 19, 2020 at 19:17:30_
_Originally opened as: project-topaz/topaz - Issue 975_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Project Topaz was recently informed of an exploit in which any player using a widely available client interface may create a situation in which they may duplicate gil. **This duplication exploit allows players to purchase items from bazaars without spending gil while the seller still receives the purchase amount.**

This is a resolution which will prevent the exploit and display notices that a player is attempting it.

**As far as we are aware, this exploit is possible on all servers derived from Darkstar Project. It is not an exploit unique to Project Topaz.**

We have already informed the operators for all servers derived from Darkstar Project of which we are aware. These servers have had advanced notice to apply this patch, and servers that have applied it will receive notifications in their server logs should a player attempt the now-patched exploit.

**As of this time Project Topaz will not be revealing the exact instructions for how to reproduce this exploit to the broader public.**

This is to give server operators who we have not contacted additional time to apply the patch from this Pull Request. Should you have theories as to how this exploit was produced, please do not publicly speculate as to the method.

**Project Topaz will disclose the exact reproduction steps for the exploit within the next few days.**

Should you operate a server, please be aware that we did reveal reproduction steps to the servers we contacted so that they may confirm the issue affects their server. **As we increase the number of people who are aware of the exploit -- and now provide this patch publicly -- Project Topaz can not guarantee that those who might take advantage of this exploit will not learn how to reproduce it.**

If your server does not currently address this exploit, we recommend updating as soon as possible.

Discussion on this Pull Request will be locked. Should you wish to provide input or additional knowledge regarding this exploit -- or any other exploit -- we ask that you please contact an official Staff member of Project Topaz in private. These members may be discovered through the following group: @project-topaz/staff
