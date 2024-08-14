# 面试经典算法题90-生命游戏

LeetCode.289

### 问题描述

根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 `m × n` 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： `1` 即为活细胞 （live），或 `0` 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
2. 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 `m x n` 网格面板 `board` 的当前状态，返回下一个状态。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/grid1.jpg)

```
输入：board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
输出：[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/grid2.jpg)

```
输入：board = [[1,1],[1,0]]
输出：[[1,1],[1,1]]
```

### 思路

1. 定义问题：给定一个 `m x n` 的二维网格，表示一个细胞自动机的状态。每个细胞的状态是 `0`（死）或 `1`（活）。根据康威的四条生存定律，计算并返回该网格的下一个状态。

2. 生存定律：

   - 活细胞周围少于两个活细胞：死亡

   - 活细胞周围有两个或三个活细胞：存活

   - 活细胞周围超过三个活细胞：死亡

   - 死细胞周围正好有三个活细胞：复活

3. 实现步骤：

   - 拷贝网格：创建原始网格的拷贝，防止在更新过程中修改原始数据。

   - 遍历网格：遍历网格中的每个细胞，计算其周围活细胞的数量。

   - 更新状态：根据生存定律，更新每个细胞的状态。

   - 更新结果：输出更新后的网格状态。

### 参考代码

#### C++

```
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        
        // 定义方向数组，表示8个相邻位置的相对坐标
        vector<vector<int>> directions = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
        
        // 创建一个拷贝的网格，用于记录初始状态
        vector<vector<int>> copy = board;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int liveNeighbors = 0;
                
                // 计算周围活细胞的数量
                for (auto dir : directions) {
                    int ni = i + dir[0];
                    int nj = j + dir[1];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n && copy[ni][nj] == 1) {
                        liveNeighbors++;
                    }
                }
                
                // 根据生存定律更新细胞状态
                if (copy[i][j] == 1) {
                    if (liveNeighbors < 2 || liveNeighbors > 3) {
                        board[i][j] = 0; // 活细胞死亡
                    }
                } else {
                    if (liveNeighbors == 3) {
                        board[i][j] = 1; // 死细胞复活
                    }
                }
            }
        }
    }

    void printBoard(vector<vector<int>>& board) {
        for (const auto& row : board) {
            for (int cell : row) {
                cout << cell << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    Solution solution;
    
    // 示例 1
    vector<vector<int>> board1 = {
        {0, 1, 0},
        {0, 0, 1},
        {1, 1, 1},
        {0, 0, 0}
    };
    cout << "Original board 1:" << endl;
    solution.printBoard(board1);
    solution.gameOfLife(board1);
    cout << "Next state board 1:" << endl;
    solution.printBoard(board1);
    
    // 示例 2
    vector<vector<int>> board2 = {
        {1, 1},
        {1, 0}
    };
    cout << "Original board 2:" << endl;
    solution.printBoard(board2);
    solution.gameOfLife(board2);
    cout << "Next state board 2:" << endl;
    solution.printBoard(board2);
    
    return 0;
}
```

#### Java

```
public class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;

        // 定义方向数组，表示8个相邻位置的相对坐标
        int[][] directions = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

        // 创建一个拷贝的网格，用于记录初始状态
        int[][] copy = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                copy[i][j] = board[i][j];
            }
        }

        // 遍历每个细胞
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int liveNeighbors = 0;

                // 计算周围活细胞的数量
                for (int[] dir : directions) {
                    int ni = i + dir[0];
                    int nj = j + dir[1];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n && copy[ni][nj] == 1) {
                        liveNeighbors++;
                    }
                }

                // 根据生存定律更新细胞状态
                if (copy[i][j] == 1) {
                    if (liveNeighbors < 2 || liveNeighbors > 3) {
                        board[i][j] = 0; // 活细胞死亡
                    }
                } else {
                    if (liveNeighbors == 3) {
                        board[i][j] = 1; // 死细胞复活
                    }
                }
            }
        }
    }

    // 辅助函数：打印网格
    public void printBoard(int[][] board) {
        for (int[] row : board) {
            for (int cell : row) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 示例 1
        int[][] board1 = {
            {0, 1, 0},
            {0, 0, 1},
            {1, 1, 1},
            {0, 0, 0}
        };
        System.out.println("Original board 1:");
        solution.printBoard(board1);
        solution.gameOfLife(board1);
        System.out.println("Next state board 1:");
        solution.printBoard(board1);

        // 示例 2
        int[][] board2 = {
            {1, 1},
            {1, 0}
        };
        System.out.println("Original board 2:");
        solution.printBoard(board2);
        solution.gameOfLife(board2);
        System.out.println("Next state board 2:");
        solution.printBoard(board2);
    }
}
```

#### Python

```
def game_of_life(board):
    """
    更新 board 到其下一个状态。
    
    :param board: List[List[int]]，二维数组，表示当前的细胞状态
    """
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])
    
    # 定义方向数组，表示8个相邻位置的相对坐标
    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),         (0, 1), 
                  (1, -1), (1, 0), (1, 1)]
    
    # 创建一个拷贝的网格，用于记录初始状态
    copy_board = [row[:] for row in board]
    
    # 遍历每个细胞
    for i in range(m):
        for j in range(n):
            live_neighbors = 0
            
            # 计算周围活细胞的数量
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < m and 0 <= nj < n and copy_board[ni][nj] == 1:
                    live_neighbors += 1
            
            # 根据生存定律更新细胞状态
            if copy_board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = 0  # 活细胞死亡
            else:
                if live_neighbors == 3:
                    board[i][j] = 1  # 死细胞复活

def print_board(board):
    """
    打印网格。
    
    :param board: List[List[int]]，二维数组，表示当前的细胞状态
    """
    for row in board:
        print(" ".join(map(str, row)))
    print()

if __name__ == "__main__":
    # 示例 1
    board1 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    print("Original board 1:")
    print_board(board1)
    game_of_life(board1)
    print("Next state board 1:")
    print_board(board1)

    # 示例 2
    board2 = [
        [1, 1],
        [1, 0]
    ]
    print("Original board 2:")
    print_board(board2)
    game_of_life(board2)
    print("Next state board 2:")
    print_board(board2)
```

