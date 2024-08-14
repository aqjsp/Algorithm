# 面试经典算法题88-旋转图像

LeetCode.48

### 问题描述

给定一个 n × n 的二维矩阵 `matrix` 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在**[ 原地](https://baike.baidu.com/item/原地算法)** 旋转图像，这意味着你需要直接修改输入的二维矩阵。**请不要** 使用另一个矩阵来旋转图像。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/mat1.jpg)

```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/mat2.jpg)

```
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

### 思路

1. 转置矩阵：转置矩阵是指将矩阵的行和列互换，即将元素 matrix[i][j] 变为 matrix[j][i]。
2. 翻转每一行：将每一行的元素顺序颠倒，这样就实现了顺时针旋转 90 度的效果。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

void rotate(vector<vector<int>>& matrix) {
    int n = matrix.size();

    // 1. 转置矩阵
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }

    // 2. 翻转每一行
    for (int i = 0; i < n; ++i) {
        reverse(matrix[i].begin(), matrix[i].end());
    }
}

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
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    cout << "原始矩阵:" << endl;
    printMatrix(matrix1);
    
    rotate(matrix1);
    cout << "顺时针旋转90度后的矩阵:" << endl;
    printMatrix(matrix1);

    vector<vector<int>> matrix2 = {
        {5, 1, 9, 11},
        {2, 4, 8, 10},
        {13, 3, 6, 7},
        {15, 14, 12, 16}
    };
    cout << "原始矩阵:" << endl;
    printMatrix(matrix2);

    rotate(matrix2);
    cout << "顺时针旋转90度后的矩阵:" << endl;
    printMatrix(matrix2);

    return 0;
}
```

#### Java

```
import java.util.Arrays;

public class RotateImage {
    public static void rotate(int[][] matrix) {
        int n = matrix.length;

        // 1. 转置矩阵
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // 2. 翻转每一行
        for (int i = 0; i < n; ++i) {
            reverseRow(matrix[i]);
        }
    }

    // 辅助函数：翻转数组的一行
    private static void reverseRow(int[] row) {
        int left = 0, right = row.length - 1;
        while (left < right) {
            int temp = row[left];
            row[left] = row[right];
            row[right] = temp;
            left++;
            right--;
        }
    }

    // 辅助函数：打印矩阵
    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }

    public static void main(String[] args) {
        int[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        System.out.println("原始矩阵:");
        printMatrix(matrix1);
        
        rotate(matrix1);
        System.out.println("顺时针旋转 90 度后的矩阵:");
        printMatrix(matrix1);

        int[][] matrix2 = {
            {5, 1, 9, 11},
            {2, 4, 8, 10},
            {13, 3, 6, 7},
            {15, 14, 12, 16}
        };
        System.out.println("原始矩阵:");
        printMatrix(matrix2);
        
        rotate(matrix2);
        System.out.println("顺时针旋转 90 度后的矩阵:");
        printMatrix(matrix2);
    }
}
```

#### Python

```
from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    # 1. 转置矩阵
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. 翻转每一行
    for i in range(n):
        matrix[i].reverse()

# 辅助函数：打印矩阵
def print_matrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)

# 测试代码
if __name__ == "__main__":
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("原始矩阵:")
    print_matrix(matrix1)
    
    rotate(matrix1)
    print("顺时针旋转 90 度后的矩阵:")
    print_matrix(matrix1)

    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    print("原始矩阵:")
    print_matrix(matrix2)
    
    rotate(matrix2)
    print("顺时针旋转 90 度后的矩阵:")
    print_matrix(matrix2)
```

