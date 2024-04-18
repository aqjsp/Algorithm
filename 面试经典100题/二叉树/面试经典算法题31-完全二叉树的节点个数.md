# 面试经典算法题31-完全二叉树的节点个数

LeetCode.222

### 问题描述

给你一棵 **完全二叉树** 的根节点 `root` ，求出该树的节点个数。

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 `h` 层，则该层包含 `1~ 2h` 个节点。

**示例 1：**

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403262246885.jpg)

```
输入：root = [1,2,3,4,5,6]
输出：6
```

**示例 2：**

```
输入：root = []
输出：0
```

**示例 3：**

```
输入：root = [1]
输出：1
```

### 思路

#### 递归

1. 由于是完全二叉树，可以利用其性质快速计算节点个数。
2. 首先计算完全二叉树的高度 `h`，从根节点开始，一直向左走到底即可。
3. 接着计算最后一层的节点数，即左子树的高度 `lh` 和右子树的高度 `rh`。
4. 如果 `lh == rh`，说明左子树是满二叉树，节点数为 `2^lh - 1`，递归计算右子树的节点数。
5. 如果 `lh != rh`，说明右子树是满二叉树，节点数为 `2^rh - 1`，递归计算左子树的节点数。
6. 最终节点数为 `1（根节点） + 左子树节点数 + 右子树节点数`。

#### 非递归

1. 非递归方法需要利用完全二叉树的性质来计算节点数。
2. 首先计算左子树的高度，然后计算右子树的高度。
3. 如果左右子树高度相同，说明左子树是满二叉树，节点数为 2^h - 1，递归计算右子树节点数。
4. 如果左右子树高度不同，说明右子树是满二叉树，节点数为 2^(h-1) - 1，递归计算左子树节点数。
5. 最后节点数为 1（根节点） + 左子树节点数 + 右子树节点数。

### 图解

这里给大家画一个详细的流程图吧。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403262331736.png)

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403262331848.png)

### 参考代码

#### C++

##### 递归

```
#include <iostream>

// 二叉树节点的定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int countNodes(TreeNode* root) {
        if (!root) {
            return 0; // 如果根节点为空，返回节点数为0
        }

        int lh = 0, rh = 0; // 左子树和右子树的高度
        TreeNode* left = root, * right = root; // 用于计算高度的指针

        // 计算左子树高度
        while (left) {
            ++lh;
            left = left->left;
        }

        // 计算右子树高度
        while (right) {
            ++rh;
            right = right->right;
        }

        // 如果左子树高度等于右子树高度，说明左子树是满二叉树
        if (lh == rh) {
            return (1 << lh) - 1; // 返回节点数
        }

        // 如果左子树高度不等于右子树高度，递归计算左右子树节点数并返回
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};

// 创建完全二叉树
TreeNode* createCompleteTree(int arr[], int n, int i) {
    if (i >= n || arr[i] == -1) {
        return nullptr; // 如果节点为空，则返回nullptr
    }
    TreeNode* root = new TreeNode(arr[i]); // 创建当前节点
    root->left = createCompleteTree(arr, n, 2 * i + 1); // 创建左子树
    root->right = createCompleteTree(arr, n, 2 * i + 2); // 创建右子树
    return root; // 返回当前节点
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6}; // 完全二叉树的数组表示
    int n = sizeof(arr) / sizeof(arr[0]); // 数组长度
    TreeNode* root = createCompleteTree(arr, n, 0); // 创建完全二叉树
    Solution solution;
    int count = solution.countNodes(root); // 计算节点个数
    std::cout << "节点个数：" << count << std::endl; // 输出节点个数

    return 0;
}
```

##### 非递归

```
#include <iostream>
#include <stack>

// 二叉树节点的定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int countNodes(TreeNode* root) {
        if (!root) {
            return 0; // 如果根节点为空，返回节点数为0
        }

        int lh = 0, rh = 0; // 左子树和右子树的高度
        TreeNode* left = root, * right = root; // 用于计算高度的指针

        // 计算左子树高度
        while (left) {
            ++lh;
            left = left->left;
        }

        // 计算右子树高度
        while (right) {
            ++rh;
            right = right->right;
        }

        // 如果左子树高度等于右子树高度，说明左子树是满二叉树
        if (lh == rh) {
            return (1 << lh) - 1; // 返回节点数
        }

        int count = 1; // 节点数初始化为1（根节点）
        std::stack<TreeNode*> stack;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            if (node->left) {
                stack.push(node->left);
                ++count;
            }
            if (node->right) {
                stack.push(node->right);
                ++count;
            }
        }

        return count;
    }
};

// 创建完全二叉树
TreeNode* createCompleteTree(int arr[], int n, int i) {
    if (i >= n || arr[i] == -1) {
        return nullptr; // 如果节点为空，则返回nullptr
    }
    TreeNode* root = new TreeNode(arr[i]); // 创建当前节点
    root->left = createCompleteTree(arr, n, 2 * i + 1); // 创建左子树
    root->right = createCompleteTree(arr, n, 2 * i + 2); // 创建右子树
    return root; // 返回当前节点
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6}; // 完全二叉树的数组表示
    int n = sizeof(arr) / sizeof(arr[0]); // 数组长度
    TreeNode* root = createCompleteTree(arr, n, 0); // 创建完全二叉树
    Solution solution;
    int count = solution.countNodes(root); // 计算节点个数
    std::cout << "节点个数：" << count << std::endl; // 输出节点个数

    return 0;
}
```

#### Java

```
// 二叉树节点的定义
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) {
            return 0; // 如果根节点为空，返回节点数为0
        }

        int lh = 0, rh = 0; // 左子树和右子树的高度
        TreeNode left = root, right = root; // 用于计算高度的指针

        // 计算左子树高度
        while (left != null) {
            ++lh;
            left = left.left;
        }

        // 计算右子树高度
        while (right != null) {
            ++rh;
            right = right.right;
        }

        // 如果左子树高度等于右子树高度，说明左子树是满二叉树
        if (lh == rh) {
            return (1 << lh) - 1; // 返回节点数
        }

        // 如果左子树高度不等于右子树高度，递归计算左右子树节点数并返回
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}

public class Main {
    public static TreeNode createCompleteTree(int[] arr, int n, int i) {
        if (i >= n || arr[i] == -1) {
            return null; // 如果节点为空，则返回null
        }
        TreeNode root = new TreeNode(arr[i]); // 创建当前节点
        root.left = createCompleteTree(arr, n, 2 * i + 1); // 创建左子树
        root.right = createCompleteTree(arr, n, 2 * i + 2); // 创建右子树
        return root; // 返回当前节点
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6}; // 完全二叉树的数组表示
        int n = arr.length; // 数组长度
        TreeNode root = createCompleteTree(arr, n, 0); // 创建完全二叉树
        Solution solution = new Solution();
        int count = solution.countNodes(root); // 计算节点个数
        System.out.println("节点个数：" + count); // 输出节点个数
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

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0  # 如果根节点为空，返回节点数为0

        lh, rh = 0, 0  # 左子树和右子树的高度
        left, right = root, root  # 用于计算高度的指针

        # 计算左子树高度
        while left:
            lh += 1
            left = left.left

        # 计算右子树高度
        while right:
            rh += 1
            right = right.right

        # 如果左子树高度等于右子树高度，说明左子树是满二叉树
        if lh == rh:
            return (1 << lh) - 1  # 返回节点数

        # 如果左子树高度不等于右子树高度，递归计算左右子树节点数并返回
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

def create_complete_tree(arr, n, i):
    if i >= n or arr[i] == -1:
        return None  # 如果节点为空，则返回None
    root = TreeNode(arr[i])  # 创建当前节点
    root.left = create_complete_tree(arr, n, 2 * i + 1)  # 创建左子树
    root.right = create_complete_tree(arr, n, 2 * i + 2)  # 创建右子树
    return root  # 返回当前节点

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]  # 完全二叉树的数组表示
    n = len(arr)  # 数组长度
    root = create_complete_tree(arr, n, 0)  # 创建完全二叉树
    solution = Solution()
    count = solution.countNodes(root)  # 计算节点个数
    print("节点个数：", count)  # 输出节点个数
```

