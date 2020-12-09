**Labels:**



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 06:50:22_
_Originally opened as: project-topaz/topaz - Issue 360_

----

This may not actually be every file, but I did the best I could.

Command applied:
    find . -type f -name "*.lua" | xargs -d '\n' sed -i 's/;//g'

Semicolons are not appropriate in Lua per the style guidelines:
    https://github.com/project-topaz/topaz/blob/master/CONTRIBUTING.md

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 06:51:11_

----

There's so many Lua files, I figured we can do it directory by directory. Otherwise it's ridiculous.

(For example: https://github.com/mrhappyasthma/topaz/commit/7277ac15d61230d0093e8cde29057dbefa00bd69)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 14:27:25_

----

And here I was considering doing the same thing and racking up some line diff counts. You beat me to it. 😉 


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 14:28:54_

----

That was just commands. Still alot more to do

On Thu, Feb 20, 2020, 8:27 AM ibm2431 <notifications@github.com> wrote:

> And here I was considering doing the same thing and racking up some line
> diff counts. You beat me to it. 😉
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/pull/360?email_source=notifications&email_token=AIPXQA5VBIV2LPLUPZ5T2LDRD2HM5A5CNFSM4KYIMGF2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEMOJ2KY#issuecomment-589077803>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AIPXQA3GNWAI4L7N4GRGWQTRD2HM5ANCNFSM4KYIMGFQ>
> .
>



----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 15:52:17_

----

Correct. It was too massive of a change to do in a single PR, so there's plenty of room to help out.

I can progressively send out PRs for this but if anyone wants to help out then even better :)
