**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Thursday Apr 09, 2020 at 20:34:46_
_Originally opened as: project-topaz/topaz - Issue 482_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I'm going to need this for the extensions to the MobSpellContainer I'm doing for Trust spellcasting, allows specifying a family of spells so you can pick the best out of them (Fire I vs Fire II) etc.

**Useful commands:**
```
SELECT spellid, name, family FROM tpzdb.spell_list;
```
```
SELECT name, family FROM tpzdb.spell_list Where family > 0;
```
```
"C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqldump" --hex-blob --extended-insert=FALSE tpzdb -h localhost -u root -proot spell_list > spell_list.sql
```



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 15, 2020 at 15:36:07_

----

Others: Results of a regex on `spell_list.sql` to put spell ID, name, and family into a table, and then running a lua script that spits out a reverse-lookup of family names.

As of ad80d14:
[family_results.txt](https://github.com/project-topaz/topaz/files/4482140/family_results.txt)
(Empty lines are from me breaking up groups while reviewing this output.)
