# 面试经典算法题96-括号生成

LeetCode.22

### 问题描述

数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

**示例 1：**

```
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
```

**示例 2：**

```
输入：n = 1
输出：["()"]
```

### 思路

1. 递归回溯生成括号：

   - 使用递归函数 `backtrack` 来生成括号组合。

   - 参数包括当前生成的括号串 `current`、已放置的左括号数量 `open_count`、已放置的右括号数量 `close_count` 以及总对数 `n`。

2. 递归结束条件：当生成的括号串 `current` 长度等于 `2 * n` 时，表示已经生成了一个有效的括号组合，将其加入结果列表 `result` 中。

3. 生成有效组合的规则：

   - 左括号 `(` 的数量不能超过 `n`，右括号 `)` 的数量不能超过左括号的数量。

   - 只要左括号 `(` 数量小于 `n`，可以继续添加左括号。

   - 只要右括号 `)` 数量小于左括号的数量，可以继续添加右括号。

4. 递归探索：在满足条件的前提下，递归添加左括号或右括号，直到生成所有可能的有效组合。

### 参考代码

#### C++

```
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        backtrack(result, "", 0, 0, n);
        return result;
    }

private:
    // 递归回溯函数
    void backtrack(vector<string>& result, string current, int open_count, int close_count, int n) {
        // 终止条件：如果当前字符串的长度等于 2 * n
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }

        // 如果左括号数量小于 n，继续添加左括号
        if (open_count < n) {
            backtrack(result, current + "(", open_count + 1, close_count, n);
        }

        // 如果右括号数量小于左括号数量，继续添加右括号
        if (close_count < open_count) {
            backtrack(result, current + ")", open_count, close_count + 1, n);
        }
    }
};

// 示例运行
int main() {
    Solution solution;
    int n = 3; // 示例输入
    vector<string> result = solution.generateParenthesis(n);
    
    // 输出结果
    for (const string& s : result) {
        printf("%s\n", s.c_str());
    }

    return 0;
}
```

#### Java

```
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, "", 0, 0, n);
        return result;
    }

    private void backtrack(List<String> result, String current, int openCount, int closeCount, int n) {
        // 终止条件：如果当前字符串的长度等于 2 * n
        if (current.length() == 2 * n) {
            result.add(current);
            return;
        }

        // 如果左括号数量小于 n，继续添加左括号
        if (openCount < n) {
            backtrack(result, current + "(", openCount + 1, closeCount, n);
        }

        // 如果右括号数量小于左括号数量，继续添加右括号
        if (closeCount < openCount) {
            backtrack(result, current + ")", openCount, closeCount + 1, n);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 3; // 示例输入
        List<String> result = solution.generateParenthesis(n);

        // 输出结果
        for (String s : result) {
            System.out.println(s);
        }
    }
}
```

#### Python

```
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(result, "", 0, 0, n)
        return result

    def backtrack(self, result: List[str], current: str, open_count: int, close_count: int, n: int):
        # 终止条件：如果当前字符串的长度等于 2 * n
        if len(current) == 2 * n:
            result.append(current)
            return

        # 如果左括号数量小于 n，继续添加左括号
        if open_count < n:
            self.backtrack(result, current + "(", open_count + 1, close_count, n)

        # 如果右括号数量小于左括号数量，继续添加右括号
        if close_count < open_count:
            self.backtrack(result, current + ")", open_count, close_count + 1, n)

if __name__ == "__main__":
    solution = Solution()
    n = 3  # 示例输入
    result = solution.generateParenthesis(n)

    # 输出结果
    for s in result:
        print(s)
```

