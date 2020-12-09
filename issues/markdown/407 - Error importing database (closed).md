**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Mar 08, 2020 at 17:31:26_
_Originally opened as: project-topaz/topaz - Issue 407_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

When importing database through terminal using mysql get the following errors:
Importing account_ip_record.sql into the database...mysql: [Warning] Using a password on the command line interface can be insecure.
ERROR 1067 (42000) at line 12: Invalid default value for 'login_time'




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Mar 08, 2020 at 17:58:03_

----

has to do with mysql version no longer supporting that format as a default.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Mar 08, 2020 at 17:58:55_

----

https://stackoverflow.com/questions/25349126/how-can-i-set-the-default-value-of-a-field-as-0000-00-00-000000#25351733


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Mar 09, 2020 at 00:15:00_

----

Changed wiki to use mariadb and libmariadb instead of mysql (just like windows build) , this resolves issue.
