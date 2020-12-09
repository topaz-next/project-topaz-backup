**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Sep 27, 2020 at 05:58:39_
_Originally opened as: project-topaz/topaz - Issue 1200_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This would fix #1197

I created a retail trial account to check this. The guards are apparently extremely repetitive. When choosing an EXP ring from the guards inventory he/she will trigger three descriptive strings. (special nature > possible recharge > great war)
Then if you choose to buy it and one of the conditions discussed in #1197 triggers, the same strings will again be called and printed to the chatlog including a preceding "you don't meet the requirements"-string. This applies to both, trying to buy with another ring in inventory and trying to buy before tally reset. See the screenshot (the first time the three strings are called, they're not logged):

![img_20200927_002300](https://user-images.githubusercontent.com/1492317/94357098-78953380-005b-11eb-91ec-69705dc3de7c.jpg)

The commit is a little bit less superfluous and only prints:

> **You do not meet the requirements to purchase [item].**
> **Due to its special nature, you can only purchase or recharge [item] once until the conquest results tally is performed. Also, you cannot purchase this item if a similar item is already in your possession.**

