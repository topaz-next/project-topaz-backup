**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:05_
_Originally opened as: project-topaz/topaz - Issue 1_

----

<a href="https://github.com/Jupiter065"><img src="https://avatars3.githubusercontent.com/u/7451641?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Jupiter065](https://github.com/Jupiter065)**
_Sunday Jun 22, 2014 at 01:41 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 349_

----

So there are a whole bunch of mobs that are taking bonus/reduced damage from certain element spells. Basically every mob.  It seems mobs are taking bonus damage from elemental spells they are weak to and reduced damage from elemental spells they are strong from. I haven't played retail in a while, but I thought that elemental strengths/weaknesses only affected resistance rates, other than in very rare cases (Sahagin taking 50% damage from water, for example), and I've been having a hard time finding any info that says otherwise.

Was this a design choice, a retail update I'm not aware of, or just a mistake?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:07_

----

<a href="https://github.com/Jupiter065"><img src="https://avatars3.githubusercontent.com/u/7451641?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Jupiter065](https://github.com/Jupiter065)**
_Sunday Jun 22, 2014 at 02:15 GMT_

----

It looks like it's going the other way too, in that mobs that take 50% magic damage are also getting a +50 magic evasion bonus, making landing enfeebles on them virtually impossible. Basically, the elemental columns in the mob_family_system table seem to be using the same number for 2 different things.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:58:08_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Jun 23, 2014 at 00:40 GMT_

----

yes, it uses the same number for two different things.  it's always been like that and nobody's really bothered to fix it, though


