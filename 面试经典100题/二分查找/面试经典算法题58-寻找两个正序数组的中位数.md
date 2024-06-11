# 面试经典算法题58-寻找两个正序数组的中位数

LeetCode.4

### 问题描述

给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 **中位数** 。

算法的时间复杂度应该为 `O(log (m+n))` 。

**示例 1：**

```
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
```

**示例 2：**

```
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
```

### 思路

1. 定义中位数：

   - 如果两个数组的长度之和为奇数，中位数是第 (m+n)/2 个元素。

   - 如果两个数组的长度之和为偶数，中位数是第 (m+n)/2 和 (m+n)/2 - 1 两个元素的平均值。

2. 利用二分查找：

   - 对两个数组中较短的那个数组进行二分查找，设较短的数组为 nums1，较长的为 nums2。

   - 设 nums1 的当前划分位置为 i，nums2 的当前划分位置为 j，使得 i + j = (m + n + 1) / 2。

   - 调整 i 和 j 的值，使得 nums1[i-1] <= nums2[j] 且 nums2[j-1] <= nums1[i]，即找到了合适的划分位置。

3. 计算中位数：
   - 根据划分位置计算中位数。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
using namespace std;

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    // 确保 nums1 是较短的数组，以便二分查找的范围更小
    if (nums1.size() > nums2.size()) {
        return findMedianSortedArrays(nums2, nums1);
    }
    
    int m = nums1.size();
    int n = nums2.size();
    int imin = 0, imax = m;
    int half_len = (m + n + 1) / 2;

    while (imin <= imax) {
        int i = (imin + imax) / 2;  // 二分查找中 nums1 的划分位置
        int j = half_len - i;       // 对应 nums2 的划分位置

        // 检查划分是否合适，i 太小，需要右移
        if (i < m && nums1[i] < nums2[j-1]) {
            imin = i + 1;
        } 
        // i 太大，需要左移
        else if (i > 0 && nums1[i-1] > nums2[j]) {
            imax = i - 1;
        } 
        // 找到了合适的划分位置
        else {
            int max_of_left;
            // 处理边界情况，如果 i == 0 则 nums1 没有左边部分，最大值来自 nums2
            if (i == 0) { max_of_left = nums2[j-1]; }
            // 如果 j == 0 则 nums2 没有左边部分，最大值来自 nums1
            else if (j == 0) { max_of_left = nums1[i-1]; }
            // 否则，最大值为 nums1 和 nums2 左边部分的最大值
            else { max_of_left = max(nums1[i-1], nums2[j-1]); }
            
            // 如果总长度是奇数，中位数就是左边部分的最大值
            if ((m + n) % 2 == 1) {
                return max_of_left;
            }
            
            int min_of_right;
            // 处理边界情况，如果 i == m 则 nums1 没有右边部分，最小值来自 nums2
            if (i == m) { min_of_right = nums2[j]; }
            // 如果 j == n 则 nums2 没有右边部分，最小值来自 nums1
            else if (j == n) { min_of_right = nums1[i]; }
            // 否则，最小值为 nums1 和 nums2 右边部分的最小值
            else { min_of_right = min(nums1[i], nums2[j]); }
            
            // 如果总长度是偶数，中位数为左边最大值和右边最小值的平均
            return (max_of_left + min_of_right) / 2.0;
        }
    }
    return 0.0;  // 符合题意的输入不会到这里
}

int main() {
    vector<int> nums1 = {1, 3};
    vector<int> nums2 = {2};
    cout << "中位数是: " << findMedianSortedArrays(nums1, nums2) << endl;

    vector<int> nums1_2 = {1, 2};
    vector<int> nums2_2 = {3, 4};
    cout << "中位数是: " << findMedianSortedArrays(nums1_2, nums2_2) << endl;

    return 0;
}
```

#### Java

```
public class MedianOfTwoSortedArrays {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // 确保 nums1 是较短的数组，以便二分查找的范围更小
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.length;
        int n = nums2.length;
        int imin = 0, imax = m;
        int halfLen = (m + n + 1) / 2;

        while (imin <= imax) {
            int i = (imin + imax) / 2;  // 二分查找中 nums1 的划分位置
            int j = halfLen - i;        // 对应 nums2 的划分位置

            // 检查划分是否合适，i 太小，需要右移
            if (i < m && nums1[i] < nums2[j-1]) {
                imin = i + 1;
            } 
            // i 太大，需要左移
            else if (i > 0 && nums1[i-1] > nums2[j]) {
                imax = i - 1;
            } 
            // 找到了合适的划分位置
            else {
                int maxOfLeft;
                // 处理边界情况，如果 i == 0 则 nums1 没有左边部分，最大值来自 nums2
                if (i == 0) { maxOfLeft = nums2[j-1]; }
                // 如果 j == 0 则 nums2 没有左边部分，最大值来自 nums1
                else if (j == 0) { maxOfLeft = nums1[i-1]; }
                // 否则，最大值为 nums1 和 nums2 左边部分的最大值
                else { maxOfLeft = Math.max(nums1[i-1], nums2[j-1]); }
                
                // 如果总长度是奇数，中位数就是左边部分的最大值
                if ((m + n) % 2 == 1) {
                    return maxOfLeft;
                }
                
                int minOfRight;
                // 处理边界情况，如果 i == m 则 nums1 没有右边部分，最小值来自 nums2
                if (i == m) { minOfRight = nums2[j]; }
                // 如果 j == n 则 nums2 没有右边部分，最小值来自 nums1
                else if (j == n) { minOfRight = nums1[i]; }
                // 否则，最小值为 nums1 和 nums2 右边部分的最小值
                else { minOfRight = Math.min(nums1[i], nums2[j]); }
                
                // 如果总长度是偶数，中位数为左边最大值和右边最小值的平均
                return (maxOfLeft + minOfRight) / 2.0;
            }
        }
        return 0.0;  // 符合题意的输入不会到这里
    }

    public static void main(String[] args) {
        int[] nums1 = {1, 3};
        int[] nums2 = {2};
        System.out.println("中位数是: " + findMedianSortedArrays(nums1, nums2));

        int[] nums1_2 = {1, 2};
        int[] nums2_2 = {3, 4};
        System.out.println("中位数是: " + findMedianSortedArrays(nums1_2, nums2_2));
    }
}
```

#### Python

```
def findMedianSortedArrays(nums1, nums2):
    # 确保 nums1 是较短的数组，以便二分查找的范围更小
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2  # 二分查找中 nums1 的划分位置
        j = half_len - i  # 对应 nums2 的划分位置

        # 检查划分是否合适，i 太小，需要右移
        if i < m and nums1[i] < nums2[j-1]:
            imin = i + 1
        # i 太大，需要左移
        elif i > 0 and nums1[i-1] > nums2[j]:
            imax = i - 1
        # 找到了合适的划分位置
        else:
            # 处理边界情况，如果 i == 0 则 nums1 没有左边部分，最大值来自 nums2
            if i == 0:
                max_of_left = nums2[j-1]
            # 如果 j == 0 则 nums2 没有左边部分，最大值来自 nums1
            elif j == 0:
                max_of_left = nums1[i-1]
            # 否则，最大值为 nums1 和 nums2 左边部分的最大值
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])
            
            # 如果总长度是奇数，中位数就是左边部分的最大值
            if (m + n) % 2 == 1:
                return max_of_left
            
            # 处理边界情况，如果 i == m 则 nums1 没有右边部分，最小值来自 nums2
            if i == m:
                min_of_right = nums2[j]
            # 如果 j == n 则 nums2 没有右边部分，最小值来自 nums1
            elif j == n:
                min_of_right = nums1[i]
            # 否则，最小值为 nums1 和 nums2 右边部分的最小值
            else:
                min_of_right = min(nums1[i], nums2[j])
            
            # 如果总长度是偶数，中位数为左边最大值和右边最小值的平均
            return (max_of_left + min_of_right) / 2.0

    return 0.0  # 符合题意的输入不会到这里

# 测试用例
nums1 = [1, 3]
nums2 = [2]
print("中位数是:", findMedianSortedArrays(nums1, nums2))

nums1_2 = [1, 2]
nums2_2 = [3, 4]
print("中位数是:", findMedianSortedArrays(nums1_2, nums2_2))
```

