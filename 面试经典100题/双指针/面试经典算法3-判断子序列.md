## 判断子序列

LeetCode.392

### 问题描述

给定字符串 **s** 和 **t** ，判断 **s** 是否为 **t** 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，`"ace"`是`"abcde"`的一个子序列，而`"aec"`不是）。

**进阶：**

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

**示例 1：**

```
输入：s = "abc", t = "ahbgdc"
输出：true
```

**示例 2：**

```
输入：s = "axc", t = "ahbgdc"
输出：false
```

 **提示：**

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- 两个字符串都只由小写字符组成。

### 思路

1. 初始化指针：初始化两个指针 `i` 和 `j` 分别指向字符串 s 和 t 的起始位置。
2. 遍历比较：使用双指针遍历字符串 t，比较 `s[i]` 和 `t[j]` 的字符：
   - 如果 `s[i]` 和 `t[j]` 的字符相等，则移动 `i` 指向 s 的下一个字符。
   - 无论是否相等，都移动 `j` 指向 t 的下一个字符。
3. 判断子序列：如果 `i` 移动到了 s 的末尾，则说明 s 是 t 的子序列，返回 `true`；否则返回 `false`。

这种方法的时间复杂度是 O(n+m)，其中 n 和 m 分别是字符串 s 和 t 的长度。

### 演示过程

这里根据给出的第一个示例给大家演示一下这个流程。

1. 初始状态：i 指向 s 的首个字符，j 指向 t 的首个字符。

![image-20240120222551123](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401210006977.png)

2. 遍历字符串，因为 s[i] = t[j]，同时移动 i 和 j。

![image-20240120223047478](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401210006642.png)

3. 因为s[i] != t[j]，只移动j。

![image-20240120223250111](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401210006118.png)

4. 因为 s[i] = t[j]，同时移动 i 和 j。

![image-20240120223431042](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401210006935.png)

5. 因为s[i] != t[j]，只移动j。

![image-20240120223548114](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401210006906.png)

6. 因为s[i] != t[j]，只移动j。

![image-20240120223636434](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401210006653.png)

7. 因为 s[i] = t[j]，同时移动 i 和 j。

![image-20240120223811659](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401210006078.png)

### 参考代码

#### C++

```
#include <iostream>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0; // s 的索引
        int j = 0; // t 的索引

        // 使用双指针遍历字符串 t
        while (i < s.size() && j < t.size()) {
            if (s[i] == t[j]) {
                // 如果当前字符匹配，则移动 s 的指针
                i++;
            }
            // 无论是否匹配，都移动 t 的指针
            j++;
        }

        // 如果 s 的指针移动到了末尾，说明 s 是 t 的子序列
        return i == s.size();
    }
};

int main() {
    Solution solution;
    string s = "abc";
    string t = "ahbgdc";
    cout << "Input: s = \"" << s << "\", t = \"" << t << "\"" << endl;
    cout << "Output: " << (solution.isSubsequence(s, t) ? "true" : "false") << endl;
    return 0;
}
```

#### Java

```
public class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0; // s 的索引
        int j = 0; // t 的索引

        // 使用双指针遍历字符串 t
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                // 如果当前字符匹配，则移动 s 的指针
                i++;
            }
            // 无论是否匹配，都移动 t 的指针
            j++;
        }

        // 如果 s 的指针移动到了末尾，说明 s 是 t 的子序列
        return i == s.length();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "abc";
        String t = "ahbgdc";
        System.out.println("Input: s = \"" + s + "\", t = \"" + t + "\"");
        System.out.println("Output: " + (solution.isSubsequence(s, t) ? "true" : "false"));
    }
}
```

#### Python

```
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # s 的索引
        j = 0  # t 的索引

        # 使用双指针遍历字符串 t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                # 如果当前字符匹配，则移动 s 的指针
                i += 1
            # 无论是否匹配，都移动 t 的指针
            j += 1

        # 如果 s 的指针移动到了末尾，说明 s 是 t 的子序列
        return i == len(s)

if __name__ == "__main__":
    solution = Solution()
    s = "abc"
    t = "ahbgdc"
    print("Input: s = \"" + s + "\", t = \"" + t + "\"")
    print("Output:", solution.isSubsequence(s, t))
```

