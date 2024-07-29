# 面试经典算法题82-编辑距离

LeetCode.72

### 问题描述

给你两个单词 `word1` 和 `word2`， *请返回将 `word1` 转换成 `word2` 所使用的最少操作数* 。

你可以对一个单词进行如下三种操作：

- 插入一个字符
- 删除一个字符
- 替换一个字符

**示例 1：**

```
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```

**示例 2：**

```
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

### 思路

1. 定义状态：用 `dp[i][j]` 表示将 `word1` 的前 `i` 个字符转换为 `word2` 的前 `j` 个字符所需的最少操作数。

2. 初始化：

   - 当 `i == 0` 时，需要进行 `j` 次插入操作才能将空字符串变为 `word2` 的前 `j` 个字符。

   - 当 `j == 0` 时，需要进行 `i` 次删除操作才能将 `word1` 的前 `i` 个字符变为空字符串。

3. 状态转移：

   - 如果 `word1[i-1] == word2[j-1]`，则不需要额外操作：`dp[i][j] = dp[i-1][j-1]`。

   - 如果 `word1[i-1] != word2[j-1]`，则取以下三种操作的最小值加 1：
     - 插入操作：`dp[i][j-1] + 1`
     - 删除操作：`dp[i-1][j] + 1`
     - 替换操作：`dp[i-1][j-1] + 1`

4. 最终结果：`dp[word1.length()][word2.length()]` 就是将 `word1` 转换为 `word2` 所需的最少操作数。

给个表格帮助理解：

|      |      | r    | o    | s    |
| ---- | ---- | ---- | ---- | ---- |
|      | 0    | 1    | 2    | 3    |
| h    | 1    | 1    | 2    | 3    |
| o    | 2    | 2    | 1    | 2    |
| r    | 3    | 2    | 2    | 3    |
| s    | 4    | 3    | 3    | 2    |
| e    | 5    | 4    | 4    | 3    |

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// 计算将 word1 转换成 word2 所使用的最少操作数
int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    // 初始化第一行和第一列
    for (int i = 0; i <= m; ++i) {
        dp[i][0] = i; // 将前 i 个字符转换为空字符串所需的操作数
    }
    for (int j = 0; j <= n; ++j) {
        dp[0][j] = j; // 将空字符串转换为前 j 个字符所需的操作数
    }

    // 填充 dp 表
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (word1[i - 1] == word2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1]; // 字符相同，不需要额外操作
            } else {
                dp[i][j] = min({dp[i - 1][j] + 1,   // 删除操作
                                dp[i][j - 1] + 1,   // 插入操作
                                dp[i - 1][j - 1] + 1}); // 替换操作
            }
        }
    }

    return dp[m][n]; // 返回将 word1 转换为 word2 所需的最少操作数
}

int main() {
    string word1, word2;
    cout << "输入word1: ";
    cin >> word1;
    cout << "输入word2: ";
    cin >> word2;

    int result = minDistance(word1, word2);
    cout << "将 " << word1 << " 转换为 " << word2 << " 所需的最少操作数: " << result << endl;

    return 0;
}
```

#### Java

```
import java.util.Scanner;

public class MinDistance {

    // 计算将 word1 转换成 word2 所使用的最少操作数
    public static int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        int[][] dp = new int[m + 1][n + 1];

        // 初始化第一行和第一列
        for (int i = 0; i <= m; ++i) {
            dp[i][0] = i; // 将前 i 个字符转换为空字符串所需的操作数
        }
        for (int j = 0; j <= n; ++j) {
            dp[0][j] = j; // 将空字符串转换为前 j 个字符所需的操作数
        }

        // 填充 dp 表
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1]; // 字符相同，不需要额外操作
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j] + 1, // 删除操作
                            Math.min(dp[i][j - 1] + 1, // 插入操作
                                    dp[i - 1][j - 1] + 1)); // 替换操作
                }
            }
        }

        return dp[m][n]; // 返回将 word1 转换为 word2 所需的最少操作数
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("输入word1: ");
        String word1 = scanner.nextLine();

        System.out.print("输入word2: ");
        String word2 = scanner.nextLine();

        int result = minDistance(word1, word2);
        System.out.println("将 " + word1 + " 转换为 " + word2 + " 所需的最少操作数: " + result);
    }
}
```

#### Python

```
def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化第一行和第一列
    for i in range(m + 1):
        dp[i][0] = i  # 将前 i 个字符转换为空字符串所需的操作数
    for j in range(n + 1):
        dp[0][j] = j  # 将空字符串转换为前 j 个字符所需的操作数

    # 填充 dp 表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # 字符相同，不需要额外操作
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,   # 删除操作
                               dp[i][j - 1] + 1,   # 插入操作
                               dp[i - 1][j - 1] + 1)  # 替换操作

    return dp[m][n]  # 返回将 word1 转换为 word2 所需的最少操作数

if __name__ == "__main__":
    word1 = input("输入word1: ")
    word2 = input("输入word2: ")

    result = minDistance(word1, word2)
    print(f"将 {word1} 转换为 {word2} 所需的最少操作数: {result}")
```

