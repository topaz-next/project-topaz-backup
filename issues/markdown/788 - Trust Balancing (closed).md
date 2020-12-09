**Labels:**

focus



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Wednesday Jul 01, 2020 at 10:36:46_
_Originally opened as: project-topaz/topaz - Issue 788_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Here to track trust rough numbers from retail vs canary:

| | **Lv52 Trusts (Retail) - Garliage Citadel** | **Lv52 Trusts (Canary)- Garliage Citadel**  |
| --- | --- | --- |
| Naji | 1031 HP, 0 MP | 1067 HP, 0 MP |
| Shantotto | 529 HP, 660 MP | 830 HP, 1660 MP |
| Kupipi | 596 HP, 594 MP |  830 HP, 1660 MP |
| Excenmille | 1011 HP, 182 MP | 1186 HP, 1067 MP |
| Nanaa Mihgo | 818 HP, 0 MP | 949 HP, 0 MP |
| --- | --- | --- |
| Naji | 60 hit -> Siege Bat | 113 hit -> Siege Bat |
| Naji | 72 hit -> Siege Bat | 111 hit -> Siege Bat |
| Naji | 155 Burning Blade -> Siege Bat | 112 Burning Blade -> Siege Bat |
| --- | --- | --- |
| NanaaMihgo | 33 hit -> Siege Bat | 108 hit -> Siege Bat |
| NanaaMihgo | 53 hit -> Siege Bat | 87 hit -> Siege Bat |
| NanaaMihgo | 410 King Cobra Clamp -> Siege Bat | 358 King Cobra Clamp -> Siege Bat |
| --- | --- | --- |
| Kupipi | 46 hit -> Siege Bat | 79 hit -> Siege Bat  |
| Kupipi | 71 hit -> Siege Bat | 61 hit -> Siege Bat  |
| --- | --- | --- |
| Excenmille | 137 hit -> Siege Bat | 108 hit -> Siege Bat |
| Excenmille | 156 hit -> Siege Bat | 93 hit -> Siege Bat |
| Excenmille | 283 Penta Thrust -> Siege Bat | 539 Penta Thrust -> Siege Bat |
| --- | --- | --- |
| Shantotto (I) | 450 Stone II -> Siege Bat | 334 Thunder II -> Siege Bat  |
| Shantotto (I) | 440 Stone III -> Siege Bat | 394 Stone III -> Siege Bat |
| Shantotto (I) | 304 Aero II -> Siege Bat | 282 Blizzard II -> Siege Bat |

**Other notes:**
Shantotto spells seem pretty good, but she probably needs some kind of MAB mod.
Spell selection is in the somewhat right ballpark, but still a little borked.
Shantotto shouldn't be meleeing.

I think Trusts don't have a proper concept of damage scaling for weapon type, or delay. Will look into that.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 04, 2020 at 07:07:05_

----

This was just a quick scratchpad for me to keep track of numbers while I worked. There is a patch in trust (and presumably canary) that brings these numbers pretty much in line.
