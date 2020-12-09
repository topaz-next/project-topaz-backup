**Labels:**

crafting



<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Monday Oct 12, 2020 at 17:24:01_
_Originally opened as: project-topaz/topaz - Issue 1343_

----

The long awaited and underwhelming sequel.
- Adds 2 new configuration options.
1. Allows to easily swap between era and retail skill up systems
2. Allows to configure when skill ups over 0.1 stop happening. (At lvl 60 in retail)

- Allows to get skill ups 10 levels above the recipe level. Retail behaviour.
- New skill up equation becouse the old one was returning negative values at high levels. It was also unusable and imposible to work with, in general.

- Changed some data types, becouse a variable wich are only going to hold numbers between 1 and 5 dont need to be uint32.

Dedicated to Tokenr from Canaria server, for his patience.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Oct 12, 2020 at 17:25:44_

----

@jarmengaud, they made this just for u =P


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Oct 12, 2020 at 18:45:36_

----

I encountered some [weird things on BGWiki](https://www.bg-wiki.com/bg/Category:Craft#Skilling_up) when I was testing new recipe data last week:

> A player must be within 27 skill levels of the required main skill cap as well as 27 skill levels of the required sub skill cap of the item. There is a much higher chance of failure when one's craft skill is much lower than the required skill cap, but you will have the ability to try to craft the item when you are 27 levels below it.

> Under 70 skill, there is approximately a 95% chance of getting a skill up until that recipe's natural cap. You then have approximately 66% to 75% chance to skill up on a successful synth if your natural skill is equal or up to 11 levels higher

> At or above 70 skill, you have approximately a 25% chance to skill up on a successful synth


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Monday Oct 12, 2020 at 18:57:01_

----

the quick summary is this:
Once upon a time we had crafting . You had to be under the recipe level to skill up. the skill up rate wasnt too great, but it wasnt that bad. Mats were expensive and ppl camped AH for them, so high levels were uncommon.
Then at level 99 era, SE decided to boost skill up rate like they boosted exp and so many other things and then also decided to allow ppl to skill up from recipes below their level.

The rates in BG wiki arent... very true/precise. Conflicting info from other sources and the addition of skill up foods and such doesnt help.

About the 27 skill levels, the game wont allow you to even atempt the recipe if the recipe is 27 levels avobe your craft. this applies to all crafts involved in the recipe. Multi skill recipes check if you fuck up in one skill. it then checks if you fuck up in the next skill and so on for all skills involved.

I do know I have not yet "tested" the new equation. I need more data and probably needs tuning. I was hoping for Kain to merge it into canaria so crafters can tell me how it feels. What I do know, however, is that the old one was imposible to make any coherent sense out of it.

