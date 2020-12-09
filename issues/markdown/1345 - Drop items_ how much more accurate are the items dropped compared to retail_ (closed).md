**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 00:53:02_
_Originally opened as: project-topaz/topaz - Issue 1345_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Drop items, how much more accurate are they compared to retail?
As an example, the "Qsd. Coffer Key" (itemID: 1054)
http://ffxidb.com/items/1054
![figure](https://user-images.githubusercontent.com/71148313/95802773-5a0c8900-0d39-11eb-81c7-a49587a2b205.png)

In the case of topaz, I used the following SQL to check it.
(If the SQL is wrong, I'd be happy to point it out to you.)

mysql> select mg.zoneid, mg.name, minLevel, maxLevel, md.itemRate from mob_groups mg JOIN mob_droplist md on mg.dropid = md.dropId where md.itemId=1054 group by mg.zoneid order by minLevel;
+--------+-------+----------+----------+----------+
| zoneid | name  | minLevel | maxLevel | itemRate |
+--------+-------+----------+----------+----------+
|    208 | Mimic |       56 |       59 |     1000 |
+--------+-------+----------+----------+----------+

For topaz, is "Mimic" the only monster to drop the "Qsd. Coffer Key"?
Is there a known problem with the different drop items?



----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 00:55:06_

----

Sorry, there was an extra "groupby" in the SQL statement. Ignore it.

mysql> select mg.zoneid, mg.name, minLevel, maxLevel, md.itemRate from mob_groups mg JOIN mob_droplist md on mg.dropid = md.dropId where md.itemId=1054 order by minLevel;
+--------+------------------+----------+----------+----------+
| zoneid | name             | minLevel | maxLevel | itemRate |
+--------+------------------+----------+----------+----------+
|    208 | Sand_Spider      |       51 |       55 |       10 |
|    208 | Helm_Beetle      |       51 |       58 |       20 |
|    208 | Sand_Eater       |       51 |       59 |       30 |
|    208 | Antican_Hastatus |       52 |       59 |       50 |
|    208 | Antican_Princeps |       52 |       59 |       60 |
|    208 | Antican_Signifer |       52 |       59 |       20 |
|    208 | Mimic            |       56 |       59 |     1000 |
|    208 | Sand_Lizard      |       56 |       59 |       20 |
+--------+------------------+----------+----------+----------+



----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 00:58:36_

----

If you look closely, there was only one difference.
The "Sand Eater" doesn't exist on topaz.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 04:07:39_

----

Sorry, I looked at it wrong.
The drop monster that doesn't exist in topaz is "Sabotender Bailaor".

mysql> select mg.name, mg.zoneid, minLevel, maxLevel, md.itemRate from mob_groups mg JOIN mob_droplist md on mg.dropid = md.dropId where md.itemId=1054 order by md.itemRate desc;
+------------------+--------+----------+----------+----------+
| name             | zoneid | minLevel | maxLevel | itemRate |
+------------------+--------+----------+----------+----------+
| Mimic            |    208 |       56 |       59 |     1000 |
| Antican_Princeps |    208 |       52 |       59 |       60 |
| Antican_Hastatus |    208 |       52 |       59 |       50 |
| Sand_Eater       |    208 |       51 |       59 |       30 |
| Sand_Lizard      |    208 |       56 |       59 |       20 |
| Helm_Beetle      |    208 |       51 |       58 |       20 |
| Antican_Signifer |    208 |       52 |       59 |       20 |
| Sand_Spider      |    208 |       51 |       55 |       10 |
+------------------+--------+----------+----------+----------+
8 rows in set (0.33 sec)




----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Oct 13, 2020 at 08:03:01_

----

Not sure what is your point exactly, but for sure we all know that there are probably a lot of inaccuracies left in drop rates.
Most of the rates come from ffxidb as I understand. At a time where TH was not exactly understood. And TH behavior changes at some point too (you can't see drop rates with TH>4, etc).
But it's better than nothing.
Also for rare/ex items, contrary to Topaz, on retail if you have already the item, you don't even see it dropped again. So FFXIDB could not know that you missed one.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 08:51:55_

----

Thank you for your comment.
I don't have much of an issue with the accuracy of the drop rate. (And I think the exact information is non-public...)

> Also for rare/ex items, contrary to Topaz, on retail if you have already the item, you don't even see it dropped again. So FFXIDB  could not know that you missed one.

Okay, sure. I hadn't noticed. Interesting.

What I'm concerned about is the type of drop monsters.
For example, in the case of "Qsd. Coffer Key", I think you mean that "Sabotender Bailaor" may drop at retail, but not at Topaz.
(You're saying that it could happen that if you were aiming for a drop item based on the wiki, Topaz has different specs.

Does Topaz tolerate the fact that this drop item has different specifications than the retail version? Or is there a policy to make it closer to retail?


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 09:16:58_

----

It's starting to seem like you're overly concerned with the details of the differences between retail and topaz.
Unless it's a significant specification difference, does that mean that those who notice it will take the initiative to fix it?
And it would be a huge task to make the item drop monsters completely the same as the retail ones in the first place.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 13, 2020 at 14:09:11_

----

there looks to be a language barrier here where neither of you got what the others intended meaning was


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 15:38:49_

----

I'm sorry. I will sort out the problems once, so I would like to close it.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 13, 2020 at 16:38:40_

----

We want Topaz drop lists to match retail as close as possible. This includes which mobs drop an item, and the percentage rate they drop at.

If Topaz does not match retail, it is because we do not have correct data.

People might fix reported inaccuracies. It can be difficult to determine which rate to select. There can be argument over what percentage rate to choose.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 13, 2020 at 16:48:41_

----

@ibm2431 tell them about the buckets. :stuck_out_tongue: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 13, 2020 at 18:45:30_

----

Drop rate percentages in Topaz were added before we knew the official mechanics of Treasure Hunter and the drop rate percentages.

SquareEnix has released information on how Treasure Hunter functions.
<https://forum.square-enix.com/ffxi/threads/56550-Development-Q-A-March-2020?p=624996&viewfull=1#post624996>

All items have a "rarity".
- Very Common
- Common
- UnCommon
- Rare
- Very Rare
- Super Rare
- Ultra Rare

 Items of the same rarity have the same drop rate percentage.

When correcting Topaz drop rate percentages, we should choose values that are equal to an official SquareEnix "bucket" value for Treasure Hunter.

Data on FFXIDB can be examined for TH0, TH1, and TH2. Values on FFXIDB can be compared to official SquareEnix Treasure Hunter values.

By comparing FFXIDB data to official SquareEnix Treasure Hunter values, we can guess the "rarity" of an item.

When we choose a "rarity" for an item, we can correct Topaz drop percentage rate to the official SquareEnix value.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 14, 2020 at 00:50:51_

----

Thank you for sharing the useful information.
I was able to find out about Square's "bucket" on drop rates. I will learn about the reference site.

I'd like to know your thoughts on the combination of drop items and monsters.
(Ignore the differences in drop rates here.)

For example, in the case of "Bronze Box" (item ID: 580)
In the case of topaz
The two drop monsters are Ocean_Crab and Sea_Crab
mysql> select mg.name, mg.zoneid, minLevel, maxLevel, md.itemRate from mob_groups mg JOIN mob_droplist md on mg.dropid = md.dropId where md.itemId=580 order by md.itemRate desc;
+------------+--------+----------+----------+----------+
| name       | zoneid | minLevel | maxLevel | itemRate |
+------------+--------+----------+----------+----------+
| Ocean_Crab |    221 |       10 |       14 |      980 |
| Ocean_Crab |    220 |       10 |       14 |      980 |
| Ocean_Crab |    228 |       10 |       14 |      980 |
| Ocean_Crab |    227 |       10 |       14 |      980 |
| Sea_Crab   |    227 |       10 |       20 |       80 |
| Sea_Crab   |    221 |       10 |       20 |       80 |
| Sea_Crab   |    220 |       10 |       20 |       80 |
| Sea_Crab   |    228 |       10 |       20 |       80 |
+------------+--------+----------+----------+----------+

For retail
There is only one drop monster, the Ocean_Crab
http://ffxidb.com/items/580
![figure](https://user-images.githubusercontent.com/71148313/95930969-e20a9580-0e02-11eb-97b6-4f70880654b9.png)

https://ffxiclopedia.fandom.com/wiki/Bronze_Box
![figure2](https://user-images.githubusercontent.com/71148313/95930792-5e50a900-0e02-11eb-8231-1992938c8030.png)

In the case of Topaz, why is Sea_Crab set up to drop the "Bronze Box"?
What should I think about these differences?



----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 14, 2020 at 01:05:32_

----

As a way of thinking.

It's a clear difference, and those who notice it should take the initiative to fix it.
Or.
It's just a minor issue, so don't bother, forget it.

I'd be happy to know which thinking is more common for topaz.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 14, 2020 at 03:37:53_

----

If a monster in Topaz drops an item, when sources like FFXIDB or FFXIclopedia do not say the monster drops it, it is a very clear difference.

We want to fix very clear differences.

In the case of "Sea Crab" on Topaz, it should not drop the "Bronze Box".

If a person learns of very clear differences, they are welcome to report or fix the incorrect data!


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 14, 2020 at 06:50:46_

----

Thanks so much for answering your thoughts.
From now on, I will report back if I find a clear difference in this matter.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 14, 2020 at 07:07:26_

----

Thank you for all the work you have done to investigate inaccurate things!
