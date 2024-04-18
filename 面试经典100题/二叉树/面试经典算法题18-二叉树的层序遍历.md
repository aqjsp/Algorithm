# 面试经典算法题18-二叉树的层序遍历

LeetCode.102

### 问题描述

给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

**示例 1：**

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403042241153.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
```

**示例 2：**

```
输入：root = [1]
输出：[[1]]
```

**示例 3：**

```
输入：root = []
输出：[]
```

**提示：**

- 树中节点数目在范围 `[0, 2000]` 内
- `-1000 <= Node.val <= 1000`

### 思路

#### 递归

1. 定义一个辅助函数 `levelOrderHelper`，用来递归遍历二叉树的每一层，并将节点值按层级存储在 `result` 中。
2. 辅助函数的参数包括当前节点 `root`、当前层级 `level` 和存储结果的二维数组 `result`。
3. 如果当前节点为空，则直接返回。
4. 如果当前层级大于等于 `result` 的大小，说明需要添加新的一层，因为层序遍历是逐层遍历的。
5. 将当前节点的值加入到 `result` 的对应层级中。
6. 递归遍历当前节点的左子树，层级加一。
7. 递归遍历当前节点的右子树，层级加一。
8. 主函数 `levelOrder` 中调用辅助函数 `levelOrderHelper` 开始遍历整棵树。
9. 最后返回存储结果的二维数组 `result`。

#### 非递归

1. 创建一个队列 `queue` 和一个存储结果的二维数组 `result`。
2. 将根节点入队。
3. 循环直到队列为空：
   - 从队列中取出一个节点，将其值存储到当前层级的结果数组中。
   - 如果节点有左子节点，则将左子节点入队。
   - 如果节点有右子节点，则将右子节点入队。
4. 将当前层级的结果数组加入到最终的结果中。
5. 继续循环直到队列为空，完成整个二叉树的层序遍历。

### 图解

1. 创建一个队列 `queue` 和一个存储结果的二维数组 `result`，将根节点入队。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403042200895.png)

2. 队列不为空时，新建一个空数组level，用于存储当前层级节点值，然后进行循环打印，循环次数为当前层的节点数，也就是队列的长度。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403042217492.png)

3. 将队头元素弹出，存入当前层级的数组中。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403042209147.png)

4. 接着将当前节点的左右节点依次入队（**如果有**），然后将当前层级的节点值数组加入结果中。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403042213688.png)

5. 继续第3步。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403042220360.png)

6. 继续第4步。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403042222777.png)

7. 继续第3步。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403042225520.png)

8. 继续第4步。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403042227956.png)

此时，队列为空，退出循环，返回结果集。

### 参考代码

#### C++

##### 递归

```
#include <iostream>
#include <vector>

using namespace std;

// 二叉树节点的定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 辅助函数，递归实现层序遍历
void levelOrderHelper(TreeNode* root, int level, vector<vector<int>>& result) {
    if (!root) return;
    
    if (level >= result.size()) {
        result.push_back({});
    }
    
    result[level].push_back(root->val);
    
    levelOrderHelper(root->left, level + 1, result);
    levelOrderHelper(root->right, level + 1, result);
}

// 主函数，返回二叉树的层序遍历结果
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    levelOrderHelper(root, 0, result);
    return result;
}

// 创建二叉树
TreeNode* createTree(vector<int>& nodes, int index) {
    if (index >= nodes.size() || nodes[index] == -1) {
        return nullptr; // 如果节点为空，则返回nullptr
    }
    TreeNode* root = new TreeNode(nodes[index]); // 创建当前节点
    root->left = createTree(nodes, 2 * index + 1); // 创建左子树
    root->right = createTree(nodes, 2 * index + 2); // 创建右子树
    return root; // 返回当前节点
}

// 销毁二叉树
void destroyTree(TreeNode* root) {
    if (!root) return; // 如果根节点为空，直接返回
    destroyTree(root->left); // 递归销毁左子树
    destroyTree(root->right); // 递归销毁右子树
    delete root; // 删除当前节点
}

int main() {
    // 输入数据，示例二叉树为 {3,9,20,#,#,15,7}
    vector<int> nodes = {3, 9, 20, -1, -1, 15, 7};
    TreeNode* root = createTree(nodes, 0); // 创建二叉树

    // 调用层序遍历函数
    vector<vector<int>> result = levelOrder(root);

    // 输出遍历结果
    for (vector<int> level : result) {
        for (int val : level) {
            cout << val << " ";
        }
        cout << endl;
    }

    // 销毁二叉树
    destroyTree(root);

    return 0;
}
```

##### 非递归

```
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// 二叉树节点的定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result; // 存储结果的二维数组
    if (!root) return result; // 如果根节点为空，直接返回空结果数组

    queue<TreeNode*> q; // 辅助队列，用于层序遍历
    q.push(root); // 将根节点入队

    while (!q.empty()) {
        int size = q.size(); // 当前层级的节点数
        vector<int> level; // 存储当前层级节点值的数组
        for (int i = 0; i < size; i++) {
            TreeNode* node = q.front(); // 获取队头节点
            q.pop(); // 弹出队头节点
            level.push_back(node->val); // 将节点值加入当前层级的数组中
            if (node->left) q.push(node->left); // 将左子节点入队
            if (node->right) q.push(node->right); // 将右子节点入队
        }
        result.push_back(level); // 将当前层级的节点值数组加入结果中
    }

    return result; // 返回层序遍历的结果数组
}

// 创建二叉树
TreeNode* createTree(vector<int>& nodes, int index) {
    if (index >= nodes.size() || nodes[index] == -1) {
        return nullptr; // 如果节点为空，则返回nullptr
    }
    TreeNode* root = new TreeNode(nodes[index]); // 创建当前节点
    root->left = createTree(nodes, 2 * index + 1); // 创建左子树
    root->right = createTree(nodes, 2 * index + 2); // 创建右子树
    return root; // 返回当前节点
}

// 销毁二叉树
void destroyTree(TreeNode* root) {
    if (!root) return; // 如果根节点为空，直接返回
    destroyTree(root->left); // 递归销毁左子树
    destroyTree(root->right); // 递归销毁右子树
    delete root; // 删除当前节点
}

int main() {
    vector<int> nodes = {3, 9, 20, -1, -1, 15, 7}; // 二叉树的层序遍历序列
    TreeNode* root = createTree(nodes, 0); // 创建二叉树
    vector<vector<int>> result = levelOrder(root); // 进行层序遍历
    for (auto& level : result) { // 输出遍历结果
        for (int val : level) {
            cout << val << " ";
        }
        cout << endl;
    }

    destroyTree(root); // 销毁二叉树

    return 0;
}
```

#### Java

```
import java.util.*;

// 二叉树节点的定义
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Main {

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>(); // 存储结果的二维数组
        if (root == null) return result; // 如果根节点为空，直接返回空结果数组

        Queue<TreeNode> queue = new LinkedList<>(); // 辅助队列，用于层序遍历
        queue.offer(root); // 将根节点入队

        while (!queue.isEmpty()) {
            int size = queue.size(); // 当前层级的节点数
            List<Integer> level = new ArrayList<>(); // 存储当前层级节点值的数组
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll(); // 获取队头节点
                level.add(node.val); // 将节点值加入当前层级的数组中
                if (node.left != null) queue.offer(node.left); // 将左子节点入队
                if (node.right != null) queue.offer(node.right); // 将右子节点入队
            }
            result.add(level); // 将当前层级的节点值数组加入结果中
        }

        return result; // 返回层序遍历的结果数组
    }

    // 创建二叉树
    public TreeNode createTree(Integer[] nodes, int index) {
        if (index >= nodes.length || nodes[index] == null) {
            return null; // 如果节点为空，则返回null
        }
        TreeNode root = new TreeNode(nodes[index]); // 创建当前节点
        root.left = createTree(nodes, 2 * index + 1); // 创建左子树
        root.right = createTree(nodes, 2 * index + 2); // 创建右子树
        return root; // 返回当前节点
    }

    // 销毁二叉树
    public void destroyTree(TreeNode root) {
        if (root == null) return; // 如果根节点为空，直接返回
        destroyTree(root.left); // 递归销毁左子树
        destroyTree(root.right); // 递归销毁右子树
        root = null; // 将当前节点置为null
    }

    public static void main(String[] args) {
        Integer[] nodes = {3, 9, 20, null, null, 15, 7}; // 二叉树的层序遍历序列
        Main main = new Main();
        TreeNode root = main.createTree(nodes, 0); // 创建二叉树
        List<List<Integer>> result = main.levelOrder(root); // 进行层序遍历
        for (List<Integer> level : result) { // 输出遍历结果
            for (int val : level) {
                System.out.print(val + " ");
            }
            System.out.println();
        }

        main.destroyTree(root); // 销毁二叉树
    }
}
```

#### Python

```
from typing import List
from collections import deque

# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode) -> List[List[int]]:
    result = [] # 存储结果的二维数组
    if not root:
        return result # 如果根节点为空，直接返回空结果数组

    queue = deque([root]) # 辅助队列，用于层序遍历
    while queue:
        level_size = len(queue) # 当前层级的节点数
        level = [] # 存储当前层级节点值的数组
        for _ in range(level_size):
            node = queue.popleft() # 获取队头节点
            level.append(node.val) # 将节点值加入当前层级的数组中
            if node.left:
                queue.append(node.left) # 将左子节点入队
            if node.right:
                queue.append(node.right) # 将右子节点入队
        result.append(level) # 将当前层级的节点值数组加入结果中

    return result # 返回层序遍历的结果数组

# 创建二叉树
def createTree(nodes: List[int], index: int) -> TreeNode:
    if index >= len(nodes) or nodes[index] is None:
        return None # 如果节点为空，则返回None
    root = TreeNode(nodes[index]) # 创建当前节点
    root.left = createTree(nodes, 2 * index + 1) # 创建左子树
    root.right = createTree(nodes, 2 * index + 2) # 创建右子树
    return root # 返回当前节点

# 销毁二叉树
def destroyTree(root: TreeNode) -> None:
    if not root:
        return # 如果根节点为空，直接返回
    destroyTree(root.left) # 递归销毁左子树
    destroyTree(root.right) # 递归销毁右子树
    root = None # 将当前节点置为None

# 测试代码
nodes = [3, 9, 20, None, None, 15, 7] # 二叉树的层序遍历序列
root = createTree(nodes, 0) # 创建二叉树
result = levelOrder(root) # 进行层序遍历
for level in result: # 输出遍历结果
    print(level)

destroyTree(root) # 销毁二叉树
```

