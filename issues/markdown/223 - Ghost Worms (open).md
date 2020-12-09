**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:34_
_Originally opened as: project-topaz/topaz - Issue 223_

----

<a href="https://github.com/armouredking"><img src="https://avatars1.githubusercontent.com/u/16038428?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [armouredking](https://github.com/armouredking)**
_Friday May 18, 2018 at 02:13 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4870_

----

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor (see github/DarkstarProject/darkstar - Issue 2138)
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

30180427_2 | Master

This pesky bug won't go away it seems. So, Darkstar Issue 2138 seems to have fixed the linking and roaming issues. Unfortunately you can still break a worm. If the worm is dropping down into the ground and you hit it with a ranged attack, the worm will vanish. Battle music will play, but there is no nearby worm.

Well, initially there isn't. Once you walk over to where the worm last was, it'll pop up but remain untargetable. It can hit you and cast spells (though casting spells is fairly rare). It will use weaponskills (like Gastric Bomb or Absorption) at a fairly regular basis.

You can make the worm start behaving again by attacking another worm and killing it. The battle music will clear, the original worm will move away (it will move ABOVE ground), the popup animation will play and the worm is targetable again.

![image](https://user-images.githubusercontent.com/16038428/40212610-a9c47686-5a05-11e8-84d2-907e8cc4b520.png)

Makes for a great way to cap defence skills, though definitely a bit hackneyed.

