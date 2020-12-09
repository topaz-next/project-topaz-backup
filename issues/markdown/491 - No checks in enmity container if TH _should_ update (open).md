**Labels:**

bug



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 16:53:58_
_Originally opened as: project-topaz/topaz - Issue 491_

----

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
> "are THs cumulative or just highest-tier-counts?"
> "Highest level of TH of all characters on the mob's enmity list"
<https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/src/map/entities/mobentity.cpp#L1008-L1010>
<https://github.com/project-topaz/topaz/blob/4d09173b57dd5867dd3997436fa3ee66eeea0fbb/src/map/enmity_container.cpp#L429-L444>
> "hmmm interesting, so, could a THF/WHM go around healing people to get better drops for that party?"
> "...Yes. It seems that at the moment, the only check within UpdateEnmity is whether CE + VE is more than zero"

<https://github.com/project-topaz/topaz/blob/4d09173b57dd5867dd3997436fa3ee66eeea0fbb/src/map/enmity_container.cpp#L163-173>

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**
- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated




