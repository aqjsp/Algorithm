# 面试经典算法题56-搜索旋转排序数组

LeetCode.33

### 问题描述

整数数组 `nums` 按升序排列，数组中的值 **互不相同** 。

在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`0 <= k < nums.length`）上进行了 **旋转**，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标 **从 0 开始** 计数）。例如， `[0,1,2,4,5,6,7]` 在下标 `3` 处经旋转后可能变为 `[4,5,6,7,0,1,2]` 。

给你 **旋转后** 的数组 `nums` 和一个整数 `target` ，如果 `nums` 中存在这个目标值 `target` ，则返回它的下标，否则返回 `-1` 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

**示例 1：**

```
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
```

**示例 2：**

```
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
```

**示例 3：**

```
输入：nums = [1], target = 0
输出：-1
```

### 思路

1. **识别旋转点**：数组被旋转了一次，意味着数组被分成了两个有序的子数组。例如，[4,5,6,7,0,1,2] 可以看作是两个有序子数组 [4,5,6,7] 和 [0,1,2]。
2. **二分查找**：我们可以使用二分查找来确定目标值的位置。在每次二分时，根据中间值和两端值的关系判断哪一半是有序的，并进一步缩小查找范围。

#### 二分查找的步骤

1. 初始化左右边界 `left` 和 `right`。
2. 找到中间值 `mid`。
3. 判断 mid 所在的一半是有序的还是无序的：
   - 如果左半部分 `[left, mid]` 是有序的，且目标值在这个范围内，则在左半部分继续查找，否则在右半部分查找。
   - 如果右半部分 `[mid, right]` 是有序的，且目标值在这个范围内，则在右半部分继续查找，否则在左半部分查找。
4. 迭代上述步骤，直到找到目标值或确定目标值不存在。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

int search(vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        // 检查中间值是否是目标值
        if (nums[mid] == target) {
            return mid;
        }
        
        // 判断左半部分是否有序
        if (nums[left] <= nums[mid]) {
            // 左半部分有序，检查目标值是否在这个范围内
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1; // 在左半部分查找
            } else {
                left = mid + 1; // 在右半部分查找
            }
        }
        // 否则右半部分有序
        else {
            // 右半部分有序，检查目标值是否在这个范围内
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1; // 在右半部分查找
            } else {
                right = mid - 1; // 在左半部分查找
            }
        }
    }
    
    // 如果没有找到目标值，返回 -1
    return -1;
}

int main() {
    // 示例 1
    vector<int> nums1 = {4, 5, 6, 7, 0, 1, 2};
    int target1 = 0;
    cout << "输入：nums = [4, 5, 6, 7, 0, 1, 2], target = 0" << endl;
    cout << "输出：" << search(nums1, target1) << endl;
    
    // 示例 2
    vector<int> nums2 = {4, 5, 6, 7, 0, 1, 2};
    int target2 = 3;
    cout << "输入：nums = [4, 5, 6, 7, 0, 1, 2], target = 3" << endl;
    cout << "输出：" << search(nums2, target2) << endl;
    
    // 示例 3
    vector<int> nums3 = {1};
    int target3 = 0;
    cout << "输入：nums = [1], target = 0" << endl;
    cout << "输出：" << search(nums3, target3) << endl;
    
    return 0;
}
```

#### Java

```
import java.util.Arrays;

public class RotatedArraySearch {

    public static int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // 检查中间值是否是目标值
            if (nums[mid] == target) {
                return mid;
            }

            // 判断左半部分是否有序
            if (nums[left] <= nums[mid]) {
                // 左半部分有序，检查目标值是否在这个范围内
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1; // 在左半部分查找
                } else {
                    left = mid + 1; // 在右半部分查找
                }
            } 
            // 否则右半部分有序
            else {
                // 右半部分有序，检查目标值是否在这个范围内
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1; // 在右半部分查找
                } else {
                    right = mid - 1; // 在左半部分查找
                }
            }
        }

        // 如果没有找到目标值，返回 -1
        return -1;
    }

    public static void main(String[] args) {
        // 示例 1
        int[] nums1 = {4, 5, 6, 7, 0, 1, 2};
        int target1 = 0;
        System.out.println("输入：nums = " + Arrays.toString(nums1) + ", target = " + target1);
        System.out.println("输出：" + search(nums1, target1));

        // 示例 2
        int[] nums2 = {4, 5, 6, 7, 0, 1, 2};
        int target2 = 3;
        System.out.println("输入：nums = " + Arrays.toString(nums2) + ", target = " + target2);
        System.out.println("输出：" + search(nums2, target2));

        // 示例 3
        int[] nums3 = {1};
        int target3 = 0;
        System.out.println("输入：nums = " + Arrays.toString(nums3) + ", target = " + target3);
        System.out.println("输出：" + search(nums3, target3));
    }
}
```

#### Python

```
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # 检查中间值是否是目标值
        if nums[mid] == target:
            return mid

        # 判断左半部分是否有序
        if nums[left] <= nums[mid]:
            # 左半部分有序，检查目标值是否在这个范围内
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # 在左半部分查找
            else:
                left = mid + 1  # 在右半部分查找
        # 否则右半部分有序
        else:
            # 右半部分有序，检查目标值是否在这个范围内
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # 在右半部分查找
            else:
                right = mid - 1  # 在左半部分查找

    # 如果没有找到目标值，返回 -1
    return -1

# 示例 1
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(f"输入：nums = {nums1}, target = {target1}")
print(f"输出：{search(nums1, target1)}")

# 示例 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(f"输入：nums = {nums2}, target = {target2}")
print(f"输出：{search(nums2, target2)}")

# 示例 3
nums3 = [1]
target3 = 0
print(f"输入：nums = {nums3}, target = {target3}")
print(f"输出：{search(nums3, target3)}")
```

