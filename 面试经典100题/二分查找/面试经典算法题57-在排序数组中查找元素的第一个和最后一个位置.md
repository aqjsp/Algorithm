# 面试经典算法题57-在排序数组中查找元素的第一个和最后一个位置

LeetCode.34

### 问题描述

给你一个按照非递减顺序排列的整数数组 `nums`，和一个目标值 `target`。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 `target`，返回 `[-1, -1]`。

你必须设计并实现时间复杂度为 `O(log n)` 的算法解决此问题。

**示例 1：**

```
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
```

**示例 2：**

```
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
```

**示例 3：**

```
输入：nums = [], target = 0
输出：[-1,-1]
```

### 思路

#### 1. 找第一个位置

- 使用二分查找，初始时将左右指针 `left` 和 `right` 分别设置为数组的起始和结束位置。
- 在每次循环中，计算中间位置 `mid`。
- 如果 `nums[mid]` 大于或等于目标值 `target`，将 `right` 移动到 `mid` 位置。
- 否则，将 `left` 移动到 `mid + 1` 位置。
- 最后检查 `left` 是否越界以及 `nums[left]` 是否等于 `target`。

#### 2. 找最后一个位置

- 同样使用二分查找，初始时左右指针分别设置为数组的起始和结束位置。
- 在每次循环中，计算中间位置 `mid`。
- 如果 `nums[mid]` 小于或等于目标值 `target`，将 `left` 移动到 `mid + 1` 位置。
- 否则，将 `right` 移动到 `mid` 位置。
- 最后检查 `right - 1` 是否越界以及 `nums[right - 1]` 是否等于 `target`。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        // 初始化返回结果为 [-1, -1]
        vector<int> result(2, -1);
        
        // 查找第一个位置
        int left = 0, right = nums.size();
        while (left < right) {
            int mid = (left + right) / 2; // 计算中间位置
            if (nums[mid] >= target) { // 如果中间值大于等于目标值，说明目标值可能在左半部分
                right = mid; // 调整右边界
            } else { // 否则，目标值在右半部分
                left = mid + 1; // 调整左边界
            }
        }
        // 检查找到的 left 是否在数组范围内且是否等于目标值
        if (left == nums.size() || nums[left] != target) {
            return result; // 如果没有找到，返回 [-1, -1]
        }
        result[0] = left; // 否则，记录第一个位置
        
        // 查找最后一个位置
        right = nums.size(); // 重置右边界
        while (left < right) {
            int mid = (left + right) / 2; // 计算中间位置
            if (nums[mid] <= target) { // 如果中间值小于等于目标值，说明目标值可能在右半部分
                left = mid + 1; // 调整左边界
            } else { // 否则，目标值在左半部分
                right = mid; // 调整右边界
            }
        }
        result[1] = left - 1; // 记录最后一个位置
        
        return result; // 返回结果
    }
};

int main() {
    Solution solution;
    vector<int> nums1 = {5, 7, 7, 8, 8, 10};
    int target1 = 8;
    vector<int> result1 = solution.searchRange(nums1, target1);
    cout << "输入: nums = [5,7,7,8,8,10], target = 8" << endl;
    cout << "输出: [" << result1[0] << "," << result1[1] << "]" << endl;

    vector<int> nums2 = {5, 7, 7, 8, 8, 10};
    int target2 = 6;
    vector<int> result2 = solution.searchRange(nums2, target2);
    cout << "输入: nums = [5,7,7,8,8,10], target = 6" << endl;
    cout << "输出: [" << result2[0] << "," << result2[1] << "]" << endl;

    vector<int> nums3 = {};
    int target3 = 0;
    vector<int> result3 = solution.searchRange(nums3, target3);
    cout << "输入: nums = [], target = 0" << endl;
    cout << "输出: [" << result3[0] << "," << result3[1] << "]" << endl;

    return 0;
}
```

#### Java

```
import java.util.Arrays;

public class Solution {
    public int[] searchRange(int[] nums, int target) {
        // 初始化返回结果为 [-1, -1]
        int[] result = new int[]{-1, -1};

        // 查找第一个位置
        int left = 0, right = nums.length;
        while (left < right) {
            int mid = (left + right) / 2; // 计算中间位置
            if (nums[mid] >= target) { // 如果中间值大于等于目标值，说明目标值可能在左半部分
                right = mid; // 调整右边界
            } else { // 否则，目标值在右半部分
                left = mid + 1; // 调整左边界
            }
        }
        // 检查找到的 left 是否在数组范围内且是否等于目标值
        if (left == nums.length || nums[left] != target) {
            return result; // 如果没有找到，返回 [-1, -1]
        }
        result[0] = left; // 否则，记录第一个位置

        // 查找最后一个位置
        right = nums.length; // 重置右边界
        while (left < right) {
            int mid = (left + right) / 2; // 计算中间位置
            if (nums[mid] <= target) { // 如果中间值小于等于目标值，说明目标值可能在右半部分
                left = mid + 1; // 调整左边界
            } else { // 否则，目标值在左半部分
                right = mid; // 调整右边界
            }
        }
        result[1] = left - 1; // 记录最后一个位置

        return result; // 返回结果
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] nums1 = {5, 7, 7, 8, 8, 10};
        int target1 = 8;
        int[] result1 = solution.searchRange(nums1, target1);
        System.out.println("输入: nums = [5,7,7,8,8,10], target = 8");
        System.out.println("输出: " + Arrays.toString(result1));

        int[] nums2 = {5, 7, 7, 8, 8, 10};
        int target2 = 6;
        int[] result2 = solution.searchRange(nums2, target2);
        System.out.println("输入: nums = [5,7,7,8,8,10], target = 6");
        System.out.println("输出: " + Arrays.toString(result2));

        int[] nums3 = {};
        int target3 = 0;
        int[] result3 = solution.searchRange(nums3, target3);
        System.out.println("输入: nums = [], target = 0");
        System.out.println("输出: " + Arrays.toString(result3));
    }
}
```

![执行用时](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202406062141881.png)

#### Python

```
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 初始化返回结果为 [-1, -1]
        result = [-1, -1]

        # 查找第一个位置
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2  # 计算中间位置
            if nums[mid] >= target:  # 如果中间值大于等于目标值，说明目标值可能在左半部分
                right = mid  # 调整右边界
            else:  # 否则，目标值在右半部分
                left = mid + 1  # 调整左边界
        # 检查找到的 left 是否在数组范围内且是否等于目标值
        if left == len(nums) or nums[left] != target:
            return result  # 如果没有找到，返回 [-1, -1]
        result[0] = left  # 否则，记录第一个位置

        # 查找最后一个位置
        right = len(nums)  # 重置右边界
        while left < right:
            mid = (left + right) // 2  # 计算中间位置
            if nums[mid] <= target:  # 如果中间值小于等于目标值，说明目标值可能在右半部分
                left = mid + 1  # 调整左边界
            else:  # 否则，目标值在左半部分
                right = mid  # 调整右边界
        result[1] = left - 1  # 记录最后一个位置

        return result  # 返回结果

# 测试
if __name__ == "__main__":
    solution = Solution()

    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    result1 = solution.searchRange(nums1, target1)
    print(f"输入: nums = [5,7,7,8,8,10], target = 8")
    print(f"输出: {result1}")

    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    result2 = solution.searchRange(nums2, target2)
    print(f"输入: nums = [5,7,7,8,8,10], target = 6")
    print(f"输出: {result2}")

    nums3 = []
    target3 = 0
    result3 = solution.searchRange(nums3, target3)
    print(f"输入: nums = [], target = 0")
    print(f"输出: {result3}")
```

