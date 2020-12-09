**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Nov 08, 2020 at 00:13:35_
_Originally opened as: project-topaz/topaz - Issue 1484_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

Mobs are currently completely unaware of whether they have a buff active or not. This leads to a situation where a mob can have very few or none spells other than buffs and will repeatedly cast a buff despite of having it already active or not.

A good example for this is Ouryu who is erroneously missing spells and currently only has two -ga's and stoneskin. Apart from the fact that he therefore will cast stoneskin way too often (first roll is 35% ga-chance [default], then 35% buff-chance [default], then it's 100% buff cause no "damage spell" available [[see here how that works](https://docs.google.com/spreadsheets/d/17wIamwYjD5Qv4SCkLU6YsY4BsRgFNDC_VE4iBmz5phE/edit?usp=sharing)]) he will spam stoneskin despite of not being attacked and having the buff effect active:

https://github.com/project-topaz/topaz/blob/019d51b3dba23239a0b3ef8953e378433552ca87/src/map/mob_spell_container.cpp#L200-L205

I suggest selecting the buff returned based on a while loop. I couldn't figure out if there's a way in the core to get the spell name instead of the ID (most probably there is) and then sort of concatenate that to `HasStatusEffect()`. Any ideas are welcome!

```C++
std::optional<SpellID> CMobSpellContainer::GetBuffSpell()
{
    if(m_buffList.empty()) return {};

    // don't return the rolled spell directly, store it
    auto chosenBuff = m_buffList[tpzrand::GetRandomNumber(m_buffList.size())];

    // re-roll as long as the effect is already found on mob
    // I'm not fond enough of what's available here, if it's possible to get the name of the rolled spell
    // it could be tested for with HasStatusEffect maybe?
    while (m_PMob->StatusEffectContainer->HasStatusEffect(EFFECT_chosenBuffNAME))
    {
        // as long as mob has status of chosen spell roll buff spell again
        chosenBuff = m_buffList[tpzrand::GetRandomNumber(m_buffList.size())];
    }

    return chosenBuff;
}
```

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
- Find a mob that has mainly buff spells on his list. Engage. Don't attack. Observe casts.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Nov 09, 2020 at 11:10:17_

----

There isn't a need to put a `while` loop in here, `AIContainer` is "small"-ticked every 400ms, so you can either look for something randomly once per "small"-tick, or do what I do when determining valid positions for trusts and just try 3-5 times, and bail out if you don't get a good result - the next attempt is coming soon anyway.

I added `tpzrand::GetRandomElement` recently, which makes the picking random things out of vectors and other stl containers a bit less gruesome looking. `tpzrand::GetRandomElement(m_buffList);` etc.

I wouldn't recommend comparing the name of the Spell to anything at runtime, but if you need more information about the spell, you can use `spell::GetSpell(spellID)` to return a `CSpell*` which has `getName()` and all the other accessors a spell needs.

There is currently no way to know from a `CSpell` what it does. We can infer a bunch of stuff:
- Relative power (if it's the 5th spell in a spellFamily)
- If it is a Severe spell
- The skill type
- The element
- AOE and Spell Flags

I'd _love_ to figure out some information to add to spells to annotate their effects. Example: If we could mark `Spell - Bio` as inflicting `Effect - Bio`, that would let us cut out... a LOT of code. (For trusts this would make my life 200% easier)


