# 面试经典算法题33-最长公共前缀

LeetCode.14

### 问题描述

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。

**示例 1：**

```
输入：strs = ["flower","flow","flight"]
输出："fl"
```

**示例 2：**

```
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
```

### 思路

1. 如果字符串数组为空，则直接返回空字符串。
2. 初始化最长公共前缀为数组的第一个字符串。
3. 遍历字符串数组，依次比较每个字符串和当前最长公共前缀的公共前缀，更新最长公共前缀。
4. 如果遍历完后最长公共前缀为空，则返回空字符串，否则返回最长公共前缀。

### 流程图

```
               +------------------------------------+
               | 初始化 prefix 为 strs[0] = "flower" |
               +------------------------------------+
                              |
                              V
               +----------------------------------+
               |   遍历数组：strs = {"flower",      |
               |             "flow", "flight"}    |
               +----------------------------------+
                              |
                              V
            +------------------------------------------+
            |         比较当前字符串与 prefix 的公共前缀    |
            +------------------------------------------+
                              |
                +-----------------------------+
                | 如果公共前缀为空，直接返回空字符串|
                +-----------------------------+
                              |
                              V
               +----------------------------------+
               | 更新 prefix 为当前字符串的公共前缀    |
               +----------------------------------+
                              |
                              V
               +----------------------------------+
               |   继续遍历数组中的下一个字符串        |
               +----------------------------------+
                              |
                              V
               +----------------------------------+
               |           返回最终的 prefix        |
               +----------------------------------+

```

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) {
            return ""; // 如果字符串数组为空，直接返回空字符串
        }

        string prefix = strs[0]; // 初始化最长公共前缀为数组的第一个字符串

        for (int i = 1; i < strs.size(); ++i) {
            int j = 0;
            // 比较当前字符串和最长公共前缀的公共前缀
            while (j < strs[i].size() && j < prefix.size() && strs[i][j] == prefix[j]) {
                ++j;
            }
            if (j == 0) {
                return ""; // 如果最长公共前缀为空，直接返回空字符串
            }
            prefix = prefix.substr(0, j); // 更新最长公共前缀
        }

        return prefix; // 返回最长公共前缀
    }
};

int main() {
    vector<string> strs = {"flower", "flow", "flight"}; // 输入字符串数组
    Solution solution;
    string result = solution.longestCommonPrefix(strs); // 查找最长公共前缀
    cout << "最长公共前缀：" << result << endl; // 输出结果

    return 0;
}
```

#### Java

```
import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return ""; // 如果字符串数组为空，直接返回空字符串
        }

        String prefix = strs[0]; // 初始化最长公共前缀为数组的第一个字符串

        for (int i = 1; i < strs.length; i++) {
            int j = 0;
            // 比较当前字符串和最长公共前缀的公共前缀
            while (j < strs[i].length() && j < prefix.length() && strs[i].charAt(j) == prefix.charAt(j)) {
                j++;
            }
            if (j == 0) {
                return ""; // 如果最长公共前缀为空，直接返回空字符串
            }
            prefix = prefix.substring(0, j); // 更新最长公共前缀
        }

        return prefix; // 返回最长公共前缀
    }
}

public class Main {
    public static void main(String[] args) {
        String[] strs = {"flower", "flow", "flight"}; // 输入字符串数组
        Solution solution = new Solution();
        String result = solution.longestCommonPrefix(strs); // 查找最长公共前缀
        System.out.println("最长公共前缀：" + result); // 输出结果
    }
}
```

#### Python

```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""  # 如果字符串数组为空，直接返回空字符串

        prefix = strs[0]  # 初始化最长公共前缀为数组的第一个字符串

        for i in range(1, len(strs)):
            j = 0
            # 比较当前字符串和最长公共前缀的公共前缀
            while j < len(strs[i]) and j < len(prefix) and strs[i][j] == prefix[j]:
                j += 1
            if j == 0:
                return ""  # 如果最长公共前缀为空，直接返回空字符串
            prefix = prefix[:j]  # 更新最长公共前缀

        return prefix  # 返回最长公共前缀

# 测试
solution = Solution()
strs = ["flower", "flow", "flight"]  # 输入字符串数组
result = solution.longestCommonPrefix(strs)  # 查找最长公共前缀
print("最长公共前缀：", result)  # 输出结果
```

