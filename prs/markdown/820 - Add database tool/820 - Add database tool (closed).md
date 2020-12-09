**Labels:**

merge ready



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jul 07, 2020 at 03:28:52_
_Originally opened as: project-topaz/topaz - Issue 820_

----

-Deprecate migrations script
-Refactor give_items

Saves commit hash to version.conf when updating. On future updates, will
diff that hash against current hash to only import files that have
changed. Saves settings.

Optional args (both update options will also backup and migrate):
`python dbtool.py backup` will backup databse.
`python dbtool.py backup lite` will create a backup of only the tables marked as protected (player_data in config)
`python dbtool.py update` will check versions and only update if necessary.
`python dbtool.py update full` will do a full update.
`python dbtool.py migrate` will check and perform any needed migrations.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 20, 2020 at 20:26:14_

----

Dunno if this might interfere with being able to upload/edit/clone YAML files that we want shared, like Travis or containers. May want to assign the ignore to just the tools subdirectory for now.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jul 21, 2020 at 17:32:58_

----

Updated to ignore just this file for now.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 20, 2020 at 20:26:14_

----

Dunno if this might interfere with being able to upload/edit/clone YAML files that we want shared, like Travis or containers. May want to assign the ignore to just the tools subdirectory for now.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jul 21, 2020 at 17:32:58_

----

Updated to ignore just this file for now.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jul 07, 2020 at 04:18:00_

----

> Tested the version before this one for both initial setup and update, adding items to ignore list and performing backups. Had one issue that was resolved in this version, everything else worked great!

IDK how recent this was, but a lot has changed since we discussed this! Adding items to the ignore list is now saved to a file and persists, and you can even provide and change the MySQL bin path if it's not found in the system paths. I also changed how some stuff is displayed to hopefully make it easier to understand and use.
