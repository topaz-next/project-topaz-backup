**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Nov 08, 2020 at 09:01:06_
_Originally opened as: project-topaz/topaz - Issue 1485_

----

This allows:

```cpp
std::vector<int> v{ 1, 2, 3, 4, 5 };
auto ptrToV = &v;

tpzrand::GetRandomElement(v);
tpzrand::GetRandomElement(ptrToV);
tpzrand::GetRandomElement({ 1, 2, 3, 4, 5 });
```
... on any type that has  `at()` and `size()`.

For the C++ nerds out there, I tried to use SFINAE to validate if passed in containers had access to `at()` and `size()`, but template voodoo isn't my speciality. I got as far as:

```cpp
template <typename T, typename Enable = void>
inline constexpr bool is_container_like = false;

template <typename T>
inline constexpr bool is_container_like
<T, std::void_t<
    decltype(std::declval<T>().at()),
    decltype(std::declval<T>().size())>
> = true;

template <typename T>
static inline auto GetRandomElement(T* container)
-> std::enable_if_t<is_container_like<T>, typename T::value_type>
{
    return container->at(GetRandomNumber<std::size_t>(0U, container->size()));
}
```

🤷 

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


