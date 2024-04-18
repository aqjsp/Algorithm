# 面试经典算法题29-合并二叉树

LeetCode.617

### 问题描述

给你两棵二叉树： `root1` 和 `root2` 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，**不为** null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

**注意:** 合并过程必须从两个树的根节点开始。

**示例 1：**

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403212228539.jpg)

```
输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
输出：[3,4,5,5,4,null,7]
```

**示例 2：**

```
输入：root1 = [1], root2 = [1,2]
输出：[2,2]
```

### 思路

#### 递归

1. 如果两个节点都存在，将它们的值相加作为新节点的值，然后递归地合并它们的左子树和右子树。
2. 如果其中一个节点为空，直接返回另一个节点（即另一棵树中对应的节点或空节点）。
3. 递归结束条件为其中一个节点为空，此时返回另一个节点或空节点，表示合并完成。

#### 非递归

1. 初始化：创建一个队列，并将两棵树的根节点同时入队。
2. 迭代：循环遍历队列直到队列为空。
   - 从队列中取出两个节点，分别代表两棵树当前层的节点。
   - 将两个节点的值相加，作为新节点的值。
   - 分别处理两个节点的左子节点和右子节点：
     - 如果两个节点的左子节点都存在，则将左子节点同时入队。
     - 如果其中一个节点的左子节点为空，则将另一个节点的左子节点直接作为新节点的左子节点。
     - 对右子节点的处理与左子节点类似。
3. **返回结果**：返回合并后的树的根节点。

### 图解

1. 如果两个树都存在根节点，创建一个队列，并将两棵树的根节点同时入队。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403212257938.png)

2. 如果队列不为空，将队列的元素弹出队列。因为都有根节点，所以将两个节点的值加起来作为新的根节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403212306645.png)

3. 当两个树的根节点都有左子节点，将左节点同时入队。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403212309174.png)

4. 当两个树的根节点都有右子节点，将右节点同时入队。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403212309559.png)

5. 此时队列不为空，将两个左子节点同时弹出队列。将两个节点的值加起来作为新的左节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403212311951.png)

6. 继续处理左子节点，此时第一棵树有左子节点，第二棵树没左子节点，直接将第一棵树的左子节点复制给新的节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403212316564.png)

7. 继续处理右子节点，此时第一棵树没右子节点，第二棵树有右子节点，直接将第二棵树的右子节点复制给新的节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403212318464.png)

8. 此时队列不为空，将两个右子节点同时弹出队列。将两个节点的值加起来作为新的右子节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403212320605.png)

9. 当前节点无左子节点，处理右子节点，第一棵树也无右子节点，第二棵树有右子节点，直接将第二棵树的右子节点复制给新的节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403212322343.png)

此时队列为空，退出循环，返回新树的根节点。

### 参考代码

#### C++

##### 递归

```
#include <iostream>
#include <queue>

using namespace std;

// 二叉树节点的定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        if (!root1) {
            return root2; // 如果 root1 为空，返回 root2
        }
        if (!root2) {
            return root1; // 如果 root2 为空，返回 root1
        }

        TreeNode* merged = new TreeNode(root1->val + root2->val); // 创建合并后的新节点
        merged->left = mergeTrees(root1->left, root2->left); // 递归合并左子树
        merged->right = mergeTrees(root1->right, root2->right); // 递归合并右子树

        return merged; // 返回合并后的根节点
    }
};

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

// 中序遍历打印二叉树
void inorderTraversal(TreeNode* root) {
    if (!root) {
        return;
    }
    inorderTraversal(root->left);
    cout << root->val << " ";
    inorderTraversal(root->right);
}

int main() {
    vector<int> nodes1 = {1, 3, 2, 5}; // 第一棵二叉树的先序遍历序列
    vector<int> nodes2 = {2, 1, 3, -1, 4, -1, 7}; // 第二棵二叉树的先序遍历序列

    TreeNode* root1 = createTree(nodes1, 0); // 创建第一棵二叉树
    TreeNode* root2 = createTree(nodes2, 0); // 创建第二棵二叉树

    Solution solution;
    TreeNode* mergedTree = solution.mergeTrees(root1, root2); // 合并两棵二叉树
    inorderTraversal(mergedTree); // 打印合并后的二叉树（中序遍历）

    return 0;
}
```

##### 非递归

```
#include <iostream>
#include <queue>

using namespace std;

// 二叉树节点的定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        if (!root1) {
            return root2; // 如果 root1 为空，返回 root2
        }
        if (!root2) {
            return root1; // 如果 root2 为空，返回 root1
        }

        queue<pair<TreeNode*, TreeNode*>> q;
        q.push({root1, root2}); // 将两棵树的根节点同时入队

        while (!q.empty()) {
            auto [node1, node2] = q.front();
            q.pop();

            // 如果两个节点都存在，将它们的值相加作为新节点的值
            node1->val += node2->val;

            // 处理左子节点
            if (node1->left && node2->left) {
                q.push({node1->left, node2->left}); // 将左子节点同时入队
            } else if (node2->left) {
                node1->left = node2->left; // 如果 node1 的左子节点为空，直接复制 node2 的左子节点
            }

            // 处理右子节点
            if (node1->right && node2->right) {
                q.push({node1->right, node2->right}); // 将右子节点同时入队
            } else if (node2->right) {
                node1->right = node2->right; // 如果 node1 的右子节点为空，直接复制 node2 的右子节点
            }
        }

        return root1; // 返回合并后的根节点
    }
};

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

// 打印二叉树的先序遍历结果
void printPreorder(TreeNode* root) {
    if (!root) {
        return;
    }
    cout << root->val << " ";
    printPreorder(root->left);
    printPreorder(root->right);
}

int main() {
    vector<int> nodes1 = {1, 3, 2, 5}; // 第一棵二叉树的先序遍历序列
    TreeNode* root1 = createTree(nodes1, 0); // 创建第一棵二叉树

    vector<int> nodes2 = {2, 1, 3, -1, 4, -1, 7}; // 第二棵二叉树的先序遍历序列
    TreeNode* root2 = createTree(nodes2, 0); // 创建第二棵二叉树

    Solution solution;
    TreeNode* mergedRoot = solution.mergeTrees(root1, root2); // 合并两棵二叉树
    printPreorder(mergedRoot); // 输出合并后的二叉树的先序遍历结果
    cout << endl;

    return 0;
}
```

#### Java

```
import java.util.LinkedList;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        // 如果其中一棵树为空，则返回另一棵树
        if (root1 == null) return root2;
        if (root2 == null) return root1;

        // 创建一个队列，用于存储需要处理的节点对
        Queue<TreeNode[]> queue = new LinkedList<>();
        queue.offer(new TreeNode[]{root1, root2}); // 将根节点对入队

        // 遍历队列，直到队列为空
        while (!queue.isEmpty()) {
            TreeNode[] nodes = queue.poll(); // 取出队首的节点对
            TreeNode node1 = nodes[0], node2 = nodes[1]; // 分别表示两棵树的对应节点

            // 将两个节点的值相加，并更新到第一棵树上
            node1.val += node2.val;

            // 处理左子树
            if (node1.left != null && node2.left != null) {
                queue.offer(new TreeNode[]{node1.left, node2.left}); // 将左子节点对入队
            } else if (node1.left == null) {
                node1.left = node2.left; // 如果第一棵树的左子节点为空，则直接将第二棵树的左子节点赋值给它
            }

            // 处理右子树
            if (node1.right != null && node2.right != null) {
                queue.offer(new TreeNode[]{node1.right, node2.right}); // 将右子节点对入队
            } else if (node1.right == null) {
                node1.right = node2.right; // 如果第一棵树的右子节点为空，则直接将第二棵树的右子节点赋值给它
            }
        }

        // 返回合并后的第一棵树
        return root1;
    }

    // 测试
    public static void main(String[] args) {
        Solution solution = new Solution();

        // 创建两棵树
        TreeNode root1 = new TreeNode(1);
        root1.left = new TreeNode(3);
        root1.right = new TreeNode(2);
        root1.left.left = new TreeNode(5);

        TreeNode root2 = new TreeNode(2);
        root2.left = new TreeNode(1);
        root2.right = new TreeNode(3);
        root2.left.right = new TreeNode(4);
        root2.right.right = new TreeNode(7);

        // 合并两棵树
        TreeNode merged = solution.mergeTrees(root1, root2);

        // 输出合并后的树
        System.out.println("合并后的树：");
        printTree(merged);
    }

    // 辅助函数，中序遍历打印二叉树
    private static void printTree(TreeNode root) {
        if (root == null) return;
        printTree(root.left);
        System.out.print(root.val + " ");
        printTree(root.right);
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

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        queue = [(root1, root2)]  # 创建一个队列，用于存储需要处理的节点对

        while queue:
            node1, node2 = queue.pop(0)  # 取出队首的节点对

            # 将两个节点的值相加，并更新到第一棵树上
            node1.val += node2.val

            # 处理左子树
            if node1.left and node2.left:
                queue.append((node1.left, node2.left))  # 将左子节点对入队
            elif not node1.left:
                node1.left = node2.left  # 如果第一棵树的左子节点为空，则直接将第二棵树的左子节点赋值给它

            # 处理右子树
            if node1.right and node2.right:
                queue.append((node1.right, node2.right))  # 将右子节点对入队
            elif not node1.right:
                node1.right = node2.right  # 如果第一棵树的右子节点为空，则直接将第二棵树的右子节点赋值给它

        return root1  # 返回合并后的第一棵树

# 测试
def main():
    solution = Solution()

    # 创建两棵树
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)

    # 合并两棵树
    merged = solution.mergeTrees(root1, root2)

    # 输出合并后的树
    print("合并后的树：")
    printTree(merged)

# 辅助函数，中序遍历打印二叉树
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)

if __name__ == "__main__":
    main()
```

