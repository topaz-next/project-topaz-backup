**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:25_
_Originally opened as: project-topaz/topaz - Issue 211_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Thursday Feb 15, 2018 at 18:28 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4563_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30171223_0


**_Server Version_** (type `!revision` in game) **:** fae4c89


**_Source Branch_** (master/stable) **:** master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

1. Grab a buddy
2. Load up your inventory so you have no slots left
3. Have your buddy trade you an item.
4. Note the error message "You cannot trade" due to you having no spots available for the trade
5. Have your buddy trade you the same item but this time, include an item of your own in the trade window.
6. Note the "trade complete" message.
7. Also, note that your item was never received from your buddy and you now have 1 spot available.
  --the item just disappears into the nothingness never to be seen again
8. Also, note the if both players inventories are completely full and a trade happens between them, only 1 of the items traded will disappear into the void.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:26_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Feb 15, 2018 at 18:34 GMT_

----

I'm guessing on retail both parties must have enough space before the trade
starts

On Feb 15, 2018 11:29 AM, "Wiggo" <notificationsgithub.com> wrote:

> *I have:*
>
>    - searched existing issues (http://github.com/darkstarproject/darkstar/
>    issues/ <github/darkstarproject/darkstar - Issue >) to see
>    if the issue I am posting has already been addressed or opened by another
>    contributor
>    - checked the commit log to see if my issue has been resolved since my
>    server was last updated
>
> *Client Version* (type /ver in game) *:* 30171223_0
>
> *Server Version* (type !revision in game) *:* fae4c89
> <github/DarkstarProject/darkstar/commit/fae4c89592b701f76dbd48cc4b232fe57924aca7>
>
> *Source Branch* (master/stable) *:* master
>
> *Additional Information* (Steps to reproduce/Expected behavior) *:*
>
>    1. Grab a buddy
>    2. Load up your inventory so you have no slots left
>    3. Have your buddy trade you an item.
>    4. Note the error message "You cannot trade" due to you having no
>    spots available for the trade
>    5. Have your buddy trade you the same item but this time, include an
>    item of your own in the trade window.
>    6. Note the "trade complete" message.
>    7. Also, note that your item was never received from your buddy and
>    you now have 1 spot available.
>    --the item just disappears into the nothingness never to be seen again
>    8. Also, note the if both players inventories are completely full and
>    a trade happens between them, only 1 of the items traded will disappear
>    into the void.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 4563>, or mute the
> thread
> <github/notifications/unsubscribe-auth/ABGI_7p_zrBjT78cU9F_1Z3cogEcIyfeks5tVHdqgaJpZM4SHTGN>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:27_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Thursday Feb 15, 2018 at 18:58 GMT_

----

That is correct, and gil counts as an item. So, even with 1 slot (and i just did this on retail) you cannot accept an item plus gil.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:28_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Feb 15, 2018 at 19:18 GMT_

----

Wiggo32 Huh, I wonder if that's why there's an item ID for gil.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:29_

----

<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Apr 14, 2018 at 18:25 GMT_

----


Experienced this issue on Version: 30180329_1
Same steps to reproduce behavior, item lost.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:31_

----

<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Oct 23, 2019 at 06:06 GMT_

----

I havent experienced this lately, cannot say if it was fixed or not



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:32_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Dec 02, 2019 at 00:38 GMT_

----

so this is still a thing, just reminding. 

> [7:03 PM] Rheine: just traded two merman rings from one toon to another vs 3 stacks of crystals. bad trade, i know. toon to receive rings was 80/80 thats why i switched the crystals, to make room. trade completed. but the rings have disapeared. lost. just a glitch or me bad from trying that trade?

Server log shows:

> [0m[01/Dec] [15:55:31][1;37m[Notice][0m [1;36mRheine->Cat trade updating trade slot id 1 with item mermans_ring, quantity 1
[0m[01/Dec] [15:55:32][1;37m[Notice][0m [1;36mRheine->Cat trade updating trade slot id 2 with item mermans_ring, quantity 1
[0m[01/Dec] [15:55:53][1;37m[Notice][0m [1;36mRheine->Cat trade updating trade slot id 1 with item mermans_ring, quantity 1
[0m[01/Dec] [15:55:54][1;37m[Notice][0m [1;36mRheine->Cat trade updating trade slot id 2 with item mermans_ring, quantity 1
[0m[01/Dec] [15:55:57][1;37m[Notice][0m [1;36mCat->Rheine trade updating trade slot id 1 with item wind_crystal, quantity 12
[0m[01/Dec] [15:55:59][1;37m[Notice][0m [1;36mCat->Rheine trade updating trade slot id 2 with item wind_crystal, quantity 12
[0m[01/Dec] [15:56:01][1;37m[Notice][0m [1;36mCat->Rheine trade updating trade slot id 3 with item wind_crystal, quantity 12

I queried inventories and verified neither player has those merman's rings.



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 31, 2020 at 16:18:18_

----

It appears https://github.com/project-topaz/topaz/pull/387 fixes and should have closed this issue but somehow Github didn't notice.
