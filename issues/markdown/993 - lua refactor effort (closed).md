**Labels:**

WIP



<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 19:45:11_
_Originally opened as: project-topaz/topaz - Issue 993_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**Sorry for the double PR, but we using a new repo at Rebirth so... figured it b est ot just do a new one**

This is a WIP PR. That being said, these commits will be cleaned up but I wanted to get this out the door so reviewers could start looking it over.

**New Lua System**
This code marks the possible beginning of a massive refactor effort for the Topaz project. It could be the model for all future lua code, including proper integration testing and changing the way that the Core invokes lua code.

This design heavily leverages lua table mechanics. The benefits of this is that the code can be written in a more clean and concise manner, it is easier to test, and it supports a module system for people that are interested in customization.

It also follows a C++ language core principle, where possible, of not paying for what you do not use. You will see that there are very few decision paths: ie, each function is responsible for one thing and one thing only. There is no, "if I'm this, do X, if I'm that, do Y." This design focuses on, "I'm me, and this is what I do" type design (super technical terminology).

This design will eventually be extended to weaponskills, blue magic, ninjutsu, summoning magic, avatar damage, puppet master damage, etc, etc. 

**Core Interface Functions**
This method seems like it might be a bit extra, and it is definitely different than how the design currently looks (especially considering the design moves away from individual files for things like spells, weaponskills, items, etc, and uses lua tables instead). At first, you may think, "why not just call the spell directly from C++ instead of loading the interface function and THEN calling the spell." The reason to not do it that way is that it excludes people from writing modules that could adjust the process of how C interacts with Lua.

**Testing**
The current design of the testing rig can be run from the base director using lua directly. I have fabbed up libraries that it will use to simulate calls to the Core.

*lua scripts/test_suite/test_magic.lua* 

The tests themselves are very non-committal in terms of numbers. They mostly focus on relative numbers to validate that things are working logically and that there are no bugs in any of the paths. The reason for this non-committal approach is that so people who want to customize their code do not have to continually update tests to match their specific numbers just because they want AM2 to do more damage.

**Modules (not included in this PR, but can be if @zach2good doesn't find anything he likes for modules)**
I have included a single module. The idea of the modules is that people who want to customize their code do not have to edit the main project code (potentially creating conflicts when updating, etc). The example module is FAR from a polished product. It is simply to show how the mechanics should/could work, but there should be some formalization process put towards how a Topaz module should look / be executed. For now, I've just hacked it in to show the potential of the new system.

**Work List (not comprehensive, yet...):**
 * [x] Outline basics of new lua code design / testing / modules
 * [ ] Create a unified pDIF table for both the Core and the Lua stuff. Core will load pDIF table from Lua so that modules can affect pDIF reliant code in the Core
 * [ ] Extend design to cover ...
     * [ ] physical weaponskills
     * [ ] magical weaponskills
     * [ ] "unique" weaponskills
     * [ ] enfeebles (magic)
     * [ ] enfeebles (songs)
     * [ ] buffs (white magic)
     * [ ] buffs (bard)
     * [ ] blue physical spells
     * [ ] blue magical spells
     * [ ] blue buffs
     * [ ] avatar damage
     * [ ] automatons
 * [ ] Back fill all the data (plans to automate this process, doing it by hand is insane)
     * [ ] elemental nukes
     * [ ] physical weaponskills
     * [ ] "unique" weaponskills
     * [ ] enfeebles (magic)
     * [ ] enfeebles (songs)
     * [ ] buffs (white magic)
     * [ ] buffs (bard)
     * [ ] blue physical spells
     * [ ] blue magical spells
     * [ ] blue buffs
     * [ ] avatar damage
     * [ ] automatons
 * [ ] Testing
     * [ ] elemental nukes
     * [ ] physical weaponskills
     * [ ] "unique" weaponskills
     * [ ] enfeebles (magic)
     * [ ] enfeebles (songs)
     * [ ] buffs (white magic)
     * [ ] buffs (bard)
     * [ ] blue physical spells
     * [ ] blue magical spells
     * [ ] blue buffs
     * [ ] avatar damage
     * [ ] automatons
 * [ ] Migrate spell.lua to replace magic.lua in order to unify the language. Anything from the "magic" menu should be in magic.lua. Same thing from weaponskill, etc, etc.
 * [ ] remove all hardcoded numbers in favor of "customizable" tables.

**Supporting Changes**
Things considered "final" commits are preprended with "PR"

In order...
 * Unified the language and mechanics of elemental resistances vs. specific damage taken
 * Added support for the nuke wall mechanic that exists on Notorious Monsters
 * Changed the way magic burst damage is handled due to certain portions being capped and others not.
 * Added support for the cumulative magic effects that -ja spells do.
 * Mod'ified Ebullience (for you Teo!)
 * Mod'ified Focalization (for you Teo!)
 * Unified Elemental Staff mod language to be more inline with how bg-wiki outlines it.

