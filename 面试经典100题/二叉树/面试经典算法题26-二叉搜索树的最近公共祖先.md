# 面试经典算法题26-二叉搜索树的最近公共祖先

LeetCode.235

### 问题描述

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

某百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

例如，给定如下二叉搜索树: root = [6,2,8,0,4,7,9,null,null,3,5]

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403132129683.png)

**示例 1:**

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
```

**示例 2:**

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
```

**说明:**

- 所有节点的值都是唯一的。
- p、q 为不同节点且均存在于给定的二叉搜索树中。

### 思路

#### 递归

1. 从根节点开始遍历二叉搜索树。
2. 如果根节点的值大于两个指定节点的值，则最近公共祖先在左子树中，递归处理左子树。
3. 如果根节点的值小于两个指定节点的值，则最近公共祖先在右子树中，递归处理右子树。
4. 如果根节点的值位于两个指定节点的值之间，则根节点即为最近公共祖先。

#### 非递归

1. 从根节点开始遍历二叉搜索树。
2. 如果当前节点的值大于两个目标节点的值，说明最近公共祖先在当前节点的左子树中，移动到左子节点继续遍历。
3. 如果当前节点的值小于两个目标节点的值，说明最近公共祖先在当前节点的右子树中，移动到右子节点继续遍历。
4. 如果当前节点的值在两个目标节点的值之间，说明当前节点就是最近公共祖先，直接返回当前节点。

使用栈：

1. 从根节点开始，使用栈来辅助进行迭代遍历。
2. 对于每个节点，判断其值与要查找的两个节点的值的关系：
   - 如果节点的值在两个节点的值之间，或者等于其中一个节点的值，则当前节点就是最近公共祖先。
   - 如果当前节点的值大于两个节点值的最大值，则说明最近公共祖先在当前节点的左子树中，将左子节点入栈。
   - 如果当前节点的值小于两个节点值的最小值，则说明最近公共祖先在当前节点的右子树中，将右子节点入栈。
3. 不断重复上述过程，直到找到最近公共祖先为止。

### 图解

根据示例二给大家进行图解。

1. 2和4都小于根节点6，所以2和4都在根节点6的左子树上。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403132258485.png)

2. 根节点的左子结点就是2，而4大于2，肯定在节点2的右节点上了。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403132300853.png)

所以，节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

### 参考代码

#### C++

##### 递归

```
#include <iostream>

using namespace std;

// 二叉树节点的定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 寻找二叉搜索树中两个节点的最近公共祖先
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root) return nullptr; // 如果根节点为空，返回nullptr
    if (root->val > p->val && root->val > q->val) {
        // 如果根节点的值大于两个节点的值，则最近公共祖先在左子树中
        return lowestCommonAncestor(root->left, p, q);
    } else if (root->val < p->val && root->val < q->val) {
        // 如果根节点的值小于两个节点的值，则最近公共祖先在右子树中
        return lowestCommonAncestor(root->right, p, q);
    } else {
        // 如果根节点的值位于两个节点的值之间，则根节点即为最近公共祖先
        return root;
    }
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
    vector<int> nodes = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5}; // 二叉搜索树的先序遍历序列
    TreeNode* root = createTree(nodes, 0); // 创建二叉树
    TreeNode* p = root->left->left; // 指定节点 p
    TreeNode* q = root->left->right->left; // 指定节点 q
    TreeNode* ancestor = lowestCommonAncestor(root, p, q); // 查找最近公共祖先
    cout << "The lowest common ancestor of " << p->val << " and " << q->val << " is " << ancestor->val << endl;

    destroyTree(root); // 销毁二叉树

    return 0;
}
```

##### 非递归

```
#include <iostream>

// 二叉树节点的定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 找到两个节点的最近公共祖先
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    while (root) {
        if (root->val > p->val && root->val > q->val) {
            root = root->left;  // 如果根节点值大于 p 和 q 的值，说明最近公共祖先在左子树
        } else if (root->val < p->val && root->val < q->val) {
            root = root->right;  // 如果根节点值小于 p 和 q 的值，说明最近公共祖先在右子树
        } else {
            break;  // 如果根节点的值介于 p 和 q 的值之间，说明当前节点就是最近公共祖先
        }
    }
    return root;
}

// 创建二叉树
TreeNode* createTree(std::vector<int>& nodes, int index) {
    if (index >= nodes.size() || nodes[index] == -1) {
        return nullptr;  // 如果节点为空，则返回nullptr
    }
    TreeNode* root = new TreeNode(nodes[index]);  // 创建当前节点
    root->left = createTree(nodes, 2 * index + 1);  // 创建左子树
    root->right = createTree(nodes, 2 * index + 2);  // 创建右子树
    return root;  // 返回当前节点
}

// 销毁二叉树
void destroyTree(TreeNode* root) {
    if (!root) return;  // 如果根节点为空，直接返回
    destroyTree(root->left);  // 递归销毁左子树
    destroyTree(root->right);  // 递归销毁右子树
    delete root;  // 删除当前节点
}

int main() {
    std::vector<int> nodes = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5};  // 二叉搜索树的先序遍历序列
    TreeNode* root = createTree(nodes, 0);  // 创建二叉树
    TreeNode* p = new TreeNode(2);  // 节点p的值为2
    TreeNode* q = new TreeNode(4);  // 节点q的值为4
    TreeNode* result = lowestCommonAncestor(root, p, q);  // 找到最近公共祖先
    std::cout << "最近公共祖先的值为：" << result->val << std::endl;

    // 销毁二叉树
    destroyTree(root);
    delete p;
    delete q;

    return 0;
}
```

###### 使用栈

```
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

// 二叉树节点的定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 非递归方式寻找二叉搜索树中两个节点的最近公共祖先
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    stack<TreeNode*> stack;
    stack.push(root); // 将根节点入栈

    TreeNode* ancestor = nullptr;
    while (!stack.empty()) {
        TreeNode* node = stack.top();
        stack.pop();

        // 如果节点的值在 p 和 q 的值之间，或者等于 p 或 q 的值，则当前节点为最近公共祖先
        if ((node->val >= p->val && node->val <= q->val) || (node->val <= p->val && node->val >= q->val)) {
            ancestor = node;
        }

        // 如果当前节点的值大于 p 和 q 的值之间的较大值，则继续向左子树查找
        if (node->val > max(p->val, q->val)) {
            if (node->left) {
                stack.push(node->left);
            }
        }

        // 如果当前节点的值小于 p 和 q 的值之间的较小值，则继续向右子树查找
        if (node->val < min(p->val, q->val)) {
            if (node->right) {
                stack.push(node->right);
            }
        }
    }

    return ancestor;
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
    vector<int> nodes = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5}; // 二叉搜索树的先序遍历序列
    TreeNode* root = createTree(nodes, 0); // 创建二叉树
    TreeNode* p = root->left->left; // 指定节点 p
    TreeNode* q = root->left->right->left; // 指定节点 q
    TreeNode* ancestor = lowestCommonAncestor(root, p, q); // 查找最近公共祖先
    cout << "The lowest common ancestor of " << p->val << " and " << q->val << " is " << ancestor->val << endl;

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

public class Solution {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root; // 如果根节点为空，或者等于 p 或 q 中的一个，直接返回根节点
        }

        Deque<TreeNode> stack = new ArrayDeque<>(); // 辅助栈，用于迭代遍历
        Map<TreeNode, TreeNode> parent = new HashMap<>(); // 存储每个节点的父节点

        stack.push(root); // 将根节点入栈
        parent.put(root, null); // 根节点的父节点为空

        while (!parent.containsKey(p) || !parent.containsKey(q)) {
            TreeNode node = stack.pop(); // 弹出栈顶节点

            if (node.left != null) {
                stack.push(node.left); // 左子节点入栈
                parent.put(node.left, node); // 记录左子节点的父节点
            }

            if (node.right != null) {
                stack.push(node.right); // 右子节点入栈
                parent.put(node.right, node); // 记录右子节点的父节点
            }
        }

        Set<TreeNode> ancestors = new HashSet<>(); // 存储从 p 到根节点的所有祖先节点
        while (p != null) {
            ancestors.add(p); // 将 p 加入祖先集合
            p = parent.get(p); // 移动到 p 的父节点
        }

        while (!ancestors.contains(q)) {
            q = parent.get(q); // 不断向上查找 q 的父节点，直到找到最近公共祖先
        }

        return q; // 返回最近公共祖先
    }

    // 创建二叉树
    public static TreeNode createTree(Integer[] nodes, int index) {
        if (index >= nodes.length || nodes[index] == null) {
            return null; // 如果节点为空，则返回null
        }
        TreeNode root = new TreeNode(nodes[index]); // 创建当前节点
        root.left = createTree(nodes, 2 * index + 1); // 创建左子树
        root.right = createTree(nodes, 2 * index + 2); // 创建右子树
        return root; // 返回当前节点
    }

    // 销毁二叉树
    public static void destroyTree(TreeNode root) {
        if (root == null) return; // 如果根节点为空，直接返回
        destroyTree(root.left); // 递归销毁左子树
        destroyTree(root.right); // 递归销毁右子树
        root.left = null;
        root.right = null;
    }

    public static void main(String[] args) {
        Integer[] nodes = {6, 2, 8, 0, 4, 7, 9, null, null, 3, 5}; // 二叉搜索树的先序遍历序列
        TreeNode root = createTree(nodes, 0); // 创建二叉树
        TreeNode p = new TreeNode(2); // 节点p的值为2
        TreeNode q = new TreeNode(4); // 节点q的值为4
        Solution solution = new Solution();
        TreeNode result = solution.lowestCommonAncestor(root, p, q); // 找到最近公共祖先
        System.out.println("最近公共祖先的值为：" + result.val);

        destroyTree(root); // 销毁二叉树
    }
}
```

#### Python

```
# 二叉树节点的定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root  # 如果根节点为空，或者等于 p 或 q 中的一个，直接返回根节点

    stack = []  # 辅助栈，用于迭代遍历
    parent = {root: None}  # 存储每个节点的父节点
    stack.append(root)  # 将根节点入栈

    while p not in parent or q not in parent:
        node = stack.pop()  # 弹出栈顶节点

        if node.left:
            stack.append(node.left)  # 左子节点入栈
            parent[node.left] = node  # 记录左子节点的父节点

        if node.right:
            stack.append(node.right)  # 右子节点入栈
            parent[node.right] = node  # 记录右子节点的父节点

    ancestors = set()  # 存储从 p 到根节点的所有祖先节点
    while p:
        ancestors.add(p)  # 将 p 加入祖先集合
        p = parent[p]  # 移动到 p 的父节点

    while q not in ancestors:
        q = parent[q]  # 不断向上查找 q 的父节点，直到找到最近公共祖先

    return q  # 返回最近公共祖先

# 创建二叉树
def createTree(nodes, index):
    if index >= len(nodes) or nodes[index] is None:
        return None  # 如果节点为空，则返回None
    root = TreeNode(nodes[index])  # 创建当前节点
    root.left = createTree(nodes, 2 * index + 1)  # 创建左子树
    root.right = createTree(nodes, 2 * index + 2)  # 创建右子树
    return root  # 返回当前节点

# 销毁二叉树
def destroyTree(root):
    if not root:
        return  # 如果根节点为空，直接返回
    destroyTree(root.left)  # 递归销毁左子树
    destroyTree(root.right)  # 递归销毁右子树
    root.left = None
    root.right = None

# 输入数据
nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]  # 二叉搜索树的先序遍历序列
root = createTree(nodes, 0)  # 创建二叉树
p = TreeNode(2)  # 节点p的值为2
q = TreeNode(4)  # 节点q的值为4
result = lowestCommonAncestor(root, p, q)  # 找到最近公共祖先
print("最近公共祖先的值为：", result.val)

# 销毁二叉树
destroyTree(root)
```

