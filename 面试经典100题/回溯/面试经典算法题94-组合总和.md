# 面试经典算法题94-组合总和

LeetCode.39

### 问题描述

给你一个 无重复元素 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

`candidates` 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。

**示例 1：**

```
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
```

**示例 2：**

```
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
```

**示例 3：**

```
输入: candidates = [2], target = 1
输出: []
```

### 思路

1. 定义递归函数：

   - 定义一个递归函数，用于找到所有可能的组合。

   - 递归函数需要三个参数：当前组合、当前组合的总和和开始索引。

2. 终止条件：

   - 如果当前组合的总和等于目标数，则将当前组合加入结果列表。

   - 如果当前组合的总和超过目标数，则停止递归。

3. 递归生成组合：

   - 从开始索引开始遍历所有候选数。

   - 对于每个候选数，选择该数并递归处理剩余数（包括当前数，因为每个数可以无限制重复被选取）。

4. 回溯：每次递归返回时，回溯到上一个状态，移除最后添加的数，继续尝试其他可能的数。

5. 输出结果：最终生成的所有组合存储在一个结果列表中，返回该列表。

### 参考代码

#### C++

```
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    void backtrack(vector<int>& candidates, int target, vector<vector<int>>& result, vector<int>& current_combination, int current_sum, int start_index) {
        // 如果当前组合的和等于目标数，将当前组合加入结果列表
        if (current_sum == target) {
            result.push_back(current_combination);
            return;
        }
        // 如果当前组合的和超过目标数，终止当前递归
        if (current_sum > target) {
            return;
        }

        // 从当前索引开始遍历候选数组
        for (int i = start_index; i < candidates.size(); ++i) {
            // 将候选数加入当前组合
            current_combination.push_back(candidates[i]);
            // 递归处理剩余的数（可以重复选择当前数）
            backtrack(candidates, target, result, current_combination, current_sum + candidates[i], i);
            // 移除当前选择的数，回溯到上一个状态
            current_combination.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current_combination;
        backtrack(candidates, target, result, current_combination, 0, 0);
        return result;
    }
};

// 主函数
int main() {
    Solution solution;
    vector<int> candidates = {2, 3, 6, 7}; // 输入候选数组
    int target = 7; // 目标数
    vector<vector<int>> result = solution.combinationSum(candidates, target); // 生成所有组合

    // 输出结果
    for (const auto& combination : result) {
        cout << "[";
        for (int i = 0; i < combination.size(); ++i) {
            cout << combination[i];
            if (i < combination.size() - 1) cout << ",";
        }
        cout << "]" << endl;
    }

    return 0;
}
```

#### Java

```
import java.util.ArrayList;
import java.util.List;

public class Solution {
    // 递归函数，用于生成所有可能的组合
    private void backtrack(int[] candidates, int target, List<List<Integer>> result, List<Integer> currentCombination, int currentSum, int startIndex) {
        // 如果当前组合的和等于目标数，将当前组合加入结果列表
        if (currentSum == target) {
            result.add(new ArrayList<>(currentCombination));
            return;
        }
        // 如果当前组合的和超过目标数，终止当前递归
        if (currentSum > target) {
            return;
        }

        // 从当前索引开始遍历候选数组
        for (int i = startIndex; i < candidates.length; i++) {
            // 将候选数加入当前组合
            currentCombination.add(candidates[i]);
            // 递归处理剩余的数（可以重复选择当前数）
            backtrack(candidates, target, result, currentCombination, currentSum + candidates[i], i);
            // 移除当前选择的数，回溯到上一个状态
            currentCombination.remove(currentCombination.size() - 1);
        }
    }

    // 主函数，用于生成所有组合
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentCombination = new ArrayList<>();
        backtrack(candidates, target, result, currentCombination, 0, 0);
        return result;
    }

    // 主程序
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] candidates = {2, 3, 6, 7}; // 输入候选数组
        int target = 7; // 目标数
        List<List<Integer>> result = solution.combinationSum(candidates, target); // 生成所有组合

        // 输出结果
        for (List<Integer> combination : result) {
            System.out.println(combination);
        }
    }
}
```

#### Python

```
from typing import List

class Solution:
    # 递归函数，用于生成所有可能的组合
    def backtrack(self, candidates: List[int], target: int, result: List[List[int]], current_combination: List[int], current_sum: int, start_index: int):
        # 如果当前组合的和等于目标数，将当前组合加入结果列表
        if current_sum == target:
            result.append(list(current_combination))
            return
        # 如果当前组合的和超过目标数，终止当前递归
        if current_sum > target:
            return

        # 从当前索引开始遍历候选数组
        for i in range(start_index, len(candidates)):
            # 将候选数加入当前组合
            current_combination.append(candidates[i])
            # 递归处理剩余的数（可以重复选择当前数）
            self.backtrack(candidates, target, result, current_combination, current_sum + candidates[i], i)
            # 移除当前选择的数，回溯到上一个状态
            current_combination.pop()

    # 主函数，用于生成所有组合
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current_combination = []
        self.backtrack(candidates, target, result, current_combination, 0, 0)
        return result

# 主程序
if __name__ == "__main__":
    solution = Solution()
    candidates = [2, 3, 6, 7] # 输入候选数组
    target = 7 # 目标数
    result = solution.combinationSum(candidates, target) # 生成所有组合

    # 输出结果
    for combination in result:
        print(combination)
```

