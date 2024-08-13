# 面试经典算法题93-全排列

LeetCode.46

### 问题描述

给定一个不含重复数字的数组 `nums` ，返回其所有可能的全排列。你可以 按任意顺序 返回答案。

**示例 1：**

```
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**示例 2：**

```
输入：nums = [0,1]
输出：[[0,1],[1,0]]
```

**示例 3：**

```
输入：nums = [1]
输出：[[1]]
```

### 思路

1. 定义递归函数：

   - 定义一个递归函数，用于生成所有可能的排列。

   - 递归函数需要三个参数：当前选择的排列、已选择的元素列表和结果列表。

2. 终止条件：当当前排列的长度等于数组长度时，将当前排列加入结果列表。

3. 递归生成排列：遍历所有元素，对于未被选择的元素，选择该元素，递归处理剩余元素。

4. 回溯：每次递归返回时，回溯到上一个状态，移除最后添加的元素，继续尝试其他可能的元素。

5. 输出结果：最终生成的所有排列存储在一个结果列表中，返回该列表。

### 参考代码

#### C++

```
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    // 递归函数，用于生成全排列
    void backtrack(vector<int>& nums, vector<int>& current, vector<bool>& used, vector<vector<int>>& result) {
        // 终止条件，当当前排列长度等于数组长度时，将其加入结果列表
        if (current.size() == nums.size()) {
            result.push_back(current);
            return;
        }

        // 遍历所有元素
        for (int i = 0; i < nums.size(); ++i) {
            // 跳过已选择的元素
            if (used[i]) continue;
            // 选择当前元素
            current.push_back(nums[i]);
            used[i] = true;
            // 递归处理剩余元素
            backtrack(nums, current, used, result);
            // 回溯，移除最后一个元素
            current.pop_back();
            used[i] = false;
        }
    }

    // 主函数，生成全排列并返回结果
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result; // 结果列表
        vector<int> current; // 当前排列
        vector<bool> used(nums.size(), false); // 标记已选择的元素
        backtrack(nums, current, used, result); // 调用递归函数
        return result; // 返回结果
    }
};

// 主程序
int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3}; // 输入数组
    vector<vector<int>> result = solution.permute(nums); // 生成全排列

    // 输出结果
    for (const auto& permutation : result) {
        for (int num : permutation) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}
```

#### Java

```
import java.util.ArrayList;
import java.util.List;

public class Solution {
    // 递归函数，用于生成全排列
    private void backtrack(List<List<Integer>> result, List<Integer> current, boolean[] used, int[] nums) {
        // 终止条件，当当前排列长度等于数组长度时，将其加入结果列表
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        // 遍历所有元素
        for (int i = 0; i < nums.length; i++) {
            // 跳过已选择的元素
            if (used[i]) continue;
            // 选择当前元素
            current.add(nums[i]);
            used[i] = true;
            // 递归处理剩余元素
            backtrack(result, current, used, nums);
            // 回溯，移除最后一个元素
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }

    // 主函数，生成全排列并返回结果
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>(); // 结果列表
        List<Integer> current = new ArrayList<>(); // 当前排列
        boolean[] used = new boolean[nums.length]; // 标记已选择的元素
        backtrack(result, current, used, nums); // 调用递归函数
        return result; // 返回结果
    }

    // 主程序
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1, 2, 3}; // 输入数组
        List<List<Integer>> result = solution.permute(nums); // 生成全排列

        // 输出结果
        for (List<Integer> permutation : result) {
            System.out.println(permutation);
        }
    }
}
```

#### Python

```
def permute(nums):
    # 递归函数，用于生成全排列
    def backtrack(current):
        # 终止条件，当当前排列长度等于数组长度时，将其加入结果列表
        if len(current) == len(nums):
            result.append(current[:])
            return

        # 遍历所有元素
        for num in nums:
            # 跳过已选择的元素
            if num in current:
                continue
            # 选择当前元素
            current.append(num)
            # 递归处理剩余元素
            backtrack(current)
            # 回溯，移除最后一个元素
            current.pop()

    result = []  # 结果列表
    backtrack([])  # 调用递归函数
    return result  # 返回结果


# 主程序
if __name__ == "__main__":
    nums = [1, 2, 3]  # 输入数组
    result = permute(nums)  # 生成全排列

    # 输出结果
    for permutation in result:
        print(permutation)
```

