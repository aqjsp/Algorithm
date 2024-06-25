# 面试经典算法题66-同构字符串

LeetCode.205

### 问题描述

给定两个字符串 `s` 和 `t` ，判断它们是否是同构的。

如果 `s` 中的字符可以按某种映射关系替换得到 `t` ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

**示例 1:**

```
输入：s = "egg", t = "add"
输出：true
```

**示例 2：**

```
输入：s = "foo", t = "bar"
输出：false
```

**示例 3：**

```
输入：s = "paper", t = "title"
输出：true
```

### 思路

1. 建立字符映射关系：

   - 使用两个哈希表分别记录字符串 `s` 和 `t` 中字符之间的映射关系。

   - 一个哈希表 `s_to_t` 记录 `s` 中字符到 `t` 中字符的映射关系。

   - 另一个哈希表 `t_to_s` 记录 `t` 中字符到 `s` 中字符的映射关系。

2. 检查映射关系：

   - 遍历字符串 `s` 和 `t` 中的每一个字符。

   - 如果字符 `s[i]` 已经在 `s_to_t` 中存在映射关系且不等于当前字符 `t[i]`，说明 `s` 和 `t` 不是同构的。

   - 如果字符 `t[i]` 已经在 `t_to_s` 中存在映射关系且不等于当前字符 `s[i]`，说明 `s` 和 `t` 不是同构的。

   - 如果上述情况都不满足，则将字符 `s[i]` 和 `t[i]` 的映射关系记录下来。

3. 返回结果：

   - 遍历结束后，如果没有发现冲突的映射关系，说明字符串 `s` 和 `t` 是同构的，返回 `true`。

   - 否则返回 `false`。

### 参考代码

#### C++

```
#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

bool isIsomorphic(string s, string t) {
    // 两个哈希表分别记录 s 到 t 和 t 到 s 的映射关系
    unordered_map<char, char> s_to_t;
    unordered_map<char, char> t_to_s;
    
    // 遍历两个字符串的字符
    for (int i = 0; i < s.length(); ++i) {
        char s_char = s[i];
        char t_char = t[i];
        
        // 检查 s 中的字符是否已经有对应的 t 中的字符
        if (s_to_t.count(s_char)) {
            // 如果存在映射关系且不等于当前 t 中的字符，则返回 false
            if (s_to_t[s_char] != t_char) {
                return false;
            }
        } else {
            // 如果没有映射关系，则建立新的映射
            s_to_t[s_char] = t_char;
        }
        
        // 检查 t 中的字符是否已经有对应的 s 中的字符
        if (t_to_s.count(t_char)) {
            // 如果存在映射关系且不等于当前 s 中的字符，则返回 false
            if (t_to_s[t_char] != s_char) {
                return false;
            }
        } else {
            // 如果没有映射关系，则建立新的映射
            t_to_s[t_char] = s_char;
        }
    }
    
    // 如果没有发现冲突的映射关系，则返回 true
    return true;
}

int main() {
    string s1 = "egg", t1 = "add";
    string s2 = "foo", t2 = "bar";
    string s3 = "paper", t3 = "title";

    cout << boolalpha; // 输出布尔值的 true 或 false

    // 示例 1
    cout << "输入: s = \"" << s1 << "\", t = \"" << t1 << "\"" << endl;
    cout << "输出: " << isIsomorphic(s1, t1) << endl; // true

    // 示例 2
    cout << "输入: s = \"" << s2 << "\", t = \"" << t2 << "\"" << endl;
    cout << "输出: " << isIsomorphic(s2, t2) << endl; // false

    // 示例 3
    cout << "输入: s = \"" << s3 << "\", t = \"" << t3 << "\"" << endl;
    cout << "输出: " << isIsomorphic(s3, t3) << endl; // true

    return 0;
}
```

#### Java

```
import java.util.HashMap;
import java.util.Map;

public class IsomorphicStrings {
    
    public static boolean isIsomorphic(String s, String t) {
        // 两个哈希表分别记录 s 到 t 和 t 到 s 的映射关系
        Map<Character, Character> sToT = new HashMap<>();
        Map<Character, Character> tToS = new HashMap<>();
        
        // 遍历两个字符串的字符
        for (int i = 0; i < s.length(); i++) {
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            
            // 检查 s 中的字符是否已经有对应的 t 中的字符
            if (sToT.containsKey(sChar)) {
                // 如果存在映射关系且不等于当前 t 中的字符，则返回 false
                if (!sToT.get(sChar).equals(tChar)) {
                    return false;
                }
            } else {
                // 如果没有映射关系，则建立新的映射
                sToT.put(sChar, tChar);
            }
            
            // 检查 t 中的字符是否已经有对应的 s 中的字符
            if (tToS.containsKey(tChar)) {
                // 如果存在映射关系且不等于当前 s 中的字符，则返回 false
                if (!tToS.get(tChar).equals(sChar)) {
                    return false;
                }
            } else {
                // 如果没有映射关系，则建立新的映射
                tToS.put(tChar, sChar);
            }
        }
        
        // 如果没有发现冲突的映射关系，则返回 true
        return true;
    }
    
    public static void main(String[] args) {
        String s1 = "egg";
        String t1 = "add";
        String s2 = "foo";
        String t2 = "bar";
        String s3 = "paper";
        String t3 = "title";

        System.out.println("输入: s = \"" + s1 + "\", t = \"" + t1 + "\"");
        System.out.println("输出: " + isIsomorphic(s1, t1)); // true

        System.out.println("输入: s = \"" + s2 + "\", t = \"" + t2 + "\"");
        System.out.println("输出: " + isIsomorphic(s2, t2)); // false

        System.out.println("输入: s = \"" + s3 + "\", t = \"" + t3 + "\"");
        System.out.println("输出: " + isIsomorphic(s3, t3)); // true
    }
}
```

#### Python

```
def is_isomorphic(s: str, t: str) -> bool:
    # 两个字典分别记录 s 到 t 和 t 到 s 的映射关系
    s_to_t = {}
    t_to_s = {}
    
    # 遍历两个字符串的字符
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        
        # 检查 s 中的字符是否已经有对应的 t 中的字符
        if s_char in s_to_t:
            # 如果存在映射关系且不等于当前 t 中的字符，则返回 false
            if s_to_t[s_char] != t_char:
                return False
        else:
            # 如果没有映射关系，则建立新的映射
            s_to_t[s_char] = t_char
        
        # 检查 t 中的字符是否已经有对应的 s 中的字符
        if t_char in t_to_s:
            # 如果存在映射关系且不等于当前 s 中的字符，则返回 false
            if t_to_s[t_char] != s_char:
                return False
        else:
            # 如果没有映射关系，则建立新的映射
            t_to_s[t_char] = s_char
    
    # 如果没有发现冲突的映射关系，则返回 true
    return True

# 示例
s1 = "egg"
t1 = "add"
s2 = "foo"
t2 = "bar"
s3 = "paper"
t3 = "title"

print("输入: s = \"{}\", t = \"{}\"".format(s1, t1))
print("输出: ", is_isomorphic(s1, t1)) # True

print("输入: s = \"{}\", t = \"{}\"".format(s2, t2))
print("输出: ", is_isomorphic(s2, t2)) # False

print("输入: s = \"{}\", t = \"{}\"".format(s3, t3))
print("输出: ", is_isomorphic(s3, t3)) # True
```

