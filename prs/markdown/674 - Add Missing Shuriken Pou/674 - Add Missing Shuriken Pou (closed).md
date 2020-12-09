**Labels:**

reviewed



<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Monday Jun 01, 2020 at 14:23:01_
_Originally opened as: project-topaz/topaz - Issue 674_

----

Additional shuriken pouches that were missing: Fuma, Juji, Manji and Shuriken.

SQL query to add usage:
INSERT INTO item_usable (itemid, name, validTargets, activation, animation)
VALUES ('6297', 'juji_shuriken_pouch', '1', '1', '55'); 
VALUES ('6298', 'manji_shuriken_pouch', '1', '1', '55'); 
VALUES ('6299', 'shuriken_pouch', '1', '1', '55'); 
VALUES ('6302', 'fuma_shuriken_pouch', '1', '1', '55');

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 07:03:14_

----

Looks good, would you mind adding those queries to `sql\item_usable.sql`?


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Wednesday Jun 03, 2020 at 13:39:58_

----

> 
> 
> Looks good, would you mind adding those queries to `sql\item_usable.sql`?

Alright, I've done so. Cheers.
