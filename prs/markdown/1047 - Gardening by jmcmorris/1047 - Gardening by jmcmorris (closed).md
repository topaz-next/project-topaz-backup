**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Monday Aug 31, 2020 at 14:55:44_
_Originally opened as: project-topaz/topaz - Issue 1047_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I reached out to @jmcmorris for some help with gardening and he **very graciously** gave me a full dump of his gardening code (that has been running on Eden for 2 or so years).  Thanks to @59blargedy for the hookup!

- Compiles, SQL imports, and game boots up.
- Otherwise untested. I suspect it's totally fine, there weren't any conflicts or shenanigans in importing/converting it.

**TODO**
- ~~Fix Linux builds~~
- This has highlighted some annoying holes with our clang-format settings, gotta patch those up
- Double/triple check I haven't missed or trampled anything during the import

**Plan**
I want this to find its way into release WITH these theoretical settings:
```
garden_day_matters: 0
garden_moonphase_matters: 0
garden_pot_matters: 0
garden_mh_aura_matters: 0
```
Then there is a point in the version history where everything works and those settings are available for people that might want them. We can rip them out after if that's what people want.

![image](https://user-images.githubusercontent.com/1389729/91733901-e6605380-ebb2-11ea-8c8b-29a60887be9a.png)

