**Labels:**

WIP



<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ShelbyZ](https://github.com/ShelbyZ)**
_Tuesday Jun 23, 2020 at 18:52:25_
_Originally opened as: project-topaz/topaz - Issue 764_

----

- MSG_SEND_LUA_COMMAND - send a command to another server to run where the target (player) is local
- MSG_SEND_LUA_ID_COMMAND - send a command to another server to run where the target (player/npc/mob) is local
- MSG_REMOTE_PRINT_TO_PLAYER - send a message to a remote player for use with remote commands
- update message_server to lookup player server and redirect command/print
- update commandhandler::call to take a caller parameter
- add support for 't' command that will check if target is server local and if not redirect to message server
- add support for 'n' command that will check if target (by id) is server local and if not redirect to message server
- add support in message for MSG_SEND_LUA_COMMAND/MSG_SEND_LUA_ID_COMMAND/MSG_REMOTE_PRINT_TO_PLAYER
- message will now report if player/entity is not found rather than scripts
- update packet_system to pass caller attribute for SmallPacket0x0B5 (chat)
- update luautils for RemotePrintToPlayer lua method
- update luautils for GetCharVariable lua method - lookup char variable by varName and char name
- update luautils for GetNameAndGMLevel - lookup name/gm level by char id
- update charutils for GetNameAndGMLevel - lookup name/gm level by char id
- update lua_baseentity::gotoPlayer - to support using char id

It would require updates to all onTrigger in the /scripts/commands directory to take a first argument of caller. It would also be suggested to copy or make globally available the updated error and print_message that will attempt to handle whether or not player:PrintToPlayer or RemotePrintToPlayer should be used based on caller and player object ids matching (or not).

Commands and plumbing are in place and just needs massive testing on a multi-server environment.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


