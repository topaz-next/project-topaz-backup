**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:47_
_Originally opened as: project-topaz/topaz - Issue 68_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [m241dan](https://github.com/m241dan)**
_Monday Dec 07, 2015 at 16:40 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2457_

----

Does recast navigation have a toggle function for doors? Right now, any openable/closable door, sky|sea in particular, mobs cannot get through. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:48_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Monday Dec 07, 2015 at 17:07 GMT_

----

Yes recast has a toggle function but it'll involve a small tweak to the navmesh. I don't think we knew the expected behavior for doors, so it was not implemented.
- Can mobs aggro through doors? (sight, sound, magic)

I know mobs chasing players will run through doors but is this consistent throughout all doors?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:49_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Monday Dec 07, 2015 at 17:31 GMT_

----

Mobs chasing players will -not- go through doors. Especially open ones.

Curiously, upon reflection, this may have to do with my adjusting it so mobs just StopWithin instead of picking a random radian around a player. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:50_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Monday Dec 07, 2015 at 22:06 GMT_

----

No I was talking about expected behaviour, right now they will not go through doors.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:51_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Tuesday Dec 08, 2015 at 00:52 GMT_

----

Mobs should neither aggro through walls nor closed doors. Players should be unable to cast on or shoot at mobs without line of sight, but I'm guessing that's already known and not an easy fix.

A mob chasing a player will open the door at which point both the mob and player can pass through the doorway freely until it closes. 

Also, the switch behind the gate to the Den of Rancor should be inoperable from the front of the gate. Currently players can avoid lighting the four lamps by simply hitting the switch from the front of the gate.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:52_

----

<a href="https://github.com/gedads"><img src="https://avatars1.githubusercontent.com/u/5845173?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gedads](https://github.com/gedads)**
_Tuesday Dec 08, 2015 at 19:30 GMT_

----

"A mob chasing a player will open the door at which point both the mob and player can pass through the doorway freely until it closes. "
That's the uggalehpi trick in the manipulator's room where you can aggro a mob you can't see behind the door and have him open it.
Other case is pso xja and the 16 rooms mission where some people where abble to aggro/pull mobs especially eyes i think before entering the room
But that problem isn't only for mobs, in campaign zones, when you're riding a chocobo, the doors are supposed to open automatically (so you don't have to dismount target and open the door).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:53_

----

<a href="https://github.com/Gravenet"><img src="https://avatars3.githubusercontent.com/u/6434865?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Gravenet](https://github.com/Gravenet)**
_Wednesday Dec 09, 2015 at 03:27 GMT_

----

There are doors such as "CS" doors that require a key to trigger (This can be confirmed I believe also in Temple of Uggly People) where if you aggro a Mob from inside, that door will in fact NOT open -- they will just come through... This was confirmed during one of our run through's on retail last week I just cant remember which door it was... But as Gedads stated above his trick works on Majority of  doors throughout the game.  

As for the mobs aggro- or being attacked - Walls such as doors or shifting walls such as Sacrarium are just NPCs with different settings (IE open close) and do in fact aggro through them.  Wiki specifically states in some areas that you may aggro through the wall in some areas regardless of line of sight, only thing in common with them is their ability to move as opposed to being a SOLID wall.  

I agree in most cases mobs SHOULDN'T aggro through a closed door... but this is just not the case on retail, and depending on the type of door dictates whether the door opens or not. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:54_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Wednesday Dec 09, 2015 at 05:39 GMT_

----

Yeah so the door issues will have to be fixed on a case by case basis. I think we should start with the highest priority doors first, probably the doors in sky? How do those function?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:55_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Dec 09, 2015 at 09:15 GMT_

----

Deadwing is active if you want to go poke around up there bendangelo 

I thought about mentioning the temple of uggalepih when writing my comment but decided not to bring it up. It was perhaps also a bit misleading of me to say that players are unable to cast/shoot mobs without line of sight because I remember doing it in uggalepih through closed doors. I believe it was a tricky process even with fillmode to aggro through the door was it not?

I completely forgot about pso'xja though, and now that you mention it I do remember certain doors (probably the switch doors in sky, possibly the weight doors in Qicksand Caves) that will not open to let mobs through-- they'll just run through the closed door.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:56_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Monday Dec 21, 2015 at 18:41 GMT_

----

"Also, the switch behind the gate to the Den of Rancor should be inoperable from the front of the gate. Currently players can avoid lighting the four lamps by simply hitting the switch from the front of the gate."

I just created a pull to fix this, but while I was testing it I was unable to interact with the switch from the wrong side - it was always too far. Either way, there probably should be a check.


