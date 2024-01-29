## 恰好移动 k 步到达某一位置的方法数目

LeetCode.2400

### 问题描述

给你两个 **正** 整数 `startPos` 和 `endPos` 。最初，你站在 **无限** 数轴上位置 `startPos` 处。在一步移动中，你可以向左或者向右移动一个位置。

给你一个正整数 `k` ，返回从 `startPos` 出发、**恰好** 移动 `k` 步并到达 `endPos` 的 **不同** 方法数目。由于答案可能会很大，返回对 `109 + 7` **取余** 的结果。

如果所执行移动的顺序不完全相同，则认为两种方法不同。

**注意：**数轴包含负整数。

**示例 1：**

```
输入：startPos = 1, endPos = 2, k = 3
输出：3
解释：存在 3 种从 1 到 2 且恰好移动 3 步的方法：
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
可以证明不存在其他方法，所以返回 3 。
```

**示例 2：**

```
输入：startPos = 2, endPos = 5, k = 10
输出：0
解释：不存在从 2 到 5 且恰好移动 10 步的方法。
```

**提示：**

- `1 <= startPos, endPos, k <= 1000`

### 思路

1. 初始化：创建一个二维数组 `dp`，用于存储从 `startPos` 出发，经过 `i` 步到达位置 `j - k` 的方法数目。数组的大小为 `(k + 1) * (2 * k + 1)`，并将初始位置的方法数设为 1，即 `dp[0][k] = 1`。

2. 状态转移：对于当前步数 `i` 和位置 `j`，根据上一步的状态 `dp[i - 1][j]` 来更新当前步的状态 `dp[i][j]`。具体地：

   - 如果 `dp[i - 1][j]` 不为 0，表示在上一步可以到达位置 `j - k`。那么可以在当前步向右移动一步到达位置 `j + 1 - k`，或者向左移动一步到达位置 `j - 1 - k`。因此，更新 `dp[i][j + 1]` 和 `dp[i][j - 1]` 的值：

     ```
     dp[i][j + 1] = (dp[i][j + 1] + dp[i - 1][j]) % MOD; // 向右移动一步
     dp[i][j - 1] = (dp[i][j - 1] + dp[i - 1][j]) % MOD; // 向左移动一步
     ```

   - 这样，通过状态转移方程，可以逐步填充 `dp` 数组，直到计算出从 `startPos` 出发，恰好移动 `k` 步到达 `endPos` 的方法数目。

3. 边界条件处理：在计算过程中，需要考虑特殊情况，例如需要移动的步数超过了 `k`，此时无法到达目标位置，返回 0。

4. 返回结果：最后，返回从 `startPos` 出发，恰好移动 `k` 步到达 `endPos` 的方法数目，即 `dp[k][k + n]`。

### 参考代码

#### C++

```
class Solution {
public:
    int numberOfWays(int startPos, int endPos, int k) {
        const long long MOD = 1e9 + 7;
        // 计算需要移动的步数
        int n = abs(startPos - endPos);
        // 创建一个二维数组 dp，用于存储从 startPos 出发，经过 i 步到达位置 j - k 的方法数目
        std::vector<std::vector<long long>> dp(k + 1, std::vector<long long>(2 * k + 1, 0));
        // 初始位置的方法数为 1
        dp[0][k] = 1;

        // 动态规划的状态转移
        for (int i = 1; i <= k; i++) {
            for (int j = 0; j <= 2 * k; j++) {
                if (dp[i - 1][j] != 0) {
                    // 更新 dp[i][j + 1]，表示向右移动一步
                    dp[i][j + 1] = (dp[i][j + 1] + dp[i - 1][j]) % MOD;
                    // 更新 dp[i][j - 1]，表示向左移动一步
                    dp[i][j - 1] = (dp[i][j - 1] + dp[i - 1][j]) % MOD;
                }
            }
        }

        // 如果需要移动的步数超过了 k，则无法到达目标位置，返回 0
        if (n > k) {
            return 0;
        }

        // 返回从 startPos 出发，恰好移动 k 步到达 endPos 的方法数目
        return dp[k][k + n];
    }
};
```

#### Java

```
class Solution {
    public int numberOfWays(int startPos, int endPos, int k) {
        final long MOD = 1000000007;
        // 计算需要移动的步数
        int n = Math.abs(startPos - endPos);
        // 创建一个二维数组 dp，用于存储从 startPos 出发，经过 i 步到达位置 j - k 的方法数目
        long[][] dp = new long[k + 1][2 * k + 1];
        // 初始位置的方法数为 1
        dp[0][k] = 1;

        // 动态规划的状态转移
        for (int i = 1; i <= k; i++) {
            for (int j = 0; j <= 2 * k; j++) {
                if (dp[i - 1][j] != 0) {
                    // 更新 dp[i][j + 1]，表示向右移动一步
                    dp[i][j + 1] = (dp[i][j + 1] + dp[i - 1][j]) % MOD;
                    // 更新 dp[i][j - 1]，表示向左移动一步
                    dp[i][j - 1] = (dp[i][j - 1] + dp[i - 1][j]) % MOD;
                }
            }
        }

        // 如果需要移动的步数超过了 k，则无法到达目标位置，返回 0
        if (n > k) {
            return 0;
        }

        // 返回从 startPos 出发，恰好移动 k 步到达 endPos 的方法数目
        return (int) dp[k][k + n];
    }
}
```

#### Python

```
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        # 计算需要移动的步数
        n = abs(startPos - endPos)
        # 创建一个二维数组 dp，用于存储从 startPos 出发，经过 i 步到达位置 j - k 的方法数目
        dp = [[0] * (2 * k + 1) for _ in range(k + 1)]
        # 初始位置的方法数为 1
        dp[0][k] = 1

        # 动态规划的状态转移
        for i in range(1, k + 1):
            for j in range(2 * k + 1):
                if dp[i - 1][j] != 0:
                    # 更新 dp[i][j + 1]，表示向右移动一步
                    dp[i][j + 1] = (dp[i][j + 1] + dp[i - 1][j]) % MOD
                    # 更新 dp[i][j - 1]，表示向左移动一步
                    dp[i][j - 1] = (dp[i][j - 1] + dp[i - 1][j]) % MOD

        # 如果需要移动的步数超过了 k，则无法到达目标位置，返回 0
        if n > k:
            return 0

        # 返回从 startPos 出发，恰好移动 k 步到达 endPos 的方法数目
        return dp[k][k + n]
```