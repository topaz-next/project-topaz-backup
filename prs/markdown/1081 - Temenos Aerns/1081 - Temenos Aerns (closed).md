**Labels:**

reviewed



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Sep 09, 2020 at 04:17:45_
_Originally opened as: project-topaz/topaz - Issue 1081_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Assigned new jobs to Temenos Aerns, and adjusted their pools to match retail.

Thanks to Nyu for retail captures and determining which job each Aerns is on retail.

Spreadsheet we're using to fix Aerns is [here](https://docs.google.com/spreadsheets/d/1miQYoxtuk20sjWEKB-u97q1Fcvg6l55fjN_LQgnjHTQ/edit#gid=0).



----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 04:19:37_

----

my records show this 58 is a rdm, and 60 is the bst, after 2 runs. 
https://github.com/project-topaz/topaz/issues/513#issuecomment-652149187


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 04:34:16_

----

this was the bst on my runs, with 16929058  being the rdm


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 04:41:50_

----

i had 16929082 as another rdm on my runs


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Sep 10, 2020 at 15:07:43_

----

Hm.  I see that your list in issue 513 says that 16929058 is a RDM, but

1. The NPClogger data attached to 513 agrees with Nyu's cap that 16929058 has model 00005905, which is the axe model used by WAR/RNG/BST; and
2. The Aern's Euvhi with id 16929059 immediately follows this Aern, and can't belong to any other.  Pets always come after their master in the extracts (they don't always immediately follow, but they always come after; never before)

Similarly, 16929060 has model 00005A05, in both Nyu's cap and yours, which is the sword model used by RDM/PLD/DRK.  And no pet follows it in the data.

So I'm inclined to believe the jobs currently in this PR are correct.



----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Sep 10, 2020 at 15:12:38_

----

16929082 is a RDM in this PR too.  (It already was one; this PR didn't change it.)


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 20:11:41_

----

fair enough, data doesnt lie. thanks for taking a second look!


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 20:15:14_

----

i did not see it here and still don't, but i'm sure i'm just missing something - was looking where it jumps from 16929081 to 16929086. not a comment on the pr, but the seemingly missing data. where is that spawn??? ill look around.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Sep 10, 2020 at 21:02:09_

----

I believe this is just a side effect of viewing the diff of a large file on github.  It's only showing you the edited lines plus a few on either side, and leaving out many of the unchanged lines between the edits.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 04:19:37_

----

my records show this 58 is a rdm, and 60 is the bst, after 2 runs. 
https://github.com/project-topaz/topaz/issues/513#issuecomment-652149187


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 04:34:16_

----

this was the bst on my runs, with 16929058  being the rdm


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 04:41:50_

----

i had 16929082 as another rdm on my runs


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Sep 10, 2020 at 15:07:43_

----

Hm.  I see that your list in issue 513 says that 16929058 is a RDM, but

1. The NPClogger data attached to 513 agrees with Nyu's cap that 16929058 has model 00005905, which is the axe model used by WAR/RNG/BST; and
2. The Aern's Euvhi with id 16929059 immediately follows this Aern, and can't belong to any other.  Pets always come after their master in the extracts (they don't always immediately follow, but they always come after; never before)

Similarly, 16929060 has model 00005A05, in both Nyu's cap and yours, which is the sword model used by RDM/PLD/DRK.  And no pet follows it in the data.

So I'm inclined to believe the jobs currently in this PR are correct.



----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Sep 10, 2020 at 15:12:38_

----

16929082 is a RDM in this PR too.  (It already was one; this PR didn't change it.)


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 20:11:41_

----

fair enough, data doesnt lie. thanks for taking a second look!


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 20:15:14_

----

i did not see it here and still don't, but i'm sure i'm just missing something - was looking where it jumps from 16929081 to 16929086. not a comment on the pr, but the seemingly missing data. where is that spawn??? ill look around.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Sep 10, 2020 at 21:02:09_

----

I believe this is just a side effect of viewing the diff of a large file on github.  It's only showing you the edited lines plus a few on either side, and leaving out many of the unchanged lines between the edits.
