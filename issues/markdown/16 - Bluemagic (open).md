**Labels:**

bug

focus



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:08_
_Originally opened as: project-topaz/topaz - Issue 16_

----

<a href="https://github.com/Turttle"><img src="https://avatars0.githubusercontent.com/u/10113722?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Turttle](https://github.com/Turttle)**
_Sunday Apr 12, 2015 at 18:27 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1281_

----

Blue magic physical spells don't actually miss, instead they do 0 damage and their additional effects can still be proc. All spells have a range of 20 yalms instead of 5.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:09_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Monday Apr 13, 2015 at 09:49 GMT_

----

Hmm. I am in the process of standardizing the luas. Maybe I should also note range? Only problem is, not alot of ranges listed on the wiki.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:10_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Apr 13, 2015 at 14:43 GMT_

----

Range isn't part of the script




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:11_

----

<a href="https://github.com/metalfiiish"><img src="https://avatars1.githubusercontent.com/u/6957288?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [metalfiiish](https://github.com/metalfiiish)**
_Wednesday Sep 02, 2015 at 02:04 GMT_

----

Range is typically in the sql table for the move, along with a vast amount of other variables. For instance the range for the blue magic move "screwdriver" can be seen here:

INSERT INTO `spell_list` VALUES ('519', 'screwdriver', 0x0000000000000000000000000000001A000000000000, '3', '16', '0', '4', '43', '21', '500', '14000', '2', '0', '642', '4000', '0', '0', '1.00', '0', '0', '0', '34','TOAU');

Reviewing the header informaiton at the beggining of the sql file you can see the second to last variable (34) is the spell_range.

https://raw.githubusercontent.com/DarkstarProject/darkstar/e41c17615cdbcba03023f5961b875fd93e84e1fe/sql/spell_list.sql




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:12_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Sep 02, 2015 at 02:33 GMT_

----

the range column doesn't get used in spell_list yet

On Tue, Sep 1, 2015 at 8:04 PM, metalfiiish notificationsgithub.com
wrote:

> Range is typically in the sql table for the move, along with a vast amount
> of other variables. For instance the range for the blue magic move
> "screwdriver" can be seen here:
> 
> INSERT INTO spell_list VALUES ('519', 'screwdriver',
> 0x0000000000000000000000000000001A000000000000, '3', '16', '0', '4', '43',
> '21', '500', '14000', '2', '0', '642', '4000', '0', '0', '1.00', '0', '0',
> '0', '34','TOAU');
> 
> Reviewing the header informaiton at the beggining of the sql file you can
> see the second to last variable (34) is the spell_range.
> 
> https://raw.githubusercontent.com/DarkstarProject/darkstar/e41c17615cdbcba03023f5961b875fd93e84e1fe/sql/spell_list.sql
> 
> —
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 1281Darkstar Issue issuecomment-136914190
> .


