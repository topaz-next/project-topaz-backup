**Labels:**

merge ready



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 28, 2020 at 00:41:57_
_Originally opened as: project-topaz/topaz - Issue 896_

----

No more extra diffs or merge conflicts due to people removing line-ending semicolons in Lua scripts.

(Will probably conflict with a lot of recently-merged PRs or PRs which are still open. But I'd be on the hook for resolving conflicts in the merged PRs _anyway_.)

Two commits, the first is literally just:
![replace-all](https://user-images.githubusercontent.com/13112942/88604531-2342a300-d067-11ea-977e-ee5f7689ef12.png)

Results:
> 2988 changed files
> Total replaced: 29694

I will freely admit to not reviewing the diff - there shouldn't be need to. Anything that might break from this _deserves_ to.

The second commit was upon a test boot, the server complaining about [missing table element separators here](https://github.com/project-topaz/topaz/blob/c52431e2c48516954aa2f5ebbb331238f43cc3d8/scripts/globals/limbus.lua#L65-L75). I resolved those then did a findall for `};\n` on un-replaced release branch and manually looked through all results for any other instances:
![table-seperate](https://user-images.githubusercontent.com/13112942/88604927-0a86bd00-d068-11ea-9993-2c8327217142.png)

That Limbus file was the only one that attempted to separate tables within tables with semicolon-newline separators. And the server boots without errors in the log (please ignore my outdated conf):
![boots](https://user-images.githubusercontent.com/13112942/88605593-e035ff00-d069-11ea-938d-b197b4d9b10e.png)

It is technically possible for some script somewhere to have done the following
```lua
my_table = {
  thinga;
  thingb;
  thingc
}
```
And those tables will now be broken until spotted.

But to be honest, I'm not particularly concerned about such tables. They'd be old, obscure ones which _deserve_ to break for using a semicolon as an element separator. I'd rather _kill all the line-ending semicolons_ now in one fell swoop and then potentially fix up any obscure scripts later. **We've put up with these semicolons _long_ enough.**

**This particular PR will miss semicolons which occur as the final character in a file.** mrhappyasthma tried to move us closer to being able to doing something like this in #426, but I'm seeing instances after my mass-replace which were missed. For the sake of keeping a PR of this diff magnitude **as simple as possible (literally all I did was replace `;\n` with `\n` inside `/scripts/`)**, those last line-ending semicolon survivors will be addressed at a future date.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 28, 2020 at 00:46:01_

----

For the curious, this was the last conflict I was willing to let those evil semicolons create:
![conflict](https://user-images.githubusercontent.com/13112942/88606216-a1a14400-d06b-11ea-9073-bde3c540e82e.png)



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 28, 2020 at 01:09:41_

----

The above commit is just:
![comment-regex](https://user-images.githubusercontent.com/13112942/88607475-db277e80-d06e-11ea-85f9-b8170b172bc9.png)

> Matching files: 528
> Total replaced: 2294

And removes line-ending semicolons which were followed by comments.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 28, 2020 at 01:59:53_

----

Sorry @wrenffxi , this is going to merge conflict you on #879 and #889.

I hope you of all people will understand~ 😅 
