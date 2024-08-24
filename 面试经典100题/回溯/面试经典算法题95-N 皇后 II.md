# 面试经典算法题95-N 皇后 II

LeetCode.52

### 问题描述

n 皇后问题 研究的是如何将 `n` 个皇后放置在 `n × n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回 n 皇后问题 不同的解决方案的数量。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/queens.jpg)

```
输入：n = 4
输出：2
解释：如上图所示，4 皇后问题存在两个不同的解法。
```

**示例 2：**

```
输入：n = 1
输出：1
```

### 思路

1. 定义递归回溯函数：

   - 创建一个递归函数 `backtrack`，用于尝试在每一行放置皇后。

   - 递归函数需要参数：当前行 `row`、用于标记列是否被占用的集合 `columns`、用于标记正对角线是否被占用的集合 `diagonals1`、用于标记反对角线是否被占用的集合 `diagonals2`。

2. 终止条件：如果当前行等于 `n`，表示已经成功放置了 `n` 个皇后，此时计数加一。

3. 递归回溯：

   - 对于每一行的每一列，检查该位置是否可以放置皇后。

   - 如果可以放置皇后，更新列和对角线的标记，并递归处理下一行。

   - 递归完成后，回溯：移除皇后，恢复列和对角线的标记。

4. 计算结果：

   - 初始化计数器 `count`，调用递归函数。

   - 最终返回计数器 `count` 的值，即不同解决方案的数量。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <unordered_set>

class Solution {
public:
    int totalNQueens(int n) {
        count = 0;
        std::unordered_set<int> columns;      // 用于标记列是否被占用
        std::unordered_set<int> diagonals1;   // 用于标记正对角线是否被占用
        std::unordered_set<int> diagonals2;   // 用于标记反对角线是否被占用
        backtrack(n, 0, columns, diagonals1, diagonals2);
        return count;
    }

private:
    int count;

    // 递归回溯函数
    void backtrack(int n, int row, std::unordered_set<int>& columns, std::unordered_set<int>& diagonals1, std::unordered_set<int>& diagonals2) {
        // 终止条件：如果当前行等于 n，表示已经成功放置了 n 个皇后
        if (row == n) {
            count++;
            return;
        }

        // 遍历当前行的每一列
        for (int col = 0; col < n; col++) {
            // 检查该位置是否可以放置皇后
            if (columns.count(col) || diagonals1.count(row - col) || diagonals2.count(row + col)) {
                continue;
            }

            // 放置皇后并更新标记
            columns.insert(col);
            diagonals1.insert(row - col);
            diagonals2.insert(row + col);

            // 递归处理下一行
            backtrack(n, row + 1, columns, diagonals1, diagonals2);

            // 回溯：移除皇后并恢复标记
            columns.erase(col);
            diagonals1.erase(row - col);
            diagonals2.erase(row + col);
        }
    }
};

int main() {
    Solution solution;
    int n = 4;  // 示例输入
    std::cout << "Number of solutions for " << n << " queens: " << solution.totalNQueens(n) << std::endl;
    return 0;
}
```

#### Java

```
import java.util.HashSet;
import java.util.Set;

public class NQueens {
    private int count;

    public int totalNQueens(int n) {
        count = 0;
        Set<Integer> columns = new HashSet<>();      // 用于标记列是否被占用
        Set<Integer> diagonals1 = new HashSet<>();   // 用于标记正对角线是否被占用
        Set<Integer> diagonals2 = new HashSet<>();   // 用于标记反对角线是否被占用
        backtrack(n, 0, columns, diagonals1, diagonals2);
        return count;
    }

    private void backtrack(int n, int row, Set<Integer> columns, Set<Integer> diagonals1, Set<Integer> diagonals2) {
        // 终止条件：如果当前行等于 n，表示已经成功放置了 n 个皇后
        if (row == n) {
            count++;
            return;
        }

        // 遍历当前行的每一列
        for (int col = 0; col < n; col++) {
            // 检查该位置是否可以放置皇后
            if (columns.contains(col) || diagonals1.contains(row - col) || diagonals2.contains(row + col)) {
                continue;
            }

            // 放置皇后并更新标记
            columns.add(col);
            diagonals1.add(row - col);
            diagonals2.add(row + col);

            // 递归处理下一行
            backtrack(n, row + 1, columns, diagonals1, diagonals2);

            // 回溯：移除皇后并恢复标记
            columns.remove(col);
            diagonals1.remove(row - col);
            diagonals2.remove(row + col);
        }
    }

    public static void main(String[] args) {
        NQueens solution = new NQueens();
        int n = 4;  // 示例输入
        System.out.println("Number of solutions for " + n + " queens: " + solution.totalNQueens(n));
    }
}
```

#### Python

```
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int) -> None:
            # 终止条件：如果当前行等于 n，表示已经成功放置了 n 个皇后
            if row == n:
                self.count += 1
                return
            
            # 遍历当前行的每一列
            for col in range(n):
                if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue
                
                # 放置皇后并更新标记
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)
                
                # 递归处理下一行
                backtrack(row + 1)
                
                # 回溯：移除皇后并恢复标记
                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)
        
        self.count = 0
        columns = set()      # 用于标记列是否被占用
        diagonals1 = set()   # 用于标记正对角线是否被占用
        diagonals2 = set()   # 用于标记反对角线是否被占用
        backtrack(0)
        return self.count

# 示例运行
solution = Solution()
n = 4  # 示例输入
print("Number of solutions for {} queens: {}".format(n, solution.totalNQueens(n)))
```

