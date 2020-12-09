**Labels:**



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Monday May 04, 2020 at 17:02:22_
_Originally opened as: project-topaz/topaz - Issue 584_

----

(Look at `mob_skill_lists` first to understand the diff in `mob_pools`)

- Slip in a new skill list for NM Soulflayers right after the skill list for NQ Soulflayers
- Slide Spheroid, Spider, and "Structure" back by one
- Discover that "Structure" is a skill list for exoplates, but was also being assigned to random "structure" "mobs" which are non-combat. zero those skill lists out in their pools.
- Discover that although there isn't a skill list defined for them, pools for SOA reive "mob" structures (roots, nests, etc) have a skill list of 237 defined, zero them out
- Discovered that pool for Archaic Mirror (_not_ Rampart) was given skill list 238, despite it also being a non-combat structure, zero _that_ out too
- Finally, assign existing Soulflayer NMs' skill lists to be the new one we're slipping in after the NQs
- Delete duplicated Soulflayer NM skill lists and free up IDs

@kaincenteno 

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date


