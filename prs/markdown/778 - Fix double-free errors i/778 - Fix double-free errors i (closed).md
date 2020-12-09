**Labels:**

approved



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Saturday Jun 27, 2020 at 19:05:12_
_Originally opened as: project-topaz/topaz - Issue 778_

----

do_final was written in such a way that it was only ever intended to be called once. However, since the signal_handler calls do_abort and do_final in response to various error states, this means do_final could be (and often is) called multiple times if that signal/error occurs during (or as a result of) the shutdown process itself. This is a problem since there weren't any safeguards against memory attempting to be de-allocated a second time.

This PR ensures that called shutdown procedures are safe (or at least, resistant) against double-freeing. It should also reduce the chance do_final gets caught in a recursive error loop.

This will hopefully lend insight into the real sources of some difficult-to-reproduce crashes, since the recursive double-frees after an error were often trampling over the stack and obfuscating the original cause in those cases.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Jun 27, 2020 at 19:07:10_

----

Pinging issue #702 as an impetus for this; whose root cause may hopefully be more easily determined with a cleaner error log. :)
