# 面试经典算法题89-矩阵置零

LeetCode.73

### 问题描述

给定一个 `m x n` 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用原地算法。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/mat1.jpg)

```
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/mat2.jpg)

```
输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

### 思路

要将矩阵中包含 0 的行和列全部置零，可以采用一种高效的原地算法，避免使用额外的空间。

1. 第一遍遍历：
   - 使用矩阵的第一行和第一列作为标记行和标记列，记录哪些行和哪些列需要被置零。
   - 遍历矩阵，如果 `matrix[i][j]` 为 0，则将 `matrix[i][0]` 和 `matrix[0][j]` 置为 0 作为标记。
2. 第二遍遍历：使用标记行和标记列，根据标记将需要置零的行和列进行置零处理。
3. 特殊处理第一行和第一列：单独检查第一行和第一列是否需要被置零（因为它们是标记列和标记行），最后处理。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

void setZeroes(vector<vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    bool firstRowZero = false;
    bool firstColZero = false;

    // 1. 检查第一行和第一列是否有零
    for (int i = 0; i < m; ++i) {
        if (matrix[i][0] == 0) {
            firstColZero = true;
            break;
        }
    }
    for (int j = 0; j < n; ++j) {
        if (matrix[0][j] == 0) {
            firstRowZero = true;
            break;
        }
    }

    // 2. 使用第一行和第一列作为标记
    for (int i = 1; i < m; ++i) {
        for (int j = 1; j < n; ++j) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // 3. 根据标记将相应的行和列置零
    for (int i = 1; i < m; ++i) {
        for (int j = 1; j < n; ++j) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // 4. 处理第一行和第一列
    if (firstColZero) {
        for (int i = 0; i < m; ++i) {
            matrix[i][0] = 0;
        }
    }
    if (firstRowZero) {
        for (int j = 0; j < n; ++j) {
            matrix[0][j] = 0;
        }
    }
}

// 辅助函数：打印矩阵
void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
}

int main() {
    vector<vector<int>> matrix1 = {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1}
    };
    cout << "原始矩阵:" << endl;
    printMatrix(matrix1);

    setZeroes(matrix1);
    cout << "处理后的矩阵:" << endl;
    printMatrix(matrix1);

    vector<vector<int>> matrix2 = {
        {0, 1, 2, 0},
        {3, 4, 5, 2},
        {1, 3, 1, 5}
    };
    cout << "原始矩阵:" << endl;
    printMatrix(matrix2);

    setZeroes(matrix2);
    cout << "处理后的矩阵:" << endl;
    printMatrix(matrix2);

    return 0;
}
```

#### Java

```
public class SetMatrixZeroes {
    public static void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        boolean firstRowZero = false;
        boolean firstColZero = false;
        
        // 检查第一列是否有零
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
                break;
            }
        }
        
        // 检查第一行是否有零
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                firstRowZero = true;
                break;
            }
        }
        
        // 使用第一行和第一列记录需要置零的行和列
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        // 根据第一行和第一列的标记置零
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        
        // 如果第一列有零，则将整个第一列置零
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
        
        // 如果第一行有零，则将整个第一行置零
        if (firstRowZero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] matrix1 = {
            {1, 1, 1},
            {1, 0, 1},
            {1, 1, 1}
        };

        int[][] matrix2 = {
            {0, 1, 2, 0},
            {3, 4, 5, 2},
            {1, 3, 1, 5}
        };

        System.out.println("Original matrix 1:");
        printMatrix(matrix1);
        setZeroes(matrix1);
        System.out.println("Matrix 1 after setZeroes:");
        printMatrix(matrix1);

        System.out.println("Original matrix 2:");
        printMatrix(matrix2);
        setZeroes(matrix2);
        System.out.println("Matrix 2 after setZeroes:");
        printMatrix(matrix2);
    }
}
```

#### Python

```
def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    
    first_row_zero = False
    first_col_zero = False
    
    # 检查第一列是否有零
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    # 检查第一行是否有零
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_zero = True
            break
    
    # 使用第一行和第一列记录需要置零的行和列
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # 根据第一行和第一列的标记置零
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # 如果第一列有零，则将整个第一列置零
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
    
    # 如果第一行有零，则将整个第一行置零
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

matrix2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

print("Original matrix 1:")
printMatrix(matrix1)
setZeroes(matrix1)
print("Matrix 1 after setZeroes:")
printMatrix(matrix1)

print("Original matrix 2:")
printMatrix(matrix2)
setZeroes(matrix2)
print("Matrix 2 after setZeroes:")
printMatrix(matrix2)
```

