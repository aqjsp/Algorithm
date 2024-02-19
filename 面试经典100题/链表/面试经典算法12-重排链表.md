# 面试经典算法12-重排链表

LeetCode.143

### 问题描述

给定一个单链表 `L` 的头节点 `head` ，单链表 `L` 表示为：

` L0 → L1 → … → Ln-1 → Ln `
请将其重新排列后变为：

```
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
```

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

**示例 1:**

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402192204936.png)

```
输入: head = [1,2,3,4]
输出: [1,4,2,3]
```

**示例 2:**

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402192204438.png)

```
输入: head = [1,2,3,4,5]
输出: [1,5,2,4,3]
```

**提示：**

- 链表的长度范围为 `[1, 5 * 104]`
- `1 <= node.val <= 1000`

### 思路

1. 找到链表中点：使用快慢指针找到链表的中点。快指针每次移动两步，慢指针每次移动一步，当快指针到达链表末尾时，慢指针指向链表中点。
2. 反转后半部分链表：从中点处将链表分为两部分，将后半部分链表进行反转。
3. 合并链表：将前半部分链表和反转后的后半部分链表依次交替合并，即可得到重新排列后的链表。
4. 处理边界情况：需要注意链表为空或只有一个节点的情况，直接返回即可。

### 图解

这里根据示例二来给大家讲解。

1. 找链表的中间节点，这里使用快慢指针。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402192250407.png)

2. 慢指针一次走一步，快指针一次走两步，最后快指针遍历完链表后，慢指针所指的节点就是中间节点，得到中间节点便可以得到后半段的头节点。当链表节点数为奇数时，前半段要比后半段多一个节点。拆分后，如下：

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402192251160.png)

3. 将链表后半部分进行反转。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402192254834.png)

4. 合并两个链表

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402192306848.png)

即

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402192307977.png)

### 参考代码

#### C++

```
#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next) return; // 如果链表为空或只有一个节点，无需重排

        // 找到链表的中间节点
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // 反转后半部分链表
        ListNode* pre = nullptr;
        ListNode* cur = slow->next;
        slow->next = nullptr; // 断开前后两部分链表
        while (cur) {
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }

        // 合并两部分链表
        ListNode* p1 = head;
        ListNode* p2 = pre;
        while (p2) {
            ListNode* tmp1 = p1->next;
            ListNode* tmp2 = p2->next;
            p1->next = p2;
            p2->next = tmp1;
            p1 = tmp1;
            p2 = tmp2;
        }
    }
};

// 创建链表
ListNode* createList(std::vector<int>& nums) {
    if (nums.empty()) return nullptr;
    ListNode* head = new ListNode(nums[0]);
    ListNode* cur = head;
    for (int i = 1; i < nums.size(); ++i) {
        cur->next = new ListNode(nums[i]);
        cur = cur->next;
    }
    return head;
}

// 输出链表
void printList(ListNode* head) {
    ListNode* cur = head;
    while (cur) {
        std::cout << cur->val << " ";
        cur = cur->next;
    }
    std::cout << std::endl;
}

int main() 
{
    std::vector<int> nums = {1, 2, 3, 4, 5};
    ListNode* head = createList(nums);

    // 重排链表
    Solution solution;
    solution.reorderList(head);

    // 输出重排后的链表
    printList(head);

    return 0;
}
```

#### Java

```
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;

        // 找到链表的中间节点
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // 反转后半部分链表
        ListNode pre = null;
        ListNode cur = slow.next;
        slow.next = null; // 断开前后两部分链表
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }

        // 合并两部分链表
        ListNode p1 = head;
        ListNode p2 = pre;
        while (p2 != null) {
            ListNode tmp1 = p1.next;
            ListNode tmp2 = p2.next;
            p1.next = p2;
            p2.next = tmp1;
            p1 = tmp1;
            p2 = tmp2;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5};
        ListNode head = createList(nums);

        // 重排链表
        Solution solution = new Solution();
        solution.reorderList(head);

        // 输出重排后的链表
        printList(head);
    }

    // 创建链表
    public static ListNode createList(int[] nums) {
        if (nums.length == 0) return null;
        ListNode head = new ListNode(nums[0]);
        ListNode cur = head;
        for (int i = 1; i < nums.length; ++i) {
            cur.next = new ListNode(nums[i]);
            cur = cur.next;
        }
        return head;
    }

    // 输出链表
    public static void printList(ListNode head) {
        ListNode cur = head;
        while (cur != null) {
            System.out.print(cur.val + " ");
            cur = cur.next;
        }
        System.out.println();
    }
}
```

#### Python

```
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return

        # 找到链表的中间节点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半部分链表
        pre, cur = None, slow.next
        slow.next = None  # 断开前后两部分链表
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        # 合并两部分链表
        p1, p2 = head, pre
        while p2:
            tmp1, tmp2 = p1.next, p2.next
            p1.next = p2
            p2.next = tmp1
            p1, p2 = tmp1, tmp2

def createList(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head

def printList(head):
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()

# 示例
nums = [1, 2, 3, 4, 5]
head = createList(nums)

solution = Solution()
solution.reorderList(head)

printList(head)
```

