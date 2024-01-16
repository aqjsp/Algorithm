# 哈希

## 1、两数之和

### 1.1、问题描述

给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。

（注：返回的数组下标从1开始算起，保证target一定可以由数组里面2个数字相加得到）

> **示例1**
>
> 输入：[3,2,4],6
>
> 返回值：[2,3]
>
> 说明：因为 2+4=6 ，而 2的下标为2 ， 4的下标为3 ，又因为 下标2 < 下标3 ，所以返回[2,3]            
>
> **示例2**
>
> 输入：[20,70,110,150],90
>
> 返回值：[1,2]
>
> 说明：20+70=90  

### 1.2、思路及代码

思路：

1. 创建一个哈希表（unordered_map）来存储数组中的元素和它们的下标。
2. 遍历数组，对于每个元素 `numbers[i]`，检查 `target - numbers[i]` 是否存在于哈希表中。
3. 如果存在，说明找到了两个数，它们的和等于 `target`，返回它们的下标。
4. 如果不存在，将当前元素 `numbers[i]` 加入哈希表，键为元素值，值为元素下标。
5. 如果遍历完数组仍然没有找到满足条件的两个数，根据题目要求返回一个非零索引（题目要求索引从 1 开始），可以设置一个初始值为 -1 的变量 `index1` 和 `index2`，在遍历的过程中，如果找到答案，将 `index1` 和 `index2` 分别设置为 `i` 和哈希表中 `target - numbers[i]` 对应的值（即第一个数的下标），并将它们加 1（因为题目要求索引从 1 开始）。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int>& numbers, int target) {
    std::vector<int> result;
    std::unordered_map<int, int> numToIndex; // 哈希表

    int index1 = -1, index2 = -1; // 初始化索引

    for (int i = 0; i < numbers.size(); i++) {
        int complement = target - numbers[i]; // 计算补数

        if (numToIndex.find(complement) != numToIndex.end()) {
            // 找到满足条件的两个数
            index1 = i;
            index2 = numToIndex[complement];
            break;
        }

        numToIndex[numbers[i]] = i; // 将当前数和下标加入哈希表
    }

    result.push_back(index2 + 1); // 为了满足题目要求，索引从 1 开始
    result.push_back(index1 + 1);

    return result;
}

int main() {
    std::vector<int> numbers = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> result = twoSum(numbers, target);

    std::cout << "两个数的索引为: " << result[0] << " 和 " << result[1] << std::endl;

    return 0;
}
```

## 2、**数组中出现次数超过一半的数字**

### 2.1、问题描述

给一个长度为 n 的数组，数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。

> **示例1**
>
> 输入：[1,2,3,2,2,2,5,4,2]
>
> 返回值：2
>
> **示例2**
>
> 输入：[3,3,3,3,2,2,2]
>
> 返回值：3
>
> **示例3**
>
> 输入：[1]
>
> 返回值：1

### 2.2、思路及代码

思路：

1. 初始化两个变量 `candidate` 和 `count`。`candidate` 用于存储可能的多数元素，`count` 用于跟踪 `candidate` 的出现次数。
2. 遍历数组，对于每个元素：
   1. 如果 `count` 为 0，将当前元素赋值给 `candidate`，并将 `count` 设置为 1。
   2. 如果当前元素与 `candidate` 相同，增加 `count`。
   3. 如果当前元素与 `candidate` 不同，减少 `count`。
3. 在遍历完整个数组后，`candidate` 可能是多数元素。
4. 最后，需要再次遍历数组，统计 `candidate` 的出现次数，确保它的出现次数确实超过数组长度的一半。

参考代码：

```C++
#include <iostream>
#include <vector>

int majorityElement(std::vector<int>& nums) {
    int candidate = 0; // 候选元素
    int count = 0; // 候选元素的计数

    for (int num : nums) {
        if (count == 0) {
            candidate = num; // 如果计数为0，设置当前元素为候选元素
            count = 1;
        } else if (num == candidate) {
            count++; // 如果当前元素与候选元素相同，增加计数
        } else {
            count--; // 如果当前元素与候选元素不同，减少计数
        }
    }

    // 现在的candidate可能是多数元素，需要再次遍历数组确认
    count = 0;
    for (int num : nums) {
        if (num == candidate) {
            count++;
        }
    }

    // 如果count超过一半数组长度，candidate即为多数元素
    if (count > nums.size() / 2) {
        return candidate;
    }
    return -1; // 如果没有多数元素，返回-1或者其他适当的值
}

int main() {
    std::vector<int> nums = {1, 2, 3, 2, 2, 2, 5, 4, 2};
    int result = majorityElement(nums);
    
    if (result != -1) {
        std::cout << "出现次数超过一半的元素是: " << result << std::endl;
    } else {
        std::cout << "没有出现次数超过一半的元素" << std::endl;
    }
    
    return 0;
}
```

## 3、**数组中只出现一次的两个数字**

### 3.1、问题描述

一个整型数组里除了两个数字只出现一次，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

> **示例1**
>
> 输入：[1,4,1,6]
>
> 返回值：[4,6]
>
> 说明：返回的结果中较小的数排在前面     
>
> **示例2**
>
> 输入：[1,2,3,3,2,9]
>
> 返回值：[1,9]

### 3.2、思路及代码

思路：

首先，我们需要了解异或操作的性质：

1. 任何数与自身异或的结果为0：`a ^ a = 0`
2. 任何数与0异或的结果仍为自身：`a ^ 0 = a`
3. 异或操作满足交换律：`a ^ b = b ^ a`

根据这些性质，我们可以设计一个算法来找到数组中仅出现一次的两个数字：

1. 遍历整个数组并计算所有数字的异或结果。由于相同的数字异或为0，因此最终的异或结果将是两个不同数字的异或结果。
2. 找出异或结果中的任意一位为1的位，可以使用一个标志位来实现，例如，假设最右边的为1的位是第n位，那么我们可以将数组中的数字分成两组，一组是第n位为1的数字，另一组是第n位为0的数字。
3. 接下来，对这两组数字分别执行异或操作，分别得到两个独立的数字。这两个数字就是数组中仅出现一次的两个数字。

参考代码：

```C++
#include <iostream>
#include <vector>

std::vector<int> FindNumbersAppearOnce(std::vector<int>& nums) {
    std::vector<int> result;

    int xorResult = 0;
    for (int num : nums) {
        xorResult ^= num; // 计算所有数字的异或结果
    }

    // 找到异或结果中最右边的为1的位
    int bitPosition = 0;
    while ((xorResult & 1) == 0) {
        xorResult >>= 1;
        bitPosition++;
    }

    int group1 = 0;
    int group2 = 0;

    // 根据bitPosition将数组分为两组并分别执行异或操作
    for (int num : nums) {
        if (((num >> bitPosition) & 1) == 0) {
            group1 ^= num;
        } else {
            group2 ^= num;
        }
    }

    result.push_back(group1);
    result.push_back(group2);

    return result;
}

int main() {
    std::vector<int> nums = {4, 5, 6, 7, 7, 6, 9, 9};
    std::vector<int> result = FindNumbersAppearOnce(nums);

    std::cout << "仅出现一次的两个数字分别是: " << result[0] << " 和 " << result[1] << std::endl;

    return 0;
}
```

## 4、**缺失的第一个正整数**

### 4.1、问题描述

给定一个无重复元素的整数数组nums，请你找出其中没有出现的最小的正整数

进阶： 空间复杂度 *O*(1)，时间复杂度*O*(*n*)

> **示例1**
>
> 输入：[1,0,2]
>
> 返回值：3
>
> **示例2**
>
> 输入：[-2,3,4,1,5]
>
> 返回值：2
>
> **示例3**
>
> 输入：[4,5,6,8,9]
>
> 返回值：1

### 4.2、思路及代码

思路：

1. 遍历数组 `nums`，将每个元素调整到正确的位置上。如果元素 `x` 在区间 `[1, n]` 内，就将它放到索引 `x-1` 处。我们只关心正整数，忽略负数和大于 `n` 的数。
2. 再次遍历数组，找到第一个不在正确位置上的元素，其索引加 1 即为缺失的最小正整数。

参考代码：

```C++
#include <iostream>
#include <vector>

int firstMissingPositive(std::vector<int>& nums) {
    int n = nums.size();

    // 第一次遍历，将元素放到正确的位置上
    for (int i = 0; i < n; i++) {
        while (nums[i] > 0 && nums[i] <= n && nums[i] != nums[nums[i] - 1]) {
            std::swap(nums[i], nums[nums[i] - 1]);
        }
    }

    // 第二次遍历，找到第一个不在正确位置上的元素
    for (int i = 0; i < n; i++) {
        if (nums[i] != i + 1) {
            return i + 1;
        }
    }

    // 如果数组本身是 [1,2,3,...,n]，返回 n + 1
    return n + 1;
}

int main() {
    std::vector<int> nums = {3, 4, -1, 1};
    int result = firstMissingPositive(nums);
    std::cout << "没有出现的最小正整数是: " << result << std::endl;

    return 0;
}
```

## 5、三数之和

### 5.1、问题描述

给出一个有n个元素的数组S，S中是否有元素a,b,c满足a+b+c=0？找出数组S中所有满足条件的三元组。

> 注意：
>
> 1. 三元组（a、b、c）中的元素必须按非降序排列。（即a≤b≤c）
> 2. 解集中不能包含重复的三元组。
>
> 例如，给定的数组 S = {-10 0 10 20 -10 -40},解集为(-10, -10, 20),(-10, 0, 10) 
>
> **示例1**
>
> 输入：[0]
>
> 返回值：[]
>
> **示例2**
>
> 输入：[-2,0,1,1,2]
>
> 返回值：[[-2,0,2],[-2,1,1]]
>
> **示例3**
>
> 输入：[-10,0,10,20,-10,-40]
>
> 返回值：[[-10,-10,20],[-10,0,10]]

### 5.2、思路及代码

思路：

可以利用双指针法来查找三元组。首先，我们对数组 `S` 进行排序。然后，我们可以使用两层循环遍历数组，以第一个循环中的元素作为固定值 `a`，并使用双指针来查找满足 `b + c = -a` 的 `b` 和 `c`。

具体步骤：

1. 首先对数组 `S` 进行排序，以便在查找过程中使用双指针。
2. 固定一个元素 `a`，从左到右遍历数组。
3. 使用双指针法在当前 `a` 的右侧查找两个元素 `b` 和 `c`，使得 `b + c = -a`。这需要将左指针指向 `b` 的位置，右指针指向 `c` 的位置。
4. 在双指针的过程中，需要注意去重处理，避免出现重复的三元组。
5. 当找到一个满足条件的三元组时，将它添加到结果中。
6. 继续遍历数组，继续寻找下一个 `a` 值的三元组。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <algorithm>

std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
    std::vector<std::vector<int>> result;
    int n = nums.size();
    if (n < 3) {
        return result; // 如果数组长度小于 3，无法组成三元组
    }
    
    std::sort(nums.begin(), nums.end()); // 先对数组排序
    
    for (int i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue; // 避免重复固定值
        }
        
        int a = nums[i]; // 固定第一个值 a
        
        int left = i + 1; // 左指针，指向第二个值
        int right = n - 1; // 右指针，指向最后一个值
        
        while (left < right) {
            int b = nums[left]; // 第二个值 b
            int c = nums[right]; // 第三个值 c
            int sum = a + b + c;
            
            if (sum == 0) {
                result.push_back({a, b, c}); // 找到一个满足条件的三元组
                while (left < right && nums[left] == b) {
                    left++; // 避免重复的第二个值
                }
                while (left < right && nums[right] == c) {
                    right--; // 避免重复的第三个值
                }
            } else if (sum < 0) {
                left++; // 总和小于 0，移动左指针
            } else {
                right--; // 总和大于 0，移动右指针
            }
        }
    }
    
    return result;
}

int main() {
    std::vector<int> nums = {-1, 0, 1, 2, -1, -4};
    std::vector<std::vector<int>> result = threeSum(nums);
    
    std::cout << "满足条件的三元组为：" << std::endl;
    for (const auto& triple : result) {
        std::cout << "[";
        for (int i = 0; i < triple.size(); i++) {
            std::cout << triple[i];
            if (i < 2) {
                std::cout << ", ";
            }
        }
        std::cout << "]" << std::endl;
    }
    
    return 0;
}
```