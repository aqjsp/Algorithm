# 面试经典算法题37-反转字符串中的单词

LeetCode.151

### 问题描述

给你一个字符串 `s` ，请你反转字符串中 **单词** 的顺序。

**单词** 是由非空格字符组成的字符串。`s` 中使用至少一个空格将字符串中的 **单词** 分隔开。

返回 **单词** 顺序颠倒且 **单词** 之间用单个空格连接的结果字符串。

**注意：**输入字符串 `s`中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

**示例 1：**

```
输入：s = "the sky is blue"
输出："blue is sky the"
```

**示例 2：**

```
输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。
```

**示例 3：**

```
输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
```

### 思路

1. 倒序遍历字符串 `s` ，记录每个单词的起始和结束位置；
2. 将每个单词拼接到结果字符串中，单词之间用一个空格分隔。

### 图解

这里根据示例一给大家进行一个流程的分解。

```
            +--------------------------------+
            |         开始执行程序             |
            +--------------------------------+
                           |
                           v
            +--------------------------------+
            |         输入字符串s              |
            |      s = "the sky is blue"     |
            +--------------------------------+
                           |
                           v
            +--------------------------------+
            |       初始化结果字符串result      |
            |            result = ""         |
            +--------------------------------+
                           |
                           v
            +--------------------------------+
            |       初始化结束位置end          |
            |          end = 14              |
            +--------------------------------+
                           |
                           v
            +--------------------------------+
            |       从后向前遍历字符串s         |
            +--------------------------------+
                           |
                           v
            +--------------------------------+
            |      当前字符为' '时             |
            |      更新结束位置end             |
            +--------------------------------+
                           |
                           v
    +-------------------------------------------------+
    |      当前字符为非空格且前一个字符为空格或当前位置为0时  |
    |      如果结果字符串result非空，添加一个空格到result   |
    |      将当前单词加入结果字符串result                 |
    +-------------------------------------------------+
                           |
                           v
            +---------------------------------+
            |         返回结果字符串result      |
            |      result = "blue is sky the" |
            +---------------------------------+
                           |
                           v
            +--------------------------------+
            |           结束程序              |
            +--------------------------------+

```

### 参考代码

#### C++

```
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string result = ""; // 初始化结果字符串
        int end = s.length(); // 结束位置为字符串长度

        for (int i = s.length() - 1; i >= 0; --i) { // 倒序遍历字符串
            if (s[i] == ' ') { // 遇到空格，更新结束位置
                end = i;
            } else if (i == 0 || s[i - 1] == ' ') { // 遇到单词起始位置
                if (!result.empty()) { // 如果结果字符串非空，加入一个空格
                    result += " ";
                }
                result += s.substr(i, end - i); // 将单词加入结果字符串
            }
        }

        return result; // 返回结果字符串
    }
};

int main() {
    string s = "the sky is blue"; // 输入字符串
    Solution solution;
    string result = solution.reverseWords(s); // 反转单词顺序
    cout << "反转后的字符串：" << result << endl; // 输出结果

    return 0;
}
```

这个方法直接封神！

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202404022243485.png)

#### Java

```
public class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+"); // 按空格分割字符串
        StringBuilder result = new StringBuilder(); // 初始化结果字符串

        for (int i = words.length - 1; i >= 0; i--) { // 倒序遍历单词数组
            result.append(words[i]); // 将单词加入结果字符串
            if (i > 0) {
                result.append(" "); // 添加单词间的空格
            }
        }

        return result.toString(); // 返回结果字符串
    }

    public static void main(String[] args) {
        String s = "the sky is blue"; // 输入字符串
        Solution solution = new Solution();
        String result = solution.reverseWords(s); // 反转单词顺序
        System.out.println("反转后的字符串：" + result); // 输出结果
    }
}
```

#### Python

```
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # 按空格分割字符串
        words.reverse()  # 反转单词列表
        return ' '.join(words)  # 连接成字符串

# 测试代码
s = "the sky is blue"  # 输入字符串
solution = Solution()
result = solution.reverseWords(s)  # 反转单词顺序
print("反转后的字符串：", result)  # 输出结果
```

