# 面试经典算法题45-分发糖果

LeetCode.135

### 问题描述

`n` 个孩子站成一排。给你一个整数数组 `ratings` 表示每个孩子的评分。你需要按照以下要求，给这些孩子分发糖果：

- 每个孩子至少分配到 `1` 个糖果。
- 相邻两个孩子评分更高的孩子会获得更多的糖果。

请你给每个孩子分发糖果，计算并返回需要准备的 **最少糖果数目** 。

**示例 1：**

```
输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
```

**示例 2：**

```
输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
```

### 思路

1. **初始化变量**：首先，我们初始化一个数组 `candies`，用来存储每个孩子分配的糖果数量，将数组的所有元素都设为1，表示每个孩子至少有一个糖果。
2. **从左到右遍历**：我们从数组的第二个元素开始向右遍历，对于每个孩子 `i`，如果他的评分比左边孩子的评分高，那么他应该比左边孩子获得更多糖果，因此我们更新 `candies[i] = candies[i - 1] + 1`。
3. **从右到左遍历**：接着，我们从倒数第二个元素开始向左遍历，对于每个孩子 `i`，如果他的评分比右边孩子的评分高，并且他当前的糖果数量不大于右边孩子的糖果数量，那么他应该比右边孩子获得更多糖果，因此我们更新 `candies[i] = std::max(candies[i], candies[i + 1] + 1)`。
4. **计算总糖果数**：最后，我们计算数组 `candies` 中所有元素的总和，这个总和就是我们需要准备的最少糖果数目。

### 图解

```
            +-------------------------+
            |      开始执行程序         |
            +-------------------------+
                         |
                         v
            +-------------------------+
            |     初始化变量            |
            |     ratings = [1, 0, 2] |
            |     candies = [1, 1, 1] |
            +-------------------------+
                         |
                         v
+-------------------------------------------------------+
|     从左到右遍历评分                                     |
|     i = 1: ratings[1] = 0,                            |
|     不增加糖果数量，candies = [1, 1, 1]                  |
|     i = 2: ratings[2] = 2, 比前一个孩子高，              |
|     增加糖果数量为前一个孩子糖果数量加1，candies = [1, 1, 2]|
+-------------------------------------------------------+
                         |
                         v
+-------------------------------------------------------+
|     从右到左遍历评分                                    |
|     i = 1: ratings[1] = 0, 比右边孩子高，               |
|     但糖果数量已经是1，不变，candies = [2, 1, 2]          |
|     i = 0: ratings[0] = 1, 比右边孩子高，               |
|     增加糖果数量为右边孩子糖果数量加1，candies = [2, 1, 2]  |
+-------------------------------------------------------+
                         |
                         v
          +-----------------------------+
          |     计算总糖果数              |
          |     candies = [2, 1, 2]     |
          |     总糖果数 = 2 + 1 + 2 = 5 |
          +-----------------------------+
                         |
                         v
            +---------------------------+
            |     输出结果               |
            |     需要准备的最少糖果数目：5 |
            +---------------------------+
```

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

int candy(std::vector<int>& ratings) {
    int n = ratings.size();
    if (n == 0) return 0;

    std::vector<int> candies(n, 1); // 初始化每个孩子至少分配一个糖果

    // 从左往右遍历，保证评分高的孩子获得更多糖果
    for (int i = 1; i < n; ++i) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }

    // 从右往左遍历，保证评分高的孩子获得更多糖果
    for (int i = n - 2; i >= 0; --i) {
        if (ratings[i] > ratings[i + 1]) {
            candies[i] = std::max(candies[i], candies[i + 1] + 1);
        }
    }

    // 计算总糖果数
    int total = 0;
    for (int candy : candies) {
        total += candy;
    }

    return total;
}

int main() {
    std::vector<int> ratings = {1, 0, 2};
    int result = candy(ratings);
    std::cout << "需要准备的最少糖果数目：" << result << std::endl;
    return 0;
}
```

#### Java

```
public class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        if (n == 0) return 0;

        int[] candies = new int[n]; // 初始化每个孩子至少分配一个糖果

        // 从左往右遍历，保证评分高的孩子获得更多糖果
        candies[0] = 1;
        for (int i = 1; i < n; ++i) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            } else {
                candies[i] = 1;
            }
        }

        // 从右往左遍历，保证评分高的孩子获得更多糖果
        int total = candies[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
            }
            total += candies[i];
        }

        return total;
    }

    public static void main(String[] args) {
        int[] ratings = {1, 0, 2};
        Solution solution = new Solution();
        int result = solution.candy(ratings);
        System.out.println("需要准备的最少糖果数目：" + result);
    }
}
```

#### Python

```
def candy(ratings):
    n = len(ratings)
    if n == 0:
        return 0

    candies = [1] * n  # 初始化每个孩子至少分配一个糖果

    # 从左往右遍历，保证评分高的孩子获得更多糖果
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # 从右往左遍历，保证评分高的孩子获得更多糖果
    total = candies[-1]
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
        total += candies[i]

    return total

ratings = [1, 0, 2]
result = candy(ratings)
print("需要准备的最少糖果数目：", result)
```

