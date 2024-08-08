# 面试经典算法题91-电话号码的字母组合

LeetCode.17

### 问题描述

给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![img](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/200px-telephone-keypad2svg.png)

**示例 1：**

```
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**示例 2：**

```
输入：digits = ""
输出：[]
```

**示例 3：**

```
输入：digits = "2"
输出：["a","b","c"]
```

### 思路

1. 构建映射关系：使用一个映射表，将数字 `2-9` 映射到对应的字母列表。例如：`2` 对应 `"abc"`，`3` 对应 `"def"` 等。

数字到字母的映射：

``` 
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"
```

2. 处理特殊情况：如果输入的 `digits` 为空字符串，直接返回空列表，因为没有数字对应任何字母组合。

3. 回溯法生成组合：

   - 定义一个回溯函数，用于生成所有可能的字母组合。

   - 在回溯过程中，依次取出每个数字对应的字母，并将其添加到当前的组合路径中。

   - 每次递归处理下一个数字，直到处理完所有数字为止。

   - 当组合路径长度与输入数字字符串长度一致时，将该组合加入结果列表。

4. 回溯和剪枝：

   - 在递归回溯时，每次添加一个字母后继续处理剩余的数字。

   - 当递归返回时，回溯到上一个状态，移除最后添加的字母，继续尝试其他可能的字母。

5. 输出结果：最终生成的所有字母组合会存储在一个结果列表中，返回该列表。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // 如果输入为空，返回空结果
        if (digits.empty()) {
            return {};
        }

        // 数字到字母的映射表
        vector<string> mapping = {
            "",    // 0 (没有对应的字母)
            "",    // 1 (没有对应的字母)
            "abc", // 2
            "def", // 3
            "ghi", // 4
            "jkl", // 5
            "mno", // 6
            "pqrs",// 7
            "tuv", // 8
            "wxyz" // 9
        };

        // 结果存储的容器
        vector<string> result;
        
        // 递归回溯函数
        backtrack(result, mapping, digits, 0, "");

        return result;
    }

private:
    void backtrack(vector<string>& result, const vector<string>& mapping, const string& digits, int index, string current) {
        // 如果当前组合的长度等于输入字符串的长度，则将当前组合加入结果集
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }

        // 获取当前数字对应的字母集合
        string letters = mapping[digits[index] - '0'];
        
        // 遍历每个字母，递归处理后续的数字
        for (char letter : letters) {
            backtrack(result, mapping, digits, index + 1, current + letter);
        }
    }
};

// 主函数用于测试
int main() {
    Solution solution;

    // 示例 1
    string digits1 = "23";
    vector<string> result1 = solution.letterCombinations(digits1);
    cout << "输入: " << digits1 << "\n输出: ";
    for (const string& s : result1) {
        cout << s << " ";
    }
    cout << endl;

    // 示例 2
    string digits2 = "";
    vector<string> result2 = solution.letterCombinations(digits2);
    cout << "输入: " << digits2 << "\n输出: ";
    for (const string& s : result2) {
        cout << s << " ";
    }
    cout << endl;

    // 示例 3
    string digits3 = "2";
    vector<string> result3 = solution.letterCombinations(digits3);
    cout << "输入: " << digits3 << "\n输出: ";
    for (const string& s : result3) {
        cout << s << " ";
    }
    cout << endl;

    return 0;
}
```

#### Java

```
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> letterCombinations(String digits) {
        // 如果输入为空，直接返回空列表
        if (digits == null || digits.length() == 0) {
            return new ArrayList<>();
        }

        // 数字到字母的映射表
        String[] mapping = new String[]{
            "",    // 0
            "",    // 1
            "abc", // 2
            "def", // 3
            "ghi", // 4
            "jkl", // 5
            "mno", // 6
            "pqrs",// 7
            "tuv", // 8
            "wxyz" // 9
        };

        List<String> result = new ArrayList<>();
        backtrack(result, digits, mapping, 0, new StringBuilder());
        return result;
    }

    // 回溯算法的核心函数
    private void backtrack(List<String> result, String digits, String[] mapping, int index, StringBuilder current) {
        // 如果当前组合的长度等于输入数字串的长度，则添加到结果集中
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }

        // 获取当前数字对应的字母
        String letters = mapping[digits.charAt(index) - '0'];
        // 遍历每个字母，递归处理下一个数字
        for (char letter : letters.toCharArray()) {
            current.append(letter);             // 添加当前字母
            backtrack(result, digits, mapping, index + 1, current); // 递归处理下一个数字
            current.deleteCharAt(current.length() - 1); // 回溯，删除当前字母
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 示例1
        String digits1 = "23";
        System.out.println("输入: " + digits1);
        System.out.println("输出: " + solution.letterCombinations(digits1));

        // 示例2
        String digits2 = "";
        System.out.println("输入: " + digits2);
        System.out.println("输出: " + solution.letterCombinations(digits2));

        // 示例3
        String digits3 = "2";
        System.out.println("输入: " + digits3);
        System.out.println("输出: " + solution.letterCombinations(digits3));
    }
}
```

#### Python

```
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # 如果输入为空，返回空列表
        if not digits:
            return []

        # 数字到字母的映射表
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(index, path):
            # 如果路径长度等于数字长度，加入结果
            if index == len(digits):
                combinations.append("".join(path))
                return

            # 获取当前数字对应的字母
            letters = mapping[digits[index]]
            for letter in letters:
                path.append(letter)          # 添加当前字母
                backtrack(index + 1, path)   # 递归处理下一个数字
                path.pop()                   # 回溯，移除当前字母

        combinations = []
        backtrack(0, [])
        return combinations

# 示例测试
solution = Solution()

# 示例1
digits1 = "23"
print(f"输入: {digits1}\n输出: {solution.letterCombinations(digits1)}")

# 示例2
digits2 = ""
print(f"输入: {digits2}\n输出: {solution.letterCombinations(digits2)}")

# 示例3
digits3 = "2"
print(f"输入: {digits3}\n输出: {solution.letterCombinations(digits3)}")
```

