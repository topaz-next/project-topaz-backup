**Labels:**

help wanted

research needed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Friday Aug 14, 2020 at 02:02:48_
_Originally opened as: project-topaz/topaz - Issue 945_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

We all know that the suicide Bomb Toss from goblins is too high on Topaz.  On private servers running stock topaz bomb toss scripts, you'll see that no one can actually form an exp party to specifically hunt IT goblins, unlike retail.  This is because suicide bomb toss is doing 2-3x more damage than it should.  The formula developed to emulate SE's bomb toss was made arbitrarily because we don't actually have a method to determine how mob parameters exactly affect the damage.  I propose we slash the bomb toss power in half, and the only evidence I can offer to support this is this video from 2009 where a party is exping on a goblin, and it blows up at 25% for 25ish damage to each member:
https://youtu.be/9-4PGvPxuu8?t=420

On Topaz I believe that same bomb would have caused 60ish damage per party member.  
**Cast your vote to end the tyranny of bomb toss on private servers!**


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Aug 14, 2020 at 09:20:35_

----

I know that I don't have any official role, but I 100% agree with this change...!


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 15, 2020 at 18:36:53_

----

I'm not necessarily opposed to "for now" fixes, but I worry that this will fix it "enough," and then we'll never revisit this issue. So, if people are feeling passionate about it in the moment, I would like to capitalize on that passion and get a bit of research from one of our retail researchers. 

Maybe something like 25 bomb tosses to naked characters per 3-4 different level ranges. Then we could either do some sort of linear regression to figure out the correct formula or just hack something that's a little more average. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 27, 2020 at 13:30:27_

----

> [ ] that I've tested my code since the last commit in the PR, and will test after any later commits

Core experiences need to be tested. Unfortunately for players, getting their asses kicked by Gobbie Bombs is part of the experience. Theorycrafting is fine when it's backed up by a lot of data, one video and some anecdotal evidence is not enough.

> Maybe something like 25 bomb tosses to naked characters per 3-4 different level ranges. Then we could either do some sort of linear regression to figure out the correct formula or just hack something that's a little more average.

This is 10/10 the correct way to do it. As painful as it may be. This is the kind of work that went into figuring out that the damage output from `Pinecone Bomb` was essentially just random...

It sucks, but it's what's required.
