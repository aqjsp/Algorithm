# 面试经典算法题72-最长连续序列

LeetCode.128

### 问题描述

给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

**示例 1：**

```
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```

**示例 2：**

```
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
```

### 思路

1. 将所有数字存入哈希表：将数组中的所有元素插入到一个哈希表中，方便快速查找元素是否存在。

2. 遍历数组中的每个数字：

   - 对于每个数字，检查其是否是序列的起始数字（即当前数字减一后不存在于哈希表中）。

   - 如果是序列的起始数字，便开始向上检查序列中的下一个数字（即当前数字加一，依次类推），计算当前序列的长度。

   - 更新最长序列的长度。

3. 返回最长序列的长度：遍历结束后，最长序列的长度即为结果。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <unordered_set>

int longestConsecutive(std::vector<int>& nums) {
    // 用于存储数组中的所有元素
    std::unordered_set<int> num_set(nums.begin(), nums.end());
    int longest_streak = 0;

    // 遍历数组中的每个元素
    for (int num : nums) {
        // 只在当前数字是序列的起始数字时，开始计算序列长度
        if (!num_set.count(num - 1)) {
            int current_num = num;
            int current_streak = 1;

            // 计算当前序列的长度
            while (num_set.count(current_num + 1)) {
                current_num += 1;
                current_streak += 1;
            }

            // 更新最长序列的长度
            longest_streak = std::max(longest_streak, current_streak);
        }
    }

    return longest_streak;
}

int main() {
    std::vector<int> nums1 = {100, 4, 200, 1, 3, 2};
    std::cout << "输入: [100, 4, 200, 1, 3, 2]" << std::endl;
    std::cout << "输出: " << longestConsecutive(nums1) << std::endl; // 输出: 4

    std::vector<int> nums2 = {0, 3, 7, 2, 5, 8, 4, 6, 0, 1};
    std::cout << "输入: [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]" << std::endl;
    std::cout << "输出: " << longestConsecutive(nums2) << std::endl; // 输出: 9

    return 0;
}
```

#### Java

```
import java.util.HashSet;
import java.util.Set;

public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        // 用于存储数组中的所有元素
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int longestStreak = 0;

        // 遍历数组中的每个元素
        for (int num : nums) {
            // 只在当前数字是序列的起始数字时，开始计算序列长度
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                // 计算当前序列的长度
                while (numSet.contains(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                // 更新最长序列的长度
                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }

    public static void main(String[] args) {
        LongestConsecutiveSequence solution = new LongestConsecutiveSequence();
        
        int[] nums1 = {100, 4, 200, 1, 3, 2};
        System.out.println("输入: [100, 4, 200, 1, 3, 2]");
        System.out.println("输出: " + solution.longestConsecutive(nums1)); // 输出: 4

        int[] nums2 = {0, 3, 7, 2, 5, 8, 4, 6, 0, 1};
        System.out.println("输入: [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]");
        System.out.println("输出: " + solution.longestConsecutive(nums2)); // 输出: 9
    }
}
```

#### Python

```
def longestConsecutive(nums):
    # 用于存储数组中的所有元素
    num_set = set(nums)
    longest_streak = 0

    # 遍历数组中的每个元素
    for num in nums:
        # 只在当前数字是序列的起始数字时，开始计算序列长度
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # 计算当前序列的长度
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # 更新最长序列的长度
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# 示例用法
nums1 = [100, 4, 200, 1, 3, 2]
print("输入:", nums1)
print("输出:", longestConsecutive(nums1)) # 输出: 4

nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print("输入:", nums2)
print("输出:", longestConsecutive(nums2)) # 输出: 9
```

