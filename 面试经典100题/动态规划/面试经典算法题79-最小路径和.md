# 面试经典算法题79-最小路径和

LeetCode.64

### 问题描述

给定一个包含非负整数的 `*m* x *n*` 网格 `grid` ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

**说明：**每次只能向下或者向右移动一步。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/minpath.jpg)

```c
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
```

**示例 2：**

```c
输入：grid = [[1,2,3],[4,5,6]]
输出：12
```

### 思路

1. 状态定义：使用一个二维数组 `dp`，其中 `dp[i][j]` 表示到达位置 (i, j) 的最小路径和。
2. 状态转移方程：到达位置 (i, j) 只能从上方 (i-1, j) 或左方 (i, j-1) 移动过来。因此状态转移方程为：`dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`。
3. 初始状态：`dp[0][0]` 初始为 `grid[0][0]`，因为这是起点。
4. 结果：最终结果存储在 `dp[m-1][n-1]` 中，即从左上角到右下角的最小路径和。

### 参考代码

#### C++

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minPathSum(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    
    // 创建一个二维 dp 数组，并初始化为与 grid 大小相同
    vector<vector<int>> dp(m, vector<int>(n, 0));
    
    // 初始化起点
    dp[0][0] = grid[0][0];
    
    // 初始化第一列
    for (int i = 1; i < m; ++i) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }
    
    // 初始化第一行
    for (int j = 1; j < n; ++j) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }
    
    // 填充 dp 数组
    for (int i = 1; i < m; ++i) {
        for (int j = 1; j < n; ++j) {
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
        }
    }
    
    // 返回从左上角到右下角的最小路径和
    return dp[m-1][n-1];
}

int main() {
    vector<vector<int>> grid1 = {
        {1, 3, 1},
        {1, 5, 1},
        {4, 2, 1}
    };
    cout << "输入: [[1,3,1],[1,5,1],[4,2,1]]" << endl;
    cout << "输出: " << minPathSum(grid1) << endl;  // 输出: 7

    vector<vector<int>> grid2 = {
        {1, 2, 3},
        {4, 5, 6}
    };
    cout << "输入: [[1,2,3],[4,5,6]]" << endl;
    cout << "输出: " << minPathSum(grid2) << endl;  // 输出: 12

    return 0;
}
```

#### Java

```java
import java.util.Arrays;

public class MinPathSum {

    // 计算从左上角到右下角的最小路径和
    public int minPathSum(int[][] grid) {
        int m = grid.length; // 获取网格的行数
        int n = grid[0].length; // 获取网格的列数

        // 创建一个二维数组 dp，用于存储到达每个位置的最小路径和
        int[][] dp = new int[m][n];

        // 初始化起点
        dp[0][0] = grid[0][0];

        // 初始化第一列
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }

        // 初始化第一行
        for (int j = 1; j < n; j++) {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }

        // 填充 dp 数组
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = grid[i][j] + Math.min(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        // 返回从左上角到右下角的最小路径和
        return dp[m - 1][n - 1];
    }

    public static void main(String[] args) {
        MinPathSum solution = new MinPathSum();

        int[][] grid1 = {
            {1, 3, 1},
            {1, 5, 1},
            {4, 2, 1}
        };
        System.out.println("输入: [[1,3,1],[1,5,1],[4,2,1]]");
        System.out.println("输出: " + solution.minPathSum(grid1));  // 输出: 7

        int[][] grid2 = {
            {1, 2, 3},
            {4, 5, 6}
        };
        System.out.println("输入: [[1,2,3],[4,5,6]]");
        System.out.println("输出: " + solution.minPathSum(grid2));  // 输出: 12
    }
}
```

#### Python

```python
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 获取网格的行数和列数
        m, n = len(grid), len(grid[0])

        # 创建一个二维数组 dp，用于存储到达每个位置的最小路径和
        dp = [[0] * n for _ in range(m)]

        # 初始化起点
        dp[0][0] = grid[0][0]

        # 初始化第一列
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 初始化第一行
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 填充 dp 数组
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        # 返回从左上角到右下角的最小路径和
        return dp[m - 1][n - 1]

# 测试代码
if __name__ == "__main__":
    solution = Solution()

    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print("输入: [[1,3,1],[1,5,1],[4,2,1]]")
    print("输出:", solution.minPathSum(grid1))  # 输出: 7

    grid2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print("输入: [[1,2,3],[4,5,6]]")
    print("输出:", solution.minPathSum(grid2))  # 输出: 12
```

