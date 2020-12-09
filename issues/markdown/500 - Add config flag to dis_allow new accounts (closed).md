**Labels:**

merge ready



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Wednesday Apr 15, 2020 at 17:25:17_
_Originally opened as: project-topaz/topaz - Issue 500_

----

There are surely people hosting private servers for themselves or their friends who would prefer not have open registrations. True, the chance of someone port scanning you, finding your server, and logging in is minimal but most server emulators offer an option to disable registration entirely. This PR adds that capability.

Adds new flag "account_creation" (true/false) in login.conf file which permits new accounts to be created. Defaults to true. A one-line warning will also show at topaz_connect startup if this flag is set False, as this could be a cause of issues or confusion if someone had done so inadvertently or had forgotten they'd done so.

Considerations:
If account creation is disabled, topaz_connect will always return 0x04 ERROR_CREATE when receiving a new account request, which is visibly shown as "Username is taken" in xiloader. This is of course not **entirely** accurate, but as xiloader only recognizes a few return codes, this was the most suitable available.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits
