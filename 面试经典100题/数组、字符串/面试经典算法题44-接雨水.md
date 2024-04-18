# 面试经典算法题44-接雨水

LeetCode.42

### 问题描述

给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

**示例 1：**

![img](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202404172001285.png)

```
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
```

**示例 2：**

```
输入：height = [4,2,0,3,2,5]
输出：9
```

### 思路

1. **首先，找到每个柱子能接的雨水量。**
   我们可以观察到，每个柱子上方能够存储的雨水量取决于该柱子左侧最高柱子的高度（left_max）和右侧最高柱子的高度（right_max）中较小的那个。这是因为雨水的高度不能超过两侧最高柱子中较小的那个。

2. **为了找到每个柱子左侧和右侧的最高柱子，我们可以使用两个辅助数组来保存这些信息。**
   一个数组 `left_max`，用于保存每个柱子左侧最高柱子的高度。从左向右遍历数组，更新 `left_max[i]` 为 `max(height[i], left_max[i - 1])`，其中 `height[i]` 是当前柱子的高度。

   同样，另一个数组 `right_max` 用于保存每个柱子右侧最高柱子的高度。从右向左遍历数组，更新 `right_max[i]` 为 `max(height[i], right_max[i + 1])`，其中 `height[i]` 是当前柱子的高度。

3. **遍历每个柱子，计算该柱子能接的雨水量。**
   对于每个柱子，其能接的雨水量为 `min(left_max[i], right_max[i]) - height[i]`，其中 `height[i]` 是当前柱子的高度。如果该值为正，则说明当前柱子能够接到雨水，将其累加到总雨水量中。

4. **返回总雨水量作为结果。**

### 图解

```
                 +-------------------------+
                 |      开始执行程序         |
                 +-------------------------+
                             |
                             v
    +------------------------------------------------------+
    |     初始化变量                                         |
    |     left_max = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  |
    |     right_max = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
    |     total_water = 0                                  |
    +------------------------------------------------------+
                             |
                             v
            +----------------------------------+
            |     计算 left_max                 |
            |     left_max[0] = 0              |
            |     left_max[1] = max(0, 1) = 1  |
            |     left_max[2] = max(1, 0) = 1  |
            |     left_max[3] = max(1, 2) = 2  |
            |     left_max[4] = max(2, 1) = 2  |
            |     left_max[5] = max(2, 0) = 2  |
            |     left_max[6] = max(2, 1) = 2  |
            |     left_max[7] = max(2, 3) = 3  |
            |     left_max[8] = max(3, 2) = 3  |
            |     left_max[9] = max(3, 1) = 3  |
            |     left_max[10] = max(3, 2) = 3 |
            |     left_max[11] = max(3, 1) = 3 |
            +----------------------------------+
                             |
                             v
            +-----------------------------------+
            |     计算 right_max                 |
            |     right_max[11] = 0             |
            |     right_max[10] = max(0, 1) = 1 |
            |     right_max[9] = max(1, 2) = 2  |
            |     right_max[8] = max(2, 1) = 2  |
            |     right_max[7] = max(2, 3) = 3  |
            |     right_max[6] = max(3, 1) = 3  |
            |     right_max[5] = max(3, 2) = 3  |
            |     right_max[4] = max(3, 1) = 3  |
            |     right_max[3] = max(3, 2) = 3  |
            |     right_max[2] = max(3, 1) = 3  |
            |     right_max[1] = max(3, 2) = 3  |
            |     right_max[0] = max(3, 0) = 3  |
            +-----------------------------------+
                             |
                             v
+-----------------------------------------------------------------+
|     计算总雨水量                                                  |
|     i = 0: water = min(3, 0) - 0 = 0                            |
|     i = 1: water = min(1, 3) - 1 = 0                            |
|     i = 2: water = min(1, 3) - 0 = 1                            |
|     i = 3: water = min(2, 3) - 2 = 0                            |
|     i = 4: water = min(2, 3) - 1 = 1                            |
|     i = 5: water = min(2, 3) - 0 = 2                            |
|     i = 6: water = min(2, 3) - 1 = 1                            |
|     i = 7: water = min(3, 3) - 3 = 0                            |
|     i = 8: water = min(3, 3) - 2 = 1                            |
|     i = 9: water = min(3, 2) - 1 = 1                            |
|     i = 10: water = min(3, 1) - 2 = 0                           |
|     i = 11: water = min(3, 0) - 1 = 0                           |
|     总雨水量 = 0 + 0 + 1 + 0 + 1 + 2 + 1 + 0 + 1 + 1 + 0 + 0 = 6  |
+-----------------------------------------------------------------+
                             |
                             v
                +-------------------------+
                |     输出结果             |
                |     能接的雨水量：6       |
                +-------------------------+
```



### 参考代码

#### C++

```
#include <iostream>
#include <vector>

int trap(std::vector<int>& height) {
    int n = height.size();
    if (n == 0) return 0;

    std::vector<int> left_max(n); // 保存每个柱子左侧最高柱子的高度
    std::vector<int> right_max(n); // 保存每个柱子右侧最高柱子的高度

    // 初始化左侧最高柱子数组
    left_max[0] = height[0];
    for (int i = 1; i < n; ++i) {
        left_max[i] = std::max(left_max[i - 1], height[i]);
    }

    // 初始化右侧最高柱子数组
    right_max[n - 1] = height[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        right_max[i] = std::max(right_max[i + 1], height[i]);
    }

    int total_water = 0; // 总雨水量

    // 计算每个柱子能接的雨水量
    for (int i = 0; i < n; ++i) {
        int water = std::min(left_max[i], right_max[i]) - height[i];
        if (water > 0) {
            total_water += water;
        }
    }

    return total_water;
}

int main() {
    std::vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    int result = trap(height);
    std::cout << "能接的雨水量：" << result << std::endl;
    return 0;
}
```

#### Java

```
import java.util.Arrays;

public class Main {
    public static int trap(int[] height) {
        int n = height.length;
        if (n == 0) return 0;

        int[] left_max = new int[n]; // 保存每个柱子左侧最高柱子的高度
        int[] right_max = new int[n]; // 保存每个柱子右侧最高柱子的高度

        // 初始化左侧最高柱子数组
        left_max[0] = height[0];
        for (int i = 1; i < n; ++i) {
            left_max[i] = Math.max(left_max[i - 1], height[i]);
        }

        // 初始化右侧最高柱子数组
        right_max[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            right_max[i] = Math.max(right_max[i + 1], height[i]);
        }

        int total_water = 0; // 总雨水量

        // 计算每个柱子能接的雨水量
        for (int i = 0; i < n; ++i) {
            int water = Math.min(left_max[i], right_max[i]) - height[i];
            if (water > 0) {
                total_water += water;
            }
        }

        return total_water;
    }

    public static void main(String[] args) {
        int[] height = {0,1,0,2,1,0,1,3,2,1,2,1};
        int result = trap(height);
        System.out.println("能接的雨水量：" + result);
    }
}
```

#### Python

```
def trap(height):
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n  # 保存每个柱子左侧最高柱子的高度
    right_max = [0] * n  # 保存每个柱子右侧最高柱子的高度

    # 初始化左侧最高柱子数组
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # 初始化右侧最高柱子数组
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    total_water = 0  # 总雨水量

    # 计算每个柱子能接的雨水量
    for i in range(n):
        water = min(left_max[i], right_max[i]) - height[i]
        if water > 0:
            total_water += water

    return total_water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = trap(height)
print("能接的雨水量：", result)
```

