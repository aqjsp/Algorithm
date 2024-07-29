# 面试经典算法题84-买卖股票的最佳时机 IV

LeetCode.188

### 问题描述

给你一个整数数组 `prices` 和一个整数 `k` ，其中 `prices[i]` 是某支给定的股票在第 `i` 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 `k` 笔交易。也就是说，你最多可以买 `k` 次，卖 `k` 次。

**注意：**你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1：**

```
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
```

**示例 2：**

```
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
```

### 思路

1. 定义状态：

   - 使用二维数组 `dp[i][j]`，其中 `i` 表示第 `i` 天，`j` 表示最多进行 `j` 次交易时的最大利润。

   - 使用一个数组 `min_price[j]`，表示第 `j` 次交易之前的最低价格。

2. 初始状态：

   - `dp[i][0] = 0`：不进行任何交易的利润为0。

   - `dp[0][j] = 0`：第0天进行任何交易的利润为0。

3. 状态转移方程：

   - 对于每一天 `i` 和每一个交易次数 `j`，计算 `dp[i][j]`：`dp[i][j]=max(dp[i−1][j],prices[i]−minprice[j])`

   - 更新 `min_price[j]`： `minprice[j]=min(minprice[j],prices[i]−dp[i−1][j−1])`

4. 最终结果：`dp[n-1][k]` 为最后一天进行最多 `k` 次交易的最大利润。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 计算最多进行 k 次交易的最大利润
int maxProfit(int k, vector<int>& prices) {
    int n = prices.size();
    if (n == 0) return 0; // 如果价格数组为空，直接返回0

    // 如果 k 大于 n / 2，等价于可以进行任意次交易
    if (k > n / 2) {
        int maxProfit = 0;
        for (int i = 1; i < n; ++i) {
            if (prices[i] > prices[i - 1]) {
                maxProfit += prices[i] - prices[i - 1];
            }
        }
        return maxProfit;
    }

    // 创建二维数组 dp，dp[i][j] 表示在第 i 天最多进行 j 次交易的最大利润
    vector<vector<int>> dp(n, vector<int>(k + 1, 0));
    // 创建数组 min_price，记录第 j 次交易之前的最低价格
    vector<int> min_price(k + 1, prices[0]);

    // 填充 dp 表
    for (int j = 1; j <= k; ++j) { // 枚举交易次数
        for (int i = 1; i < n; ++i) { // 枚举天数
            // 更新 min_price[j]
            min_price[j] = min(min_price[j], prices[i] - dp[i-1][j-1]);
            // 更新 dp[i][j]
            dp[i][j] = max(dp[i-1][j], prices[i] - min_price[j]);
        }
    }

    return dp[n-1][k]; // 返回在最后一天最多进行 k 次交易的最大利润
}

int main() {
    int k;
    cout << "输入交易次数 k: ";
    cin >> k; // 从用户获取交易次数 k

    int n;
    cout << "输入价格数组长度: ";
    cin >> n; // 从用户获取价格数组长度

    vector<int> prices(n);
    cout << "输入价格数组: ";
    for (int i = 0; i < n; ++i) {
        cin >> prices[i]; // 从用户获取价格数组
    }

    int result = maxProfit(k, prices);
    cout << "最多可以获得的利润: " << result << endl; // 输出最多可以获得的利润

    return 0;
}
```

#### Java

```
import java.util.Scanner;

public class MaxProfit {

    // 计算最多进行 k 次交易的最大利润
    public static int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (n == 0) return 0; // 如果价格数组为空，直接返回0

        // 如果 k 大于 n / 2，等价于可以进行任意次交易
        if (k > n / 2) {
            int maxProfit = 0;
            for (int i = 1; i < n; ++i) {
                if (prices[i] > prices[i - 1]) {
                    maxProfit += prices[i] - prices[i - 1];
                }
            }
            return maxProfit;
        }

        // 创建二维数组 dp，dp[i][j] 表示在第 i 天最多进行 j 次交易的最大利润
        int[][] dp = new int[n][k + 1];
        // 创建数组 minPrice，记录第 j 次交易之前的最低价格
        int[] minPrice = new int[k + 1];

        // 初始化 minPrice 数组
        for (int j = 0; j <= k; ++j) {
            minPrice[j] = prices[0];
        }

        // 填充 dp 表
        for (int j = 1; j <= k; ++j) { // 枚举交易次数
            for (int i = 1; i < n; ++i) { // 枚举天数
                // 更新 minPrice[j]
                minPrice[j] = Math.min(minPrice[j], prices[i] - dp[i-1][j-1]);
                // 更新 dp[i][j]
                dp[i][j] = Math.max(dp[i-1][j], prices[i] - minPrice[j]);
            }
        }

        return dp[n-1][k]; // 返回在最后一天最多进行 k 次交易的最大利润
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("输入交易次数 k: ");
        int k = scanner.nextInt(); // 从用户获取交易次数 k

        System.out.print("输入价格数组长度: ");
        int n = scanner.nextInt(); // 从用户获取价格数组长度

        int[] prices = new int[n];
        System.out.print("输入价格数组: ");
        for (int i = 0; i < n; ++i) {
            prices[i] = scanner.nextInt(); // 从用户获取价格数组
        }

        int result = maxProfit(k, prices);
        System.out.println("最多可以获得的利润: " + result); // 输出最多可以获得的利润
    }
}
```

#### Python

```
def maxProfit(k, prices):
    n = len(prices)
    if n == 0:
        return 0  # 如果价格数组为空，直接返回0

    # 如果 k 大于 n / 2，等价于可以进行任意次交易
    if k > n // 2:
        max_profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

    # 创建二维数组 dp，dp[i][j] 表示在第 i 天最多进行 j 次交易的最大利润
    dp = [[0] * (k + 1) for _ in range(n)]
    # 创建数组 min_price，记录第 j 次交易之前的最低价格
    min_price = [prices[0]] * (k + 1)

    # 填充 dp 表
    for j in range(1, k + 1):  # 枚举交易次数
        for i in range(1, n):  # 枚举天数
            # 更新 min_price[j]
            min_price[j] = min(min_price[j], prices[i] - dp[i-1][j-1])
            # 更新 dp[i][j]
            dp[i][j] = max(dp[i-1][j], prices[i] - min_price[j])

    return dp[n-1][k]  # 返回在最后一天最多进行 k 次交易的最大利润

if __name__ == "__main__":
    import sys

    k = int(input("输入交易次数 k: "))  # 从用户获取交易次数 k

    prices = list(map(int, input("输入价格数组（用空格分隔）: ").split()))  # 从用户获取价格数组

    result = maxProfit(k, prices)
    print("最多可以获得的利润:", result)  # 输出最多可以获得的利润
```

