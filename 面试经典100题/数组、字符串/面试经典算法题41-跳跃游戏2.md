# 面试经典算法题41-跳跃游戏2

LeetCode.45

### 问题描述

给定一个长度为 `n` 的 **0 索引**整数数组 `nums`。初始位置为 `nums[0]`。

每个元素 `nums[i]` 表示从索引 `i` 向前跳转的最大长度。换句话说，如果你在 `nums[i]` 处，你可以跳转到任意 `nums[i + j]` 处:

- `0 <= j <= nums[i]` 
- `i + j < n`

返回到达 `nums[n - 1]` 的最小跳跃次数。生成的测试用例可以到达 `nums[n - 1]`。

**示例 1:**

```
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
```

**示例 2:**

```
输入: nums = [2,3,0,1,4]
输出: 2
```

### 思路

1. 使用贪心算法，每次选择能够跳跃的最远距离内能够到达的下一个位置，这样可以保证跳跃次数最小。
2. 维护两个变量，`max_pos` 表示当前能够到达的最远位置，`end` 表示当前跳跃的边界，即在当前位置下一步能够到达的最远位置。
3. 遍历数组，更新 `end` 和 `max_pos`，如果当前位置达到了 `end`，则增加跳跃次数，并更新 `end` 为 `max_pos`。

### 图解

```
         +-------------------+
         |    开始执行程序     |
         +-------------------+
                  |
                  v
    +-----------------------------+
    |   初始化变量：jumps = 0,      |
    |   end = 0, max_pos = 0      |
    +-----------------------------+
                  |
                  v
    +-----------------------------+
    |      第1次循环：i = 0,        |
    |max_pos = max(0, 0 + 2) = 2, |
    |      i == end 不成立         |
    +-----------------------------+
                  |
                  v
    +-----------------------------+
    |     第2次循环：i = 1,         |
    |max_pos = max(2, 1 + 3) = 4, |
    |     i == end 不成立          |
    +-----------------------------+
                  |
                  v
    +-----------------------------+
    |      第3次循环：i = 2,        |
    |max_pos = max(4, 2 + 1) = 4, |
    |      i == end 不成立         |
    +-----------------------------+
                  |
                  v
+--------------------------------------+
|         第4次循环：i = 3,              |
|    max_pos = max(4, 3 + 1) = 4,      |
|i == end 成立，更新 end = 4, jumps = 1  |
+--------------------------------------+
                  |
                  v
    +-----------------------------+
    |     第5次循环：i = 4,         |
    |max_pos = max(4, 4 + 4) = 4, |
    |      i == end 不成立         |
    +-----------------------------+
                  |
                  v
    +-----------------------------+
    |   循环结束，返回 jumps = 2    |
    +-----------------------------+
```

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int jumps = 0;
        int end = 0;
        int max_pos = 0;

        for (int i = 0; i < n - 1; ++i) {
            max_pos = max(max_pos, i + nums[i]);
            if (i == end) {
                end = max_pos;
                jumps++;
            }
        }

        return jumps;
    }
};

int main() {
    vector<int> nums = {2, 3, 1, 1, 4}; // 输入数组
    Solution solution;
    int result = solution.jump(nums); // 计算最小跳跃次数
    cout << "最小跳跃次数：" << result << endl; // 输出结果

    return 0;
}
```

#### Java

```
import java.util.Arrays;

public class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int jumps = 0;
        int end = 0;
        int maxPos = 0;

        for (int i = 0; i < n - 1; ++i) {
            maxPos = Math.max(maxPos, i + nums[i]);
            if (i == end) {
                end = maxPos;
                jumps++;
            }
        }

        return jumps;
    }

    public static void main(String[] args) {
        int[] nums = {2, 3, 1, 1, 4}; // 输入数组
        Solution solution = new Solution();
        int result = solution.jump(nums); // 计算最小跳跃次数
        System.out.println("最小跳跃次数：" + result); // 输出结果
    }
}
```

#### Python

```
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        end = 0
        max_pos = 0

        for i in range(n - 1):
            max_pos = max(max_pos, i + nums[i])
            if i == end:
                end = max_pos
                jumps += 1

        return jumps

# 测试代码
nums = [2, 3, 1, 1, 4]
solution = Solution()
result = solution.jump(nums)
print("最小跳跃次数：", result)
```

