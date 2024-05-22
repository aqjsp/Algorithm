# 面试经典算法题53-搜索插入位置

LeetCode.35

### 问题描述

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

**示例 1:**

```
输入: nums = [1,3,5,6], target = 5
输出: 2
```

**示例 2:**

```
输入: nums = [1,3,5,6], target = 2
输出: 1
```

**示例 3:**

```
输入: nums = [1,3,5,6], target = 7
输出: 4
```

### 思路

1. 定义左右边界：定义左右指针，分别指向数组的起始和结束位置。
2. 二分查找：计算中间位置的索引，并将中间位置的值与目标值进行比较。
3. 调整边界：
   - 如果中间位置的值等于目标值，直接返回中间位置的索引。
   - 如果中间位置的值小于目标值，将左边界指针移动到中间位置的右侧，即 `left = mid + 1`。
   - 如果中间位置的值大于目标值，将右边界指针移动到中间位置的左侧，即 `right = mid - 1`。
4. **插入位置**：如果没有找到目标值，当 `left` 大于 `right` 时，`left` 就是目标值应当插入的位置。

### 图解

1. 定义左右指针，分别指向数组的起始和结束位置。

![1](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405230006413.png)

2. 当left <= right时，计算mid=left + (right - left) / 2

![2](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405230009677.png)

3. 中间位置的值小于目标值，将左边界指针移动到中间位置的右侧，即 `left = mid + 1`。

![3](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405230009099.png)

4. 当left <= right时，继续计算mid=left + (right - left) / 2

![4](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405230013877.png)

5. 中间位置的值等于目标值，直接返回中间位置的索引。返回left，即left=2。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
using namespace std;

int searchInsert(vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;
    
    // 二分查找
    while (left <= right) {
        int mid = left + (right - left) / 2; // 避免溢出，等同于 (left + right) / 2
        if (nums[mid] == target) {
            return mid; // 找到目标值，返回其索引
        } else if (nums[mid] < target) {
            left = mid + 1; // 目标值在右半部分
        } else {
            right = mid - 1; // 目标值在左半部分
        }
    }
    
    // 没有找到目标值，返回插入位置
    return left;
}

int main() {
    vector<int> nums = {1, 3, 5, 6};
    int target;
    cout << "请输入目标值：";
    cin >> target;
    
    int index = searchInsert(nums, target);
    cout << "目标值应插入的位置索引为：" << index << endl;
    
    return 0;
}
```

#### Java

```
import java.util.Scanner;

public class SearchInsertPosition {

    public static int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        
        // 二分查找
        while (left <= right) {
            int mid = left + (right - left) / 2; // 避免溢出，等同于 (left + right) / 2
            if (nums[mid] == target) {
                return mid; // 找到目标值，返回其索引
            } else if (nums[mid] < target) {
                left = mid + 1; // 目标值在右半部分
            } else {
                right = mid - 1; // 目标值在左半部分
            }
        }
        
        // 没有找到目标值，返回插入位置
        return left;
    }

    public static void main(String[] args) {
        int[] nums = {1, 3, 5, 6};
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("请输入目标值：");
        int target = scanner.nextInt();
        
        int index = searchInsert(nums, target);
        System.out.println("目标值应插入的位置索引为：" + index);
        
        scanner.close();
    }
}
```

#### Python

```
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    # 二分查找
    while left <= right:
        mid = left + (right - left) // 2  # 避免溢出，等同于 (left + right) // 2
        if nums[mid] == target:
            return mid  # 找到目标值，返回其索引
        elif nums[mid] < target:
            left = mid + 1  # 目标值在右半部分
        else:
            right = mid - 1  # 目标值在左半部分
    
    # 没有找到目标值，返回插入位置
    return left

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = int(input("请输入目标值："))
    
    index = search_insert(nums, target)
    print("目标值应插入的位置索引为：", index)
```

