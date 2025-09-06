# 面试经典算法题73-爬楼梯

LeetCode.70

### 问题描述

假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。

每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？

**示例 1：**

```c++
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
```

**示例 2：**

```c++
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
```

### 思路

1. 定义状态：定义 `dp[i]` 表示到达第 `i` 阶的方法数。

2. 状态转移方程：

   - 如果你要到达第 `i` 阶，你可以从第 `i-1` 阶爬一个台阶上来，或者从第 `i-2` 阶爬两个台阶上来。

   - 因此，状态转移方程为：`dp[i] = dp[i-1] + dp[i-2]`。

3. 初始条件：

   - 到达第 1 阶的方法只有一种：`dp[1] = 1`。

   - 到达第 2 阶的方法有两种：`dp[2] = 2`。

4. 计算结果：根据状态转移方程，从第 3 阶开始，逐步计算到第 `n` 阶的方法数。

### 参考代码

#### C++

```c++
#include <iostream>
#include <vector>

int climbStairs(int n) {
    if (n == 1) return 1;  // 只有1阶时，只有一种方法
    if (n == 2) return 2;  // 只有2阶时，有两种方法
    
    // 初始化dp数组，dp[i]表示到达第i阶的方法数
    std::vector<int> dp(n + 1);
    dp[1] = 1;
    dp[2] = 2;

    // 计算从第3阶到第n阶的方法数
    for (int i = 3; i <= n; ++i) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    // 返回到达第n阶的方法数
    return dp[n];
}

int main() {
    int n1 = 2;
    std::cout << "输入: " << n1 << std::endl;
    std::cout << "输出: " << climbStairs(n1) << std::endl; // 输出: 2

    int n2 = 3;
    std::cout << "输入: " << n2 << std::endl;
    std::cout << "输出: " << climbStairs(n2) << std::endl; // 输出: 3

    int n3 = 5;
    std::cout << "输入: " << n3 << std::endl;
    std::cout << "输出: " << climbStairs(n3) << std::endl; // 输出: 8

    return 0;
}
```

#### Java

```java
public class ClimbingStairs {

    public int climbStairs(int n) {
        // 如果只有一阶楼梯，只有一种爬法
        if (n == 1) {
            return 1;
        }
        
        // 初始化dp数组，dp[i]表示到达第i阶的方法数
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;

        // 计算从第3阶到第n阶的方法数
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        // 返回到达第n阶的方法数
        return dp[n];
    }

    public static void main(String[] args) {
        ClimbingStairs solution = new ClimbingStairs();

        int n1 = 2;
        System.out.println("输入: " + n1);
        System.out.println("输出: " + solution.climbStairs(n1)); // 输出: 2

        int n2 = 3;
        System.out.println("输入: " + n2);
        System.out.println("输出: " + solution.climbStairs(n2)); // 输出: 3

        int n3 = 5;
        System.out.println("输入: " + n3);
        System.out.println("输出: " + solution.climbStairs(n3)); // 输出: 8
    }
}
```

#### Python

```python
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # 初始化 dp 数组
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    # 填充 dp 数组
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# 示例用法
n1 = 2
print("输入:", n1)
print("输出:", climbStairs(n1)) # 输出: 2

n2 = 3
print("输入:", n2)
print("输出:", climbStairs(n2)) # 输出: 3

n3 = 5
print("输入:", n3)
print("输出:", climbStairs(n3)) # 输出: 8
```

