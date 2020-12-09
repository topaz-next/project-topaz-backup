**Labels:**

bug



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Thursday Mar 12, 2020 at 16:19:42_
_Originally opened as: project-topaz/topaz - Issue 412_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

While mounted you can use the attack action to hop off of your mount and start attacking a mob. When you do so the "Mounted" status remains until you strike the enemy.

When you hit the dismount button you correctly lose the mounted status.

I have tested that you cannot call your mount in combat.

Tested on a few different mounts.

This is probably a good first issue for someone wanting to poke around in core.

This on player engage might be one direction to investigate 👍 

```
        if (PChar->StatusEffectContainer->HasStatusEffect(EFFECT_MOUNTED))
        {
            PChar->StatusEffectContainer->DelStatusEffect(EFFECT_MOUNTED);
        }
```

Or maybe:
```
targ:delStatusEffect(tpz.effect.MOUNTED)
```
in the mounted effect, who knows?

![image](https://user-images.githubusercontent.com/1389729/76542400-97502600-648d-11ea-8413-0c212bc1ee03.png)




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 23:11:37_

----

> While mounted you can use the attack action to hop off of your mount and start attacking a mob.

Is this retail? I'll admit to never having tried it. Does the action appear in the menu?

(Reading this due to #417 , making sure that we shouldn't be blocking the attack action outright.)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Mar 17, 2020 at 12:19:43_

----

@ibm2431  on retail your character will do a dismount animation but the initial melee attack will happen before the animation is completed (dmg is in log already) so it doesn't block it at all
