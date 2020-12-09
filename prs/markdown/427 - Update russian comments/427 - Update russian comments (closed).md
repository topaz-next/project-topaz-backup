**Labels:**

merge ready



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Mar 15, 2020 at 01:32:41_
_Originally opened as: project-topaz/topaz - Issue 427_

----

Translated comments in:

- documentation/*
- src/common/*
- src/login/*
- src/search/*

NOTE: I also did some whitespace cleanups and removed empty comment blocks to fix up some of these files. However I will be doing separate pull requests to replace pre-existing tabs w/ spaces.

The only directories that still need translations are:

- src/map/*

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Mar 15, 2020 at 01:34:16_

----

This was the only comment in these files that I couldn't quite understand enough to translate.

It's something about skipping the final bits, but by reading through the code it's not obvious why this is done or what's happening.

The phrase `кучу` here could possibly mean "heap", "struct", or "packet". Or perhaps something else...


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 18, 2020 at 20:56:07_

----

They might be referring to extra information that's usually supposed to be in the same packet, but is being skipped because it's not always there.

I've probably booted the search server _once_, and I'm not finding anything useful in Windower's packet library, so I couldn't guess what that information might potentially be.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 18, 2020 at 20:58:41_

----

What's your preference for this one? I was tempted to just leave it as is.

I could drop in a more literal translation of the text, but I worry if it's not accurate then it won't be meaningful.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Mar 15, 2020 at 01:34:16_

----

This was the only comment in these files that I couldn't quite understand enough to translate.

It's something about skipping the final bits, but by reading through the code it's not obvious why this is done or what's happening.

The phrase `кучу` here could possibly mean "heap", "struct", or "packet". Or perhaps something else...


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 18, 2020 at 20:56:07_

----

They might be referring to extra information that's usually supposed to be in the same packet, but is being skipped because it's not always there.

I've probably booted the search server _once_, and I'm not finding anything useful in Windower's packet library, so I couldn't guess what that information might potentially be.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 18, 2020 at 20:58:41_

----

What's your preference for this one? I was tempted to just leave it as is.

I could drop in a more literal translation of the text, but I worry if it's not accurate then it won't be meaningful.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Mar 15, 2020 at 04:45:51_

----

saw several comment blocks that were empty, wouldn't it be better to fill them with information related to what is below? Maybe whomever wrote that meant to do that?


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Mar 15, 2020 at 05:08:57_

----

I could add them back, in the meantime, if we wanted to keep this PR better scoped, but I felt that they made the files easier to work with for the short term.

I agree that ideally we should comment all of the methods (even those without a placeholder comment block), but I felt it was outside the scope of this immediate change -- which was largely to change existing comments from Russian to English.

I'm also not the original author of the code, so it took me a while between Google Translate and tracing the code to make sure I ported the comments as accurately as possible. So it may take some time to add proper comments to all undocumented methods as well.

So my opinion is that adding documentation to undocumented code would be better scoped in a separate pull request.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 18, 2020 at 20:59:13_

----

No problem. I'll slowly go through the remaining files as well. :)
