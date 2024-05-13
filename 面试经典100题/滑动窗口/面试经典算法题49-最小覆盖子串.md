# 面试经典算法题49-最小覆盖子串

LeetCode.76

### 问题描述

给你一个字符串 `s` 、一个字符串 `t` 。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果 `s` 中不存在涵盖 `t` 所有字符的子串，则返回空字符串 `""` 。

**注意：**

- 对于 `t` 中重复字符，我们寻找的子字符串中该字符数量必须不少于 `t` 中该字符数量。
- 如果 `s` 中存在这样的子串，我们保证它是唯一的答案。

**示例 1：**

```
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
```

**示例 2：**

```
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
```

**示例 3:**

```
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
```

### 思路

1. 使用滑动窗口技巧，定义两个指针 `left` 和 `right`，分别表示窗口的左右边界，初始时两者都指向字符串的开头。
2. 移动右指针 `right` 扩展窗口，直到窗口中包含了 `t` 中的所有字符。
3. 记录当前窗口的字符出现次数，以及 `t` 中字符的总数。
4. 移动左指针 `left` 缩小窗口，直到无法继续缩小为止，记录当前最小窗口的起始位置和长度。
5. 重复步骤 2 和 4，直到右指针 `right` 到达字符串的末尾。

### 参考代码

#### C++

```
#include <iostream>
#include <string>
#include <unordered_map>

std::string minWindow(std::string s, std::string t) {
    if (s.empty() || t.empty()) {
        return "";
    }

    std::unordered_map<char, int> targetMap, windowMap;
    // 统计 t 中每个字符的出现次数
    for (char c : t) {
        targetMap[c]++;
    }

    int left = 0, right = 0, minLen = INT_MAX, minStart = 0, count = 0;

    while (right < s.size()) {
        char c = s[right];
        // 如果当前字符是 t 中的字符，则在窗口中增加该字符的出现次数
        if (targetMap.find(c) != targetMap.end()) {
            windowMap[c]++;
            // 如果窗口中该字符的出现次数不超过 t 中该字符的出现次数，则 count++
            if (windowMap[c] <= targetMap[c]) {
                count++;
            }
        }

        // 如果窗口中包含了 t 中的所有字符
        while (count == t.size()) {
            // 更新最小覆盖子串的长度和起始位置
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minStart = left;
            }

            char leftChar = s[left];
            // 如果左边界字符是 t 中的字符
            if (targetMap.find(leftChar) != targetMap.end()) {
                // 减少窗口中左边界字符的出现次数
                windowMap[leftChar]--;
                // 如果窗口中左边界字符的出现次数小于 t 中该字符的出现次数，则 count--
                if (windowMap[leftChar] < targetMap[leftChar]) {
                    count--;
                }
            }

            left++; // 缩小窗口
        }

        right++; // 扩大窗口
    }

    return minLen == INT_MAX ? "" : s.substr(minStart, minLen);
}

int main() {
    std::string s = "ADOBECODEBANC";
    std::string t = "ABC";
    std::string result = minWindow(s, t);
    std::cout << "最小覆盖子串：" << result << std::endl;
    return 0;
}
```

#### Java

```
import java.util.HashMap;
import java.util.Map;

public class Solution {

    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() == 0 || t.length() == 0) {
            return "";
        }

        // 统计 t 中每个字符的出现次数
        Map<Character, Integer> targetMap = new HashMap<>();
        for (char c : t.toCharArray()) {
            targetMap.put(c, targetMap.getOrDefault(c, 0) + 1);
        }

        int left = 0, right = 0, minLen = Integer.MAX_VALUE, minStart = 0, count = 0;
        Map<Character, Integer> windowMap = new HashMap<>();

        while (right < s.length()) {
            char c = s.charAt(right);
            // 如果当前字符是 t 中的字符，则在窗口中增加该字符的出现次数
            windowMap.put(c, windowMap.getOrDefault(c, 0) + 1);
            // 如果窗口中该字符的出现次数不超过 t 中该字符的出现次数，则 count++
            if (targetMap.containsKey(c) && windowMap.get(c).intValue() <= targetMap.get(c).intValue()) {
                count++;
            }

            // 如果窗口中包含了 t 中的所有字符
            while (count == t.length()) {
                // 更新最小覆盖子串的长度和起始位置
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                }

                char leftChar = s.charAt(left);
                // 如果左边界字符是 t 中的字符
                if (targetMap.containsKey(leftChar)) {
                    // 减少窗口中左边界字符的出现次数
                    windowMap.put(leftChar, windowMap.get(leftChar) - 1);
                    // 如果窗口中左边界字符的出现次数小于 t 中该字符的出现次数，则 count--
                    if (windowMap.get(leftChar).intValue() < targetMap.get(leftChar).intValue()) {
                        count--;
                    }
                }

                left++; // 缩小窗口
            }

            right++; // 扩大窗口
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLen);
    }

    public static void main(String[] args) {
        String s = "ADOBECODEBANC";
        String t = "ABC";
        Solution solution = new Solution();
        String result = solution.minWindow(s, t);
        System.out.println("最小覆盖子串：" + result);
    }
}
```

#### Python

```
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # 统计 t 中每个字符的出现次数
        target_map = {}
        for c in t:
            target_map[c] = target_map.get(c, 0) + 1

        left, right, min_len, min_start, count = 0, 0, float("inf"), 0, 0
        window_map = {}

        while right < len(s):
            c = s[right]
            # 如果当前字符是 t 中的字符，则在窗口中增加该字符的出现次数
            window_map[c] = window_map.get(c, 0) + 1
            # 如果窗口中该字符的出现次数不超过 t 中该字符的出现次数，则 count++
            if c in target_map and window_map[c] <= target_map[c]:
                count += 1

            # 如果窗口中包含了 t 中的所有字符
            while count == len(t):
                # 更新最小覆盖子串的长度和起始位置
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                left_char = s[left]
                # 如果左边界字符是 t 中的字符
                if left_char in target_map:
                    # 减少窗口中左边界字符的出现次数
                    window_map[left_char] -= 1
                    # 如果窗口中左边界字符的出现次数小于 t 中该字符的出现次数，则 count--
                    if window_map[left_char] < target_map[left_char]:
                        count -= 1

                left += 1  # 缩小窗口

            right += 1  # 扩大窗口

        return "" if min_len == float("inf") else s[min_start:min_start + min_len]

    def main(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        solution = Solution()
        result = solution.minWindow(s, t)
        print("最小覆盖子串：", result)

if __name__ == "__main__":
    Solution().main()
```

