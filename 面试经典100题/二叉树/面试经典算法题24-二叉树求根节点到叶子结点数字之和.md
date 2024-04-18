# 面试经典算法题24-二叉树求根节点到叶子结点数字之和

LeetCode.129

### 问题描述

给你一个二叉树的根节点 `root` ，树中每个节点都存放有一个 `0` 到 `9` 之间的数字。

每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 `1 -> 2 -> 3` 表示数字 `123` 。

计算从根节点到叶节点生成的 **所有数字之和** 。

**叶节点** 是指没有子节点的节点。

**示例 1：**

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403112218093.jpg)

```
输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25
```

**示例 2：**

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403112218502.jpg)

```
输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026
```

**提示：**

- 树中节点的数目在范围 `[1, 1000]` 内
- `0 <= Node.val <= 9`
- 树的深度不超过 `10`

### 思路

#### 递归

1. 使用深度优先搜索（DFS）遍历二叉树，遍历过程中记录从根节点到当前节点的路径数字；
2. 当遍历到叶节点时，将当前路径数字加到总和中；
3. 遍历完成后，返回总和即可。

#### 非递归

1. 使用两个栈 `nodeStack` 和 `numStack` 分别存储节点和对应的路径数字。
2. 将根节点入栈 `nodeStack` 和 `numStack`。
3. 循环执行以下步骤直到 nodeStack 为空：
   - 弹出栈顶节点 `node` 和对应的路径数字 `num`。
   - 如果 `node` 是叶节点，则将 `num` 加到总和中。
   - 如果 `node` 不是叶节点，则将 `node` 的子节点和对应的路径数字入栈。
4. 返回总和。

### 图解

1. 申请两个栈nodeStack和numStack分别存放节点和对应的路径数字（这里为了看起来直观，就将节点也将节点数字表示）。将根节点入栈。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403112258016.png)

2. 如果存储节点的栈不为空，就将栈顶节点和栈顶路径数字弹出。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403112301430.png)

3. 先将右子节点入栈，再将左子结点入栈。并将对应的值入栈。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403112341645.png)

5. 将栈顶元素弹出。

   - 先将左子节点弹出

   ![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403112355932.png)

   - 再将右子节点弹出

   ![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403112356777.png)

6. 左子结点非叶子结点，就继续将其右左节点依次入栈。右子节点是叶子结点。所以就将路径数字加到总和中。

![image-20240312000041838](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403120000880.png)

7. 重复5、6步。但是这两个节点都是叶子结点，所以就将其加到总和中。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403120005220.png)

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

int sumNumbers(TreeNode* root) {
    if (!root) return 0; // 如果根节点为空，直接返回0

    int totalSum = 0; // 总和
    vector<int> path; // 当前路径

    // 深度优先搜索函数
    function<void(TreeNode*)> dfs = [&](TreeNode* node) {
        if (!node) return; // 如果节点为空，直接返回
        path.push_back(node->val); // 将当前节点值加入路径
        if (!node->left && !node->right) { // 如果是叶节点
            int pathNum = 0;
            for (int num : path) {
                pathNum = pathNum * 10 + num; // 计算路径数字
            }
            totalSum += pathNum; // 将路径数字加到总和中
        } else {
            dfs(node->left); // 递归处理左子节点
            dfs(node->right); // 递归处理右子节点
        }
        path.pop_back(); // 回溯，移除当前节点值
    };

    dfs(root); // 从根节点开始深度优先搜索

    return totalSum; // 返回总和
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
    vector<int> nodes = {1, 2, 3}; // 二叉树的先序遍历序列
    TreeNode* root = createTree(nodes, 0); // 创建二叉树
    int result = sumNumbers(root); // 计算所有路径数字之和
    cout << result << endl; // 输出结果

    destroyTree(root); // 销毁二叉树

    return 0;
}
```

##### 非递归

```
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

// 二叉树节点的定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

int sumNumbers(TreeNode* root) {
    if (!root) return 0; // 如果根节点为空，直接返回0

    int totalSum = 0; // 总和
    stack<TreeNode*> nodeStack; // 存储节点的栈
    stack<int> numStack; // 存储路径数字的栈
    nodeStack.push(root); // 将根节点入栈
    numStack.push(root->val); // 将根节点的值加入路径数字栈

    while (!nodeStack.empty()) {
        TreeNode* node = nodeStack.top(); // 获取栈顶节点
        nodeStack.pop(); // 弹出栈顶节点
        int num = numStack.top(); // 获取栈顶路径数字
        numStack.pop(); // 弹出栈顶路径数字

        if (!node->left && !node->right) { // 如果是叶节点
            totalSum += num; // 将路径数字加到总和中
        } else {
            if (node->right) { // 如果有右子节点，入栈右子节点和对应的路径数字
                nodeStack.push(node->right);
                numStack.push(num * 10 + node->right->val);
            }
            if (node->left) { // 如果有左子节点，入栈左子节点和对应的路径数字
                nodeStack.push(node->left);
                numStack.push(num * 10 + node->left->val);
            }
        }
    }

    return totalSum; // 返回总和
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
    vector<int> nodes = {1, 2, 3}; // 二叉树的先序遍历序列
    TreeNode* root = createTree(nodes, 0); // 创建二叉树
    int result = sumNumbers(root); // 计算所有路径数字之和
    cout << result << endl; // 输出结果

    destroyTree(root); // 销毁二叉树

    return 0;
}
```

#### Java

```
import java.util.*;

// 定义二叉树节点
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution {
    public int sumNumbers(TreeNode root) {
        if (root == null) return 0;

        int totalSum = 0;
        Stack<TreeNode> nodeStack = new Stack<>(); // 用于存储节点的栈
        Stack<Integer> numStack = new Stack<>(); // 用于存储路径数字的栈
        nodeStack.push(root);
        numStack.push(root.val);

        while (!nodeStack.isEmpty()) {
            TreeNode node = nodeStack.pop();
            int num = numStack.pop();

            if (node.left == null && node.right == null) {
                totalSum += num; // 如果是叶节点，将路径数字加到总和中
            } else {
                if (node.right != null) {
                    nodeStack.push(node.right);
                    numStack.push(num * 10 + node.right.val); // 将右子节点和路径数字入栈
                }
                if (node.left != null) {
                    nodeStack.push(node.left);
                    numStack.push(num * 10 + node.left.val); // 将左子节点和路径数字入栈
                }
            }
        }

        return totalSum; // 返回总和
    }

    // 创建二叉树
    public TreeNode createTree(Integer[] nodes, int index) {
        if (index >= nodes.length || nodes[index] == null) {
            return null;
        }
        TreeNode root = new TreeNode(nodes[index]);
        root.left = createTree(nodes, 2 * index + 1);
        root.right = createTree(nodes, 2 * index + 2);
        return root;
    }

    // 测试
    public static void main(String[] args) {
        Solution solution = new Solution();
        Integer[] nodes = {1, 2, 3};
        TreeNode root = solution.createTree(nodes, 0);
        int result = solution.sumNumbers(root);
        System.out.println(result);
    }
}
```

#### Python

```
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    if not root:
        return 0

    total_sum = 0
    node_stack = [root]  # 用于存储节点的栈
    num_stack = [root.val]  # 用于存储路径数字的栈

    while node_stack:
        node = node_stack.pop()
        num = num_stack.pop()

        if not node.left and not node.right:
            total_sum += num  # 如果是叶节点，将路径数字加到总和中
        else:
            if node.right:
                node_stack.append(node.right)
                num_stack.append(num * 10 + node.right.val)  # 将右子节点和路径数字入栈
            if node.left:
                node_stack.append(node.left)
                num_stack.append(num * 10 + node.left.val)  # 将左子节点和路径数字入栈

    return total_sum  # 返回总和

# 创建二叉树
def create_tree(nodes, index):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = create_tree(nodes, 2 * index + 1)
    root.right = create_tree(nodes, 2 * index + 2)
    return root

# 测试
nodes = [1, 2, 3]
root = create_tree(nodes, 0)
result = sumNumbers(root)
print(result)
```

