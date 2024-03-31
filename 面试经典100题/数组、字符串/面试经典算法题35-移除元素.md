# 面试经典算法题35-移除元素

LeetCode.27

### 问题描述

给你一个数组 `nums` 和一个值 `val`，你需要 原地 移除所有数值等于 `val` 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 `O(1)` 额外空间并 原地。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

### 思路

#### 方法一  遍历 - 去除匹配项

1. 初始化一个变量 `count` 用于计数非给定值的元素。
2. 遍历数组，当遇到非给定值的元素时，将其移到数组的前面，并增加 `count`。
3. 修改数组的长度为 `count`，即可移除给定值的元素。

#### 方法二  双指针

1. 初始化两个指针：我们使用两个指针 `left` 和 `right`，初始时都指向数组的开头。
2. 遍历数组：遍历数组，当 `nums[right]` 等于给定值 `val` 时，右指针 `right` 向右移动一位；否则，将 `nums[right]` 的值赋给 `nums[left]`，并同时将 `left` 和 `right` 向右移动一位。
3. 返回新长度：遍历结束后，`left` 指向的位置即为新数组的长度。

#### 方法三  双指针 - 交换移除

1. 初始化两个指针 `left` 和 `right`，初始时 `left` 指向数组开头，`right` 指向数组末尾。
2. 当 `nums[left]` 等于给定值 `val` 时，将 `nums[left]` 与 `nums[right]` 交换，并将 `right` 向左移动一位。
3. 如果交换后的 `nums[left]` 仍然等于给定值 `val`，则继续交换直到 `nums[left]` 不等于 `val`。
4. 将 `left` 向右移动一位，重复步骤 2 和 3，直到 `left` 大于等于 `right`。
5. 返回新数组的长度，即 `left` 的值。

### 图解

### 方法一

![流程图](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403312314502.png)

#### 方法二

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403312332526.png)

### 参考代码

#### C++

##### 方法一

```
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0; // 初始化指针 i，指向数组的第一个位置
        for (int j = 0; j < nums.size(); ++j) { // 遍历数组，j指向当前处理的元素
            if (nums[j] != val) { // 如果当前元素不等于给定值
                nums[i] = nums[j]; // 将当前元素移动到指针 i 的位置，并同时移动指针 i
                ++i; // 指针 i 向后移动
            }
        }
        return i; // 返回新数组的长度，即指针 i 的值
    }
};

int main() {
    vector<int> nums = {3, 2, 2, 3}; // 输入数组
    int val = 3; // 给定值
    Solution solution;
    int result = solution.removeElement(nums, val); // 移除给定值并返回新数组长度
    cout << "新数组长度：" << result << endl; // 输出结果
    return 0;
}
```

##### 方法二

```
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0, right = 0; // 初始化左右指针
        while (right < nums.size()) { // 遍历数组
            if (nums[right] != val) { // 如果当前元素不等于给定值
                nums[left] = nums[right]; // 将当前元素赋值给左指针指向的位置
                left++; // 左指针向右移动一位
            }
            right++; // 右指针向右移动一位
        }
        return left; // 返回新数组的长度
    }
};

int main() {
    vector<int> nums = {3, 2, 2, 3}; // 输入数组
    int val = 3; // 给定值
    Solution solution;
    int result = solution.removeElement(nums, val); // 移除元素
    cout << "新数组长度：" << result << endl; // 输出结果

    return 0;
}
```

##### 方法三

```
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0, right = nums.size(); // 初始化左右指针，left指向数组开头，right指向数组末尾的下一个位置
        while (left < right) { // 循环直到左指针大于等于右指针
            if (nums[left] == val) { // 如果左指针指向的值等于给定值
                nums[left] = nums[right - 1]; // 将左指针指向的值与右指针前一个位置的值交换
                right--; // 缩小数组长度
            } else { // 如果左指针指向的值不等于给定值
                left++; // 左指针右移
            }
        }
        return left; // 返回新数组的长度，即左指针的值
    }
};

int main() {
    vector<int> nums = {3, 2, 2, 3}; // 输入数组
    int val = 3; // 给定值
    Solution solution;
    int result = solution.removeElement(nums, val); // 移除给定值并返回新数组长度
    cout << "新数组长度：" << result << endl; // 输出结果
    return 0;
}
```

#### Java

```
class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0; // 初始化指针 i，指向数组的第一个位置
        for (int j = 0; j < nums.length; ++j) { // 遍历数组，j指向当前处理的元素
            if (nums[j] != val) { // 如果当前元素不等于给定值
                nums[i] = nums[j]; // 将当前元素移动到指针 i 的位置，并同时移动指针 i
                ++i; // 指针 i 向后移动
            }
        }
        return i; // 返回新数组的长度，即指针 i 的值
    }
}

public class Main {
    public static void main(String[] args) {
        int[] nums = {3, 2, 2, 3}; // 输入数组
        int val = 3; // 给定值
        Solution solution = new Solution();
        int result = solution.removeElement(nums, val); // 移除给定值并返回新数组长度
        System.out.println("新数组长度：" + result); // 输出结果
    }
}
```

#### Python

```
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # 初始化指针 i，指向数组的第一个位置
        for j in range(len(nums)):  # 遍历数组，j指向当前处理的元素
            if nums[j] != val:  # 如果当前元素不等于给定值
                nums[i] = nums[j]  # 将当前元素移动到指针 i 的位置，并同时移动指针 i
                i += 1  # 指针 i 向后移动
        return i  # 返回新数组的长度，即指针 i 的值

# 测试代码
nums = [3, 2, 2, 3]  # 输入数组
val = 3  # 给定值
solution = Solution()
result = solution.removeElement(nums, val)  # 移除给定值并返回新数组长度
print("新数组长度：", result)  # 输出结果
```

