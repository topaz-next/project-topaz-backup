**Labels:**



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Sunday Sep 27, 2020 at 17:18:03_
_Originally opened as: project-topaz/topaz - Issue 1205_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

It's more for tracking purposes, as looking at the code, it has been all commented out with a TODO:

charentity.cpp

// Try to double shot
    //#TODO: figure out the packet structure of double/triple shot
    //if (this->StatusEffectContainer->HasStatusEffect(EFFECT_DOUBLE_SHOT, 0) && !this->secondDoubleShotTaken &&	!isBarrage && !isSange)
    //{
    //    uint16 doubleShotChance = getMod(Mod::DOUBLE_SHOT_RATE);
    //    if (tpzrand::GetRandomNumber(100) < doubleShotChance)
    //    {
    //        this->secondDoubleShotTaken = true;
    //        m_ActionType = ACTION_RANGED_FINISH;
    //        this->m_rangedDelay = 0;
    //        return;
    //    }
    //}

