**Labels:**



<a href="https://github.com/Shirk"><img src="https://avatars0.githubusercontent.com/u/304352?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Shirk](https://github.com/Shirk)**
_Friday Jun 05, 2020 at 12:13:26_
_Originally opened as: project-topaz/topaz - Issue 686_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

- build Topaz according to the current wiki guideline
- setup a default configuration
- add the following settings to `packet_tcp.conf`

```
debug: yes
order: allow,deny

allow: 127.0.0.1
allow: 192.168.99.0/24
deny: all
```

- start Topaz and attempt to connect from the 192.168.99.0/24 subnet

**_Expected behavior_**

- debug log: "access_ipmask: Loaded IP:127.0.0.1 mask: 255.255.255.255"
- debug log: "access_ipmask: Loaded IP:192.168.99.0 mask:192.168.99.0"
- connections are accepted from localhost (127.0.0.1)
- connections are accepted from any host in the 192.168.99.0/24 subnet

**_Actual behavior_**

- debug log: "access_ipmask: Loaded IP:1.0.0.127 mask: 255.255.255.255"
- debug log: "access_ipmask: Loaded IP:0.99.168.192 mask:0.99.168.192"
- no connections match the allow rules
- all connection attempts are rejected

**_Workaround_**

To get IP allow/deny lists working properly the IP addresses and net masks have to be specified in reverse order like this:


```
debug: yes
order: allow,deny

allow: 1.0.0.127
allow: 0.99.168.192/0.255.255.255
deny: all
```

Tested on git HEAD / b86db9da3603, build with Visual Studio 2019 16.6.1 on Windows 10 64bit
