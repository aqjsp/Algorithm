# 面试经典算法题46-找出字符串中第一个匹配项的下标

LeetCode.28

### 问题描述

给你两个字符串 `haystack` 和 `needle` ，请你在 `haystack` 字符串中找出 `needle` 字符串的第一个匹配项的下标（下标从 0 开始）。如果 `needle` 不是 `haystack` 的一部分，则返回 `-1` 。

**示例 1：**

```
输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
```

**示例 2：**

```
输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
```

### 思路

1. 遍历 `haystack` 字符串，将当前字符与 `needle` 字符串的第一个字符进行比较。
2. 如果找到了与 `needle` 第一个字符相等的字符，则从当前位置开始比较后续字符是否与 `needle` 字符串完全匹配。
3. 如果匹配成功，则返回当前位置；否则，继续遍历 `haystack` 字符串。

### 图解

```
       +-------------------------+
       |       开始执行程序        |
       +-------------------------+
                   |
                   v
       +-------------------------+
       |       初始化变量          |
       |  haystack = "sadbutsad" |
       |  needle = "sad"         |
       |  needle_len = 3         |
       |  haystack_len = 9       |
       |  i = 0                  |
       +-------------------------+
                   |
                   v
       +-------------------------+
       |       进入匹配循环        |
       +-------------------------+
                   |
                   v
 +------------------------------------+
 |            检查是否匹配              |
 | haystack[i:i+needle_len] == needle |
 |      i = 0, "sad" == "sad", 匹配    |
 +------------------------------------+
                   |
                   v
      +-------------------------+
      |        输出结果          |
      |     第一个匹配项下标：0    |
      +-------------------------+
```



### 参考代码

#### C++

```
#include <iostream>
#include <string>

int strStr(std::string haystack, std::string needle) {
    int m = haystack.size(), n = needle.size();
    if (n == 0) return 0; // 如果 needle 是空字符串，返回 0
    for (int i = 0; i <= m - n; ++i) { // 从头到尾遍历 haystack
        if (haystack[i] == needle[0]) { // 找到与 needle 第一个字符相等的字符
            int j = 1;
            while (j < n && haystack[i + j] == needle[j]) ++j; // 比较后续字符是否匹配
            if (j == n) return i; // 完全匹配，返回当前位置
        }
    }
    return -1; // 未找到匹配项，返回 -1
}

int main() {
    std::string haystack = "hello", needle = "ll";
    int result = strStr(haystack, needle);
    std::cout << "匹配项的下标为：" << result << std::endl;
    return 0;
}
```

#### Java

```
#include <iostream>
#include <string>

int strStr(std::string haystack, std::string needle) {
    int m = haystack.size(), n = needle.size();
    if (n == 0) return 0; // 如果 needle 是空字符串，返回 0
    for (int i = 0; i <= m - n; ++i) { // 从头到尾遍历 haystack
        if (haystack[i] == needle[0]) { // 找到与 needle 第一个字符相等的字符
            int j = 1;
            while (j < n && haystack[i + j] == needle[j]) ++j; // 比较后续字符是否匹配
            if (j == n) return i; // 完全匹配，返回当前位置
        }
    }
    return -1; // 未找到匹配项，返回 -1
}

int main() {
    std::string haystack = "hello", needle = "ll";
    int result = strStr(haystack, needle);
    std::cout << "匹配项的下标为：" << result << std::endl;
    return 0;
}
```

#### Python

```
def strStr(haystack: str, needle: str) -> int:
    m, n = len(haystack), len(needle)
    if n == 0:
        return 0  # 如果 needle 是空字符串，返回 0
    for i in range(m - n + 1):  # 从头到尾遍历 haystack
        if haystack[i] == needle[0]:  # 找到与 needle 第一个字符相等的字符
            j = 1
            while j < n and haystack[i + j] == needle[j]:  # 比较后续字符是否匹配
                j += 1
            if j == n:  # 完全匹配，返回当前位置
                return i
    return -1  # 未找到匹配项，返回 -1

# 测试
haystack = "hello"
needle = "ll"
result = strStr(haystack, needle)
print("匹配项的下标为：", result)
```

