# 面试经典算法题47-长度最小的子数组

LeetCode.209

### 问题描述

给定一个含有 `n` 个正整数的数组和一个正整数 `target` **。**

找出该数组中满足其总和大于等于 `target` 的长度最小的 **连续子数组**`[numsl, numsl+1, ..., numsr-1, numsr]` ，并返回其长度**。**如果不存在符合条件的子数组，返回 `0` 。

**示例 1：**

```
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
```

**示例 2：**

```
输入：target = 4, nums = [1,4,4]
输出：1
```

**示例 3：**

```
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```

### 思路

1. 初始化左指针 `left` 和右指针 `right`，分别指向数组的起始位置。
2. 初始化子数组的和 `sum` 为 0，用于记录当前子数组的元素之和。
3. 遍历数组，右指针 `right` 不断向右移动，每次将当前指向的元素加入子数组中，并更新 `sum`。
4. 当 `sum` 大于等于 `target` 时，记录当前子数组的长度，并尝试将左指针 `left` 向右移动，缩小子数组的范围，直到 `sum` 小于 `target`。
5. 在移动左指针的过程中，不断更新最小子数组的长度。
6. 返回最终的最小子数组长度。

### 图解

1. 初始化左指针 `left` 和右指针 `right`，分别指向数组的起始位置。初始化子数组的和 `sum` 为 0，用于记录当前子数组的元素之和。

![1](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102323040.png)

2. 遍历数组，当right=0时，将当前指向的元素加入子数组中，并更新 `sum`。

![2](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102327846.png)

3. 继续遍历数组，右指针 `right` 向右移动，每次将当前指向的元素加入子数组中，并更新 `sum`。

![3](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102328670.png)

4. 继续遍历数组，右指针 `right` 向右移动，每次将当前指向的元素加入子数组中，并更新 `sum`。

![4](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102329117.png)

5. 继续遍历数组，右指针 `right` 向右移动，每次将当前指向的元素加入子数组中，并更新 `sum`。

![5](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102330697.png)

6. 此时sum >= target，更新最小子数组的长度为right - left + 1，将左边界的元素从子数组中移出，左指针向右移动，缩小子数组的范围。这里将两步合一起了。

![6](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102337986.png)

7. 继续遍历数组，右指针 `right` 向右移动，每次将当前指向的元素加入子数组中，并更新 `sum`。

![7](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102337551.png)

8. 此时sum >= target，更新最小子数组的长度为right - left + 1，将左边界的元素从子数组中移出，左指针向右移动，缩小子数组的范围。这里将两步合一起了。

![8](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102343774.png)

9. 此时sum >= target，更新最小子数组的长度为right - left + 1，将左边界的元素从子数组中移出，左指针向右移动，缩小子数组的范围。这里将两步合一起了。

![9](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102345700.png)

10. 继续遍历数组，右指针 `right` 向右移动，每次将当前指向的元素加入子数组中，并更新 `sum`。

![10](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102346547.png)

11. 此时sum >= target，更新最小子数组的长度为right - left + 1，将左边界的元素从子数组中移出，左指针向右移动，缩小子数组的范围。这里将两步合一起了。

![11](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102348303.png)

12. 此时sum >= target，更新最小子数组的长度为right - left + 1，将左边界的元素从子数组中移出，左指针向右移动，缩小子数组的范围。这里将两步合一起了。

![12](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102351641.png)

13. 继续遍历数组，右指针 `right` 向右移动，每次将当前指向的元素加入子数组中，并更新 `sum`。

![13](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405102353182.png)

跳出循环，子数组 [4,3] 是该条件下的长度最小的子数组，最小长度为2。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

int minSubArrayLen(int target, std::vector<int>& nums) {
    int left = 0, right = 0; // 双指针，分别表示子数组的左右边界
    int sum = 0; // 当前子数组的元素之和
    int minLen = INT_MAX; // 最小子数组的长度

    for (right = 0; right < nums.size(); right++) {
        sum += nums[right]; // 将右边界的元素加入子数组
        while (sum >= target) { // 如果当前子数组的和大于等于目标值
            minLen = std::min(minLen, right - left + 1); // 更新最小子数组的长度
            sum -= nums[left]; // 将左边界的元素从子数组中移出
            left++; // 左指针向右移动，缩小子数组的范围
        }
    }

    return minLen == INT_MAX ? 0 : minLen; // 如果没有符合条件的子数组，则返回0，否则返回最小子数组长度
}

int main() {
    std::vector<int> nums = {2,3,1,2,4,3};
    int target = 7;
    int result = minSubArrayLen(target, nums);
    std::cout << "长度最小的连续子数组的长度为：" << result << std::endl;
    return 0;
}
```

#### Java

```
public class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, right = 0; // 双指针，分别表示子数组的左右边界
        int sum = 0; // 当前子数组的元素之和
        int minLen = Integer.MAX_VALUE; // 最小子数组的长度

        for (right = 0; right < nums.length; right++) {
            sum += nums[right]; // 将右边界的元素加入子数组
            while (sum >= target) { // 如果当前子数组的和大于等于目标值
                minLen = Math.min(minLen, right - left + 1); // 更新最小子数组的长度
                sum -= nums[left]; // 将左边界的元素从子数组中移出
                left++; // 左指针向右移动，缩小子数组的范围
            }
        }

        return minLen == Integer.MAX_VALUE ? 0 : minLen; // 如果没有符合条件的子数组，则返回0，否则返回最小子数组长度
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {2,3,1,2,4,3};
        int target = 7;
        int result = solution.minSubArrayLen(target, nums);
        System.out.println("长度最小的连续子数组的长度为：" + result);
    }
}
```

#### Python

```
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0  # 子数组左边界
        sum_val = 0  # 当前子数组的元素之和
        min_len = float('inf')  # 最小子数组的长度

        for right in range(len(nums)):  # 遍历数组，右指针向右移动
            sum_val += nums[right]  # 将右边界的元素加入子数组
            while sum_val >= target:  # 如果当前子数组的和大于等于目标值
                min_len = min(min_len, right - left + 1)  # 更新最小子数组的长度
                sum_val -= nums[left]  # 将左边界的元素从子数组中移出
                left += 1  # 左指针向右移动，缩小子数组的范围

        return min_len if min_len != float('inf') else 0  # 如果没有符合条件的子数组，则返回0，否则返回最小子数组长度

solution = Solution()
nums = [2,3,1,2,4,3]
target = 7
result = solution.minSubArrayLen(target, nums)
print("长度最小的连续子数组的长度为：", result)
```

