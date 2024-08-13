# 面试经典算法题92-组合

LeetCode.77

### 问题描述

给定两个整数 `n` 和 `k`，返回范围 `[1, n]` 中所有可能的 `k` 个数的组合。

你可以按 任何顺序 返回答案。

**示例 1：**

```
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

**示例 2：**

```
输入：n = 1, k = 1
输出：[[1]]
```

### 思路

1. 构建递归函数：

   - 定义一个递归函数用于生成所有可能的组合。

   - 递归函数需要两个参数：当前选择的组合和起始位置。

2. 终止条件：当组合的长度达到 `k` 时，将当前组合加入结果列表。

3. 递归生成组合：

   - 从当前起始位置开始，依次选择每个数字，添加到当前组合中。

   - 递归处理下一个数字，起始位置增加，避免重复选择同一个数字。

4. 回溯和剪枝：每次递归返回时，回溯到上一个状态，移除最后添加的数字，继续尝试其他可能的数字。

5. 输出结果：最终生成的所有组合会存储在一个结果列表中，返回该列表。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

using namespace std;

// 定义递归函数用于生成组合
void backtrack(int start, int n, int k, vector<int>& current, vector<vector<int>>& result) {
    // 终止条件，当当前组合长度达到 k 时，将其加入结果列表
    if (current.size() == k) {
        result.push_back(current);
        return;
    }
    
    // 从起始位置 start 开始，依次选择每个数字
    for (int i = start; i <= n; ++i) {
        current.push_back(i);           // 将当前数字加入当前组合
        backtrack(i + 1, n, k, current, result);  // 递归处理下一个数字
        current.pop_back();             // 回溯，移除最后一个数字
    }
}

// 主函数，生成组合并返回结果
vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> result;         // 结果列表
    vector<int> current;                // 当前组合
    backtrack(1, n, k, current, result); // 调用递归函数
    return result;                      // 返回结果
}

// 主程序
int main() {
    int n = 4; // 输入的 n 值
    int k = 2; // 输入的 k 值
    vector<vector<int>> combinations = combine(n, k); // 生成组合
    
    // 输出结果
    for (const auto& combination : combinations) {
        cout << "[";
        for (size_t i = 0; i < combination.size(); ++i) {
            cout << combination[i];
            if (i < combination.size() - 1) {
                cout << ",";
            }
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

public class Combinations {
    // 递归函数用于生成组合
    private void backtrack(int start, int n, int k, List<Integer> current, List<List<Integer>> result) {
        // 终止条件，当当前组合长度达到 k 时，将其加入结果列表
        if (current.size() == k) {
            result.add(new ArrayList<>(current));
            return;
        }

        // 从起始位置 start 开始，依次选择每个数字
        for (int i = start; i <= n; ++i) {
            current.add(i); // 将当前数字加入当前组合
            backtrack(i + 1, n, k, current, result); // 递归处理下一个数字
            current.remove(current.size() - 1); // 回溯，移除最后一个数字
        }
    }

    // 主函数，生成组合并返回结果
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>(); // 结果列表
        List<Integer> current = new ArrayList<>(); // 当前组合
        backtrack(1, n, k, current, result); // 调用递归函数
        return result; // 返回结果
    }

    // 主程序
    public static void main(String[] args) {
        Combinations combinations = new Combinations();
        int n = 4; // 输入的 n 值
        int k = 2; // 输入的 k 值
        List<List<Integer>> result = combinations.combine(n, k); // 生成组合

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

class Combinations:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 结果列表
        result = []
        # 递归函数，用于生成组合
        def backtrack(start: int, current: List[int]):
            # 终止条件，当当前组合长度达到 k 时，将其加入结果列表
            if len(current) == k:
                result.append(current[:])
                return
            # 从起始位置 start 开始，依次选择每个数字
            for i in range(start, n + 1):
                current.append(i)  # 将当前数字加入当前组合
                backtrack(i + 1, current)  # 递归处理下一个数字
                current.pop()  # 回溯，移除最后一个数字
        # 调用递归函数
        backtrack(1, [])
        return result

# 主程序
if __name__ == "__main__":
    combinations = Combinations()
    n = 4  # 输入的 n 值
    k = 2  # 输入的 k 值
    result = combinations.combine(n, k)  # 生成组合
    # 输出结果
    for combination in result:
        print(combination)
```

