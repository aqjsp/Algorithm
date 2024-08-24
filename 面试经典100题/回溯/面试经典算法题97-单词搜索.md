# 面试经典算法题97-单词搜索

LeetCode.79

### 问题描述

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回 `false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/word2.jpg)

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/word-1.jpg)

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
```

**示例 3：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/word3.jpg)

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
```

### 思路

1. 回溯法：通过递归进行回溯，尝试匹配 `word` 中的每个字符，判断它们是否能按照给定规则在 `board` 中找到。

2. 递归搜索：

   - 从 `board` 中的每个字符作为起点，进行深度优先搜索 (DFS)，检查是否能顺利匹配 `word`。

   - 每次递归时，检查当前字符是否匹配目标字符，并移动到相邻的四个方向（上下左右）进行下一步匹配。

3. 终止条件：

   - 如果全部字符都匹配成功，则返回 `true`。

   - 如果当前字符不匹配或者已经越界，则回溯（即撤回上一步的选择）继续搜索。

4. 避免重复使用单元格：在搜索过程中，使用一个标记数组或暂时修改 `board` 上的字符来避免重复使用同一个单元格。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int rows = board.size();
        int cols = board[0].size();
        
        // 遍历每个字符，寻找匹配的起点
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

private:
    bool dfs(vector<vector<char>>& board, const string& word, int i, int j, int index) {
        // 匹配成功
        if (index == word.size()) return true;

        // 越界或字符不匹配，返回 false
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != word[index]) {
            return false;
        }

        // 保存当前字符
        char temp = board[i][j];
        // 标记该字符已被使用
        board[i][j] = '*';

        // 搜索四个方向
        bool found = dfs(board, word, i + 1, j, index + 1) ||
                     dfs(board, word, i - 1, j, index + 1) ||
                     dfs(board, word, i, j + 1, index + 1) ||
                     dfs(board, word, i, j - 1, index + 1);

        // 恢复当前字符
        board[i][j] = temp;
        return found;
    }
};

int main() {
    Solution solution;
    vector<vector<char>> board = {{'A','B','C','E'},
                                  {'S','F','C','S'},
                                  {'A','D','E','E'}};
    string word1 = "ABCCED";
    string word2 = "SEE";
    string word3 = "ABCB";

    // 输出结果
    cout << (solution.exist(board, word1) ? "true" : "false") << endl; // 输出 true
    cout << (solution.exist(board, word2) ? "true" : "false") << endl; // 输出 true
    cout << (solution.exist(board, word3) ? "true" : "false") << endl; // 输出 false

    return 0;
}
```

#### Java

```
class Solution {
    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;

        // 遍历网格中的每个单元格作为起点
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // 如果找到匹配的起点，返回 true
                if (dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false; // 如果未找到，返回 false
    }

    private boolean dfs(char[][] board, String word, int i, int j, int index) {
        // 如果所有字符都匹配，返回 true
        if (index == word.length()) {
            return true;
        }

        // 检查越界和字符匹配
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(index)) {
            return false;
        }

        // 临时保存当前字符，并标记为已访问
        char temp = board[i][j];
        board[i][j] = '*';

        // 在四个方向进行递归搜索
        boolean found = dfs(board, word, i + 1, j, index + 1) ||
                        dfs(board, word, i - 1, j, index + 1) ||
                        dfs(board, word, i, j + 1, index + 1) ||
                        dfs(board, word, i, j - 1, index + 1);

        // 恢复当前单元格的字符
        board[i][j] = temp;

        return found; // 返回结果
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        char[][] board = {
            {'A','B','C','E'},
            {'S','F','C','S'},
            {'A','D','E','E'}
        };

        String word1 = "ABCCED";
        String word2 = "SEE";
        String word3 = "ABCB";

        // 输出结果
        System.out.println(solution.exist(board, word1)); // 输出 true
        System.out.println(solution.exist(board, word2)); // 输出 true
        System.out.println(solution.exist(board, word3)); // 输出 false
    }
}
```

#### Python

```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # 定义DFS函数
        def dfs(i, j, index):
            # 如果所有字符都匹配，返回 True
            if index == len(word):
                return True
            
            # 检查越界或当前字符不匹配
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[index]:
                return False

            # 临时保存当前单元格的值，并标记为已访问
            temp = board[i][j]
            board[i][j] = '#'

            # 在四个方向进行递归搜索
            found = (dfs(i + 1, j, index + 1) or
                     dfs(i - 1, j, index + 1) or
                     dfs(i, j + 1, index + 1) or
                     dfs(i, j - 1, index + 1))

            # 恢复当前单元格的字符
            board[i][j] = temp

            return found

        # 从网格中的每个单元格作为起点进行搜索
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False

# 示例测试
if __name__ == "__main__":
    solution = Solution()

    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]

    word1 = "ABCCED"
    word2 = "SEE"
    word3 = "ABCB"

    # 输出结果
    print(solution.exist(board, word1))  # 输出: True
    print(solution.exist(board, word2))  # 输出: True
    print(solution.exist(board, word3))  # 输出: False
```

