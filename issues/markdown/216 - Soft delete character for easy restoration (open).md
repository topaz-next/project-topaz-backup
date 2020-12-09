**Labels:**

feature



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:53_
_Originally opened as: project-topaz/topaz - Issue 216_

----

<a href="https://github.com/nasomi"><img src="https://avatars0.githubusercontent.com/u/6567800?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [nasomi](https://github.com/nasomi)**
_Wednesday Feb 28, 2018 at 23:01 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4607_

----

github/DarkstarProject/darkstar/blob/master/src/login/lobby.cppDarkstar Issue L547

Replace with:
`const char *pfmtQuery = "update chars set charname = concat(charname, 'deleted'), accid = concat(999,accid) where charid = %i";
`



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:55_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 01, 2018 at 02:43 GMT_

----

Suggestion:
`concat(charname, '_deleted')` so Timmy becomes Timmy_deleted instead of Timmydeleted



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:56_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Mar 01, 2018 at 02:44 GMT_

----

probably would be best to just have a new column in chars for deleted or not

On Wed, Feb 28, 2018 at 7:43 PM, TeoTwawki <notificationsgithub.com> wrote:

> Suggestion:
> concat(charname, '_deleted') so Timmy becomes Timmy_deleted instead of
> Timmydeleted
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 4607Darkstar Issue issuecomment-369456168>,
> or mute the thread
> <github/notifications/unsubscribe-auth/ABGI_3ubTovQ4LBmzNMnj6iq9-P3TDOuks5tZ2BsgaJpZM4SXflO>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:57_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 01, 2018 at 03:01 GMT_

----

Depends on if you want to free up the name or not I guess



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:58_

----

<a href="https://github.com/nasomi"><img src="https://avatars0.githubusercontent.com/u/6567800?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nasomi](https://github.com/nasomi)**
_Thursday Mar 01, 2018 at 03:23 GMT_

----

Freeing up the charname is the whole point of deleting character. People will make and remake chars lots of times using the same name but changing appearance.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:59_

----

<a href="https://github.com/kamajii7"><img src="https://avatars0.githubusercontent.com/u/13575698?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [kamajii7](https://github.com/kamajii7)**
_Friday Mar 02, 2018 at 00:24 GMT_

----

Not sure if this is my place, but to make it unique shouldn't we add the character id? i.e. Timmy_10_deleted. I just see the issue of freeing up a name then someone else taking the name then another soft delete happening, causing two Timmy_deleted's, may cause confusion for administrators.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:00_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Friday Mar 02, 2018 at 00:26 GMT_

----

Better solution is to add a deleted column, and upon deletion, move the
name from name to deleted. Keeps the name for querying later, but takes it
out of the actual name column for uniqueness.

On Mar 1, 2018 5:24 PM, "Rob" <notificationsgithub.com> wrote:

> Not sure if this is my place, but to make it unique shouldn't we add the
> character id? i.e. Timmy_10_deleted. I just see the issue of freeing up a
> name then someone else taking the name then another soft delete happening,
> causing two Timmy_deleted's, may cause confusion for administrators.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 4607Darkstar Issue issuecomment-369778327>,
> or mute the thread
> <github/notifications/unsubscribe-auth/ABGI_xlFY3wCuwwJVshEqgsX3fYNyBR_ks5taJFDgaJpZM4SXflO>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:02_

----

<a href="https://github.com/kamajii7"><img src="https://avatars0.githubusercontent.com/u/13575698?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [kamajii7](https://github.com/kamajii7)**
_Friday Mar 02, 2018 at 00:33 GMT_

----

I completely agree. I am just thinking of the interim for a quick solution. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:03_

----

<a href="https://github.com/nasomi"><img src="https://avatars0.githubusercontent.com/u/6567800?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nasomi](https://github.com/nasomi)**
_Friday Mar 02, 2018 at 03:49 GMT_

----

Yeah this does not need to be this complicated. I’ve been running this system for 2 years now and it’s served every undelelete I needed. A distinct name is hardly required for deleted chars, you could just look up the unmodofied account id to see the login. The person in question should be able to provide the login name for the char they want Undeleted. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:04_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Friday Mar 02, 2018 at 12:51 GMT_

----

an additional field in chars will do
is_deleted



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:05_

----

<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Friday Mar 02, 2018 at 19:24 GMT_

----

teschnei and takhlaq suggestion/solution is nice since it doesn't require modification to the name field, and accomplishes the task with a bit change instead of a string change. One wrench in the works by using the extra field method is that some of the tertiary things that interface with the db might be impacted by this change (Arcanus, Afterhours AH, DSP Web, etc) when doing a lookup by character name. 

Deleted character records would still be uniquely identified via charid/accid, but until tertiary applications update their logic to look for an additional flag to delete/exclude/do-something-else, there may be some confusion in query results.

You'd need a manual process/procedure to deal with a name collision if the character name has been re-used between deletion and restoration request (think about malicious or account takeover scenarios), but that's out of scope for this conversation.

As an aside, I'm not aware of an un-delete method in Retail that allows a user to restore a character without [contacting customer support](http://support.na.square-enix.com/faqarticle.php?kid=12457&id=20&la=1&ret=faq&pv=20&page=1&c=0&sc=0&so=0), so this would still be in line with how the Retail world does things.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:06_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Friday Mar 02, 2018 at 19:32 GMT_

----

they shouldnt be affected if the field is added on to the end, even if external tools 
```sql
SELECT * FROM chars
```

instead of selecting each field by name



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:08_

----

<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Friday Mar 02, 2018 at 19:59 GMT_

----

It depends on how their query is being built:

`
SELECT charid,accid,charname FROM chars WHERE charname like "something%"`

This would return multiple hits for different characters instead of a unique result by name as it does today. This isn't world ending, the query could be modified to include an additional qualifier:

`
SELECT charid,accid,charname FROM chars WHERE charname like "something%" AND is_deleted != 1`

Just wanted to bring it up as something to consider as a repercussion of this proposed change.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:09_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [xipies](https://github.com/xipies)**
_Sunday Mar 04, 2018 at 05:14 GMT_

----

The two routes I have gone on other projects are:

* A flag, like is_deleted, and all queries had to be updated and/or rerouted (e.g., through a filtered view).
* Renamed the entity to a random value (uuid), and if needed (was not always), stored the original name somewhere else, such as another column. This was done where I less control over the usage.


