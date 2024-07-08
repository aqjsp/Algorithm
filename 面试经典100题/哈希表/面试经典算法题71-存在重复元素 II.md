# 面试经典算法题71-存在重复元素 II

LeetCode.219

### 问题描述

给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引** `i` 和 `j` ，满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k` 。如果存在，返回 `true` ；否则，返回 `false` 。

**示例 1：**

```
输入：nums = [1,2,3,1], k = 3
输出：true
```

**示例 2：**

```
输入：nums = [1,0,1,1], k = 1
输出：true
```

**示例 3：**

```
输入：nums = [1,2,3,1,2,3], k = 2
输出：false
```

### 思路

1. 遍历数组：我们需要遍历数组中的每个元素，并记录它们的索引。
2. 哈希表：使用一个哈希表（unordered_map）来存储每个元素及其最近一次出现的索引。
3. 检查条件：在遍历的过程中，如果当前元素在哈希表中已经存在，则检查当前索引与哈希表中记录的索引之差是否小于等于 kkk。如果是，返回 `true`。否则，更新哈希表中该元素的索引为当前索引。
4. 遍历结束：如果遍历结束后没有找到符合条件的索引对，返回 `false`。

### 参考代码

#### C++

```
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>

// 判断数组中是否存在两个不同的索引 i 和 j 满足 nums[i] == nums[j] 且 abs(i - j) <= k
bool containsNearbyDuplicate(const std::vector<int>& nums, int k) {
    // 创建一个哈希表，键为数组元素，值为该元素最后一次出现的索引
    std::unordered_map<int, int> index_map;
    
    // 遍历数组
    for (int i = 0; i < nums.size(); ++i) {
        // 检查当前元素是否已经在哈希表中存在
        if (index_map.find(nums[i]) != index_map.end()) {
            // 如果当前索引与哈希表中记录的索引之差小于等于 k，则返回 true
            if (i - index_map[nums[i]] <= k) {
                return true;
            }
        }
        // 更新哈希表中该元素的索引为当前索引
        index_map[nums[i]] = i;
    }
    
    // 遍历结束后没有找到符合条件的索引对，返回 false
    return false;
}

// 主函数
int main() {
    // 示例 1
    std::vector<int> nums1 = {1, 2, 3, 1};
    int k1 = 3;
    std::cout << "输入：nums = [1, 2, 3, 1], k = 3" << std::endl;
    std::cout << "输出：" << (containsNearbyDuplicate(nums1, k1) ? "true" : "false") << std::endl;

    // 示例 2
    std::vector<int> nums2 = {1, 0, 1, 1};
    int k2 = 1;
    std::cout << "输入：nums = [1, 0, 1, 1], k = 1" << std::endl;
    std::cout << "输出：" << (containsNearbyDuplicate(nums2, k2) ? "true" : "false") << std::endl;

    // 示例 3
    std::vector<int> nums3 = {1, 2, 3, 1, 2, 3};
    int k3 = 2;
    std::cout << "输入：nums = [1, 2, 3, 1, 2, 3], k = 2" << std::endl;
    std::cout << "输出：" << (containsNearbyDuplicate(nums3, k3) ? "true" : "false") << std::endl;

    return 0;
}
```

#### Java

```
import java.util.HashMap;
import java.util.Map;

public class ContainsNearbyDuplicate {

    // 判断数组中是否存在两个不同的索引 i 和 j 满足 nums[i] == nums[j] 且 abs(i - j) <= k
    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        // 创建一个哈希表，键为数组元素，值为该元素最后一次出现的索引
        Map<Integer, Integer> indexMap = new HashMap<>();
        
        // 遍历数组
        for (int i = 0; i < nums.length; i++) {
            // 检查当前元素是否已经在哈希表中存在
            if (indexMap.containsKey(nums[i])) {
                // 如果当前索引与哈希表中记录的索引之差小于等于 k，则返回 true
                if (i - indexMap.get(nums[i]) <= k) {
                    return true;
                }
            }
            // 更新哈希表中该元素的索引为当前索引
            indexMap.put(nums[i], i);
        }
        
        // 遍历结束后没有找到符合条件的索引对，返回 false
        return false;
    }

    // 主函数
    public static void main(String[] args) {
        // 示例 1
        int[] nums1 = {1, 2, 3, 1};
        int k1 = 3;
        System.out.println("输入：nums = [1, 2, 3, 1], k = 3");
        System.out.println("输出：" + (containsNearbyDuplicate(nums1, k1) ? "true" : "false"));

        // 示例 2
        int[] nums2 = {1, 0, 1, 1};
        int k2 = 1;
        System.out.println("输入：nums = [1, 0, 1, 1], k = 1");
        System.out.println("输出：" + (containsNearbyDuplicate(nums2, k2) ? "true" : "false"));

        // 示例 3
        int[] nums3 = {1, 2, 3, 1, 2, 3};
        int k3 = 2;
        System.out.println("输入：nums = [1, 2, 3, 1, 2, 3], k = 2");
        System.out.println("输出：" + (containsNearbyDuplicate(nums3, k3) ? "true" : "false"));
    }
}
```

#### Python

```
def containsNearbyDuplicate(nums, k):
    """
    判断数组中是否存在两个不同的索引 i 和 j ，
    满足 nums[i] == nums[j] 且 abs(i - j) <= k
    """
    # 创建一个字典，键为数组元素，值为该元素最后一次出现的索引
    index_map = {}

    # 遍历数组
    for i, num in enumerate(nums):
        # 检查当前元素是否已经在字典中存在
        if num in index_map:
            # 如果当前索引与字典中记录的索引之差小于等于 k，则返回 True
            if i - index_map[num] <= k:
                return True
        # 更新字典中该元素的索引为当前索引
        index_map[num] = i
    
    # 遍历结束后没有找到符合条件的索引对，返回 False
    return False

# 主函数
if __name__ == "__main__":
    # 示例 1
    nums1 = [1, 2, 3, 1]
    k1 = 3
    print("输入：nums = [1, 2, 3, 1], k = 3")
    print("输出：", containsNearbyDuplicate(nums1, k1))  # 输出: True

    # 示例 2
    nums2 = [1, 0, 1, 1]
    k2 = 1
    print("输入：nums = [1, 0, 1, 1], k = 1")
    print("输出：", containsNearbyDuplicate(nums2, k2))  # 输出: True

    # 示例 3
    nums3 = [1, 2, 3, 1, 2, 3]
    k3 = 2
    print("输入：nums = [1, 2, 3, 1, 2, 3], k = 2")
    print("输出：", containsNearbyDuplicate(nums3, k3))  # 输出: False
```

