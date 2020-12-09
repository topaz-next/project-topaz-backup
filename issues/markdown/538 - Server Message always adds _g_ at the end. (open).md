**Labels:**

bug



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Monday Apr 27, 2020 at 21:13:37_
_Originally opened as: project-topaz/topaz - Issue 538_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

"g" is added to your server message in most cases.  I also found that if you add "g" to the end of your message, it just erases the last character of your message.

![image](https://user-images.githubusercontent.com/37684138/80421451-5ff8d580-8891-11ea-8479-2b1a46705013.png)

![image](https://user-images.githubusercontent.com/37684138/80421540-80c12b00-8891-11ea-8e48-3b572882bce6.png)


Unrelated, I think the SystemMessage that follows about reporting bugs to topaz should be able to be toggled on or off.



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Apr 27, 2020 at 22:02:52_

----

it's for all our topaz' gs lol


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 27, 2020 at 22:07:46_

----

add or remove a single space in your message. its not always, its length dependent. the calculation is a bit off due to retails use of an odd character set.

also if you change the line ends between unix and windows type, you can wind up with `ÿ` (or a yen symbol) instead of `g` - again depending on the total length of the message


----
<a href="https://github.com/tagban"><img src="https://avatars1.githubusercontent.com/u/7320004?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tagban](https://github.com/tagban)**
_Tuesday Apr 28, 2020 at 14:45:09_

----

This was an issue in dsp also.


----
<a href="https://github.com/Xlaits"><img src="https://avatars1.githubusercontent.com/u/32484365?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xlaits](https://github.com/Xlaits)**
_Sunday May 03, 2020 at 11:25:18_

----

Usually, hitting 'enter' at the end of the line fixes this.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 18:00:01_

----

> Usually, hitting 'enter' at the end of the line fixes this.

Thats just changing the message length by including more newlines. Depending on line end type, that can add 2 invisible character instead of 1.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Tuesday May 12, 2020 at 05:58:32_

----

This is a duplicate of issue #21 


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Friday May 22, 2020 at 15:45:08_

----

I believe this issue was closed with a recent PR, was it not?


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday May 22, 2020 at 15:53:07_

----

If you mean 
https://github.com/project-topaz/topaz/commit/8b7d1ac15375e5fae9a3cc64ea9e42b486b38062

Then no, I believe that only changed the default message so it had a length which didn't exhibit this bug.


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Friday May 22, 2020 at 16:59:10_

----

Ah, okay. I thought I read a commit about changing the line-end or EOF
styles so they wouldn't produce that issue but maybe I'm misremembering

On Fri, May 22, 2020 at 11:53 AM Kreidos <notifications@github.com> wrote:

> If you mean
> 8b7d1ac
> <https://github.com/project-topaz/topaz/commit/8b7d1ac15375e5fae9a3cc64ea9e42b486b38062>
>
> Then no, I believe that only changed the default so that the default
> message had a length which didn't exhibit this bug.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/issues/538#issuecomment-632765876>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AJIPZIALO7W26HPL2APOLU3RS2NXFANCNFSM4MSIT2UA>
> .
>



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 27, 2020 at 11:35:38_

----

I believe what you're thinking of was a batch-replace making sure that newlines were EOF.

This is a bit of an odd issue related to the character set that retail uses not being the same as ours. It'd need a more-involved fix for the true underlying issue.


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Wednesday May 27, 2020 at 14:13:55_

----

Ah okay. An easy workaround is to leave a newline at the bottom, just so
everyone knows :)

On Wed, May 27, 2020 at 7:35 AM ibm2431 <notifications@github.com> wrote:

> I believe what you're thinking of was a batch-replace making sure that
> newlines were EOF.
>
> This is a bit of an odd issue related to the character set that retail
> uses not being the same as ours. It'd need a more-involved fix for the true
> underlying issue.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/issues/538#issuecomment-634602049>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AJIPZID3B7G32JE3MTW72GLRTT3JRANCNFSM4MSIT2UA>
> .
>

