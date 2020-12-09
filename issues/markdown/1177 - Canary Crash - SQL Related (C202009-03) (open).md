**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 22, 2020 at 03:06:49_
_Originally opened as: project-topaz/topaz - Issue 1177_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

```
225			ShowWarning ("You are running Topaz as the root superuser.\n");
226			ShowWarning ("It is unnecessary and unsafe to run with root privileges.\n");
227			sleep(3);
228	    }
229	#endif
230	}
231	
232	/************************************************************************
233	*												*
234	*  CORE : MAINROUTINE										*
#0  0x00007ffff75c5ff3 in mysql_ping () from /usr/lib/x86_64-linux-gnu/libmysqlclient.so.20
#1  0x00005555555902b8 in Sql_Ping (self=0x555587568c10) at src/common/sql.cpp:168
#2  Sql_P_KeepaliveTimer (tick=..., PTask=<optimized out>) at src/common/sql.cpp:187
#3  0x0000555555592479 in CTaskMgr::DoTimer (this=0x555555ad0b10, tick=...) at src/common/taskmgr.cpp:78
#4  0x0000555555571d60 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x7ffff75c5fed <mysql_ping+29>:	sarb   $0xff,0xe(%rsi)
   0x7ffff75c5ff4 <mysql_ping+36>:	push   %rax
   0x7ffff75c5ff5 <mysql_ping+37>:	or     %bl,0xf(%rdx)
   0x7ffff75c5ff8 <mysql_ping+40>:	mov    $0xc3c959c0,%esi
   0x7ffff75c5ffd <mysql_ping+45>:	nopl   (%rax)
```

Currently running the https://github.com/project-topaz/topaz/releases/tag/C202009-03


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 22, 2020 at 04:44:07_

----

More than likely this is also caused by whatever is causing: https://github.com/project-topaz/topaz/issues/1152
If there is a stack overflow the machine is getting starved of resources. When resources eventually run out, it will crash on whatever it's doing. So in this case: It might be trying to allocate a buffer to hold a response from SQL - which fails. Or the SQL service might have died due to lack of resources - fail. etc etc.

Guess we're going to have to go through every PR that went in the last release and track down what's wrecking the Lua stack


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 22, 2020 at 21:28:36_

----

another crash looks exactly the same,  just posting it here just to say it can happen and it wasnt just a 1 time fluke lol

```
[22/Sep] [14:22:11][Info] parse: 01A | 179A 1799 0E from user: Kong
[22/Sep] [14:22:11][Action Info] CLIENT Kong PERFORMING ACTION 09
[22/Sep] [14:22:13][Info] Pinging SQL server to keep connection alive...

Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
0x00007ffff75caed8 in ?? () from /usr/lib/x86_64-linux-gnu/libmysqlclient.so.20
230     }
231
232     /************************************************************************
233     *                                                                      *
234     *  CORE : MAINROUTINE                                                  *
235     *                                                                      *
236     ************************************************************************/
237
238     int main (int argc, char **argv)
239     {
#0  0x00007ffff75caed8 in ?? () from /usr/lib/x86_64-linux-gnu/libmysqlclient.so.20
#1  0x00007ffff75c6014 in mysql_ping () from /usr/lib/x86_64-linux-gnu/libmysqlclient.so.20
#2  0x00005555555902b8 in Sql_Ping (self=0x55558681e560) at src/common/sql.cpp:168
#3  Sql_P_KeepaliveTimer (tick=..., PTask=<optimized out>) at src/common/sql.cpp:187
#4  0x0000555555592479 in CTaskMgr::DoTimer (this=0x555555ad0b10, tick=...) at src/common/taskmgr.cpp:78
#5  0x0000555555571d60 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x7ffff75caed2:      je     0x7ffff75cafa0
=> 0x7ffff75caed8:      cmpq   $0x0,(%rax)
   0x7ffff75caedc:      je     0x7ffff75caf2d
   0x7ffff75caede:      movq   $0x0,-0x40(%rbp)
   0x7ffff75caee6:      movl   $0x0,-0x38(%rbp)
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Oct 06, 2020 at 15:04:32_

----

Crash still present in C202010-01

```
230	}
231	
232	/************************************************************************
233	*																		*
234	*  CORE : MAINROUTINE													*
235	*																		*
236	************************************************************************/
237	
238	int main (int argc, char **argv)
239	{
#0  0x00007ffff75da781 in ?? () from /usr/lib/x86_64-linux-gnu/libmysqlclient.so.20
#1  0x00007ffff75caf29 in ?? () from /usr/lib/x86_64-linux-gnu/libmysqlclient.so.20
#2  0x00007ffff75c6014 in mysql_ping () from /usr/lib/x86_64-linux-gnu/libmysqlclient.so.20
#3  0x0000555555590388 in Sql_Ping (self=0x555586f76140) at src/common/sql.cpp:168
#4  Sql_P_KeepaliveTimer (tick=..., PTask=<optimized out>) at src/common/sql.cpp:187
#5  0x0000555555592549 in CTaskMgr::DoTimer (this=0x555555ad0b10, tick=...) at src/common/taskmgr.cpp:78
#6  0x0000555555571df0 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x7ffff75da77b:	pushq  0x18(%rbp)
   0x7ffff75da77e:	pushq  0x10(%rbp)
=> 0x7ffff75da781:	callq  *0x68(%r13)
   0x7ffff75da785:	movzbl -0x31(%rbp),%r9d
   0x7ffff75da78a:	mov    %eax,%r15d
```
