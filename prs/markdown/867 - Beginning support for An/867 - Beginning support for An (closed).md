**Labels:**



<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [m241dan](https://github.com/m241dan)**
_Saturday Jul 18, 2020 at 21:01:32_
_Originally opened as: project-topaz/topaz - Issue 867_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I will be the first to admit that I am not a DevOps expert, but these commits get us off the ground.

One thing comment about the Docker stuff is that the Docker environment is used mainly for a build/run environment. There is  no artifact management. That is something I'll be implementing at a later date, but anyone on something that is hard up on disk space would suffer.

Oh, you can ignore anything in the tools/ansible/roles/ director. I didn't write any of those roles, they are by geerlingguy, pretty popular dude in the Ansible scene. I think they can be trusted.

The one thing missing from the playbook that does nginx and certbot (*-n-ssl) is missing a config for the .conf file for NGINX. You'll have to do that yourself or figure out how to get it to work with geerlingguy's role. I couldn't manage that / got tired.


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jul 19, 2020 at 14:52:04_

----

Might want to consider nuking /var/lib/apt/lists/* after this runs.  Could possibly merge update/install/nuke into a single RUN:

```
ARG DEPS="\
                git\
                libmysqlclient-dev\
                libssl-dev\
                libluajit-5.1-dev\
                libzmq3-dev\
                pkg-config\
                build-essential\
                cmake"

RUN apt-get update && \
    apt-get install -y $DEPS && \
    rm -rf /var/lib/apt/lists/*
```

Also was not sure that `libssl-dev` is required for the build phase.  We may also want to explicitly call out which compiler to bring in.


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jul 19, 2020 at 14:59:11_

----

Where is xiserver defined?


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Jul 19, 2020 at 15:05:40_

----

The build container defines the image. That process should be streamlined, but it becomes weird when we aren't doing this in a managed artifact way (which is sort of by design). 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Jul 19, 2020 at 15:06:28_

----

@ShelbyZ here


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Jul 19, 2020 at 15:08:37_

----

I dunno about that. It is listed on the wiki for setup so I kept it in there. The build container (Dockerfile) is the same for both build and runtime. It is essentially just an environment. Like I said, no artifact management, etc. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:26:23_

----

For some reason, I thought we already had a Dockerfile kicking around... I guess not


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 14:04:00_

----

There is an old branch on DSP. 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 14:04:24_

----

Hoping Nnobles (discord name) produces some better ones soon since he was bragging about them two weeks ago. 


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jul 19, 2020 at 14:52:04_

----

Might want to consider nuking /var/lib/apt/lists/* after this runs.  Could possibly merge update/install/nuke into a single RUN:

```
ARG DEPS="\
                git\
                libmysqlclient-dev\
                libssl-dev\
                libluajit-5.1-dev\
                libzmq3-dev\
                pkg-config\
                build-essential\
                cmake"

RUN apt-get update && \
    apt-get install -y $DEPS && \
    rm -rf /var/lib/apt/lists/*
```

Also was not sure that `libssl-dev` is required for the build phase.  We may also want to explicitly call out which compiler to bring in.


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jul 19, 2020 at 14:59:11_

----

Where is xiserver defined?


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Jul 19, 2020 at 15:05:40_

----

The build container defines the image. That process should be streamlined, but it becomes weird when we aren't doing this in a managed artifact way (which is sort of by design). 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Jul 19, 2020 at 15:06:28_

----

@ShelbyZ here


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Jul 19, 2020 at 15:08:37_

----

I dunno about that. It is listed on the wiki for setup so I kept it in there. The build container (Dockerfile) is the same for both build and runtime. It is essentially just an environment. Like I said, no artifact management, etc. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:26:23_

----

For some reason, I thought we already had a Dockerfile kicking around... I guess not


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 14:04:00_

----

There is an old branch on DSP. 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 14:04:24_

----

Hoping Nnobles (discord name) produces some better ones soon since he was bragging about them two weeks ago. 


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jul 19, 2020 at 00:25:47_

----

This feels like a niche offering.  To get the project introduced to Docker I would think it better to offer build and run as separate containers targeting a single distribution.  I do like the environment variables as a way to feed in values to the system, but the approach needs some cleanup.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Jul 19, 2020 at 02:20:24_

----

> Consider setting the cofig values from env rather than loading adhoc. Many of these changes would not be required.
> 
> For login -
> 
> https://github.com/project-topaz/topaz/blob/f2c28089956fbc385006521bbae651b5a62b3fae/src/login/login.cpp#L83-L90
> 
> For map -
> 
> https://github.com/project-topaz/topaz/blob/08fcc59f5fc1a5a929037ca24b13ce9cec8f287f/src/map/map.cpp#L167-L168
> 
> For search -
> 
> https://github.com/project-topaz/topaz/blob/8648c4071c1885ad1a388d74e7f868e39df2f75e/src/search/search.cpp#L170-L172
> 
> I would suggest making new methods or adjusting the read to populate values to the appropriate config objects for the environment when available.

I'm confused, you mean ALL the config values?

Edit: Oh, I get it. Not necessarily sure if that's better or not. But, whatever the project thinks is best. 

EditEdit: Yup, that would be better the more I think about it.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Jul 19, 2020 at 02:22:11_

----

> This feels like a niche offering. To get the project introduced to Docker I would think it better to offer build and run as separate containers targeting a single distribution. I do like the environment variables as a way to feed in values to the system, but the approach needs some cleanup.

Also confused by this one, there is a build one and a run one. 


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jul 19, 2020 at 02:46:53_

----

~If you are suggesting the docker/docker-compose buried in the ansible code that is not something I would hand off to someone starting with Docker.  The top-level dockerfile looked responsible for build only.~

I think this might be biting off more functionality in a single PR. It would be easier to consume breaking it into:

- topaz using environment variables
- topaz using docker
- topaz using ansible to run server

I should also clarify I find this kind of updates interesting and potentially beneficial for the project as a whole.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Jul 19, 2020 at 03:09:20_

----

> ~If you are suggesting the docker/docker-compose buried in the ansible code that is not something I would hand off to someone starting with Docker. The top-level dockerfile looked responsible for build only.~
> 
> I think this might be biting off more functionality in a single PR. It would be easier to consume breaking it into:
> 
> * topaz using environment variables
> * topaz using docker
> * topaz using ansible to run server
> 
> I should also clarify I find this kind of updates interesting and potentially beneficial for the project as a whole.

In terms of consumption, I have tried to break my commits up into that very logical order. If you don't view it in terms of a single PR and instead a sequence of commits, that might help? Ultimately, I can break it up into differing PRs, but you'll just find 3 PRs with those same commits.

Let me know if I'm misunderstanding you.

EDIT: Each commit in the sequence is compile'able and run'able (for the most part) with the functionality up to that point.


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jul 19, 2020 at 03:17:01_

----

I am not suggesting the changes as a whole do not work, but you will find easier inroads breaking up this PR, but may want to wait and see what other project members suggest.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Jul 19, 2020 at 03:39:34_

----

> I am not suggesting the changes as a whole do not work, but you will find easier inroads breaking up this PR, but may want to wait and see what other project members suggest.

I get that. I guess what I'm saying is that the changes in pieces work too ^^


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Jul 23, 2020 at 23:28:27_

----

> > Consider setting the cofig values from env rather than loading adhoc. Many of these changes would not be required.
> > For login -
> > https://github.com/project-topaz/topaz/blob/f2c28089956fbc385006521bbae651b5a62b3fae/src/login/login.cpp#L83-L90
> > 
> > For map -
> > https://github.com/project-topaz/topaz/blob/08fcc59f5fc1a5a929037ca24b13ce9cec8f287f/src/map/map.cpp#L167-L168
> > 
> > For search -
> > https://github.com/project-topaz/topaz/blob/8648c4071c1885ad1a388d74e7f868e39df2f75e/src/search/search.cpp#L170-L172
> > 
> > I would suggest making new methods or adjusting the read to populate values to the appropriate config objects for the environment when available.
> 
> I'm confused, you mean ALL the config values?
> 
> Edit: Oh, I get it. Not necessarily sure if that's better or not. But, whatever the project thinks is best.
> 
> EditEdit: Yup, that would be better the more I think about it.

Done


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 14:10:03_

----

> Let me preface this comment with: I _love_ CI and DevOps stuff when it's up and working, but I _hate_ having to maintain it.
> 
> I think there is a lot of merit in the part where you can optionally read config stuff from environment vars, but I think the rest (everything under the ansible and Jenkins folders) is out of the project's scope.
> 
> I'd love for this to exist _alongside_ the main repo, maybe in a similar way to PyDarkstar. I'd be super happy to link to this in the advanced setup guide saying "If you're interested in using Ansible and monitoring things with Jenkins, check out this repo".
> 
> My main reason for opposing this is that I wouldn't know how to maintain it, and if someone comes in asking questions about it, I absolutely won't have any answers, and I don't think many other people apart from you and Shelby will either.

I would support moving the Ansible stuff to a separate repo. But, moving the Jenkinsfile or Docker to a support repo would be like moving git actions to a separate repo, it doesn't work.

In terms of maintenance, I understand, but again it's optional. I don't see the problem with carrying this stuff along and if anyone asks, it's optional tooling you could use or not. I wrote a little documentation that is included about use, and if its not enough, the person probably isn't ready to use it yet. Minus the fact that it's incredibly simple to use. 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 14:10:47_

----

All kind of moot at the moment anyway, because I need to work the db-tool into it. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 27, 2020 at 13:13:09_

----

If a simple dockerfile that used dbtool were to appear one day, it would make it in almost immediately.

Everything else is out of the scope of the project, and whether or not it's optional for people to use - its existence will produce questions very few people will be able to answer. Sorry :(


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Sep 27, 2020 at 13:24:52_

----

Just grab the first few commits for loading from environment variables,
before I got burnt out I was going to close that and submit it in its own
anyway.

On Sun, Sep 27, 2020, 7:13 AM Zach Toogood <notifications@github.com> wrote:

> If a simple dockerfile that used dbtool were to appear one day, it would
> make it in almost immediately.
>
> Everything else is out of the scope of the project, and whether or not
> it's optional for people to use - its existence will produce questions very
> few people will be able to answer. Sorry :(
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/pull/867#issuecomment-699634075>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AA3KLWKO46DW35MCGLYM5XLSH427BANCNFSM4PALXEIA>
> .
>

