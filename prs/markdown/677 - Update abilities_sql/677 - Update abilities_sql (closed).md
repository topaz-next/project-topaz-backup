**Labels:**



<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [illzbee](https://github.com/illzbee)**
_Tuesday Jun 02, 2020 at 03:05:56_
_Originally opened as: project-topaz/topaz - Issue 677_

----

added 295,'curing_waltz_v'

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 08:11:49_

----

Looks good, is there a reason you moved this out of order? It looked like you had it in the right place in the first commit.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jun 03, 2020 at 11:35:31_

----

looks like travis was having a partial outage at the time of the 1st commit, guessing you mistakenly thought you needed to put new stuff at the bottom because of that error. the rows should stay sorted by primary key and the error was just the service being partly out.
> apt-get install failed
The command "sudo -E apt-get -yq --no-install-suggests --no-install-recommends $(travis_apt_get_options) install software-properties-common g++-7 luajit-5.1-dev libzmq3-dev mysql-client-core-5.6 mysql-server-5.6 mysql-client-5.6 luarocks python3.7" failed and exited with 100 during .


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jun 03, 2020 at 11:36:02_

----

p.s. commit messages should be more descriptive than "update thing"


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Wednesday Jun 03, 2020 at 12:21:15_

----

When I went on my test files it moved it on the bottom. Which made me think
that was the cause of the error. I won't make the mistake again. Thanks for
letting me know.

On Wed, Jun 3, 2020, 7:35 AM TeoTwawki <notifications@github.com> wrote:

> looks like travis was having a partial outage at the time of the 1st
> commit, guessing you mistakenly thought you needed to put new stuff at the
> bottom because of that error. the rows should stay sorted by primary key
> and the error was just the service being partly out.
>
> apt-get install failed
> The command "sudo -E apt-get -yq --no-install-suggests
> --no-install-recommends $(travis_apt_get_options) install
> software-properties-common g++-7 luajit-5.1-dev libzmq3-dev
> mysql-client-core-5.6 mysql-server-5.6 mysql-client-5.6 luarocks python3.7"
> failed and exited with 100 during .
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/pull/677#issuecomment-638139654>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/APXN6B6CLRAQOAV4TDUNVODRUYYRBANCNFSM4NQKQQNA>
> .
>

