# 面试经典算法题87-螺旋矩阵

LeetCode.54

### 问题描述

给你一个 `m` 行 `n` 列的矩阵 `matrix` ，请按照 **顺时针螺旋顺序** ，返回矩阵中的所有元素。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/image-20240731231208763.png)

```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/image-20240731231223139.png)

```
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
```

### 思路

1. 定义边界：初始化矩阵的四个边界：上边界 `top`，下边界 `bottom`，左边界 `left`，右边界 `right`。

2. 按顺时针方向遍历矩阵元素：

   - 从左到右遍历上边界，之后上边界下移。

   - 从上到下遍历右边界，之后右边界左移。

   - 从右到左遍历下边界，之后下边界上移。

   - 从下到上遍历左边界，之后左边界右移。

3. 边界检查：

   - 每次遍历后更新边界并检查是否越界。

   - 如果 `top > bottom` 或 `left > right`，则遍历结束。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return {};

    vector<int> result;
    int top = 0, bottom = matrix.size() - 1;
    int left = 0, right = matrix[0].size() - 1;

    while (top <= bottom && left <= right) {
        // 从左到右遍历上边界
        for (int i = left; i <= right; ++i) {
            result.push_back(matrix[top][i]);
        }
        ++top;

        // 从上到下遍历右边界
        for (int i = top; i <= bottom; ++i) {
            result.push_back(matrix[i][right]);
        }
        --right;

        if (top <= bottom) {
            // 从右到左遍历下边界
            for (int i = right; i >= left; --i) {
                result.push_back(matrix[bottom][i]);
            }
            --bottom;
        }

        if (left <= right) {
            // 从下到上遍历左边界
            for (int i = bottom; i >= top; --i) {
                result.push_back(matrix[i][left]);
            }
            ++left;
        }
    }

    return result;
}

int main() {
    vector<vector<int>> matrix = {{1, 2, 3},
                                  {4, 5, 6},
                                  {7, 8, 9}};
    
    vector<int> result = spiralOrder(matrix);
    cout << "顺时针螺旋顺序输出矩阵中的所有元素: ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
```

#### Java

```
import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
    public static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }

        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            // 从左到右遍历上边界
            for (int i = left; i <= right; i++) {
                result.add(matrix[top][i]);
            }
            top++;

            // 从上到下遍历右边界
            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;

            if (top <= bottom) {
                // 从右到左遍历下边界
                for (int i = right; i >= left; i--) {
                    result.add(matrix[bottom][i]);
                }
                bottom--;
            }

            if (left <= right) {
                // 从下到上遍历左边界
                for (int i = bottom; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
                left++;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[][] matrix1 = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };
        System.out.println("顺时针螺旋顺序输出矩阵中的所有元素: " + spiralOrder(matrix1));

        int[][] matrix2 = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12}
        };
        System.out.println("顺时针螺旋顺序输出矩阵中的所有元素: " + spiralOrder(matrix2));
    }
}
```

#### Python

```
def spiralOrder(matrix):
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # 从左到右遍历上边界
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # 从上到下遍历右边界
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # 从右到左遍历下边界
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # 从下到上遍历左边界
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# 示例
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("顺时针螺旋顺序输出矩阵中的所有元素:", spiralOrder(matrix1))

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print("顺时针螺旋顺序输出矩阵中的所有元素:", spiralOrder(matrix2))
```

