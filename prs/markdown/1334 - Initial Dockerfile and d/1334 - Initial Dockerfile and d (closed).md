**Labels:**

approved

reviewed



<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [NassirAlawar](https://github.com/NassirAlawar)**
_Monday Oct 12, 2020 at 02:13:42_
_Originally opened as: project-topaz/topaz - Issue 1334_

----

I have added a way to launch a server using docker. I have included instructions in the DOCKER file. I also included a third party script called wait-for-it and the license to go with it. The docker server uses the configuration found in conf/docker with the key difference being the mysql_host is set to "db" so the two services can communicate. Lastly I included the adminer service which allows for easy access to the database through the web on localhost:8080

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 12, 2020 at 04:59:34_

----

Congrats on your first PR! Thanks for these! 

I had a quick glance through all the docker stuff (but not the readme yet) and they're pretty much the level of simplicity I was wanting out of something like this, good job!

~~I had a look through the copied conf files, and I didn't _see_ anything special apart from filled out login details?~~ db, got it!

I also wonder, do we need this `wait-for-it.sh` thing in the repo? Is there no way we can call out for it when we need it and cache it?

Would the content in this PR help you? 
https://github.com/project-topaz/topaz/pull/1202

I've been holding off because I don't know what names I should be using (`MYSQL_PWD` vs `DB_PASS` etc.), would this make your life easier and allow you to not have to edit conf files?


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Monday Oct 12, 2020 at 05:33:37_

----

Thanks, hopefully more to come :)
That other PR is interesting for sure. That would simplify it since we could use the default config then just override the mysql_host and set it do "db". I could set it the same way I set this one `ENV DEBIAN_FRONTEND=noninteractive`. Let me know if you'd like me to change it, I can wait for that to get merged in.

As for `wait-for-it.sh` I could write something simplier. I mostly grabbed it as the easiest solution from docker's website. If you'd prefer I can work on writing something simple specifically for this use case. Could also pull his repo but he has other files in there other than just the license and that script but that seemed like overkill


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 12, 2020 at 05:45:11_

----

You might be able to get around using `wait-for-it` with this stuff we have in the CI scripts:
https://github.com/project-topaz/topaz/blob/release/.github/workflows/build.yml#L154

Admittedly, a lot of the CI script stuff is cobbled together copy-paste, because I don't yaml 👀 


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Monday Oct 12, 2020 at 05:53:48_

----

I can try it out tomorrow and see if I can come up with something in-house. The `"mysqladmin ping"` might be enough but I think it will still need to be a script. I don't think docker supports doing scripts like this in the docker-compose file ```run: |
        mysql -h 127.0.0.1 -uroot -proot -e "SHOW DATABASES"``` but I'll give that a shot too 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 12, 2020 at 10:17:24_

----

I'm gonna sort out that other PR I listed later today (I hope), while that's happening - can you investigate the mounting of folders in docker images?
The thing I'm concerned about is this:
The current linux build, or running `cmake .` polutes the source tree - which is bad practice. We do this on CI because that filesystem will get nuked after run. We don't want to pollute the filesystem of the docker image's host. 

Solvable by doing an "out of tree" build:
```
mkdir build
cd build
cmake ..
cd ..
```

The CMake scripts are set up to put the finished binaries in the root folder anyway, so you don't have to worry about relative paths etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 13, 2020 at 12:53:20_

----

https://github.com/project-topaz/topaz/pull/1202 has now been merged, should make your life a little easier 👍 


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Tuesday Oct 13, 2020 at 17:07:33_

----

Sure I should be able to do the build change 👍 I didn't get a chance to look at the wait-for-it yesterday but I should have time for all three today


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Tuesday Oct 13, 2020 at 21:45:48_

----

I've implemented the env variables settings and moved the build to a /build folder which I delete after it completes.
I think I can look into the wait-for-it tonight


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Wednesday Oct 14, 2020 at 22:54:08_

----

Let me know if there's anything else, I've solved all the issues listed and tested the build. I had to make a change to the wait script in order to bring up the server in the correct order with proper delay. I believe in the future we can make the server logic smarter and remove this wait script by allowing the server to retry connections.

I have tested and I am able to launch the server, create an account, create a character and log into the world 👍 


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 15, 2020 at 05:36:58_

----

Sure, I can try that tomorrow, I think it's possible if I update the paths


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 15, 2020 at 08:34:09_

----

Took a look at moving everything to a docker folder, I don't think it's as trivial as it seems. For security reasons docker-compose cannot access any directory above the current directory.
I also tried leaving only the docker-compose in the topaz folder then moved everything else to a docker folder and pointed it to the Dockerfile but I got errors when trying to do `docker-compose up`. There might be ways around the directory part with additional command line args but not sure what's causing the other errors.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 15, 2020 at 08:47:12_

----

In that case I think we're good to go, DOCKER AWAY 🐳 


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 15, 2020 at 18:13:07_

----

![mergedparrot](https://user-images.githubusercontent.com/22628472/96169675-629ac600-0ed7-11eb-962c-2711950acf32.gif)

