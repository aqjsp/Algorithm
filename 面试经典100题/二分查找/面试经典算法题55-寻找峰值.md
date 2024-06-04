# 面试经典算法题55-寻找峰值

LeetCode.162

### 问题描述

峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 `nums`，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 **任何一个峰值** 所在位置即可。

你可以假设 `nums[-1] = nums[n] = -∞` 。

你必须实现时间复杂度为 `O(log n)` 的算法来解决此问题。

**示例 1：**

```
输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
```

**示例 2：**

```
输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
```

### 思路

1. 使用二分查找法在数组中寻找峰值元素。
2. 定义左右边界，初始时左边界为0，右边界为数组长度减1。
3. 当左边界小于等于右边界时，执行以下操作： 
   - 计算中间位置mid = (left + right) / 2。
   - 如果nums[mid] > nums[mid + 1]，说明峰值在左侧，更新右边界为mid。
   - 否则，峰值在右侧，更新左边界为mid + 1。
4. 返回左边界或右边界，因为此时它们指向同一个峰值元素。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

// 寻找峰值元素的函数
int findPeakElement(vector<int>& nums) {
    int left = 0, right = nums.size() - 1; // 定义左右边界
    while (left < right) { // 当左边界小于右边界时，执行循环
        int mid = left + (right - left) / 2; // 计算中间位置
        if (nums[mid] > nums[mid + 1]) { // 如果当前元素大于右侧元素，说明峰值在左侧
            right = mid; // 更新右边界为mid
        } else { // 否则，峰值在右侧
            left = mid + 1; // 更新左边界为mid + 1
        }
    }
    return left; // 返回左边界或右边界，因为此时它们指向同一个峰值元素
}

int main() {
    vector<int> nums = {1, 2, 3, 1}; // 定义输入数组
    cout << "峰值元素的索引为：" << findPeakElement(nums) << endl; // 输出峰值元素的索引
    return 0;
}
```

#### Java

```
public class Main {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1}; // 定义输入数组
        System.out.println("峰值元素的索引为：" + findPeakElement(nums)); // 输出峰值元素的索引
    }

    // 寻找峰值元素的函数
    public static int findPeakElement(int[] nums) {
        int left = 0, right = nums.length - 1; // 定义左右边界
        while (left < right) { // 当左边界小于右边界时，执行循环
            int mid = left + (right - left) / 2; // 计算中间位置
            if (nums[mid] > nums[mid + 1]) { // 如果当前元素大于右侧元素，说明峰值在左侧
                right = mid; // 更新右边界为mid
            } else { // 否则，峰值在右侧
                left = mid + 1; // 更新左边界为mid + 1
            }
        }
        return left; // 返回左边界或右边界，因为此时它们指向同一个峰值元素
    }
}
```

#### Python

```
def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print("峰值元素的索引为：", find_peak_element(nums))
```

