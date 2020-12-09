**Labels:**



<a href="https://github.com/neosatus"><img src="https://avatars2.githubusercontent.com/u/17725395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neosatus](https://github.com/neosatus)**
_Saturday Aug 01, 2020 at 17:11:09_
_Originally opened as: project-topaz/topaz - Issue 916_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I was browsing the code for Jump to confirm the VIT scaling worked when I believe I found a bug.

Code trace:

1. https://github.com/project-topaz/topaz/blob/release/scripts/globals/abilities/jump.lua#L21

In onUseAbility, the VIT scaling is factored in as the fTP 100, 200 and 300 values.

2. https://github.com/project-topaz/topaz/blob/release/scripts/globals/abilities/jump.lua#L36

In onUseAbility, when doPhysicalWeaponskill is called, 0 is passed for the TP value.

3. https://github.com/project-topaz/topaz/blob/release/scripts/globals/weaponskills.lua#L262

In doPhysicalWeaponskill, the value of 0 is passed into calculateRawWSDamage

4. https://github.com/project-topaz/topaz/blob/release/scripts/globals/weaponskills.lua#L99

In calculateRawWSDamage, the value of 0 is passed into the fTP function

5. https://github.com/project-topaz/topaz/blob/release/scripts/globals/weaponskills.lua#L639

Finally in fTP, the values set originally in jump.lua are ignored due to the TP value being under 1000. This should be easily verifiable as the error in that code should fire every time Jump is used.
