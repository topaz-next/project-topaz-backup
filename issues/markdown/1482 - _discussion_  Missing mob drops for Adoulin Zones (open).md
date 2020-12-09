**Labels:**



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Friday Nov 06, 2020 at 16:13:05_
_Originally opened as: project-topaz/topaz - Issue 1482_

----

This is a generic issue to discuss what I intend to PR in the near future:

Since there is no data for recent zones, I have written my own parser and started killing many mobs.
I am using THFs to farm, so I then normalize the drop rate to the TH-0 equivalent.
Output is something like:
(this is for one spot in Foret de Hennetiel)

-- Drops for Phantasmagoric Umbril  (274 killed)
     31 leafkin frond  RATE 50 (f=78) (droprate=11.31%)
     32 jar of umbril ooze  RATE 50 (f=75) (droprate=11.68%)
-- Drops for Careening Twitherym  (6861 killed)
     779 twitherym wing  RATE 50 (f=78) (droprate=11.35%)
     592 zaffre yggrete shard III  RATE 50 (f=93) (droprate=8.63%)
-- Drops for Hoary Craklaw  (1577 killed)
     131 zaffre yggrete shard III  RATE 50 (f=87) (droprate=8.31%)
     162 craklaw pincer  RATE 50 (f=88) (droprate=10.27%)

 Total mobs: 8719    including 1610 with weather

Seals drop rate:  8.87%
   Sacred Kindred's crest:  20%
   beastmen's seal:  0%
   Kindred's seal:  0%
   Kindred's crest:  37%
   High Kindred's crest:  41%

w/weather Geode  drop rate: 3.04%
w/weather Avatar drop rate: 6.65%
No-weather Geode  drop rate: 0.90%
No-weather Avatar drop rate: 1.97%

The f= value gives an indication of how close is the drop rate from the closest "official values", knowing the TH level.
100 is perfect, and 50 means that the drop rate is right in-between the 2 values, probably meaning that killing more monsters is required...

In term of PR size, do you prefer that I PR an entire zone, or smaller PRs, like 4-5 mobs each?




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Nov 06, 2020 at 16:56:09_

----

awesome data :D

Can the parser be included with the tools IBM has shared before? :D 


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Wednesday Nov 11, 2020 at 16:41:01_

----

Should I understand that nobody cares? 
It takes an awful lot of time to gather data on retail, so I'm going to stop if the Topaz team is not interested.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 11, 2020 at 16:58:41_

----

wow dude..


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Nov 11, 2020 at 17:12:33_

----

This is the second time in two weeks that I've had to post this:

> Please remember that staff/reviewers are volunteers. This will get re-reviewed and/or tested when someone has time.

ibm and I are currently the only staff. This post is only 5 days old. I'm still picking apart PRs from July. Here is my current workload:
https://trello.com/b/oyUAm25i/zach2good-ffxi-topaz-work

I'm trying to get Trusts into their final stage, and into release, before the end of the year.

I also have a real life and a real job. Time is a finite resource. 

I understand that you're upset that you've invested time into this and you want recognition, but **please** be respectful of _our_ time. It's encounters like this that make me want to leave the project altogether. 



----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Wednesday Nov 11, 2020 at 17:49:42_

----

Ok apologies. Got too impatient indeed...
