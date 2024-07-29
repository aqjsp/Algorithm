# 面试经典算法题83-买卖股票的最佳时机 III

LeetCode.123

### 问题描述

给定一个数组，它的第 `i` 个元素是一支给定的股票在第 `i` 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。

**注意：**你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1:**

```
输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
```

**示例 2：**

```
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
```

**示例 3：**

```
输入：prices = [7,6,4,3,1] 
输出：0 
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
```

**示例 4：**

```
输入：prices = [1]
输出：0
```

### 思路

1. 初始化：

   - `dp[i][0] = 0`，表示在任何一天不进行交易时的利润为 0。

   - 初始化一个变量 `min_price`，表示在进行第 `k` 次交易之前的最小价格。

2. 状态转移方程：

   - 对于每一天i，我们计算出k次交易的最大利润：
     - `dp[i][k] = max(dp[i-1][k], prices[i] - min_price)`
     - 其中 `min_price` 是在第 `k` 次交易之前的最低价格，初始时为 `prices[0]`，并在遍历过程中不断更新。

   - 更新 `min_price` 为 `min(min_price, prices[i] - dp[i-1][k-1])`。

3. 最终结果：最终 `dp[n-1][2]` 表示在最后一天最多完成两次交易的最大利润。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 计算最多两笔交易的最大利润
int maxProfit(vector<int>& prices) {
    if (prices.empty()) return 0;

    int n = prices.size();
    // 创建一个二维数组，dp[i][k] 表示在第 i 天进行 k 次交易的最大利润
    vector<vector<int>> dp(n, vector<int>(3, 0));

    for (int k = 1; k <= 2; ++k) {
        int min_price = prices[0];
        for (int i = 1; i < n; ++i) {
            // 更新 min_price 为在第 k 次交易前的最低价格
            min_price = min(min_price, prices[i] - dp[i-1][k-1]);
            // 计算在第 i 天进行 k 次交易的最大利润
            dp[i][k] = max(dp[i-1][k], prices[i] - min_price);
        }
    }

    return dp[n-1][2]; // 返回在最后一天最多进行两次交易的最大利润
}

int main() {
    vector<int> prices;
    int n, price;
    cout << "输入价格的数量: ";
    cin >> n;
    cout << "输入股票价格: ";
    for (int i = 0; i < n; ++i) {
        cin >> price;
        prices.push_back(price);
    }

    int result = maxProfit(prices);
    cout << "最多可以完成两笔交易的最大利润为: " << result << endl;

    return 0;
}
```

#### Java

```
import java.util.Scanner;

public class MaxProfit {
    
    // 计算最多两笔交易的最大利润
    public static int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) {
            return 0; // 如果价格数组为空，返回0
        }

        int n = prices.length; // 获取价格数组的长度
        int[][] dp = new int[n][3]; // 创建一个二维数组，dp[i][k] 表示在第 i 天进行 k 次交易的最大利润

        // 遍历交易次数，从1到2次交易
        for (int k = 1; k <= 2; k++) {
            int minPrice = prices[0]; // 初始化在第 k 次交易前的最低价格为第1天的价格
            for (int i = 1; i < n; i++) {
                // 更新 minPrice 为在第 k 次交易前的最低价格
                minPrice = Math.min(minPrice, prices[i] - dp[i-1][k-1]);
                // 计算在第 i 天进行 k 次交易的最大利润
                dp[i][k] = Math.max(dp[i-1][k], prices[i] - minPrice);
            }
        }

        return dp[n-1][2]; // 返回在最后一天最多进行两次交易的最大利润
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("输入价格的数量: ");
        int n = scanner.nextInt(); // 获取价格的数量

        int[] prices = new int[n]; // 创建价格数组
        System.out.print("输入股票价格: ");
        for (int i = 0; i < n; i++) {
            prices[i] = scanner.nextInt(); // 输入每一天的股票价格
        }

        int result = maxProfit(prices); // 计算最多两笔交易的最大利润
        System.out.println("最多可以完成两笔交易的最大利润为: " + result); // 输出结果

        scanner.close();
    }
}
```

#### Python

```
def maxProfit(prices):
    if not prices:
        return 0
    
    n = len(prices)
    dp = [[0] * 3 for _ in range(n)]
    
    for k in range(1, 3):
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i] - dp[i-1][k-1])
            dp[i][k] = max(dp[i-1][k], prices[i] - min_price)
    
    return dp[n-1][2]

# 示例测试
prices1 = [3,3,5,0,0,3,1,4]
prices2 = [1,2,3,4,5]
prices3 = [7,6,4,3,1]
prices4 = [1]

print(f"输入：{prices1}，输出：{maxProfit(prices1)}")
print(f"输入：{prices2}，输出：{maxProfit(prices2)}")
print(f"输入：{prices3}，输出：{maxProfit(prices3)}")
print(f"输入：{prices4}，输出：{maxProfit(prices4)}")
```

