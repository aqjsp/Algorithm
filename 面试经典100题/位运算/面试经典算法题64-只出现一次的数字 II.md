# 面试经典算法题64-只出现一次的数字 II

LeetCode.137

### 问题描述

给你一个整数数组 `nums` ，除某个元素仅出现 **一次** 外，其余每个元素都恰出现 **三次 。**请你找出并返回那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。

**示例 1：**

```
输入：nums = [2,2,3,2]
输出：3
```

**示例 2：**

```
输入：nums = [0,1,0,1,0,1,99]
输出：99
```

### 思路

**位运算统计法**：

- 初始化32个整型变量，分别表示二进制数的32位。
- 遍历数组中的每一个数，统计每个数的每一位的1的出现次数。
- 对每一位的1的出现次数取模3，结果就是只出现一次的那个数在该位上的值。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

int singleNumber(const vector<int>& nums) {
    // 初始化一个长度为32的数组来存储每一位的出现次数
    int bits[32] = {0};
    
    // 遍历每个数字，统计每一位上1的出现次数
    for (int num : nums) {
        for (int i = 0; i < 32; ++i) {
            bits[i] += (num >> i) & 1;
        }
    }
    
    // 将每一位的出现次数对3取模，得到只出现一次的那个数
    int result = 0;
    for (int i = 0; i < 32; ++i) {
        if (bits[i] % 3 != 0) {
            result |= (1 << i);
        }
    }
    
    return result;
}

int main() {
    // 示例输入
    vector<int> nums1 = {2, 2, 3, 2};
    vector<int> nums2 = {0, 1, 0, 1, 0, 1, 99};

    // 输出结果
    cout << "示例 1 输出：" << singleNumber(nums1) << endl;
    cout << "示例 2 输出：" << singleNumber(nums2) << endl;

    return 0;
}
```

#### Java

```
public class SingleNumber {
    public static int singleNumber(int[] nums) {
        // 初始化一个长度为32的数组来存储每一位的出现次数
        int[] bits = new int[32];
        
        // 遍历每个数字，统计每一位上1的出现次数
        for (int num : nums) {
            for (int i = 0; i < 32; ++i) {
                bits[i] += (num >> i) & 1;
            }
        }
        
        // 将每一位的出现次数对3取模，得到只出现一次的那个数
        int result = 0;
        for (int i = 0; i < 32; ++i) {
            if (bits[i] % 3 != 0) {
                result |= (1 << i);
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        // 示例输入
        int[] nums1 = {2, 2, 3, 2};
        int[] nums2 = {0, 1, 0, 1, 0, 1, 99};

        // 输出结果
        System.out.println("示例 1 输出：" + singleNumber(nums1));
        System.out.println("示例 2 输出：" + singleNumber(nums2));
    }
}
```

#### Python

```
from typing import List

def singleNumber(nums: List[int]) -> int:
    # 初始化一个长度为32的数组来存储每一位的出现次数
    bits = [0] * 32
    
    # 遍历每个数字，统计每一位上1的出现次数
    for num in nums:
        for i in range(32):
            bits[i] += (num >> i) & 1
    
    # 将每一位的出现次数对3取模，得到只出现一次的那个数
    result = 0
    for i in range(32):
        if bits[i] % 3 != 0:
            result |= (1 << i)
    
    # 处理负数的情况
    if result >= 2**31:
        result -= 2**32

    return result

# 示例输入
nums1 = [2, 2, 3, 2]
nums2 = [0, 1, 0, 1, 0, 1, 99]

# 输出结果
print("示例 1 输出：", singleNumber(nums1))
print("示例 2 输出：", singleNumber(nums2))
```

