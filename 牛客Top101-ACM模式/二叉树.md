# 二叉树

## 1、二叉树的前序遍历

### 1.1、问题描述

给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

> 示例 1：
>
> ![image-20240121201550857](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212015579.png)
>
> 输入：{1,#,2,3}
>
> 返回值：[1,2,3]

### 1.2、思路及代码

#### 1.2.1、递归

思路：

从根节点开始，首先访问根节点，然后递归地前序遍历左子树，最后递归地前序遍历右子树。

示例代码：

```C++
#include <iostream>
#include <vector>

// 定义二叉树的节点结构
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 前序遍历函数
void preorderTraversal(TreeNode* root, std::vector<int>& result) {
    if (root) {
        result.push_back(root->val);      // 访问当前节点的值
        preorderTraversal(root->left, result);  // 递归遍历左子树
        preorderTraversal(root->right, result); // 递归遍历右子树
    }
}

std::vector<int> preorderTraversal(TreeNode* root) {
    std::vector<int> result;
    preorderTraversal(root, result); // 从根节点开始前序遍历
    return result;
}

int main() {
    // 创建二叉树
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    // 进行前序遍历
    std::vector<int> result = preorderTraversal(root);

    // 输出结果
    std::cout << "Preorder Traversal: ";
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 释放内存
    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}
```

#### 1.2.2、非递归

思路：

使用一个栈 `nodeStack` 来辅助遍历，将节点入栈并逐个弹出，以确保在遍历左子树后可以正确遍历右子树。从根节点开始，每个节点都被访问一次，并按前序遍历的顺序存储在 `result` 向量中。

示例代码：

```C++
#include <iostream>
#include <vector>
#include <stack>

// 定义二叉树的节点结构
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

std::vector<int> preorderTraversal(TreeNode* root) {
    std::vector<int> result;
    std::stack<TreeNode*> nodeStack;
    
    TreeNode* current = root;
    while (current || !nodeStack.empty()) {
        while (current) {
            result.push_back(current->val);  // 访问当前节点的值
            nodeStack.push(current);
            current = current->left;  // 遍历左子树
        }
        current = nodeStack.top();
        nodeStack.pop();
        current = current->right;  // 遍历右子树
    }
    
    return result;
}

int main() {
    // 创建二叉树
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    // 进行前序遍历
    std::vector<int> result = preorderTraversal(root);

    // 输出结果
    std::cout << "Preorder Traversal: ";
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 释放内存
    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}
```

## 2、二叉树的中序遍历

### 2.1、问题描述

给定一个二叉树的根节点root，返回它的中序遍历结果。

> **示例1**
>
> 输入：{1,2,#,#,3}
>
> 返回值：[2,3,1]
>
> 说明：
>
> ![image-20240121201618969](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212016710.png)
>
> **示例2**
>
> 输入：{}
>
> 返回值：[]
>
> **示例3**
>
> 输入：{1,2}
>
> 返回值：[2,1]
>
> 说明：
>
> ![image-20240121201638716](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212016061.png)
>
> **示例4**
>
> 输入：{1,#,2}
>
> 返回值：[1,2]
>
> 说明：
>
> ![image-20240121201654377](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212016582.png)

### 2.2、思路及代码

#### 2.2.1、递归

思路：

首先遍历左子树，然后访问根节点，最后遍历右子树。

示例代码：

```C++
#include <iostream>
#include <vector>

// 定义二叉树的节点结构
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void inorderHelper(TreeNode* root, std::vector<int>& result) {
    if (root == nullptr) {
        return;
    }
    
    inorderHelper(root->left, result);  // 先遍历左子树
    result.push_back(root->val);        // 访问当前节点
    inorderHelper(root->right, result); // 再遍历右子树
}

std::vector<int> inorderTraversal(TreeNode* root) {
    std::vector<int> result;
    inorderHelper(root, result);
    return result;
}

int main() {
    // 创建二叉树
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);

    // 进行中序遍历
    std::vector<int> result = inorderTraversal(root);

    // 输出结果
    std::cout << "Inorder Traversal: ";
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 释放内存
    delete root->right->left;
    delete root->right;
    delete root;

    return 0;
}
```

#### 2.2.2、非递归

思路：

先将根节点入栈，然后遍历左子树，每次将左子树的节点入栈，直到没有左子树节点。接着弹出栈顶元素，将其值加入结果向量，然后遍历右子树，继续上述过程。

示例代码：

```C++
#include <iostream>
#include <vector>
#include <stack>

// 定义二叉树的节点结构
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

std::vector<int> inorderTraversal(TreeNode* root) {
    std::vector<int> result;
    std::stack<TreeNode*> s;
    TreeNode* current = root;

    while (current != nullptr || !s.empty()) {
        while (current != nullptr) {
            s.push(current);
            current = current->left;
        }
        current = s.top();
        s.pop();
        result.push_back(current->val);
        current = current->right;
    }

    return result;
}

int main() {
    // 创建二叉树
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);

    // 进行中序遍历
    std::vector<int> result = inorderTraversal(root);

    // 输出结果
    std::cout << "Inorder Traversal: ";
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 释放内存
    delete root->right->left;
    delete root->right;
    delete root;

    return 0;
}
```

## 3、二叉树的后序遍历

### 3.1、问题描述

给定一个二叉树，返回他的后序遍历的序列。

后序遍历是值按照 左节点->右节点->根节点 的顺序的遍历。

> 样例图
>
> ![image-20240121201717006](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212017004.png)
>
> **示例1**
>
> 输入：{1,#,2,3}
>
> 返回值：[3,2,1]
>
> 说明：如题面图  
>
> **示例2**
>
> 输入：{1}
>
> 返回值：[1]

### 3.2、思路及代码

#### 3.2.1、递归

思路：首先访问左子树，然后访问右子树，最后访问根节点。

代码：

```C++
#include <iostream>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

std::vector<int> postorderTraversal(TreeNode* root) {
    std::vector<int> result;

    // 递归出口
    if (root == nullptr) {
        return result;
    }

    // 递归遍历左子树
    if (root->left != nullptr) {
        std::vector<int> left_result = postorderTraversal(root->left);
        result.insert(result.end(), left_result.begin(), left_result.end());
    }

    // 递归遍历右子树
    if (root->right != nullptr) {
        std::vector<int> right_result = postorderTraversal(root->right);
        result.insert(result.end(), right_result.begin(), right_result.end());
    }

    // 访问根节点
    result.push_back(root->val);

    return result;
}

int main() {
    // 创建一个二叉树
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    std::cout << "Postorder Traversal: ";
    std::vector<int> result = postorderTraversal(root);
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 释放二叉树内存
    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}
```

#### 3.2.2、非递归

思路：

1. 首先将根节点和其左子树一直入栈，直到左子树为空。
2. 弹出栈顶元素，如果该元素的右子树为空或者已经访问过（通过`prev`记录），则将该节点的值加入结果集。
3. 如果右子树存在且未访问过，将右子树入栈。
4. 重复以上步骤直到栈为空。
5. 最后，将结果集反转，得到后序遍历的结果。

代码：

```C++
#include <iostream>
#include <vector>
#include <stack>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

std::vector<int> postorderTraversal(TreeNode* root) {
    std::vector<int> result;
    std::stack<TreeNode*> s;
    TreeNode* prev = nullptr;

    while (root || !s.empty()) {
        while (root) {
            s.push(root);
            root = root->left;
        }
        root = s.top();
        if (root->right && root->right != prev) {
            root = root->right;
        } else {
            result.push_back(root->val);
            s.pop();
            prev = root;
            root = nullptr;
        }
    }

    // 反转结果
    std::reverse(result.begin(), result.end());

    return result;
}

int main() {
    // 创建一个二叉树
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    std::cout << "Postorder Traversal: ";
    std::vector<int> result = postorderTraversal(root);
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 释放二叉树内存
    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}
```

## 4、求二叉树的层序遍历

### 4.1、问题描述

给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）。

> 例如： 给定的二叉树是{3,9,20,#,#,15,7},
>
> ![image-20240121201741439](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212017438.png)
>
> 该二叉树层序遍历的结果是 [ [3], [9,20], [15,7]
>
> ]
>
> 提示:
>
> 0 <= 二叉树的结点数 <= 1500
>
> **示例1**
>
> 输入：{1,2}
>
> 返回值：[[1],[2]]
>
> **示例2**
>
> 输入：{1,2,3,4,#,#,5}
>
> 返回值：[[1],[2,3],[4,5]]

### 4.2、思路及代码

思路：

1. 创建一个队列 `q`，并将根节点入队。
2. 进入循环，每次循环开始时，队列中的元素都是当前层的节点。
3. 在循环中，先获取当前队列的大小 `levelSize`，然后创建一个空的vector `levelNodes`，用于存储当前层的节点值。
4. 遍历当前层的所有节点，将它们的值加入 `levelNodes` 中，并将它们的左子节点和右子节点入队。
5. 将 `levelNodes` 添加到结果集中，重复以上步骤，直到队列为空。

代码：

```C++
#include <iostream>
#include <vector>
#include <queue>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

std::vector<std::vector<int>> levelOrder(TreeNode* root) {
    std::vector<std::vector<int>> result;
    if (!root) {
        return result;
    }

    std::queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        int levelSize = q.size();
        std::vector<int> levelNodes;

        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            levelNodes.push_back(node->val);

            if (node->left) {
                q.push(node->left);
            }

            if (node->right) {
                q.push(node->right);
            }
        }

        result.push_back(levelNodes);
    }

    return result;
}

int main() {
    // 创建一个二叉树
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    std::vector<std::vector<int>> result = levelOrder(root);

    std::cout << "Level Order Traversal:" << std::endl;
    for (const std::vector<int>& level : result) {
        for (int val : level) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }

    // 释放二叉树内存
    delete root->right->left;
    delete root->right->right;
    delete root->right;
    delete root->left;
    delete root;

    return 0;
}
```

## 5、按之字形顺序打印二叉树

### 5.1、问题描述

给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）。

> 例如： 给定的二叉树是{1,2,3,#,#,4,5}
>
> ![image-20240121201802571](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212018691.png)
>
> 该二叉树之字形层序遍历的结果是
>
> [
>
> [1],
>
> [3,2],
>
> [4,5]
>
> ]
>
> **示例1**
>
> 输入：{1,2,3,#,#,4,5}
>
> 返回值：[[1],[3,2],[4,5]]
>
> 说明：如题面解释，第一层是根节点，从左到右打印结果，第二层从右到左，第三层从左到右。     
>
> **示例2**
>
> 输入：{8,6,10,5,7,9,11}
>
> 返回值：[[8],[10,6],[5,7,9,11]]
>
> **示例3**
>
> 输入：{1,2,3,4,5}
>
> 返回值：[[1],[3,2],[4,5]]

### 5.2、思路及代码

思路：

1. 创建一个队列 `q`，将根节点入队，同时初始化布尔值 `isLeftToRight` 为 `true`。
2. 开始循环，每次循环表示一层的遍历。
3. 在循环内，首先获取当前队列的大小 `levelSize`，然后创建一个空的 `levelNodes` 用于存储当前层的节点值，同时创建一个栈 `levelStack` 用于存储从右到左的节点值。
4. 遍历当前层的所有节点，如果 `isLeftToRight` 为 `true`，将节点值加入 `levelNodes`，否则加入 `levelStack`。
5. 如果 `isLeftToRight` 为 `false`，从栈 `levelStack` 中依次弹出值加入 `levelNodes`。
6. 将 `levelNodes` 添加到结果集中，并将 `isLeftToRight` 取反，以控制下一层的遍历方向。
7. 继续循环，直到队列为空。

代码：

```C++
#include <iostream>
#include <vector>
#include <queue>
#include <stack>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

std::vector<std::vector<int>> zigzagLevelOrder(TreeNode* root) {
    std::vector<std::vector<int>> result;
    if (!root) {
        return result;
    }

    std::queue<TreeNode*> q;
    q.push(root);
    bool isLeftToRight = true;

    while (!q.empty()) {
        int levelSize = q.size();
        std::vector<int> levelNodes;
        std::stack<int> levelStack;

        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();

            if (isLeftToRight) {
                levelNodes.push_back(node->val);
            } else {
                levelStack.push(node->val);
            }

            if (node->left) {
                q.push(node->left);
            }

            if (node->right) {
                q.push(node->right);
            }
        }

        if (!isLeftToRight) {
            while (!levelStack.empty()) {
                levelNodes.push_back(levelStack.top());
                levelStack.pop();
            }
        }

        result.push_back(levelNodes);
        isLeftToRight = !isLeftToRight;
    }

    return result;
}

int main() {
    // 创建一个二叉树
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    std::vector<std::vector<int>> result = zigzagLevelOrder(root);

    std::cout << "Zigzag Level Order Traversal:" << std::endl;
    for (const std::vector<int>& level : result) {
        for (int val : level) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }

    // 释放二叉树内存
    delete root->right->left;
    delete root->right->right;
    delete root->right;
    delete root->left;
    delete root;

    return 0;
}
```

## 6、求二叉树的最大深度

### 6.1、问题描述

求给定二叉树的最大深度，深度是指树的根节点到任一叶子节点路径上节点的数量。最大深度是所有叶子节点的深度的最大值。（注：叶子节点是指没有子节点的节点。）

### 6.2、思路及代码

#### 6.2.1、递归

思路：从根节点开始，一直到叶子节点，然后回溯到父节点，计算左子树和右子树的深度，最终返回较大的深度作为当前节点的深度，一直递归下去。

代码：

```C++
#include <iostream>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

int maxDepth(TreeNode* root) {
    if (!root) {
        return 0; // 空树深度为0
    }

    int leftDepth = maxDepth(root->left); // 左子树深度
    int rightDepth = maxDepth(root->right); // 右子树深度

    return 1 + std::max(leftDepth, rightDepth); // 当前节点的深度为较大子树深度加1
}

int main() {
    // 创建一个二叉树
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    int depth = maxDepth(root);

    std::cout << "Max Depth of Binary Tree: " << depth << std::endl;

    // 释放二叉树内存
    delete root->right->left;
    delete root->right->right;
    delete root->right;
    delete root->left;
    delete root;

    return 0;
}
```

#### 6.2.2、非递归

思路：

1. 首先，检查二叉树是否为空。如果为空（即根节点为nullptr），则树的深度为0，返回0。
2. 如果树不为空，我们创建一个队列（这里使用 `std::queue`），并将根节点放入队列。
3. 初始化深度为0。这个深度表示当前正在处理的层级。
4. 使用循环来处理队列中的节点，直到队列为空。在每一轮循环中，我们处理当前层的所有节点。
5. 在循环内部，我们首先获取当前队列的大小，这个大小表示当前层的节点个数。
6. 然后，我们依次出队当前层的所有节点，并检查它们的左子节点和右子节点。如果存在左子节点，将左子节点入队。如果存在右子节点，将右子节点入队。
7. 当处理完当前层的节点后，增加深度。
8. 重复上述步骤，直到队列为空，此时深度变量中的值就是树的最大深度。
9. 返回深度作为结果。

代码：

```C++
#include <iostream>
#include <queue>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

int maxDepth(TreeNode* root) {
    if (!root) {
        return 0; // 空树深度为0
    }

    std::queue<TreeNode*> q;
    q.push(root);
    int depth = 0;

    while (!q.empty()) {
        int levelSize = q.size(); // 当前层的节点个数

        for (int i = 0; i < levelSize; ++i) {
            TreeNode* current = q.front();
            q.pop();

            if (current->left) {
                q.push(current->left);
            }

            if (current->right) {
                q.push(current->right);
            }
        }

        depth++; // 每处理完一层，深度加1
    }

    return depth;
}

int main() {
    // 创建一个二叉树
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    int depth = maxDepth(root);

    std::cout << "Max Depth of Binary Tree: " << depth << std::endl;

    // 释放二叉树内存
    delete root->right->left;
    delete root->right->right;
    delete root->right;
    delete root->left;
    delete root;

    return 0;
}
```

## 7、二叉树中和为某一值的路径（一）

### 7.1、问题描述

给定一个二叉树root和一个值 sum ，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径。

1.该题路径定义为从树的根结点开始往下一直到叶子结点所经过的结点

2.叶子节点是指没有子节点的节点

3.路径只能从父节点到子节点，不能从子节点到父节点

4.总节点数目为n

> 例如： 给出如下的二叉树， *sum*=22，
>
> ![image-20240121201830611](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212018867.png)
>
> 返回true，因为存在一条路径 5→4→11→25→4→11→2的节点值之和为 22
>
> **示例1**
>
> 输入：{5,4,8,1,11,#,9,#,#,2,7},22
>
> 返回值：true
>
> **示例2**
>
> 输入：{1,2},0
>
> 返回值：false
>
> **示例3**
>
> 输入：{1,2},3
>
> 返回值：true
>
> **示例4**
>
> 输入：{},0
>
> 返回值：false

### 7.2、思路及代码

#### 7.2.1、递归

思路：

1. 从根节点开始递归遍历二叉树，同时传递一个表示当前路径和的参数，初始值为0。
2. 在递归的过程中，将当前节点的值累加到路径和中。
3. 在每个节点处，首先检查该节点是否为叶子节点（即没有左子节点和右子节点）。如果是叶子节点，检查当前路径和是否等于给定的 `sum` 值。如果等于，则找到了一条路径，返回 `true`。如果不等于，返回 `false`。
4. 如果当前节点不是叶子节点，继续递归遍历其左子节点和右子节点，分别传递当前路径和。
5. 返回递归左子节点和右子节点的结果的逻辑或（`||`），表示只要左子节点或右子节点中有一条路径满足条件，即可返回 `true`。
6. 最终，如果整个树上都没有找到满足条件的路径，返回 `false`。

代码：

```C++
#include <iostream>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

bool hasPathSum(TreeNode* root, int sum) {
    if (root == nullptr) {
        return false;
    }

    sum -= root->val;

    if (root->left == nullptr && root->right == nullptr) {
        return sum == 0;
    }

    return hasPathSum(root->left, sum) || hasPathSum(root->right, sum);
}

int main() {
    // 构建二叉树
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(4);
    root->right = new TreeNode(8);
    root->left->left = new TreeNode(11);
    root->right->left = new TreeNode(13);
    root->right->right = new TreeNode(4);
    root->left->left->left = new TreeNode(7);
    root->left->left->right = new TreeNode(2);
    root->right->right->right = new TreeNode(1);

    int sum = 22;

    bool result = hasPathSum(root, sum);
    std::cout << (result ? "Path exists" : "Path does not exist") << std::endl;

    return 0;
}
```

#### 7.2.2、非递归

思路：

1. 创建一个栈，同时将根节点和路径和（初始为0）压入栈中。
2. 使用一个循环来迭代处理栈中的元素，直到栈为空。
3. 在每一次迭代中，弹出栈顶的元素，包括节点和路径和。如果该节点是叶子节点且路径和等于给定的 `sum` 值，则找到一条路径，返回 `true`。
4. 如果当前节点不是叶子节点，将它的子节点（如果存在）与新的路径和（累加原路径和与当前节点值）分别入栈。
5. 继续迭代直到栈为空，或者找到一条满足条件的路径。
6. 如果整个树上都没有找到满足条件的路径，返回 `false`。

代码：

```C++
#include <iostream>
#include <stack>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

bool hasPathSum(TreeNode* root, int sum) {
    if (root == nullptr) {
        return false;
    }

    std::stack<std::pair<TreeNode*, int>> nodeStack;
    nodeStack.push({root, 0});

    while (!nodeStack.empty()) {
        auto [node, currentSum] = nodeStack.top();
        nodeStack.pop();
        currentSum += node->val;

        if (node->left == nullptr && node->right == nullptr) {
            if (currentSum == sum) {
                return true;
            }
        }

        if (node->left != nullptr) {
            nodeStack.push({node->left, currentSum});
        }

        if (node->right != nullptr) {
            nodeStack.push({node->right, currentSum});
        }
    }

    return false;
}

int main() {
    // 构建二叉树
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(4);
    root->right = new TreeNode(8);
    root->left->left = new TreeNode(11);
    root->right->left = new TreeNode(13);
    root->right->right = new TreeNode(4);
    root->left->left->left = new TreeNode(7);
    root->left->left->right = new TreeNode(2);
    root->right->right->right = new TreeNode(1);

    int sum = 22;

    bool result = hasPathSum(root, sum);
    std::cout << (result ? "Path exists" : "Path does not exist") << std::endl;

    return 0;
}
```

## 8、**二叉搜索树与双向链表**

### 8.1、问题描述

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。如下图所示

![image-20240121201855416](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212018814.png)

> **输入描述：**
>
> 二叉树的根节点
>
> **返回值描述：**
>
> 双向链表的其中一个头节点。
>
> **示例1**
>
> 输入：{10,6,14,4,8,12,16}
>
> 返回值：From left to right are:4,6,8,10,12,14,16;From right to left are:16,14,12,10,8,6,4;
>
> 说明：输入题面图中二叉树，输出的时候将双向链表的头节点返回即可。     
>
> **示例2**
>
> 输入：{5,4,#,3,#,2,#,1}
>
> 返回值：From left to right are:1,2,3,4,5;From right to left are:5,4,3,2,1;
>
> 说明：
>
> ​                    5

### 8.2、思路及代码

#### 8.2.1、方法一

思路：

1. 初始化一个指向双向链表头部的指针 `head` 和一个指向当前双向链表尾部的指针 `tail`，都为空。
2. 进行中序遍历，遍历二叉搜索树。中序遍历过程中，首先递归遍历左子树，然后访问当前节点，最后递归遍历右子树。
3. 在访问当前节点时，将其插入到双向链表中：
   1. 如果 `tail` 为空，表示当前节点是双向链表的第一个节点，因此将 `head` 和 `tail` 都指向当前节点。
   2. 否则，将当前节点的左指针指向 `tail`，将 `tail` 的右指针指向当前节点，然后更新 `tail` 为当前节点。
4. 完成中序遍历后，`head` 指向双向链表的第一个节点，`tail` 指向最后一个节点。
5. 返回 `head`，即双向链表的头部。

代码：

```C++
#include <iostream>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

struct DoubleListNode {
    int val;
    DoubleListNode* prev;
    DoubleListNode* next;
    DoubleListNode(int x) : val(x), prev(nullptr), next(nullptr) {}
};

DoubleListNode* treeToDoublyList(TreeNode* root) {
    if (root == nullptr) {
        return nullptr;
    }

    DoubleListNode* head = nullptr;
    DoubleListNode* tail = nullptr;

    // Helper function to do the conversion during in-order traversal
    auto convertToDoublyList = [&head, &tail](TreeNode* node) {
        if (tail == nullptr) {
            head = new DoubleListNode(node->val);
            tail = head;
        } else {
            tail->next = new DoubleListNode(node->val);
            tail->next->prev = tail;
            tail = tail->next;
        }
    };

    // In-order traversal
    std::function<void(TreeNode*)> inorder = [&inorder, &convertToDoublyList](TreeNode* node) {
        if (node == nullptr) {
            return;
        }
        inorder(node->left);
        convertToDoublyList(node);
        inorder(node->right);
    };

    inorder(root);

    // Connect the head and tail nodes to form a circular doubly linked list
    if (head && tail) {
        head->prev = tail;
        tail->next = head;
    }

    return head;
}

// Helper function to print the doubly linked list
void printDoublyList(DoubleListNode* head) {
    if (head == nullptr) {
        return;
    }
    DoubleListNode* current = head;
    do {
        std::cout << current->val << " ";
        current = current->next;
    } while (current != head);
    std::cout << std::endl;
}

int main() {
    // Construct a sample BST
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);

    DoubleListNode* result = treeToDoublyList(root);

    // Print the doubly linked list
    printDoublyList(result);

    return 0;
}
```

#### 8.2.2、方法二

思路：

1. 初始化两个指针 `prev` 和 `head`，分别用于追踪双向链表的前一个节点和头节点。初始化它们都为 `nullptr`。
2. 使用栈来进行中序遍历，首先将根节点入栈。
3. 进行循环，直到栈为空：
   1. 将当前节点出栈，并处理它的左子树。
   2. 如果 `prev` 为空，表示当前节点是双向链表的头节点，因此将 `head` 指向当前节点。
   3. 如果 `prev` 不为空，将 `prev` 的右指针指向当前节点，同时将当前节点的左指针指向 `prev`。
   4. 更新 `prev` 为当前节点，表示当前节点已经成为前一个节点。
   5. 处理当前节点的右子树，将右子节点入栈。
4. 当遍历完成后，`head` 指向双向链表的头部，同时 `prev` 指向双向链表的尾部。
5. 返回 `head`。

代码：

```C++
#include <iostream>
#include <stack>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

struct DoubleListNode {
    int val;
    DoubleListNode* prev;
    DoubleListNode* next;
    DoubleListNode(int x) : val(x), prev(nullptr), next(nullptr) {}
};

DoubleListNode* treeToDoublyList(TreeNode* root) {
    if (root == nullptr) {
        return nullptr;
    }

    DoubleListNode* head = nullptr;
    DoubleListNode* prev = nullptr;

    std::stack<TreeNode*> nodes;
    TreeNode* current = root;

    while (current || !nodes.empty()) {
        while (current) {
            nodes.push(current);
            current = current->left;
        }
        
        current = nodes.top();
        nodes.pop();
        
        if (!prev) {
            head = new DoubleListNode(current->val);
            prev = head;
        } else {
            prev->next = new DoubleListNode(current->val);
            prev->next->prev = prev;
            prev = prev->next;
        }

        current = current->right;
    }

    head->prev = prev;
    prev->next = head;

    return head;
}

// Helper function to print the doubly linked list
void printDoublyList(DoubleListNode* head) {
    if (head == nullptr) {
        return;
    }
    DoubleListNode* current = head;
    do {
        std::cout << current->val << " ";
        current = current->next;
    } while (current != head);
    std::cout << std::endl;
}

int main() {
    // Construct a sample BST
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);

    DoubleListNode* result = treeToDoublyList(root);

    // Print the doubly linked list
    printDoublyList(result);

    return 0;
}
```

## 9、对称的二叉树

### 9.1、问题描述

给定一棵二叉树，判断其是否是自身的镜像。

> 例如：下面这棵二叉树是对称的
>
> ![image-20240121201920551](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212019540.png)
>
> 下面这棵二叉树不对称。
>
> ![image-20240121201936613](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212019676.png)
>
> 
>
> 备注：
>
> 你可以用递归和迭代两种方法解决这个问题
>
> **示例1**
>
> 输入：{1,2,2,3,4,4,3}
>
> 返回值：true
>
> **示例2**
>
> 输入：{8,6,9,5,7,7,5}
>
> 返回值：false

### 9.2、思路及代码

#### 9.2.1、递归

思路：

1. 首先，判断根节点是否为空，如果为空，返回 `true`。
2. 如果根节点不为空，比较它的左子树和右子树是否是镜像对称的。
3. 比较的方式是递归地将左子树的左子树和右子树的右子树、左子树的右子树和右子树的左子树进行比较。如果它们都相等，那么当前树是镜像的。
4. 递归地比较左子树和右子树，如果都是镜像的，返回 `true`；否则返回 `false`。

代码：

```C++
#include <iostream>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

bool isMirror(TreeNode* leftSubtree, TreeNode* rightSubtree) {
    // 如果两棵子树都为空，认为它们是镜像的
    if (leftSubtree == nullptr && rightSubtree == nullptr) {
        return true;
    }
    
    // 如果只有一棵子树为空，认为它们不是镜像的
    if (leftSubtree == nullptr || rightSubtree == nullptr) {
        return false;
    }
    
    // 比较左子树的左子树和右子树的右子树，以及左子树的右子树和右子树的左子树是否镜像
    return (leftSubtree->val == rightSubtree->val) &&
           isMirror(leftSubtree->left, rightSubtree->right) &&
           isMirror(leftSubtree->right, rightSubtree->left);
}

bool isSymmetric(TreeNode* root) {
    if (root == nullptr) {
        return true;
    }
    
    return isMirror(root->left, root->right);
}

int main() {
    // Construct a sample symmetric binary tree
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(3);

    if (isSymmetric(root)) {
        std::cout << "The binary tree is symmetric." << std::endl;
    } else {
        std::cout << "The binary tree is not symmetric." << std::endl;
    }

    return 0;
}
```

#### 9.2.2、迭代

思路：

1. 初始化一个队列，将根节点入队两次，即 `root` 和 `root`。
2. 从队列中弹出两个节点，分别表示当前层的两个节点。
3. 检查这两个节点是否对称。如果两个节点都为空，继续下一轮迭代。如果一个节点为空而另一个不为空，或它们的值不相等，返回 `false`，表示树不是自身的镜像。
4. 如果节点对称，将它们的左子节点和右子节点分别入队，但是顺序需要注意，先将第一个节点的左子节点和第二个节点的右子节点入队，再将第一个节点的右子节点和第二个节点的左子节点入队。
5. 重复步骤2~4，直到队列为空。如果在过程中没有发现不对称的节点，返回 `true`，表示树是自身的镜像。

代码：

```C++
#include <iostream>
#include <queue>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

bool isSymmetric(TreeNode* root) {
    if (root == nullptr) {
        return true; // 空树是对称的
    }
    
    std::queue<TreeNode*> q;
    q.push(root);
    q.push(root);
    
    while (!q.empty()) {
        TreeNode* node1 = q.front();
        q.pop();
        TreeNode* node2 = q.front();
        q.pop();
        
        if (node1 == nullptr && node2 == nullptr) {
            continue; // 两个节点都为空，继续下一轮迭代
        }
        if (node1 == nullptr || node2 == nullptr) {
            return false; // 一个节点为空而另一个不为空，不对称
        }
        if (node1->val != node2->val) {
            return false; // 节点值不相等，不对称
        }
        
        q.push(node1->left); // 注意入队的顺序
        q.push(node2->right);
        q.push(node1->right);
        q.push(node2->left);
    }
    
    return true;
}

int main() {
    // Construct a sample symmetric binary tree
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(3);

    if (isSymmetric(root)) {
        std::cout << "The binary tree is symmetric." << std::endl;
    } else {
        std::cout << "The binary tree is not symmetric." << std::endl;
    }

    return 0;
}
```

## 10、合并二叉树

### 10.1、问题描述

已知两颗二叉树，将它们合并成一颗二叉树。合并规则是：都存在的结点，就将结点值加起来，否则空的位置就由另一个树的结点来代替。

> 例如： 两颗二叉树是: Tree 1
>
> ![image-20240121202000161](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212020285.png)
>
> Tree 2
>
> ![image-20240121202016328](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212020630.png)
>
> 合并后的树为
>
> ![image-20240121202035935](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212020237.png)
>
> **示例1**
>
> 输入：{1,3,2,5},{2,1,3,#,4,#,7}
>
> 返回值：{3,4,5,5,4,#,7}
>
> 说明：如题面图 
>
> **示例2**
>
> 输入：{1},{}
>
> 返回值：{1}

### 10.2、思路及代码

思路：

1. 如果两棵树的根节点都为空，返回空树。
2. 如果其中一棵树的根节点为空，返回另一棵树的根节点。
3. 创建一个新节点，值为两棵树对应节点的值相加。
4. 递归处理左子树：新节点的左子树等于两棵树的左子树的合并结果。
5. 递归处理右子树：新节点的右子树等于两棵树的右子树的合并结果。
6. 返回新根节点。

代码：

```C++
#include <iostream>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
    if (t1 == nullptr && t2 == nullptr) {
        return nullptr; // 两棵树的根节点都为空，返回空树
    }
    if (t1 == nullptr) {
        return t2; // t1为空，返回t2的根节点
    }
    if (t2 == nullptr) {
        return t1; // t2为空，返回t1的根节点
    }

    TreeNode* mergedRoot = new TreeNode(t1->val + t2->val);
    mergedRoot->left = mergeTrees(t1->left, t2->left); // 递归处理左子树
    mergedRoot->right = mergeTrees(t1->right, t2->right); // 递归处理右子树

    return mergedRoot;
}

// Helper function to print the tree (in-order traversal)
void printTree(TreeNode* root) {
    if (root == nullptr) {
        return;
    }
    printTree(root->left);
    std::cout << root->val << " ";
    printTree(root->right);
}

int main() {
    // Create two sample binary trees
    TreeNode* t1 = new TreeNode(1);
    t1->left = new TreeNode(3);
    t1->right = new TreeNode(2);
    t1->left->left = new TreeNode(5);

    TreeNode* t2 = new TreeNode(2);
    t2->left = new TreeNode(1);
    t2->right = new TreeNode(3);
    t2->left->right = new TreeNode(4);
    t2->right->right = new TreeNode(7);

    // Merge the two trees
    TreeNode* mergedTree = mergeTrees(t1, t2);

    std::cout << "Merged tree: ";
    printTree(mergedTree);
    std::cout << std::endl;

    return 0;
}
```

## 11、二叉树的镜像

### 11.1、问题描述

操作给定的二叉树，将其变换为源二叉树的镜像。

> 比如：
>
> 源二叉树
>
> ![image-20240121202059228](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212021258.png)
>
> 镜像二叉树
>
> ![image-20240121202113886](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212021933.png)
>
> 
>
> **示例1**
>
> 输入：{8,6,10,5,7,9,11}
>
> 返回值：{8,10,6,11,9,7,5}
>
> 说明：如题面所示    
>
> **示例2**
>
> 输入：{}
>
> 返回值：{}

### 11.2、思路及代码

#### 11.2.1、递归

思路：

1. 如果根节点为空，直接返回空。
2. 交换根节点的左右子树。
3. 递归处理左子树，使左子树变成其镜像。
4. 递归处理右子树，使右子树变成其镜像。
5. 返回根节点。

```C++
#include <iostream>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

void mirrorTree(TreeNode* root) {
    if (root == nullptr) {
        return;
    }

    // 交换根节点的左右子树
    TreeNode* temp = root->left;
    root->left = root->right;
    root->right = temp;

    // 递归处理左子树
    mirrorTree(root->left);

    // 递归处理右子树
    mirrorTree(root->right);
}

// Helper function to print the tree (in-order traversal)
void printTree(TreeNode* root) {
    if (root == nullptr) {
        return;
    }
    printTree(root->left);
    std::cout << root->val << " ";
    printTree(root->right);
}

int main() {
    // Create a sample binary tree
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    // Mirror the tree
    mirrorTree(root);

    std::cout << "Mirrored tree: ";
    printTree(root);
    std::cout << std::endl;

    return 0;
}
```

#### 11.2.2、非递归

思路：

1. 如果根节点为空，直接返回空。
2. 创建一个栈，将根节点入栈。
3. 进入循环，直到栈为空：
   1. 弹出栈顶节点，并交换其左右子树。
   2. 如果左子树不为空，将左子树入栈。
   3. 如果右子树不为空，将右子树入栈。
4. 返回原始根节点。

代码：

```C++
#include <iostream>
#include <stack>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

void mirrorTree(TreeNode* root) {
    if (root == nullptr) {
        return;
    }

    std::stack<TreeNode*> nodeStack;
    nodeStack.push(root);

    while (!nodeStack.empty()) {
        TreeNode* currentNode = nodeStack.top();
        nodeStack.pop();

        // Swap left and right subtrees
        TreeNode* temp = currentNode->left;
        currentNode->left = currentNode->right;
        currentNode->right = temp;

        // Push left child if not null
        if (currentNode->left) {
            nodeStack.push(currentNode->left);
        }

        // Push right child if not null
        if (currentNode->right) {
            nodeStack.push(currentNode->right);
        }
    }
}

// Helper function to print the tree (in-order traversal)
void printTree(TreeNode* root) {
    if (root == nullptr) {
        return;
    }
    printTree(root->left);
    std::cout << root->val << " ";
    printTree(root->right);
}

int main() {
    // Create a sample binary tree
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    // Mirror the tree
    mirrorTree(root);

    std::cout << "Mirrored tree: ";
    printTree(root);
    std::cout << std::endl;

    return 0;
}
```

## 12、判断是不是二叉搜索树

### 12.1、问题描述

给定一个二叉树根节点，请你判断这棵树是不是二叉搜索树。

二叉搜索树满足每个节点的左子树上的所有节点均小于当前节点且右子树上的所有节点均大于当前节点。

> 例：
>
> ![image-20240121202138201](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212021343.png)
>
> 图1
>
> ![image-20240121202151419](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212021519.png)
>
> 图2
>
> **示例1**
>
> 输入：{1,2,3}
>
> 返回值：false
>
> 说明：如题面图1 
>
> **示例2**
>
> 输入：{2,1,3}
>
> 返回值：true
>
> 说明：如题面图2 

### 12.2、思路及代码

#### 12.2.1、递归

思路：

1. 创建一个中序遍历函数 `inorderTraversal`，接收一个二叉树节点和一个向量，用于存储遍历结果。
2. 在中序遍历函数中，递归遍历左子树，将左子树节点的值添加到向量中，然后遍历当前节点，最后再递归遍历右子树。
3. 在主函数中，调用中序遍历函数，并传递根节点和一个向量。
4. 检查遍历结果向量是否按升序排列，如果是，返回 `true` 表示这是一棵BST，否则返回 `false` 表示不是。

代码：

```C++
#include <iostream>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

void inorderTraversal(TreeNode* root, std::vector<int>& values) {
    if (root == nullptr) {
        return;
    }

    // Recursively traverse left subtree
    inorderTraversal(root->left, values);

    // Visit current node (store its value in the vector)
    values.push_back(root->val);

    // Recursively traverse right subtree
    inorderTraversal(root->right, values);
}

bool isValidBST(TreeNode* root) {
    std::vector<int> values;
    inorderTraversal(root, values);

    // Check if the values are in ascending order
    for (int i = 1; i < values.size(); i++) {
        if (values[i] <= values[i - 1]) {
            return false;
        }
    }

    return true;
}

int main() {
    // Create a sample binary search tree
    TreeNode* root = new TreeNode(2);
    root->left = new TreeNode(1);
    root->right = new TreeNode(3);

    bool isBST = isValidBST(root);
    if (isBST) {
        std::cout << "This is a Binary Search Tree (BST)." << std::endl;
    } else {
        std::cout << "This is not a BST." << std::endl;
    }

    return 0;
}
```

#### 12.2.2、非递归

思路：

1. 使用栈来模拟中序遍历过程。
2. 初始化一个当前节点指针 `cur` 指向根节点，创建一个空栈 `s` 来存储节点。
3. 进入循环，遍历树的节点。在循环中：
   1. 将当前节点 `cur` 入栈 `s`，然后将 `cur` 指向它的左子节点，直到左子节点为空。
   2. 弹出栈顶元素，将 `cur` 指向弹出的节点，检查其值是否大于之前遍历的节点值（前一个节点值）。如果不是，返回 `false`，因为不满足BST的条件。
   3. 将 `cur` 指向它的右子节点，然后继续遍历。
4. 如果遍历结束后都没有返回 `false`，说明树是BST，返回 `true`。

代码：

```C++
#include <iostream>
#include <stack>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

bool isValidBST(TreeNode* root) {
    if (!root) {
        return true;  // An empty tree is considered a valid BST
    }

    std::stack<TreeNode*> s;
    TreeNode* cur = root;
    TreeNode* prev = nullptr;

    while (cur || !s.empty()) {
        while (cur) {
            s.push(cur);
            cur = cur->left;
        }

        cur = s.top();
        s.pop();

        if (prev && prev->val >= cur->val) {
            return false;
        }

        prev = cur;
        cur = cur->right;
    }

    return true;
}

int main() {
    // Create a sample binary search tree
    TreeNode* root = new TreeNode(2);
    root->left = new TreeNode(1);
    root->right = new TreeNode(3);

    bool isBST = isValidBST(root);
    if (isBST) {
        std::cout << "This is a Binary Search Tree (BST)." << std::endl;
    } else {
        std::cout << "This is not a BST." << std::endl;
    }

    return 0;
}
```

## 13、判断是不是完全二叉树

### 13.1、问题描述

给定一个二叉树，确定他是否是一个完全二叉树。

完全二叉树的定义：若二叉树的深度为 h，除第 h 层外，其它各层的结点数都达到最大个数，第 h 层所有的叶子结点都连续集中在最左边，这就是完全二叉树。（第 h 层可能包含 [1~2h] 个节点）

### 13.2、思路及代码

#### 13.2.1、递归

思路：

1. 使用DFS递归遍历二叉树，同时传递当前节点的层数和编号。
2. 每次递归，比较当前节点的编号与当前层的叶子节点数。
3. 如果当前节点的编号等于叶子节点数，则继续递归左右子树。
4. 如果当前节点的编号小于叶子节点数，返回 false，因为叶子节点应该从左到右紧凑排列，当前节点编号小于叶子节点数表示缺失了某些节点，不是完全二叉树。
5. 最终，如果遍历完整个树都没有发现不满足完全二叉树性质的情况，返回 true。

代码：

```C++
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool isCompleteBinaryTree(TreeNode* root, int idx, int numNodes) {
    if (!root) return true; // 空树被认为是完全二叉树

    // 计算当前层的叶子节点数
    int numLeaves = numNodes - idx;

    // 检查当前节点是否越界
    if (idx >= numNodes) return false;

    // 检查左子树是否是完全二叉树
    if (!isCompleteBinaryTree(root->left, 2 * idx + 1, numNodes)) return false;

    // 检查右子树是否是完全二叉树
    if (!isCompleteBinaryTree(root->right, 2 * idx + 2, numNodes)) return false;

    return true;
}

bool isCompleteBinaryTree(TreeNode* root) {
    int numNodes = 0;
    // 计算二叉树的总节点数
    if (root) {
        numNodes = 1;
        if (root->left) numNodes += 1;
        if (root->right) numNodes += 1;
    }

    // 从根节点开始递归
    return isCompleteBinaryTree(root, 0, numNodes);
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);

    if (isCompleteBinaryTree(root)) {
        cout << "This is a complete binary tree." << endl;
    } else {
        cout << "This is not a complete binary tree." << endl;
    }

    return 0;
}
```

#### 13.2.2、非递归

思路：

1. 使用队列进行层序遍历。
2. 从根节点开始，将节点加入队列，并开始遍历树的每一层。
3. 当遇到第一个空节点时，应该保证之后的所有节点都是叶子节点。
4. 如果在之后的层次遍历中，出现了非叶子节点，则这棵树不是完全二叉树。
5. 如果一直遍历到队列为空，没有发现非叶子节点，则这棵树是完全二叉树。

代码：

```C++
#include <iostream>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool isCompleteBinaryTree(TreeNode* root) {
    if (!root) return true; // 空树被认为是完全二叉树
    queue<TreeNode*> q;
    q.push(root);
    bool foundEmpty = false;

    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();

        if (!node) {
            foundEmpty = true;
        } else {
            if (foundEmpty) {
                return false; // 如果之前已经找到空节点，这之后不能再有非空节点
            }
            q.push(node->left);
            q.push(node->right);
        }
    }

    return true;
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);

    if (isCompleteBinaryTree(root)) {
        cout << "This is a complete binary tree." << endl;
    } else {
        cout << "This is not a complete binary tree." << endl;
    }

    return 0;
}
```

## 14、 **判断是不是完全二叉树**

### 14.1、问题描述

给定一个二叉树，确定他是否是一个完全二叉树。

完全二叉树的定义：若二叉树的深度为 h，除第 h 层外，其它各层的结点数都达到最大个数，第 h 层所有的叶子结点都连续集中在最左边，这就是完全二叉树。（第 h 层可能包含 [1~2h] 个节点）

> 样例图1：
>
> ![image-20240121202223281](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212022388.png)
>
> 样例图2：
>
> ![image-20240121202238325](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212022342.png)
>
> 样例图3：
>
> ![image-20240121202251957](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212022918.png)
>
> **示例1**
>
> 输入：{1,2,3,4,5,6}
>
> 返回值：true
>
> **示例2**
>
> 输入：{1,2,3,4,5,6,7}
>
> 返回值：true
>
> **示例3**
>
> 输入：{1,2,3,4,5,#,6}
>
> 返回值：false

### 14.2、思路及代码

#### 14.2.1、递归

思路：

1. 首先定义一个函数 `isCompleteTree`，该函数用于判断以当前节点 `node` 为根的子树是否为完全二叉树。
2. 如果二叉树为空，即 `node` 为 `nullptr`，那么它是完全二叉树。
3. 如果 `node` 不为空，判断左子树和右子树是否为完全二叉树。
4. 通过递归检查左子树和右子树，以及它们的深度信息，来确定是否满足完全二叉树的定义。
5. 如果左子树是完全二叉树，右子树也是完全二叉树，并且它们的深度差不超过1，那么以 `node` 为根的二叉树也是完全二叉树。

参考代码：

```C++
#include <iostream>
#include <algorithm>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 定义一个辅助函数用于计算树的深度
int depth(TreeNode* node) {
    if (!node) {
        return 0;
    }
    int leftDepth = depth(node->left);
    int rightDepth = depth(node->right);
    return 1 + max(leftDepth, rightDepth);
}

bool isCompleteTree(TreeNode* root) {
    if (!root) {
        return true; // 空树是完全二叉树
    }

    int leftDepth = depth(root->left);
    int rightDepth = depth(root->right);

    return isCompleteTree(root->left) && isCompleteTree(root->right) &&
           (abs(leftDepth - rightDepth) <= 1);
}

int main() {
    // 创建一个二叉树示例
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);

    if (isCompleteTree(root)) {
        cout << "This is a complete binary tree." << endl;
    } else {
        cout << "This is not a complete binary tree." << endl;
    }

    return 0;
}
```

#### 14.2.2、非递归

思路：

1. 使用层序遍历（广度优先遍历）二叉树的方式。
2. 从根节点开始，将每个节点按照层序遍历的顺序依次入队，并检查是否满足完全二叉树的定义。
3. 如果某个节点为空，后续遍历的节点应该全部为空，否则不满足完全二叉树的定义。
4. 如果某个节点不为空，继续将其左右子节点入队，直到遍历完整棵树。
5. 最后检查队列中是否还有非空节点，如果有，则不满足完全二叉树的定义。

参考代码：

```C++
#include <iostream>
#include <queue>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool isCompleteTree(TreeNode* root) {
    if (!root) {
        return true; // 空树是完全二叉树
    }

    queue<TreeNode*> q;
    q.push(root);
    bool hasEmptyNode = false; // 标记是否出现空节点

    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();

        if (node) {
            // 遍历非空节点
            if (hasEmptyNode) {
                return false; // 如果之前出现过空节点，这个节点应为空
            }
            q.push(node->left);
            q.push(node->right);
        } else {
            hasEmptyNode = true; // 标记出现了空节点
        }
    }

    return true;
}
```

## 15、判断是不是平衡二叉树

### 15.1、问题描述

输入一棵节点数为 n 二叉树，判断该二叉树是否是平衡二叉树。

在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树

平衡二叉树（Balanced Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。

> 样例解释：
>
> ![image-20240121202314650](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212023737.png)
>
> 样例二叉树如图，为一颗平衡二叉树
>
> 注：我们约定空树是平衡二叉树。
>
> **输入描述：**
>
> 输入一棵二叉树的根节点
>
> **返回值描述：**
>
> 输出一个布尔类型的值
>
> **示例1**
>
> 输入：{1,2,3,4,5,6,7}
>
> 返回值：true
>
> **示例2**
>
> 输入：{}
>
> 返回值：true

### 15.2、思路及代码

#### 15.2.1、递归

思路：

1. 创建一个递归函数 `isBalancedTree` 来判断当前节点是否满足平衡二叉树的条件。
2. 在递归函数中，首先判断当前节点是否为空，如果为空则返回 `true`。
3. 递归地检查左右子树是否是平衡二叉树，通过计算它们的高度来判断。
4. 如果左子树和右子树都是平衡二叉树，并且它们的高度差的绝对值不超过1，那么当前节点也是平衡二叉树。
5. 返回结果时，需要同时返回当前子树的高度，这样可以在递归过程中比较左右子树的高度差。

参考代码：

```C++
#include <iostream>
#include <algorithm>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 递归函数，判断是否是平衡二叉树，以及返回树的高度
pair<bool, int> isBalancedTree(TreeNode* root) {
    if (!root) {
        return make_pair(true, 0);
    }

    pair<bool, int> left = isBalancedTree(root->left);
    pair<bool, int> right = isBalancedTree(root->right);

    bool isBalanced = left.first && right.first && abs(left.second - right.second) <= 1;
    int height = max(left.second, right.second) + 1;

    return make_pair(isBalanced, height);
}

bool isBalanced(TreeNode* root) {
    pair<bool, int> result = isBalancedTree(root);
    return result.first;
}

int main() {
    // 创建一个平衡二叉树示例
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    if (isBalanced(root)) {
        cout << "This is a balanced binary tree." << endl;
    } else {
        cout << "This is not a balanced binary tree." << endl;
    }

    return 0;
}
```

#### 15.2.2、非递归

思路：

1. 使用队列进行层序遍历，从根节点开始。
2. 对于每一层的节点，判断左右子树的高度差是否超过1，如果超过1，则该树不是平衡二叉树，返回 `false`。
3. 如果左右子树的高度差不超过1，则继续将左右子树的子节点加入队列中。
4. 重复上述过程，直到遍历完所有层的节点。
5. 如果在整个遍历过程中没有发现高度差超过1的情况，那么该树是平衡二叉树，返回 `true`。

参考代码：

```C++
#include <iostream>
#include <queue>
#include <cmath>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool isBalanced(TreeNode* root) {
    if (!root) {
        return true; // 空树是平衡二叉树
    }

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        TreeNode* current = q.front();
        q.pop();

        // 获取左子树的高度
        int leftHeight = 0;
        TreeNode* leftNode = current->left;
        while (leftNode) {
            leftHeight++;
            leftNode = leftNode->left;
        }

        // 获取右子树的高度
        int rightHeight = 0;
        TreeNode* rightNode = current->right;
        while (rightNode) {
            rightHeight++;
            rightNode = rightNode->left;
        }

        // 如果左右子树的高度差超过1，返回false
        if (abs(leftHeight - rightHeight) > 1) {
            return false;
        }

        if (current->left) {
            q.push(current->left);
        }
        if (current->right) {
            q.push(current->right);
        }
    }

    return true;
}

int main() {
    // 创建一个平衡二叉树示例
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    if (isBalanced(root)) {
        cout << "This is a balanced binary tree." << endl;
    } else {
        cout << "This is not a balanced binary tree." << endl;
    }

    return 0;
}
```

## 16、**二叉搜索树的最近公共祖先**

### 16.1、问题描述

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

1.对于该题的最近的公共祖先定义:对于有根树T的两个节点p、q，最近公共祖先LCA(T,p,q)表示一个节点x，满足x是p和q的祖先且x的深度尽可能大。在这里，一个节点也可以是它自己的祖先.

2.二叉搜索树是若它的左子树不空，则左子树上所有节点的值均小于它的根节点的值； 若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值

3.所有节点的值都是唯一的。

4.p、q 为不同节点且均存在于给定的二叉搜索树中。

### 16.2、思路及代码

#### 16.2.1、递归

思路：

1. 从根节点开始遍历二叉搜索树。
2. 如果根节点的值大于两个指定节点的值（p 和 q），说明最近公共祖先应该在根节点的左子树中，所以递归调用函数来查找左子树。
3. 如果根节点的值小于两个指定节点的值，说明最近公共祖先应该在根节点的右子树中，所以递归调用函数来查找右子树。
4. 如果根节点的值介于 p 和 q 之间（包括 p 和 q），说明根节点本身就是最近公共祖先，直接返回根节点。
5. 最终，函数会返回最近公共祖先的指针。

参考代码：

```C++
#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root) {
        return nullptr; // 根节点为空，返回 nullptr
    }

    // 如果根节点的值介于 p 和 q 之间（包括 p 和 q），根节点就是最近公共祖先
    if ((root->val >= p->val && root->val <= q->val) || (root->val <= p->val && root->val >= q->val)) {
        return root;
    }
    
    // 如果根节点的值大于 p 和 q 的值，递归查找左子树
    if (root->val > p->val && root->val > q->val) {
        return lowestCommonAncestor(root->left, p, q);
    }

    // 如果根节点的值小于 p 和 q 的值，递归查找右子树
    if (root->val < p->val && root->val < q->val) {
        return lowestCommonAncestor(root->right, p, q);
    }

    return nullptr; // 其他情况返回 nullptr
}

int main() {
    // 创建一个二叉搜索树示例
    TreeNode* root = new TreeNode(20);
    root->left = new TreeNode(10);
    root->right = new TreeNode(30);
    root->left->left = new TreeNode(5);
    root->left->right = new TreeNode(15);
    root->right->left = new TreeNode(25);
    root->right->right = new TreeNode(35);

    TreeNode* p = root->left; // 10
    TreeNode* q = root->right; // 30

    TreeNode* result = lowestCommonAncestor(root, p, q);
    cout << "Lowest Common Ancestor: " << result->val << endl;

    return 0;
}
```

#### 16.2.2、非递归

思路：

1. 从根节点开始遍历二叉树。
2. 通过迭代，找到分别指向节点 p 和节点 q 的指针，并将它们分别存储在 p_node 和 q_node 中。
3. 在遍历的过程中，根据二叉搜索树的性质，若当前节点的值大于 p 和 q 的值，说明 p 和 q 都位于当前节点的左子树，所以继续遍历左子树；若当前节点的值小于 p 和 q 的值，说明 p 和 q 都位于当前节点的右子树，继续遍历右子树。
4. 直到找到一个节点 node，它的值在 p 和 q 的值之间（包括 p 和 q），此时 node 即为最近公共祖先。

参考代码：

```C++
#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    TreeNode* p_node = nullptr;
    TreeNode* q_node = nullptr;
    
    while (root != nullptr) {
        if (root->val > p->val && root->val > q->val) {
            root = root->left;
        } else if (root->val < p->val && root->val < q->val) {
            root = root->right;
        } else {
            // Found a node that falls between p and q values
            // It's the lowest common ancestor
            return root;
        }
    }
    
    return nullptr; // Return nullptr if no common ancestor found
}

int main() {
    // Create a binary search tree example
    TreeNode* root = new TreeNode(20);
    root->left = new TreeNode(10);
    root->right = new TreeNode(30);
    root->left->left = new TreeNode(5);
    root->left->right = new TreeNode(15);
    root->right->left = new TreeNode(25);
    root->right->right = new TreeNode(35);

    TreeNode* p = root->left; // 10
    TreeNode* q = root->right; // 30

    TreeNode* result = lowestCommonAncestor(root, p, q);
    cout << "Lowest Common Ancestor: " << result->val << endl;

    return 0;
}
```

## 17、**在二叉树中找到两个节点的最近公共祖先**

### 17.1、问题描述

给定一棵二叉树(保证非空)以及这棵树上的两个节点对应的val值 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。

> 如当输入{3,5,1,6,2,0,8,#,#,7,4},5,1时，二叉树{3,5,1,6,2,0,8,#,#,7,4}如下图所示：
>
> ![image-20240121202343198](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212023438.png)
>
> 所以节点值为5和节点值为1的节点的最近公共祖先节点的节点值为3，所以对应的输出为3。
>
> 节点本身可以视为自己的祖先
>
> **示例1**
>
> 输入：{3,5,1,6,2,0,8,#,#,7,4},5,1
>
> 返回值：3
>
> **示例2**
>
> 输入：{3,5,1,6,2,0,8,#,#,7,4},2,7
>
> 返回值：2

### 17.2、思路及代码

#### 17.2.1、递归

思路：

1. 从根节点开始遍历整个二叉树。
2. 对于当前节点 node，如果该节点是 o1 或 o2 中的一个，或者是 o1 和 o2 的最近公共祖先，那么就返回该节点。
3. 递归遍历左子树和右子树，得到左子树的返回值 left 和右子树的返回值 right。
4. 如果 left 和 right 都不为空，说明 o1 和 o2 分别在左子树和右子树中，那么当前节点 node 就是它们的最近公共祖先，返回 node。
5. 如果 left 不为空而 right 为空，说明 o1 和 o2 都在左子树中，返回 left。
6. 如果 right 不为空而 left 为空，说明 o1 和 o2 都在右子树中，返回 right。
7. 如果 left 和 right 都为空，说明 o1 和 o2 都不在当前节点的子树中，返回 nullptr。

参考代码：

```C++
#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* o1, TreeNode* o2) {
    if (root == nullptr || root == o1 || root == o2) {
        return root;
    }

    TreeNode* left = lowestCommonAncestor(root->left, o1, o2);
    TreeNode* right = lowestCommonAncestor(root->right, o1, o2);

    if (left != nullptr && right != nullptr) {
        return root;
    } else if (left != nullptr) {
        return left;
    } else {
        return right;
    }
}

int main() {
    // Create a binary tree example
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(5);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(6);
    root->left->right = new TreeNode(2);
    root->right->left = new TreeNode(0);
    root->right->right = new TreeNode(8);
    root->left->right->left = new TreeNode(7);
    root->left->right->right = new TreeNode(4);

    TreeNode* o1 = root->left; // Node with value 5
    TreeNode* o2 = root->right; // Node with value 1

    TreeNode* result = lowestCommonAncestor(root, o1, o2);
    cout << "Lowest Common Ancestor: " << result->val << endl;

    return 0;
}
```

#### 17.2.2、非递归

思路：

1. 首先，使用两个栈来模拟查找 o1 和 o2 的路径。可以使用两个分别用于存储路径的栈 `path1` 和 `path2`。
2. 使用两个指针 `node1` 和 `node2` 分别初始化为根节点，开始遍历树。
3. 在遍历的过程中，使用前序遍历方式，每次将当前节点 `node1` 或 `node2` 放入相应的路径栈中，并继续遍历其左子树。
4. 当遇到 o1 或 o2 时，相应的路径栈中就存储了从根节点到 o1 或 o2 的路径。
5. 遍历完成后，就得到了两条从根节点到 o1 和 o2 的路径。
6. 接下来，比较两个路径栈，找到它们的最后一个相同节点，这个节点就是 o1 和 o2 的最近公共祖先。
7. 返回最近公共祖先节点即可。

参考代码：

```C++
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* o1, TreeNode* o2) {
    stack<TreeNode*> s1, s2;
    vector<TreeNode*> path1, path2;

    TreeNode* node1 = root;
    TreeNode* node2 = root;

    while (node1 || !s1.empty() || node2 || !s2.empty()) {
        while (node1) {
            path1.push_back(node1);
            s1.push(node1);
            if (node1 == o1) break;
            node1 = node1->left;
        }

        while (node2) {
            path2.push_back(node2);
            s2.push(node2);
            if (node2 == o2) break;
            node2 = node2->left;
        }

        if (!path1.empty()) node1 = path1.back();
        if (!path2.empty()) node2 = path2.back();

        if (node1 == o1 || node2 == o2) break;

        if (!s1.empty() && !s2.empty() && s1.top() != s2.top()) {
            if (path1.size() > path2.size()) {
                path1.pop_back();
                s1.pop();
                node1 = nullptr;
            } else {
                path2.pop_back();
                s2.pop();
                node2 = nullptr;
            }
        }
    }

    int n = min(path1.size(), path2.size());
    for (int i = 0; i < n; i++) {
        if (path1[i] != path2[i]) {
            return path1[i - 1];
        }
    }

    return path1[n - 1];
}

int main() {
    // Create a binary tree example
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(5);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(6);
    root->left->right = new TreeNode(2);
    root->right->left = new TreeNode(0);
    root->right->right = new TreeNode(8);
    root->left->right->left = new TreeNode(7);
    root->left->right->right = new TreeNode(4);

    TreeNode* o1 = root->left; // Node with value 5
    TreeNode* o2 = root->right; // Node with value 1

    TreeNode* result = lowestCommonAncestor(root, o1, o2);
    cout << "Lowest Common Ancestor: " << result->val << endl;

    return 0;
}
```

## 18、**序列化二叉树**

### 18.1、问题描述

请实现两个函数，分别用来序列化和反序列化二叉树，不对序列化之后的字符串进行约束，但要求能够根据序列化之后的字符串重新构造出一棵与原二叉树相同的树。

二叉树的序列化(Serialize)是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树等遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#） 二叉树的反序列化(Deserialize)是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

> 例如，可以根据层序遍历的方案序列化，如下图:
>
> ![image-20240121202411354](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212024347.png)
>
> 层序序列化(即用函数Serialize转化)如上的二叉树转为"{1,2,3,#,#,6,7}"，再能够调用反序列化(Deserialize)将"{1,2,3,#,#,6,7}"构造成如上的二叉树。
>
> 当然你也可以根据满二叉树结点位置的标号规律来序列化，还可以根据先序遍历和中序遍历的结果来序列化。不对序列化之后的字符串进行约束，所以欢迎各种奇思妙想。
>
> **示例1**
>
> 输入：{1,2,3,#,#,6,7}
>
> 返回值：{1,2,3,#,#,6,7}
>
> 说明：如题面图   
>
> **示例2**
>
> 输入：{8,6,10,5,7,9,11}
>
> 返回值：{8,6,10,5,7,9,11}

### 18.2、思路及代码

#### 18.2.1、递归

思路：

序列化：

1. 对于每个节点，将节点的值转化为字符串形式。
2. 使用特定字符（比如逗号 `,`）来分隔节点的值。
3. 对于空节点，用一个特殊标记（比如 "null"）表示。
4. 采用递归的方式，从根节点开始，将每个节点的值序列化为字符串，并递归地序列化其左子树和右子树。

反序列化：

1. 根据序列化字符串，按照分隔符（比如逗号 `,`）来拆分节点的值。
2. 从序列化字符串中逐一取出节点的值。
3. 如果节点值是 "null"，表示空节点。
4. 如果节点值不是 "null"，则创建一个新的节点，将节点值转化为整数，并构建当前节点的左子树和右子树。
5. 采用递归的方式，反序列化子树。

参考代码：

```C++
#include <iostream>
#include <string>
#include <sstream>
#include <queue>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) {
            return "null";
        }
        return to_string(root->val) + "," + serialize(root->left) + "," + serialize(root->right);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        return deserializeHelper(ss);
    }

    TreeNode* deserializeHelper(stringstream& ss) {
        string val;
        getline(ss, val, ',');
        if (val == "null") {
            return nullptr;
        }
        TreeNode* root = new TreeNode(stoi(val));
        root->left = deserializeHelper(ss);
        root->right = deserializeHelper(ss);
        return root;
    }
};

int main() {
    // Create a binary tree example
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(5);

    // Serialize the tree
    Codec codec;
    string serializedTree = codec.serialize(root);
    cout << "Serialized Tree: " << serializedTree << endl;

    // Deserialize the tree
    TreeNode* deserializedRoot = codec.deserialize(serializedTree);

    // Verify if deserialized tree is the same as the original tree
    string reserializedTree = codec.serialize(deserializedRoot);
    cout << "Reserialized Tree: " << reserializedTree << endl;

    return 0;
}
```

#### 18.2.2、非递归

思路：

序列化：

1. 创建一个队列（Queue）用于层序遍历二叉树。
2. 将根节点加入队列。
3. 使用循环，遍历队列中的节点，每次取出队头节点，将节点的值加入序列化结果字符串，并用特定分隔符（例如逗号 `,`）分隔。
4. 然后将节点的左孩子和右孩子（如果存在）依次加入队列。
5. 重复步骤 3 和 4 直到队列为空。
6. 最终得到序列化结果字符串。

反序列化：

1. 先将序列化字符串按照特定分隔符（例如逗号 `,`）拆分成节点值的数组。
2. 创建一个队列用于重建二叉树。
3. 将第一个节点值从数组中取出，创建根节点，加入队列。
4. 使用循环，依次取出队头节点和数组中的下一个节点值。
5. 如果节点值不是特殊标记（例如 "null"），则创建一个新节点，将值设置为当前节点值，并将其加入队列。然后从数组中取出下一个节点值，并创建右孩子节点加入队列。
6. 重复步骤 4 和 5 直到数组中的值全部被处理。
7. 最终得到反序列化后的二叉树。

参考代码：

```C++
#include <iostream>
#include <queue>
#include <sstream>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

std::string serialize(TreeNode* root) {
    std::ostringstream ss;
    std::queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();
        if (node) {
            ss << node->val << ",";
            q.push(node->left);
            q.push(node->right);
        } else {
            ss << "null,";
        }
    }

    return ss.str();
}

TreeNode* deserialize(std::string data) {
    std::istringstream ss(data);
    std::vector<std::string> values;
    std::string token;

    while (std::getline(ss, token, ',')) {
        values.push_back(token);
    }

    if (values.empty() || values[0] == "null") {
        return nullptr;
    }

    TreeNode* root = new TreeNode(std::stoi(values[0]));
    std::queue<TreeNode*> q;
    q.push(root);
    int i = 1;

    while (!q.empty() && i < values.size()) {
        TreeNode* node = q.front();
        q.pop();

        if (values[i] != "null") {
            node->left = new TreeNode(std::stoi(values[i]));
            q.push(node->left);
        }
        i++;

        if (i < values.size() && values[i] != "null") {
            node->right = new TreeNode(std::stoi(values[i]));
            q.push(node->right);
        }
        i++;
    }

    return root;
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(5);

    std::string serialized = serialize(root);
    std::cout << "Serialized tree: " << serialized << std::endl;

    TreeNode* deserialized = deserialize(serialized);

    // Check if deserialized tree matches the original tree.
    if (serialized == serialize(deserialized)) {
        std::cout << "Serialization and deserialization successful!" << std::endl;
    } else {
        std::cout << "Serialization and deserialization failed!" << std::endl;
    }

    return 0;
}
```

## 19、重建二叉树

### 19.1、问题描述

给定节点数为 n 的二叉树的前序遍历和中序遍历结果，请重建出该二叉树并返回它的头结点。

> 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建出如下图所示。
>
> ![image-20240121202436216](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212024341.png)
>
> 提示:
>
> 1.vin.length == pre.length
>
> 2.pre 和 vin 均无重复元素
>
> 3.vin出现的元素均出现在 pre里
>
> 4.只需要返回根结点，系统会自动输出整颗树做答案对比
>
> **示例1**
>
> 输入：[1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]
>
> 返回值：{1,2,3,4,#,5,6,#,7,#,#,8}
>
> 说明：返回根节点，系统会输出整颗二叉树对比结果，重建结果如题面图示    
>
> **示例2**
>
> 输入：[1],[1]
>
> 返回值：{1}
>
> **示例3**
>
> 输入：[1,2,3,4,5,6,7],[3,2,4,1,6,5,7]
>
> 返回值：{1,2,5,3,4,6,7}

### 19.2、思路及代码

#### 19.2.1、递归

思路：

1. 前序遍历的第一个节点是树的根节点。
2. 在中序遍历中找到根节点的位置，根节点左侧的部分是左子树，右侧的部分是右子树。
3. 使用前序遍历中根节点之后的节点，以及左子树和右子树的大小，在中序遍历中划分左子树和右子树。
4. 递归地构建左子树和右子树。
5. 返回根节点。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <unordered_map>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* buildTree(std::vector<int>& preorder, std::vector<int>& inorder) {
    std::unordered_map<int, int> inorder_map;
    for (int i = 0; i < inorder.size(); ++i) {
        inorder_map[inorder[i]] = i;
    }

    return buildTreeHelper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1, inorder_map);
}

TreeNode* buildTreeHelper(std::vector<int>& preorder, int preStart, int preEnd, 
                         std::vector<int>& inorder, int inStart, int inEnd,
                         std::unordered_map<int, int>& inorder_map) {
    if (preStart > preEnd || inStart > inEnd) {
        return nullptr;
    }

    int rootValue = preorder[preStart];
    TreeNode* root = new TreeNode(rootValue);
    int rootIndex = inorder_map[rootValue];
    int leftTreeSize = rootIndex - inStart;

    root->left = buildTreeHelper(preorder, preStart + 1, preStart + leftTreeSize, 
                                inorder, inStart, rootIndex - 1, inorder_map);
    root->right = buildTreeHelper(preorder, preStart + leftTreeSize + 1, preEnd, 
                                inorder, rootIndex + 1, inEnd, inorder_map);

    return root;
}

// 后序遍历打印二叉树
void postorderTraversal(TreeNode* root) {
    if (root == nullptr) {
        return;
    }
    postorderTraversal(root->left);
    postorderTraversal(root->right);
    std::cout << root->val << " ";
}

int main() {
    std::vector<int> preorder = {3, 9, 20, 15, 7};
    std::vector<int> inorder = {9, 3, 15, 20, 7};

    TreeNode* root = buildTree(preorder, inorder);

    std::cout << "Postorder Traversal Result: ";
    postorderTraversal(root);
    std::cout << std::endl;

    return 0;
}
```

#### 19.2.2、非递归

思路：

1. 我们知道，前序遍历的顺序是「根左右」，而中序遍历的顺序是「左根右」。
2. 我们可以根据前序遍历找到根节点，根据中序遍历分割左子树和右子树。
3. 使用一个栈来模拟递归的过程，这个栈用于暂时存储根节点，以及当前正在处理的节点的父节点。
4. 遍历前序遍历数组，依次取出前序遍历的元素，创建一个节点，并连接到其父节点的相应位置（左子树或右子树），同时将这个节点入栈。
5. 在入栈之前，需要检查当前前序遍历的元素是否等于中序遍历的元素，如果不等，说明还需要继续处理左子树，直到找到匹配的中序遍历元素。
6. 当找到匹配的中序遍历元素时，弹出栈中的节点，继续处理右子树，重复上述步骤，直到遍历完前序遍历数组。
7. 最后，栈中的根节点即为整个二叉树的根节点。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    if (preorder.empty() || inorder.empty() || preorder.size() != inorder.size()) {
        return nullptr;
    }

    int n = preorder.size();
    stack<TreeNode*> stk;
    TreeNode* root = new TreeNode(preorder[0]);
    TreeNode* current = root;
    int inorderIdx = 0;

    for (int i = 1; i < n; ++i) {
        if (current->val != inorder[inorderIdx]) {
            current->left = new TreeNode(preorder[i]);
            stk.push(current);
            current = current->left;
        } else {
            while (!stk.empty() && stk.top()->val == inorder[inorderIdx]) {
                current = stk.top();
                stk.pop();
                ++inorderIdx;
            }
            current->right = new TreeNode(preorder[i]);
            current = current->right;
        }
    }

    return root;
}

// 后序遍历验证
void postorderTraversal(TreeNode* root) {
    if (root) {
        postorderTraversal(root->left);
        postorderTraversal(root->right);
        cout << root->val << " ";
    }
}

int main() {
    vector<int> preorder = {3, 9, 20, 15, 7};
    vector<int> inorder = {9, 3, 15, 20, 7};

    TreeNode* root = buildTree(preorder, inorder);
    
    cout << "Postorder Traversal: ";
    postorderTraversal(root);

    return 0;
}
```

## 20、**输出二叉树的右视图**

### 20.1、问题描述

请根据二叉树的前序遍历，中序遍历恢复二叉树，并打印出二叉树的右视图。

> 如输入[1,2,4,5,3],[4,2,5,1,3]时，通过前序遍历的结果[1,2,4,5,3]和中序遍历的结果[4,2,5,1,3]可重建出以下二叉树：
>
> ![image-20240121202458873](https://raw.githubusercontent.com/aqjsp/Pictures/main/202401212025152.png)
>
> 
>
> 所以对应的输出为[1,3,5]。
>
> **示例1**
>
> 输入：[1,2,4,5,3],[4,2,5,1,3]
>
> 返回值：[1,3,5]
>
> **备注：**
>
> 二叉树每个节点的值在区间[1,10000]内，且保证每个节点的值互不相同。

### 20.2、思路及代码

#### 20.2.1、递归

思路：

1. 从前序遍历和中序遍历中恢复二叉树。
2. 打印二叉树的右视图。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 用于恢复二叉树的递归函数
TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder, int preStart, int preEnd, int inStart, int inEnd, unordered_map<int, int>& indexMap) {
    if (preStart > preEnd || inStart > inEnd) {
        return nullptr;
    }
    
    int rootVal = preorder[preStart];
    TreeNode* root = new TreeNode(rootVal);
    
    int inRootIndex = indexMap[rootVal];
    int leftTreeSize = inRootIndex - inStart;
    
    root->left = buildTree(preorder, inorder, preStart + 1, preStart + leftTreeSize, inStart, inRootIndex - 1, indexMap);
    root->right = buildTree(preorder, inorder, preStart + leftTreeSize + 1, preEnd, inRootIndex + 1, inEnd, indexMap);
    
    return root;
}

TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    unordered_map<int, int> indexMap;
    int n = inorder.size();
    
    for (int i = 0; i < n; ++i) {
        indexMap[inorder[i]] = i;
    }
    
    return buildTree(preorder, inorder, 0, n - 1, 0, n - 1, indexMap);
}

// 用于打印二叉树的右视图的递归函数
void rightSideView(TreeNode* root, int level, vector<int>& result) {
    if (!root) {
        return;
    }
    
    if (result.size() == level) {
        result.push_back(root->val);
    }
    
    rightSideView(root->right, level + 1, result);
    rightSideView(root->left, level + 1, result);
}

vector<int> rightSideView(TreeNode* root) {
    vector<int> result;
    rightSideView(root, 0, result);
    return result;
}

int main() {
    vector<int> preorder = {1, 2, 4, 5, 3, 6, 7};
    vector<int> inorder = {4, 2, 5, 1, 6, 3, 7};
    
    TreeNode* root = buildTree(preorder, inorder);
    
    vector<int> rightView = rightSideView(root);
    
    cout << "Right View of the Binary Tree: ";
    for (int val : rightView) {
        cout << val << " ";
    }
    
    return 0;
}
```

#### 20.2.2、非递归

思路：

构建二叉树：

构建二叉树的主要思路是通过迭代处理前序遍历的每个节点，然后根据中序遍历的信息来确定它的左右子树。我们维护一个栈（`nodeStack`），其中存储了节点的指针。我们首先创建根节点（根据前序遍历的第一个节点的值），然后将其推入栈中。

接下来，我们迭代处理前序遍历中的每个节点。对于当前节点，我们创建一个新节点，并根据中序遍历的信息来决定它是当前节点的左子节点还是右子节点。如果当前节点在中序遍历中的位置在当前节点的父节点的位置的左侧，那么它是左子节点；否则，它是右子节点。然后，我们将其连接到父节点上，并将当前节点压入栈中。

这样，通过迭代前序遍历的每个节点，我们不断构建二叉树。

打印右视图：

打印二叉树的右视图可以使用广度优先搜索（BFS）。我们从根节点开始，依次访问每一层的最右边节点。具体步骤如下：

- 创建一个队列 `nodeQueue` 用于 BFS。
- 将根节点入队。
- 对于每一层，首先获取当前层的节点数 `levelSize`，然后遍历该层的节点。
- 在遍历的过程中，如果是该层的最右边节点（`i == 0`），则将其值加入结果数组。
- 将下一层的节点入队。
- 继续下一层的遍历，直到完成整棵树的右视图的获取。

最后，返回右视图的结果数组。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 用于恢复二叉树的迭代函数
TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    if (preorder.empty() || inorder.empty()) {
        return nullptr;
    }

    unordered_map<int, int> indexMap;
    int n = inorder.size();

    for (int i = 0; i < n; ++i) {
        indexMap[inorder[i]] = i;
    }

    TreeNode* root = new TreeNode(preorder[0]);
    TreeNode* current = root;
    stack<TreeNode*> nodeStack;
    nodeStack.push(current);

    for (int i = 1; i < preorder.size(); ++i) {
        int val = preorder[i];
        TreeNode* newNode = new TreeNode(val);

        if (indexMap[val] < indexMap[current->val]) {
            current->left = newNode;
            current = newNode;
        } else {
            while (!nodeStack.empty() && indexMap[val] > indexMap[nodeStack.top()->val]) {
                current = nodeStack.top();
                nodeStack.pop();
            }

            current->right = newNode;
            current = newNode;
        }

        nodeStack.push(newNode);
    }

    return root;
}

// 用于打印二叉树的右视图的迭代函数
vector<int> rightSideView(TreeNode* root) {
    vector<int> result;
    if (!root) {
        return result;
    }

    queue<TreeNode*> nodeQueue;
    nodeQueue.push(root);

    while (!nodeQueue.empty()) {
        int levelSize = nodeQueue.size();

        for (int i = 0; i < levelSize; ++i) {
            TreeNode* node = nodeQueue.front();
            nodeQueue.pop();

            if (i == 0) {
                result.push_back(node->val);
            }

            if (node->right) {
                nodeQueue.push(node->right);
            }

            if (node->left) {
                nodeQueue.push(node->left);
            }
        }
    }

    return result;
}

int main() {
    vector<int> preorder = {1, 2, 4, 5, 3, 6, 7};
    vector<int> inorder = {4, 2, 5, 1, 6, 3, 7};

    TreeNode* root = buildTree(preorder, inorder);

    vector<int> rightView = rightSideView(root);

    cout << "Right View of the Binary Tree: ";
    for (int val : rightView) {
        cout << val << " ";
    }

    return 0;
}
```