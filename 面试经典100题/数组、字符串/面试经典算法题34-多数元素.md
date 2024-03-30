# 面试经典算法题34-多数元素

LeetCode.169

### 问题描述

给定一个大小为 `n` 的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

**示例 1：**

```
输入：nums = [3,2,3]
输出：3
```

**示例 2：**

```
输入：nums = [2,2,1,1,1,2,2]
输出：2
```

### 思路

1. 初始化候选多数元素 `candidate` 和其出现次数 `count`。
2. 遍历数组，对于每个元素：
   - 如果 `count` 为0，则将当前元素设为候选多数元素，并将 `count` 设为1。
   - 否则，如果当前元素等于候选多数元素，则将 `count` 加1，否则将 `count` 减1。
3. 返回候选多数元素 `candidate`。

### 图解

![阿Q作](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403302243227.png)

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = nums[0]; // 初始化候选多数元素为数组第一个元素
        int count = 1; // 初始化候选多数元素的出现次数为1

        // 遍历数组
        for (int i = 1; i < nums.size(); ++i) {
            if (count == 0) {
                candidate = nums[i]; // 更新候选多数元素
                count = 1; // 重置出现次数为1
            } else if (nums[i] == candidate) {
                count++; // 候选多数元素出现，增加出现次数
            } else {
                count--; // 候选多数元素未出现，减少出现次数
            }
        }

        return candidate; // 返回候选多数元素
    }
};

int main() {
    vector<int> nums = {3, 2, 3}; // 输入数组
    Solution solution;
    int result = solution.majorityElement(nums); // 查找多数元素
    cout << "多数元素：" << result << endl; // 输出结果

    return 0;
}
```

#### Java

```
import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        int candidate = nums[0]; // 初始化候选多数元素为数组第一个元素
        int count = 1; // 初始化候选多数元素的出现次数为1

        // 遍历数组
        for (int i = 1; i < nums.length; ++i) {
            if (count == 0) {
                candidate = nums[i]; // 更新候选多数元素
                count = 1; // 重置出现次数为1
            } else if (nums[i] == candidate) {
                count++; // 候选多数元素出现，增加出现次数
            } else {
                count--; // 候选多数元素未出现，减少出现次数
            }
        }

        return candidate; // 返回候选多数元素
    }

    public static void main(String[] args) {
        int[] nums = {3, 2, 3}; // 输入数组
        Solution solution = new Solution();
        int result = solution.majorityElement(nums); // 查找多数元素
        System.out.println("多数元素：" + result); // 输出结果
    }
}
```

#### Python

```
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0] # 初始化候选多数元素为数组第一个元素
        count = 1 # 初始化候选多数元素的出现次数为1

        # 遍历数组
        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i] # 更新候选多数元素
                count = 1 # 重置出现次数为1
            elif nums[i] == candidate:
                count += 1 # 候选多数元素出现，增加出现次数
            else:
                count -= 1 # 候选多数元素未出现，减少出现次数

        return candidate # 返回候选多数元素

# 测试
nums = [3, 2, 3] # 输入数组
solution = Solution()
result = solution.majorityElement(nums) # 查找多数元素
print("多数元素:", result) # 输出结果
```

