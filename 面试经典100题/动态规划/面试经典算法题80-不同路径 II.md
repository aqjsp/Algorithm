# 面试经典算法题80-不同路径 II

LeetCode.63

### 问题描述

一个机器人位于一个 `m x n` 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 `1` 和 `0` 来表示。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/robot1.jpg)

```c
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/robot2.jpg)

```c
输入：obstacleGrid = [[0,1],[0,0]]
输出：1
```

### 思路

1. 定义状态：使用一个二维数组 `dp`，其中 `dp[i][j]` 表示从起点到位置 `(i, j)` 的不同路径数。

2. 初始化：

   - 如果起点 `(0, 0)` 是障碍物，直接返回 0，因为无法出发。

   - 初始化 `dp[0][0]` 为 1，表示起点本身有一个路径。

   - 初始化第一列和第一行，如果在某个位置遇到障碍物，则从该位置起，后面的路径数都为 0，因为无法通过障碍物。

3. 状态转移：对于每个位置 `(i, j)`，如果该位置是障碍物，则 `dp[i][j] = 0`，否则 `dp[i][j]` 等于上方和左方位置的路径数之和，即 `dp[i][j] = dp[i-1][j] + dp[i][j-1]`。

4. 结果：返回 `dp[m-1][n-1]`，即从起点到终点的路径数。

### 参考代码

#### C++

```c++
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        
        // 如果起点就是障碍物，返回0
        if (obstacleGrid[0][0] == 1) {
            return 0;
        }
        
        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[0][0] = 1;  // 起点初始化为1
        
        // 初始化第一列
        for (int i = 1; i < m; ++i) {
            dp[i][0] = (obstacleGrid[i][0] == 1 || dp[i-1][0] == 0) ? 0 : 1;
        }
        
        // 初始化第一行
        for (int j = 1; j < n; ++j) {
            dp[0][j] = (obstacleGrid[0][j] == 1 || dp[0][j-1] == 0) ? 0 : 1;
        }
        
        // 填充dp数组
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (obstacleGrid[i][j] == 1) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        
        return dp[m-1][n-1];
    }
};

int main() {
    Solution solution;

    vector<vector<int>> obstacleGrid1 = {
        {0, 0, 0},
        {0, 1, 0},
        {0, 0, 0}
    };
    cout << "输入: [[0,0,0],[0,1,0],[0,0,0]]" << endl;
    cout << "输出: " << solution.uniquePathsWithObstacles(obstacleGrid1) << endl;  // 输出: 2

    vector<vector<int>> obstacleGrid2 = {
        {0, 1},
        {0, 0}
    };
    cout << "输入: [[0,1],[0,0]]" << endl;
    cout << "输出: " << solution.uniquePathsWithObstacles(obstacleGrid2) << endl;  // 输出: 1

    return 0;
}
```

#### Java

```java
import java.util.*;

public class UniquePathsII {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        
        // 如果起点就是障碍物，返回0
        if (obstacleGrid[0][0] == 1) {
            return 0;
        }
        
        int[][] dp = new int[m][n];
        dp[0][0] = 1;  // 起点初始化为1
        
        // 初始化第一列
        for (int i = 1; i < m; ++i) {
            dp[i][0] = (obstacleGrid[i][0] == 1 || dp[i-1][0] == 0) ? 0 : 1;
        }
        
        // 初始化第一行
        for (int j = 1; j < n; ++j) {
            dp[0][j] = (obstacleGrid[0][j] == 1 || dp[0][j-1] == 0) ? 0 : 1;
        }
        
        // 填充dp数组
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (obstacleGrid[i][j] == 1) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        
        return dp[m-1][n-1];
    }

    public static void main(String[] args) {
        UniquePathsII solution = new UniquePathsII();

        int[][] obstacleGrid1 = {
            {0, 0, 0},
            {0, 1, 0},
            {0, 0, 0}
        };
        System.out.println("输入: [[0,0,0],[0,1,0],[0,0,0]]");
        System.out.println("输出: " + solution.uniquePathsWithObstacles(obstacleGrid1));  // 输出: 2

        int[][] obstacleGrid2 = {
            {0, 1},
            {0, 0}
        };
        System.out.println("输入: [[0,1],[0,0]]");
        System.out.println("输出: " + solution.uniquePathsWithObstacles(obstacleGrid2));  // 输出: 1
    }
}
```

#### Python

```python
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    # 如果起点就是障碍物，返回0
    if obstacleGrid[0][0] == 1:
        return 0
    
    # 初始化dp数组
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    # 初始化第一列
    for i in range(1, m):
        dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
    
    # 初始化第一行
    for j in range(1, n):
        dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]
    
    # 填充dp数组
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# 测试用例
obstacleGrid1 = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print("输入: [[0,0,0],[0,1,0],[0,0,0]]")
print("输出:", uniquePathsWithObstacles(obstacleGrid1))  # 输出: 2

obstacleGrid2 = [
    [0, 1],
    [0, 0]
]
print("输入: [[0,1],[0,0]]")
print("输出:", uniquePathsWithObstacles(obstacleGrid2))  # 输出: 1
```

