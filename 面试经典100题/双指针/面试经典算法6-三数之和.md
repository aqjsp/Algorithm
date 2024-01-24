## 三数之和

LeetCode.15

### 问题描述

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请

你返回所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

**示例 1：**

```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
```

**示例 2：**

```
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
```

**示例 3：**

```
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
```

 **提示：**

- `3 <= nums.length <= 3000`
- `-105 <= nums[i] <= 105`

### 思路

1. 首先，我们对输入的整数数组进行排序。这有助于我们后面的双指针操作。排序后的数组可以使我们更容易找到解决方案，因为它们将有序排列在一起，我们可以在有限的步骤内找到所有解决方案。
2. 对于每个元素 `nums[i]`，我们都将它作为固定的第一个元素，并将问题转化为在剩余数组中寻找两数之和等于 `0 - nums[i]` 的问题。
3. 对于每个固定的元素 `nums[i]`，我们使用双指针技巧来找到剩余数组中满足条件的两个数。我们将左指针 `left` 指向剩余数组的起始位置，右指针 `right` 指向剩余数组的末尾位置。
4. 我们计算当前三个数的和 `sum`，如果 `sum` 等于 `0`，则找到一个满足条件的三元组 `[nums[i], nums[left], nums[right]]`，将其添加到结果数组中。然后，我们移动左右指针来寻找下一个解。如果 `sum` 小于 `0`，说明左边的数太小，左指针右移；如果 `sum` 大于 `0`，说明右边的数太大，右指针左移。
5. 在移动指针时，我们要注意跳过重复的元素，以避免得到重复的解。例如，如果 `nums[left]` 和 `nums[left + 1]` 相等，我们将左指针右移一位；如果 `nums[right]` 和 `nums[right - 1]` 相等，我们将右指针左移一位。
6. 最后，我们返回包含所有满足条件的三元组的结果数组。

### 演示过程

使用示例1来给大家做个演示，根据题目要求，我们首先需要将数组进行排序。得到nums = [-4,-1,-1,0,1,2]

1. 先固定首个元素，然后将第i+1初始化为left，nums.size()-1初始化为right，这样就将问题转换为两数之和，继续看看。

![image-20240124201829070](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401242019400.png)

此时，sum = nums[i] + nums[left] + nums[right] = -3 < 0

2. 将左指针右移

![image-20240124202632797](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401242026795.png)

此时，sum = nums[i] + nums[left] + nums[right] = -3 < 0

3. 将左指针右移

![image-20240124202923740](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401242029296.png)

此时，sum = nums[i] + nums[left] + nums[right] = -2 < 0

4. 将左指针右移

![image-20240124203023113](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401242030502.png)

此时，sum = nums[i] + nums[left] + nums[right] = -1 < 0

5. 将左指针右移

![image-20240124203137491](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401242031676.png)

跳出循环。

6. 继续将固定的向右移动

![image-20240124204137752](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401242041262.png)

此时，sum = nums[i] + nums[left] + nums[right] = 0，将结果加进结果数组，即result.push_back(-1,-1,2)

7. nums[left] != nums[left+1]，nums[right] != nums[right-1]，将左指针右移一位，将右指针左移一位

![image-20240124204619507](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401242046977.png)

此时，sum = nums[i] + nums[left] + nums[right] = 0，将结果加进结果数组，即result.push_back(-1,0,1)

继续移动左右指针，跳出循环。

演示到这儿就可以了，大家应该也可以根据我给的步骤继续完成后边的。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> result; // 存放结果的二维数组
        std::sort(nums.begin(), nums.end()); // 对数组进行排序，方便后续的双指针操作

        int n = nums.size();
        for (int i = 0; i < n - 2; ++i) { // 固定第一个数，转化为求两数之和的问题
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue; // 跳过重复的数字，避免重复解
            }
            int left = i + 1, right = n - 1; // 双指针分别指向剩余数组的两端
            while (left < right) { // 双指针遍历剩余数组
                int sum = nums[i] + nums[left] + nums[right]; // 计算当前三个数的和
                if (sum == 0) { // 如果和为0，找到一个满足条件的三元组
                    result.push_back({nums[i], nums[left], nums[right]}); // 将满足条件的三元组加入结果数组
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++; // 跳过重复的数字，避免重复解
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--; // 跳过重复的数字，避免重复解
                    }
                    left++; // 移动左指针，继续寻找下一个解
                    right--; // 移动右指针，继续寻找下一个解
                } else if (sum < 0) { // 如果和小于0，说明左边的数太小，左指针右移
                    left++;
                } else { // 如果和大于0，说明右边的数太大，右指针左移
                    right--;
                }
            }
        }

        return result; // 返回结果数组
    }
};

int main() {
    Solution solution;
    std::vector<int> nums = {-1, 0, 1, 2, -1, -4};
    std::vector<std::vector<int>> result = solution.threeSum(nums);
    for (const auto& triplet : result) { // 遍历结果数组并输出每个满足条件的三元组
        std::cout << "[";
        for (int num : triplet) {
            std::cout << num << ", ";
        }
        std::cout << "]" << std::endl;
    }
    return 0;
}
```

#### Java

```
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums); // 对数组进行排序，方便后续的双指针操作

        int n = nums.length;
        for (int i = 0; i < n - 2; ++i) { // 固定第一个数，转化为求两数之和的问题
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue; // 跳过重复的数字，避免重复解
            }
            int left = i + 1, right = n - 1; // 双指针分别指向剩余数组的两端
            while (left < right) { // 双指针遍历剩余数组
                int sum = nums[i] + nums[left] + nums[right]; // 计算当前三个数的和
                if (sum == 0) { // 如果和为0，找到一个满足条件的三元组
                    result.add(Arrays.asList(nums[i], nums[left], nums[right])); // 将满足条件的三元组加入结果数组
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++; // 跳过重复的数字，避免重复解
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--; // 跳过重复的数字，避免重复解
                    }
                    left++; // 移动左指针，继续寻找下一个解
                    right--; // 移动右指针，继续寻找下一个解
                } else if (sum < 0) { // 如果和小于0，说明左边的数太小，左指针右移
                    left++;
                } else { // 如果和大于0，说明右边的数太大，右指针左移
                    right--;
                }
            }
        }

        return result; // 返回结果数组
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {-1, 0, 1, 2, -1, -4};
        List<List<Integer>> result = solution.threeSum(nums);
        for (List<Integer> triplet : result) { // 遍历结果数组并输出每个满足条件的三元组
            System.out.print("[");
            for (int num : triplet) {
                System.out.print(num + ", ");
            }
            System.out.println("]");
        }
    }
}
```

#### Python

```
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [] # 存放结果的列表
        nums.sort() # 对数组进行排序，方便后续的双指针操作

        n = len(nums)
        for i in range(n - 2): # 固定第一个数，转化为求两数之和的问题
            if i > 0 and nums[i] == nums[i - 1]:
                continue # 跳过重复的数字，避免重复解
            left, right = i + 1, n - 1 # 双指针分别指向剩余数组的两端
            while left < right: # 双指针遍历剩余数组
                total = nums[i] + nums[left] + nums[right] # 计算当前三个数的和
                if total == 0: # 如果和为0，找到一个满足条件的三元组
                    result.append([nums[i], nums[left], nums[right]]) # 将满足条件的三元组加入结果数组
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 # 跳过重复的数字，避免重复解
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 # 跳过重复的数字，避免重复解
                    left += 1 # 移动左指针，继续寻找下一个解
                    right -= 1 # 移动右指针，继续寻找下一个解
                elif total < 0: # 如果和小于0，说明左边的数太小，左指针右移
                    left += 1
                else: # 如果和大于0，说明右边的数太大，右指针左移
                    right -= 1

        return result # 返回结果列表

if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(nums)
    for triplet in result: # 遍历结果列表并输出每个满足条件的三元组
        print(triplet)
```
