**Labels:**

reviewed



<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday May 31, 2020 at 13:23:38_
_Originally opened as: project-topaz/topaz - Issue 672_

----

- Removing _WINSOCK_DEPRECATED_NO_WARNINGS (connect/game)
- Remove unused functions host2ip, socket_getips
- Fixing log statements using MSGSERVTYPE and not casting to uint
- cmake updated

Tested on win/nix

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Saturday Jun 06, 2020 at 21:56:18_

----

If `ip_str` is not null, does the memory for `address` need to be freed after `strncpy`?


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jun 07, 2020 at 01:33:40_

----

I had to dig to find where it is used with an ip_str provided and found exactly 1 instance:

https://github.com/project-topaz/topaz/blob/45bfc2d4f658df99e9e30b3a88e78cfb2a440636/src/map/map.cpp#L439-L441

All other instances pass nullptr.  We do not use ip_str after calling the method.  It may be reasonable to modify the method to drop the second parameter and avoid strncpy entirely.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 07, 2020 at 03:10:35_

----

Would that still be a leak because none of the functions this is returning to frees the memory? Should we instead always pass the second param and get rid of the need for address being used here?
```cpp
const char* ip2str(uint32 ip, char ip_str[16])
{
    uint32 reversed_ip = htonl(ip);
    inet_ntop(AF_INET, &reversed_ip, ip_str, INET_ADDRSTRLEN);
    return ip_str;
}
```


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jun 07, 2020 at 05:10:12_

----

All current calls are returning the results via logging inline.  If we had a reason that some function would be wanting to store that value long term it may make sense.  I'm not sure why I went with new char[...].

```cpp
std::string ip2str(uint32 ip)
{
    uint32 reversed_ip = htonl(ip);
    char address[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &reversed_ip, address, INET_ADDRSTRLEN);
    return std::string(address);
}
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jun 08, 2020 at 23:00:18_

----

Death to `const char*` !  Long live `std::string` !

and you even remembered the nulls at the ends in the ShowWhatevers :heart: 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Saturday Jun 06, 2020 at 21:56:18_

----

If `ip_str` is not null, does the memory for `address` need to be freed after `strncpy`?


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jun 07, 2020 at 01:33:40_

----

I had to dig to find where it is used with an ip_str provided and found exactly 1 instance:

https://github.com/project-topaz/topaz/blob/45bfc2d4f658df99e9e30b3a88e78cfb2a440636/src/map/map.cpp#L439-L441

All other instances pass nullptr.  We do not use ip_str after calling the method.  It may be reasonable to modify the method to drop the second parameter and avoid strncpy entirely.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 07, 2020 at 03:10:35_

----

Would that still be a leak because none of the functions this is returning to frees the memory? Should we instead always pass the second param and get rid of the need for address being used here?
```cpp
const char* ip2str(uint32 ip, char ip_str[16])
{
    uint32 reversed_ip = htonl(ip);
    inet_ntop(AF_INET, &reversed_ip, ip_str, INET_ADDRSTRLEN);
    return ip_str;
}
```


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Jun 07, 2020 at 05:10:12_

----

All current calls are returning the results via logging inline.  If we had a reason that some function would be wanting to store that value long term it may make sense.  I'm not sure why I went with new char[...].

```cpp
std::string ip2str(uint32 ip)
{
    uint32 reversed_ip = htonl(ip);
    char address[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &reversed_ip, address, INET_ADDRSTRLEN);
    return std::string(address);
}
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jun 08, 2020 at 23:00:18_

----

Death to `const char*` !  Long live `std::string` !

and you even remembered the nulls at the ends in the ShowWhatevers :heart: 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 21:11:46_

----

I can't say I know exactly what this is doing but it builds/runs fine and nothing looks wrong with it, so I'm approving so it doesn't sit forever.
