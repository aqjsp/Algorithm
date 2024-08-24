# 面试经典算法题98-岛屿数量

LeetCode.200

### 问题描述

给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

**示例 1：**

```
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
```

**示例 2：**

```
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
```

### 思路

1. 遍历网格：我们需要遍历整个二维网格 `grid` 中的每一个位置。

2. 深度优先搜索 (DFS)：

   - 每当遇到一个 `'1'`，即表示找到一个新的岛屿。

   - 从这个 `'1'` 开始，使用 DFS 将与其相连的所有 `'1'` 都标记为 `'0'`，表示这些部分已经被访问过。

   - 继续遍历下一个位置，直到网格遍历完毕。

3. 计数：每次执行 DFS 后，岛屿的数量加 1。

4. 最终结果：遍历完整个网格后，返回岛屿的总数量。

### 参考代码

#### C++

```
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    // 计算岛屿的数量
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;

        int num_islands = 0;  // 记录岛屿数量
        int rows = grid.size();  // 网格的行数
        int cols = grid[0].size();  // 网格的列数

        // 遍历网格中的每一个位置
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                // 如果当前位置是'1'，则表示找到一个新的岛屿
                if (grid[i][j] == '1') {
                    ++num_islands;  // 岛屿数量加1
                    dfs(grid, i, j);  // 使用DFS将与此'1'相连的所有'1'都标记为'0'
                }
            }
        }

        return num_islands;  // 返回岛屿的数量
    }

private:
    // 深度优先搜索，将相连的'1'全部标记为'0'
    void dfs(vector<vector<char>>& grid, int i, int j) {
        int rows = grid.size();
        int cols = grid[0].size();

        // 如果越界或者当前位置不是'1'，直接返回
        if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] != '1') {
            return;
        }

        grid[i][j] = '0';  // 将当前'1'标记为'0'，表示已访问

        // 递归访问当前位置的上下左右四个方向
        dfs(grid, i + 1, j);  // 下
        dfs(grid, i - 1, j);  // 上
        dfs(grid, i, j + 1);  // 右
        dfs(grid, i, j - 1);  // 左
    }
};

// 测试函数
int main() {
    Solution solution;

    vector<vector<char>> grid1 = {
        {'1','1','1','1','0'},
        {'1','1','0','1','0'},
        {'1','1','0','0','0'},
        {'0','0','0','0','0'}
    };

    vector<vector<char>> grid2 = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'}
    };

    cout << "Grid 1岛屿数量: " << solution.numIslands(grid1) << endl;  // 输出: 1
    cout << "Grid 2岛屿数量: " << solution.numIslands(grid2) << endl;  // 输出: 3

    return 0;
}
```

#### Java

```
class Solution {
    public int numIslands(char[][] grid) {
        // 如果网格为空，直接返回0
        if (grid == null || grid.length == 0) {
            return 0;
        }

        int numIslands = 0;
        int rows = grid.length;
        int cols = grid[0].length;

        // 遍历每个单元格
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // 如果当前单元格是'1'，则启动DFS
                if (grid[i][j] == '1') {
                    numIslands++; // 发现一个新的岛屿
                    dfs(grid, i, j); // 将与该'1'连接的所有'1'标记为'0'
                }
            }
        }

        return numIslands; // 返回岛屿的总数量
    }

    // 深度优先搜索函数，用于标记已访问的陆地
    private void dfs(char[][] grid, int i, int j) {
        int rows = grid.length;
        int cols = grid[0].length;

        // 如果越界或者当前单元格不是'1'，直接返回
        if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] != '1') {
            return;
        }

        // 将当前'1'标记为'0'，表示已访问
        grid[i][j] = '0';

        // 递归访问上下左右四个方向的邻接单元格
        dfs(grid, i + 1, j); // 下
        dfs(grid, i - 1, j); // 上
        dfs(grid, i, j + 1); // 右
        dfs(grid, i, j - 1); // 左
    }

    // 测试代码
    public static void main(String[] args) {
        Solution solution = new Solution();

        char[][] grid1 = {
            {'1', '1', '1', '1', '0'},
            {'1', '1', '0', '1', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '0', '0', '0'}
        };

        char[][] grid2 = {
            {'1', '1', '0', '0', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '1', '0', '0'},
            {'0', '0', '0', '1', '1'}
        };

        System.out.println("Grid 1岛屿数量: " + solution.numIslands(grid1)); // 输出: 1
        System.out.println("Grid 2岛屿数量: " + solution.numIslands(grid2)); // 输出: 3
    }
}
```

#### Python

```
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            # 如果越界或当前单元格不是'1'，直接返回
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return

            grid[i][j] = '0'  # 将当前'1'标记为'0'，表示已访问

            # 递归访问当前位置的上下左右四个方向
            dfs(i + 1, j)  # 下
            dfs(i - 1, j)  # 上
            dfs(i, j + 1)  # 右
            dfs(i, j - 1)  # 左

        # 遍历每个单元格
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':  # 如果当前单元格是'1'，则表示找到一个新的岛屿
                    num_islands += 1  # 岛屿数量加1
                    dfs(i, j)  # 使用DFS将与此'1'相连的所有'1'都标记为'0'

        return num_islands

# 测试代码
if __name__ == "__main__":
    solution = Solution()

    grid1 = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]

    grid2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]

    print("Grid 1岛屿数量:", solution.numIslands(grid1))  # 输出: 1
    print("Grid 2岛屿数量:", solution.numIslands(grid2))  # 输出: 3
```

