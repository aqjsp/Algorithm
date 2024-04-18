# 面试经典算法题19-二叉树的后序遍历

LeetCode.145

### 问题描述

给你一棵二叉树的根节点 `root` ，返回其节点值的 **后序遍历** 。

**示例 1：**

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403032145343.jpg)

```
输入：root = [1,null,2,3]
输出：[3,2,1]
```

**示例 2：**

```
输入：root = []
输出：[]
```

**示例 3：**

```
输入：root = [1]
输出：[1] 
```

**提示：**

- 树中节点的数目在范围 `[0, 100]` 内
- `-100 <= Node.val <= 100`

### 思路

#### 递归

1. 若二叉树为空，则返回空列表。
2. 递归遍历左子树，将左子树的后序遍历结果添加到结果列表中。
3. 递归遍历右子树，将右子树的后序遍历结果添加到结果列表中。
4. 将当前节点的值添加到结果列表中。
5. 返回结果列表作为最终的遍历结果。

#### 非递归

1. 创建一个栈 `st` 用于存储遍历过程中的节点。
2. 初始化栈并将根节点入栈。
3. 当栈不为空时，执行以下操作：
   - 如果当前节点不为空，将其左子节点入栈，并将当前节点更新为左子节点。
   - 如果当前节点为空，说明左子树已经遍历完成，需要处理右子树：
     - 获取栈顶节点的右子节点 `node`。
     - 如果右子节点为空，说明可以访问栈顶节点：
       - 弹出栈顶节点，将其值加入结果数组。
       - 循环弹出栈顶节点，直到栈为空或者栈顶节点的右子节点不为 `node`。
       - 将 `node` 更新为当前节点的右子节点（即栈顶节点的右子节点）。
     - 如果右子节点不为空，将 `node` 更新为当前节点的右子节点。
4. 返回结果数组，即为后序遍历的结果。

### 图解

#### 非递归

1. 初始化栈并将根节点入栈。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403032229768.png)

2. 如果当前节点不为空，将其左子节点入栈，并将当前节点更新为左子节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403032247081.png)

3. 左子结点遍历完成后，将栈顶元素弹出。

![image-20240303224823930](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403032248899.png)

4. 节点2处理完毕，返回上一层根节点2，继续遍历右子节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403032253579.png)

5. 以节点3为根节点的子树，先遍历其左子树并入栈，最左节点是4.

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403032255174.png)

6. 左子节点遍历完成后，弹出栈顶元素，并遍历其右子节点加入栈中。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403032257865.png)

7. 右子节点遍历完成后，弹出栈顶元素，并返回上一层继续处理。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403032258318.png)

8. 依次处理，3,1节点，并弹出栈。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202403032300501.png)

此时，栈中元素已处理完成，栈空，遍历结束。

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

vector<int> postorderTraversal(TreeNode* root) {
    vector<int> result;
    if (!root) return result; // 如果树为空，直接返回空列表

    // 递归遍历左子树
    vector<int> left = postorderTraversal(root->left);
    result.insert(result.end(), left.begin(), left.end());

    // 递归遍历右子树
    vector<int> right = postorderTraversal(root->right);
    result.insert(result.end(), right.begin(), right.end());

    // 将当前节点的值添加到结果列表中
    result.push_back(root->val);

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
    vector<int> nodes = {1, 2, 3, -1, -1, 4, 5}; // 定义二叉树的先序遍历序列
    TreeNode* root = createTree(nodes, 0); // 创建二叉树
    vector<int> result = postorderTraversal(root); // 进行后序遍历
    for (int val : result) { // 输出遍历结果
        cout << val << " ";
    }
    cout << endl;

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

// 后序遍历
vector<int> postorderTraversal(TreeNode* root) {
    vector<int> result; // 存储遍历结果的数组
    stack<TreeNode*> st; // 辅助栈，用于存储遍历过程中的节点

    while (root || !st.empty()) {
        if (root) {
            st.push(root); // 当前节点入栈
            root = root->left; // 访问左子节点
        } else {
            TreeNode* node = st.top()->right; // 获取栈顶节点的右子节点
            if (!node) { // 如果右子节点为空，说明可以访问栈顶节点
                node = st.top(); // 获取栈顶节点
                st.pop(); // 弹出栈顶节点
                result.push_back(node->val); // 将节点值加入结果数组
                while (!st.empty() && node == st.top()->right) { // 当前节点为其父节点的右子节点时，说明父节点已经访问过
                    node = st.top(); // 获取父节点
                    st.pop(); // 弹出父节点
                    result.push_back(node->val); // 将父节点值加入结果数组
                }
            } else {
                root = node; // 如果右子节点不为空，继续遍历右子树
            }
        }
    }

    return result; // 返回后序遍历结果数组
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
    vector<int> nodes = {1, 2, 3, -1, -1, 4, 5}; // 定义二叉树的先序遍历序列
    TreeNode* root = createTree(nodes, 0); // 创建二叉树
    vector<int> result = postorderTraversal(root); // 进行后序遍历
    for (int val : result) { // 输出遍历结果
        cout << val << " ";
    }
    cout << endl;

    destroyTree(root); // 销毁二叉树

    return 0;
}
```

#### Java

```
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

// 二叉树节点的定义
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Main {
    // 后序遍历
    public static List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>(); // 存储遍历结果的列表
        Stack<TreeNode> stack = new Stack<>(); // 辅助栈，用于存储遍历过程中的节点

        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root); // 当前节点入栈
                root = root.left; // 访问左子节点
            } else {
                TreeNode node = stack.peek().right; // 获取栈顶节点的右子节点
                if (node == null) { // 如果右子节点为空，说明可以访问栈顶节点
                    node = stack.pop(); // 弹出栈顶节点
                    result.add(node.val); // 将节点值加入结果列表
                    while (!stack.isEmpty() && node == stack.peek().right) { // 当前节点为其父节点的右子节点时，说明父节点已经访问过
                        node = stack.pop(); // 获取父节点
                        result.add(node.val); // 将父节点值加入结果列表
                    }
                } else {
                    root = node; // 如果右子节点不为空，继续遍历右子树
                }
            }
        }

        return result; // 返回后序遍历结果列表
    }

    // 创建二叉树
    public static TreeNode createTree(List<Integer> nodes, int index) {
        if (index >= nodes.size() || nodes.get(index) == -1) {
            return null; // 如果节点为空，则返回null
        }
        TreeNode root = new TreeNode(nodes.get(index)); // 创建当前节点
        root.left = createTree(nodes, 2 * index + 1); // 创建左子树
        root.right = createTree(nodes, 2 * index + 2); // 创建右子树
        return root; // 返回当前节点
    }

    // 销毁二叉树
    public static void destroyTree(TreeNode root) {
        if (root == null) return; // 如果根节点为空，直接返回
        destroyTree(root.left); // 递归销毁左子树
        destroyTree(root.right); // 递归销毁右子树
        // Java的垃圾回收会自动处理内存释放，无需手动删除节点
    }

    public static void main(String[] args) {
        List<Integer> nodes = List.of(1, 2, 3, -1, -1, 4, 5); // 定义二叉树的先序遍历序列
        TreeNode root = createTree(nodes, 0); // 创建二叉树
        List<Integer> result = postorderTraversal(root); // 进行后序遍历
        for (int val : result) { // 输出遍历结果
            System.out.print(val + " ");
        }
        System.out.println();

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

# 后序遍历
def postorderTraversal(root):
    result = []  # 存储遍历结果的列表
    stack = []  # 辅助栈，用于存储遍历过程中的节点

    while root or stack:
        if root:
            stack.append(root)  # 当前节点入栈
            root = root.left  # 访问左子节点
        else:
            node = stack[-1].right  # 获取栈顶节点的右子节点
            if not node:
                node = stack.pop()  # 弹出栈顶节点
                result.append(node.val)  # 将节点值加入结果列表
                while stack and node == stack[-1].right:  # 当前节点为其父节点的右子节点时，说明父节点已经访问过
                    node = stack.pop()  # 获取父节点
                    result.append(node.val)  # 将父节点值加入结果列表
            else:
                root = node  # 如果右子节点不为空，继续遍历右子树

    return result  # 返回后序遍历结果列表

# 创建二叉树
def createTree(nodes, index):
    if index >= len(nodes) or nodes[index] == -1:
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
    # Python的垃圾回收会自动处理内存释放，无需手动删除节点

nodes = [1, 2, 3, -1, -1, 4, 5]  # 定义二叉树的先序遍历序列
root = createTree(nodes, 0)  # 创建二叉树
result = postorderTraversal(root)  # 进行后序遍历
print(result)  # 输出遍历结果

destroyTree(root)  # 销毁二叉树
```

