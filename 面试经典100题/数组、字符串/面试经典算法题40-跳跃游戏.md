# 面试经典算法题40-跳跃游戏

LeetCode.55

### 问题描述

给你一个非负整数数组 `nums` ，你最初位于数组的第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 `true` ；否则，返回 `false` 。

**示例 1：**

```
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
```

**示例 2：**

```
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
```

### 思路

1. 使用一个变量 `maxReach` 记录当前能够到达的最远位置，初始值为 0。
2. 遍历数组，对于每个位置`i`：
   - 如果当前位置 `i` 大于 `maxReach`，说明无法到达当前位置，返回 `false`。
   - 否则，更新 `maxReach` 为 `max(maxReach, i + nums[i])`，表示在当前位置能够到达的最远位置。
3. 如果遍历结束时，`maxReach` 大于等于数组的最后一个下标 `nums.size() - 1`，则返回 `true`，否则返回 `false`。

### 图解

```
+-----------------------------------------+
|             开始执行程序                  |
+-----------------------------------------+
                   |
                   v
+-----------------------------------------+
|        输入数组 nums = [2,3,1,1,4]       |
+-----------------------------------------+
                   |
                   v
+-----------------------------------------+
|       初始化最远可达位置 max_reach = 0     |
+-----------------------------------------+
                   |
                   v
+-----------------------------------------+
|        当前位置为 0，最远可达位置为 2       |
|        更新最远可达位置为 2                |
+-----------------------------------------+
                   |
                   v
+-----------------------------------------+
|        当前位置为 1，最远可达位置为 2       |
|        当前位置未超过最远可达位置，继续      |
+-----------------------------------------+
                   |
                   v
+-----------------------------------------+
|        当前位置为 2，最远可达位置为 3       |
|        更新最远可达位置为 3                |
+-----------------------------------------+
                   |
                   v
+-----------------------------------------+
|        当前位置为 3，最远可达位置为 4       |
|        更新最远可达位置为 4                |
+-----------------------------------------+
                   |
                   v
+-----------------------------------------+
|        当前位置为 4，已到达最后一个下标      |
|             返回 True                    |
+-----------------------------------------+
                   |
                   v
+-----------------------------------------+
|               结束程序                   |
+-----------------------------------------+
```

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0; // 初始化能够到达的最远位置为 0

        for (int i = 0; i < nums.size(); ++i) {
            if (i > maxReach) { // 当前位置已经超过最远位置，无法到达当前位置
                return false;
            }
            maxReach = max(maxReach, i + nums[i]); // 更新能够到达的最远位置
            if (maxReach >= nums.size() - 1) { // 如果已经到达最后一个位置，返回 true
                return true;
            }
        }

        return false;
    }
};

int main() {
    vector<int> nums = {2, 3, 1, 1, 4}; // 输入数组
    Solution solution;
    bool result = solution.canJump(nums); // 判断能否到达最后一个下标
    cout << "能否到达最后一个下标：" << (result ? "true" : "false") << endl; // 输出结果

    return 0;
}
```

#### Java

```
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0; // 初始化能够到达的最远位置为 0

        for (int i = 0; i < nums.length; ++i) {
            if (i > maxReach) { // 当前位置已经超过最远位置，无法到达当前位置
                return false;
            }
            maxReach = Math.max(maxReach, i + nums[i]); // 更新能够到达的最远位置
            if (maxReach >= nums.length - 1) { // 如果已经到达最后一个位置，返回 true
                return true;
            }
        }

        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        int[] nums = {2, 3, 1, 1, 4}; // 输入数组
        Solution solution = new Solution();
        boolean result = solution.canJump(nums); // 判断能否到达最后一个下标
        System.out.println("能否到达最后一个下标：" + result); // 输出结果
    }
}
```

#### Python

```
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0 # 初始化能够到达的最远位置为 0

        for i in range(len(nums)):
            if i > max_reach: # 当前位置已经超过最远位置，无法到达当前位置
                return False
            max_reach = max(max_reach, i + nums[i]) # 更新能够到达的最远位置
            if max_reach >= len(nums) - 1: # 如果已经到达最后一个位置，返回 True
                return True

        return False

# 测试
nums = [2, 3, 1, 1, 4] # 输入数组
solution = Solution()
result = solution.canJump(nums) # 判断能否到达最后一个下标
print("能否到达最后一个下标：", result) # 输出结果
```

