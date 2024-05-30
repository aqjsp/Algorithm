# 面试经典算法题54-搜索二维矩阵

LeetCode.74

### 问题描述

给你一个满足下述两条属性的 `m x n` 整数矩阵：

- 每行中的整数从左到右按非严格递增顺序排列。
- 每行的第一个整数大于前一行的最后一个整数。

给你一个整数 `target` ，如果 `target` 在矩阵中，返回 `true` ；否则，返回 `false` 。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405302354959.jpeg)

```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405302353531.jpeg)

```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
```

### 流程图

![流程图](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405310024033.png)

### 思路分析

1. **矩阵的特性**：
   - 每行中的整数从左到右按非严格递增顺序排列。
   - 每行的第一个整数大于前一行的最后一个整数。
   - 因此，整个矩阵可以视为一个一维有序数组。
2. **转换成一维数组**：
   - 我们可以将矩阵视为一个长度为 𝑚×𝑛的一维有序数组。
   - 对于一维数组中的索引 𝑖，对应矩阵中的位置为 (𝑖/𝑛,𝑖%𝑛)，其中 / 表示整数除法， % 表示取模运算。
3. **二分查找**：
   - 利用二分查找在一维有序数组中搜索目标值，这样可以在 𝑂(log⁡(𝑚×𝑛))的时间复杂度内完成搜索。

### 具体步骤

1. **初始化变量**：
   - 获取矩阵的行数 𝑚 和列数 𝑛。
   - 初始化左指针 𝑙𝑒𝑓𝑡=0 和右指针 𝑟𝑖𝑔ℎ𝑡=𝑚×𝑛−1，表示整个一维数组的范围。
2. **进行二分查找**：
   - 在左指针小于等于右指针的条件下进入循环。
   - 计算中间位置 𝑚𝑖𝑑，防止溢出使用 𝑚𝑖𝑑=𝑙𝑒𝑓𝑡+(𝑟𝑖𝑔ℎ𝑡−𝑙𝑒𝑓𝑡)/2。
   - 将中间位置的索引转换为矩阵中的行列坐标：
     - 行索引 𝑟𝑜𝑤=𝑚𝑖𝑑/𝑛
     - 列索引 𝑐𝑜𝑙=𝑚𝑖𝑑
   - 获取中间位置的值 𝑚𝑖𝑑_𝑣𝑎𝑙𝑢𝑒=𝑚𝑎𝑡𝑟𝑖𝑥 [row] [𝑐𝑜𝑙]。
3. **比较中间值和目标值**：
   - 如果中间值等于目标值，返回 true。
   - 如果中间值小于目标值，目标值在右半部分，移动左指针 𝑙𝑒𝑓𝑡=𝑚𝑖𝑑+1。
   - 如果中间值大于目标值，目标值在左半部分，移动右指针 𝑟𝑖𝑔ℎ𝑡=𝑚𝑖𝑑−1。
4. **返回结果**：
   - 如果循环结束后仍未找到目标值，返回 false。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

// 函数声明，接收一个二维矩阵和一个目标值，返回是否在矩阵中找到目标值
bool searchMatrix(const vector<vector<int>>& matrix, int target) {
    // 获取矩阵的行数和列数
    int m = matrix.size();
    int n = matrix[0].size();
    // 初始化左指针为0，右指针为矩阵元素的总数减1
    int left = 0;
    int right = m * n - 1;

    // 开始二分查找
    while (left <= right) {
        // 计算中间位置，防止(left + right)可能产生的溢出
        int mid = left + (right - left) / 2;
        // 将中间位置的索引转换为矩阵中的行列位置
        int row = mid / n;
        int col = mid % n;
        int mid_value = matrix[row][col];

        // 如果中间值等于目标值，返回true
        if (mid_value == target) {
            return true;
        } 
        // 如果中间值小于目标值，说明目标值在右半部分，移动左指针
        else if (mid_value < target) {
            left = mid + 1;
        } 
        // 如果中间值大于目标值，说明目标值在左半部分，移动右指针
        else {
            right = mid - 1;
        }
    }

    // 如果没有找到目标值，返回false
    return false;
}

// 主函数，用于测试
int main() {
    // 测试用例1
    vector<vector<int>> matrix1 = {
        {1, 3, 5, 7},
        {10, 11, 16, 20},
        {23, 30, 34, 60}
    };
    int target1 = 3;
    // 输出结果，目标值在矩阵中，输出true
    cout << (searchMatrix(matrix1, target1) ? "true" : "false") << endl;

    // 测试用例2
    vector<vector<int>> matrix2 = {
        {1, 3, 5, 7},
        {10, 11, 16, 20},
        {23, 30, 34, 60}
    };
    int target2 = 13;
    // 输出结果，目标值不在矩阵中，输出false
    cout << (searchMatrix(matrix2, target2) ? "true" : "false") << endl;

    return 0;
}
```

#### Java

```
import java.util.Arrays;

public class SearchMatrix {
    // 函数声明，接收一个二维矩阵和一个目标值，返回是否在矩阵中找到目标值
    public boolean searchMatrix(int[][] matrix, int target) {
        // 获取矩阵的行数和列数
        int m = matrix.length;
        int n = matrix[0].length;
        // 初始化左指针为0，右指针为矩阵元素的总数减1
        int left = 0;
        int right = m * n - 1;

        // 开始二分查找
        while (left <= right) {
            // 计算中间位置，防止(left + right)可能产生的溢出
            int mid = left + (right - left) / 2;
            // 将中间位置的索引转换为矩阵中的行列位置
            int row = mid / n;
            int col = mid % n;
            int midValue = matrix[row][col];

            // 如果中间值等于目标值，返回true
            if (midValue == target) {
                return true;
            } 
            // 如果中间值小于目标值，说明目标值在右半部分，移动左指针
            else if (midValue < target) {
                left = mid + 1;
            } 
            // 如果中间值大于目标值，说明目标值在左半部分，移动右指针
            else {
                right = mid - 1;
            }
        }

        // 如果没有找到目标值，返回false
        return false;
    }

    // 主函数，用于测试
    public static void main(String[] args) {
        SearchMatrix sm = new SearchMatrix();

        // 测试用例1
        int[][] matrix1 = {
            {1, 3, 5, 7},
            {10, 11, 16, 20},
            {23, 30, 34, 60}
        };
        int target1 = 3;
        // 输出结果，目标值在矩阵中，输出true
        System.out.println(sm.searchMatrix(matrix1, target1));  // 输出 true

        // 测试用例2
        int[][] matrix2 = {
            {1, 3, 5, 7},
            {10, 11, 16, 20},
            {23, 30, 34, 60}
        };
        int target2 = 13;
        // 输出结果，目标值不在矩阵中，输出false
        System.out.println(sm.searchMatrix(matrix2, target2));  // 输出 false
    }
}
```

#### Python

```
def searchMatrix(matrix, target):
    """
    在二维矩阵中查找目标值

    :param matrix: List[List[int]]，二维矩阵
    :param target: int，目标值
    :return: bool，目标值是否在矩阵中
    """
    # 获取矩阵的行数和列数
    m = len(matrix)
    n = len(matrix[0])
    
    # 初始化左指针为0，右指针为矩阵元素的总数减1
    left = 0
    right = m * n - 1

    # 开始二分查找
    while left <= right:
        # 计算中间位置，防止(left + right)可能产生的溢出
        mid = left + (right - left) // 2
        
        # 将中间位置的索引转换为矩阵中的行列位置
        row = mid // n
        col = mid % n
        mid_value = matrix[row][col]

        # 如果中间值等于目标值，返回True
        if mid_value == target:
            return True
        # 如果中间值小于目标值，说明目标值在右半部分，移动左指针
        elif mid_value < target:
            left = mid + 1
        # 如果中间值大于目标值，说明目标值在左半部分，移动右指针
        else:
            right = mid - 1

    # 如果没有找到目标值，返回False
    return False

# 主函数，用于测试
if __name__ == "__main__":
    # 测试用例1
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target1 = 3
    # 输出结果，目标值在矩阵中，输出True
    print(searchMatrix(matrix1, target1))  # 输出 True

    # 测试用例2
    matrix2 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target2 = 13
    # 输出结果，目标值不在矩阵中，输出False
    print(searchMatrix(matrix2, target2))  # 输出 False
```

