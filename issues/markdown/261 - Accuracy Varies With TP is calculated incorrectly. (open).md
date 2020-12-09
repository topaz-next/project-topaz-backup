**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:27_
_Originally opened as: project-topaz/topaz - Issue 261_

----

<a href="https://github.com/Enignite"><img src="https://avatars0.githubusercontent.com/u/12122667?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Enignite](https://github.com/Enignite)**
_Monday Feb 11, 2019 at 01:28 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5725_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** N/A


**_Source Branch_** (master/stable) **:** Master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I found pull request from 2015 discussing this issue but as far as I can tell nothing was done about it, currently all weapon skills with Accuracy Varies With TP use a modifier of 0.8/0.9/1.0 of total accuracy. I assume these numbers are from a same thread I found a years ago that tested Sidewinder to be -40/-20/-0 Acc and was then implemented incorrectly (iirc this was on KillingIfirit and I can no longer find the thread), that or it's a complete guess and just ended up with similar numbers. I believe the only buff in the game which changes Acc as a % of itself is food and that grants a bonus, it certainly doesn't make sense in this situation with the way FFXI calculates hitrate as it causes the penalty to increase as you get higher level/acc, potentially reaching -80 Acc or more at Lv75.

The exact same acc penalty should not also be applying to multihit weaponskills, there is no evidence of this other than that one comment in the lua and any MNK/DRG/THF/whatever can tell you that their WSs did not have -40 Acc at 100% TP (and certainly not nearly -80 Acc). Both Skewer and Penta Thrust had their TP mods changed in a 2007 patch and Skewer did not suddenly gain a massive acc boost when it was changed from Acc varies with TP, neither did Penta Thrust become wildly inaccurate when it was changed to Acc varies with TP. The only related thing I can find is that Penta Thrust and Guillotine had an accuracy penalty removed in a patch a few months after the above changes, however there's no mention of when this was added (Guillotine had not received any changes in that previous patch) and the chances are this was a minor penalty similar to how Penta Thrust has a negative cRatio mod.

