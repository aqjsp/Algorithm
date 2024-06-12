# 面试经典算法题59-寻找旋转排序数组中的最小值

LeetCode.153

### 问题描述

已知一个长度为 `n` 的数组，预先按照升序排列，经由 `1` 到 `n` 次 **旋转** 后，得到输入数组。例如，原数组 `nums = [0,1,2,4,5,6,7]` 在变化后可能得到：

- 若旋转 `4` 次，则可以得到 `[4,5,6,7,0,1,2]`
- 若旋转 `7` 次，则可以得到 `[0,1,2,4,5,6,7]`

注意，数组 `[a[0], a[1], a[2], ..., a[n-1]]` **旋转一次** 的结果为数组 `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]` 。

给你一个元素值 **互不相同** 的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 **最小元素** 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

**示例 1：**

```
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
```

**示例 2：**

```
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 3 次得到输入数组。
```

**示例 3：**

```
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
```

### 思路

1. 初始化指针：使用两个指针 `left` 和 `right` 分别指向数组的起始位置和结束位置。
2. 二分查找：
   - 计算中间位置 `mid`。
   - 如果 `nums[mid]` 小于 `nums[right]`，说明最小值在左半部分，包括 `mid`。
   - 否则，最小值在右半部分，不包括 `mid`。
3. 更新指针：根据比较结果更新 `left` 或 `right` 指针。
4. 结束条件：当 `left` 和 `right` 相遇时，`left` 或 `right` 指向的元素即为最小值。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

int findMin(vector<int>& nums) {
    int left = 0;
    int right = nums.size() - 1;
    
    // 使用二分查找法寻找最小值
    while (left < right) {
        int mid = left + (right - left) / 2; // 计算中间位置
        
        // 如果中间元素小于右边界元素，说明最小值在左半部分
        if (nums[mid] < nums[right]) {
            right = mid; // 最小值可能是 mid，因此不能排除 mid
        } else {
            left = mid + 1; // 最小值不在 mid，因此排除 mid
        }
    }
    
    // 最后 left 和 right 会相遇在最小值的位置
    return nums[left];
}

int main() {
    vector<int> nums;
    int n;
    
    cout << "请输入数组元素的数量: ";
    cin >> n;
    nums.resize(n);
    
    cout << "请输入数组元素(旋转后的数组): ";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    int minElement = findMin(nums);
    
    cout << "数组中的最小元素是: " << minElement << endl;
    
    return 0;
}
```

#### Java

```
import java.util.Scanner;

public class FindMinimumInRotatedSortedArray {
    public static int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        
        // 使用二分查找法寻找最小值
        while (left < right) {
            int mid = left + (right - left) / 2; // 计算中间位置
            
            // 如果中间元素小于右边界元素，说明最小值在左半部分
            if (nums[mid] < nums[right]) {
                right = mid; // 最小值可能是 mid，因此不能排除 mid
            } else {
                left = mid + 1; // 最小值不在 mid，因此排除 mid
            }
        }
        
        // 最后 left 和 right 会相遇在最小值的位置
        return nums[left];
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("请输入数组元素的数量: ");
        int n = scanner.nextInt();
        
        int[] nums = new int[n];
        
        System.out.print("请输入数组元素(旋转后的数组): ");
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }
        
        int minElement = findMin(nums);
        
        System.out.println("数组中的最小元素是: " + minElement);
        
        scanner.close();
    }
}
```

#### Python

```
def find_min(nums):
    left, right = 0, len(nums) - 1
    
    # 使用二分查找法寻找最小值
    while left < right:
        mid = left + (right - left) // 2  # 计算中间位置
        
        # 如果中间元素小于右边界元素，说明最小值在左半部分
        if nums[mid] < nums[right]:
            right = mid  # 最小值可能是 mid，因此不能排除 mid
        else:
            left = mid + 1  # 最小值不在 mid，因此排除 mid
    
    # 最后 left 和 right 会相遇在最小值的位置
    return nums[left]

if __name__ == "__main__":
    n = int(input("请输入数组元素的数量: "))
    nums = list(map(int, input("请输入数组元素(旋转后的数组): ").split()))
    
    min_element = find_min(nums)
    
    print("数组中的最小元素是:", min_element)
```

