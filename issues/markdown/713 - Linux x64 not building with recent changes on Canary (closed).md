**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Jun 11, 2020 at 18:10:50_
_Originally opened as: project-topaz/topaz - Issue 713_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

g++ -std=c++17 -DHAVE_CONFIG_H -I. -I./src/common   -fsigned-char -DFMT_HEADER_ONLY -Wall -Werror -Wfatal-errors      -fsigned-char -I/usr/include/luajit-2.1 -I/usr/include/mysql   -fsigned-char -g -O2 -MT topaz_game-battlefield_handler.o -MD -MP -MF .deps/topaz_game-battlefield_handler.Tpo -c -o topaz_game-battlefield_handler.o `test -f 'src/map/battlefield_handler.cpp' || echo './'`src/map/battlefield_handler.cpp
src/map/entities/trustentity.cpp: In member function ‘virtual void CTrustEntity::OnCastFinished(CMagicState&, action_t&)’:
src/map/entities/trustentity.cpp:169:10: error: unused variable ‘PTarget’ [-Werror=unused-variable]
     auto PTarget = static_cast<CBattleEntity*>(state.GetTarget());
          ^~~~~~~
compilation terminated due to -Wfatal-errors.
cc1plus: all warnings being treated as errors
Makefile:2776: recipe for target 'topaz_game-trustentity.o' failed
make: *** [topaz_game-trustentity.o] Error 1
make: *** Waiting for unfinished jobs....
mv -f .deps/topaz_game-grades.Tpo .deps/topaz_game-grades.Po
mv -f .deps/topaz_game-battlefield_handler.Tpo .deps/topaz_game-battlefield_handler.Po
mv -f .deps/topaz_game-battlefield.Tpo .deps/topaz_game-battlefield.Po


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jun 11, 2020 at 18:52:44_

----

Issue is caused by an unused variable warning in Trust changes which were merged alongside https://github.com/project-topaz/topaz/pull/688. Individually they seem fine, but the new warning flags in the new makefile are triggering this failure.

Short-term fix for anyone in need is to revert the makefile change merge until Trusts can get an update.
`git revert -m 1 7cf5220`


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Saturday Jun 13, 2020 at 15:29:57_

----

#717 
