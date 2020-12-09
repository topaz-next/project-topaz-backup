**Labels:**



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Friday May 08, 2020 at 19:49:38_
_Originally opened as: project-topaz/topaz - Issue 596_

----

Topaz previously only used one account creation status code for any and all errors, which was reported in xiloader as "Username is taken" in all cases. Many times, this was not true; particularly if account_creation is set false in the config, or if an SQL error had occurred server-side.

This PR adds 2 new return codes, and corrects their usage. This new verbosity is dependent on using the new xiloader, but it is 100% backwards compatible; old versions can still work normally with their existing reduced clarity in error reporting.

This serves to make the account-creation flag a wholly complete and properly handled feature.

**This PR should probably be held until my corresponding [PR for improvements in xiloader](https://github.com/zircon-tpl/xiloader/pull/2) is merged.**

**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits
