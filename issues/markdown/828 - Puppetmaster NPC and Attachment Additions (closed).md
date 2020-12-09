**Labels:**

merge ready



<a href="https://github.com/Cadwyn"><img src="https://avatars0.githubusercontent.com/u/67503172?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Cadwyn](https://github.com/Cadwyn)**
_Wednesday Jul 08, 2020 at 23:40:29_
_Originally opened as: project-topaz/topaz - Issue 828_

----

Hi there! First time coding/contributing to things, so sorry if this is not entirely correct.

I added some scripting to a few automaton attachments that I have tested on my personal server, and they do not crash the server as they did previously... Arcanic Cell I & II should work in theory, but Occult Acumen doesn't seem to be coded itself, nor does Double Shot Rate referenced in Repeater.lua. Arcanoclutch works exactly as intended, though!

The values are all taken from BGWiki's attachment pages, and Yoyoroon's inventory is taken from BGWiki's page on him.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jul 16, 2020 at 13:39:21_

----

Whilst i cannot help with the Occult Acumen issue or Double Shot rate, i have checked all the numbers and they all seem to match item_basic.sql numbers and all have sub id's that also line up with id's in item_puppet.sql,

Also just as a note and probly not in scope of this PR, the following items have no base sale price:

```
needs a base sale price in items_basic.sql
• 9068 barrier_module
• 9072 arcanic_cell
• 9032 strobe_ii
• 9033 tension_spring_iii
• 9066 amplifier
• 9037 accelerator_iii
• 9036 scope_ii
• 9039 armor_plate_iii
• 9040 stabilizer_iii
• 9065 inhibitor_ii
• 9230 speedloader_ii
• 9067 repeater
• 9043 stealth_screen_ii
```
