# 面试经典算法题63-只出现一次的数字

LeetCode.136

### 问题描述

给你一个 **非空** 整数数组 `nums` ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

**示例 1 ：**

```
输入：nums = [2,2,1]
输出：1
```

**示例 2 ：**

```
输入：nums = [4,1,2,1,2]
输出：4
```

**示例 3 ：**

```
输入：nums = [1]
输出：1
```

### 思路

这里先给大家讲讲异或运算的一些性质吧。

```
1. 任何数和 0 做异或运算，结果仍然是原来的数，即 a ^ 0 = a。
2. 任何数和其自身做异或运算，结果是 0，即 a ^ a = 0。
3. 异或运算满足交换律和结合律。
```

具体思路：

1. **初始化一个变量 `result` 为 0**，用来存储最终结果。
2. **遍历数组中的每个元素**，对于当前元素，将其与 `result` 进行异或运算并将结果存储回 `result` 中。
3. **最终 `result` 中存储的就是只出现一次的元素**，因为成对出现的元素异或后结果为 0，而异或运算满足交换律和结合律，因此所有成对出现的元素都会被消除，只剩下只出现一次的元素。
4. **返回 `result` 即可**。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

int singleNumber(vector<int>& nums) {
    int result = 0;
    for (int num : nums) {
        // 对每个元素进行异或运算
        result ^= num;
    }
    return result;
}

int main() {
    // 示例输入
    vector<int> nums1 = {2, 2, 1};
    vector<int> nums2 = {4, 1, 2, 1, 2};
    vector<int> nums3 = {1};

    // 输出结果
    cout << "示例 1 输出：" << singleNumber(nums1) << endl;
    cout << "示例 2 输出：" << singleNumber(nums2) << endl;
    cout << "示例 3 输出：" << singleNumber(nums3) << endl;

    return 0;
}
```

#### Java

```
public class SingleNumber {
    public static int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }

    public static void main(String[] args) {
        // 示例输入
        int[] nums1 = {2, 2, 1};
        int[] nums2 = {4, 1, 2, 1, 2};
        int[] nums3 = {1};

        // 输出结果
        System.out.println("示例 1 输出：" + singleNumber(nums1));
        System.out.println("示例 2 输出：" + singleNumber(nums2));
        System.out.println("示例 3 输出：" + singleNumber(nums3));
    }
}
```

#### Python

```
from typing import List

def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

# 示例输入
nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1]

# 输出结果
print("示例 1 输出：", singleNumber(nums1))
print("示例 2 输出：", singleNumber(nums2))
print("示例 3 输出：", singleNumber(nums3))
```

