# 面试经典算法10-K个一组反转链表

LeetCode.25

### 问题描述

给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

**示例 1：**

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402062246418.jpg)

```
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```

**示例 2：**

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402062246518.jpg)

```
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
```

**提示：**

- 链表中的节点数目为 `n`
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

### 思路

1. 创建一个虚拟头节点 `dummy`，将其 `next` 指向原链表的头节点 `head`，方便处理头部的特殊情况。
2. 使用 `pre` 指针来记录每个需要翻转的子链表的前一个节点。初始时，`pre` 指向虚拟头节点。
3. 在循环中，先找到需要翻转的子链表的起始节点 `start` 和结束节点 `end`。如果剩余节点不足 k 个，则结束循环。
4. 将当前子链表与下一个子链表断开，即将 `end->next` 置为 `nullptr`。
5. 调用 `reverse` 函数翻转当前子链表，并将翻转后的子链表连接到前一个子链表的末尾，即将 `pre->next` 指向翻转后的子链表的头节点。
6. 将翻转后的子链表的末尾与下一个子链表的开头连接，即将 `start->next` 指向下一个需要翻转的子链表的第一个节点。
7. 更新 `pre` 指向下一个需要翻转的子链表的前一个节点。
8. 循环直到所有子链表都被翻转。

### 图解

这里根据示例一进行流程演示。

1. 创建一个虚拟头节点 `dummy`，将其 `next` 指向原链表的头节点 `head`

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402062344880.png)

2.  `pre` 指针来记录每个需要翻转的子链表的前一个节点。初始时，`pre` 指向虚拟头节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402062345652.png)

3. 接下来，我们进行区间反转，找到需要翻转的子链表的起始节点 `start` 和结束节点 `end`。如果剩余节点不足 k 个（示例一中k=2），则跳出循环。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402062351099.png)

4. 再定义一个next_group 指针，指向下一个需要翻转的子链表的第一个节点，然后将当前子链表与下一个子链表断开，即将 `end->next` 置为 `nullptr`。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402070005899.png)

5. 调用 `reverse` 函数翻转当前子链表，并将翻转后的子链表连接到前一个子链表的末尾，即将 `pre->next` 指向翻转后的子链表的头节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402070006691.png)

6. 将翻转后的子链表的末尾与下一个子链表的开头连接，即将 `start->next` 指向下一个需要翻转的子链表的第一个节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402070001129.png)

7. 更新 `pre` 指向下一个需要翻转的子链表的前一个节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402070009564.png)

整理一下长这样：

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402070011499.png)

依次类推（也就是循环），返回dummy->next即为翻转后的链表的头节点。

![](https://raw.githubusercontent.com/aqjsp/Pictures/main/202402070013296.png)



### 参考代码

#### C++

```
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *dummy = new ListNode(0); // 创建一个虚拟头节点，方便处理头部的特殊情况
        dummy->next = head;
        ListNode *pre = dummy; // pre 指向每个需要翻转的子链表的前一个节点

        while (true) {
            ListNode *start = pre->next; // start 指向当前需要翻转的子链表的第一个节点
            ListNode *end = pre; // end 指向当前需要翻转的子链表的最后一个节点
            for (int i = 0; i < k && end != nullptr; ++i) {
                end = end->next; // 找到当前需要翻转的子链表的最后一个节点
            }
            if (end == nullptr) {
                break; // 如果剩余节点不足 k 个，结束循环
            }

            ListNode *next_group = end->next; // next_group 指向下一个需要翻转的子链表的第一个节点
            end->next = nullptr; // 将当前子链表与下一个子链表断开

            pre->next = reverse(start); // 翻转当前子链表，并将翻转后的子链表连接到前一个子链表的末尾
            start->next = next_group; // 将翻转后的子链表的末尾与下一个子链表的开头连接

            pre = start; // 更新 pre 指向下一个需要翻转的子链表的前一个节点
        }

        return dummy->next; // 返回虚拟头节点的下一个节点作为翻转后的链表的头节点
    }

    ListNode* reverse(ListNode* head) {
        ListNode *pre = nullptr;
        ListNode *curr = head;
        while (curr != nullptr) {
            ListNode *next = curr->next;
            curr->next = pre;
            pre = curr;
            curr = next;
        }
        return pre;
    }
};

void printList(ListNode *head) {
    ListNode *curr = head;
    while (curr != nullptr) {
        std::cout << curr->val << " ";
        curr = curr->next;
    }
    std::cout << std::endl;
}

int main() {
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    Solution solution;
    ListNode *newHead = solution.reverseKGroup(head, 2);

    printList(newHead); // 输出：2 1 4 3 5

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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0); // 创建一个虚拟头节点，方便处理头部的特殊情况
        dummy.next = head;
        ListNode prev = dummy; // prev 指向每个需要翻转的子链表的前一个节点

        while (true) {
            ListNode start = prev.next; // start 指向当前需要翻转的子链表的第一个节点
            ListNode end = prev; // end 指向当前需要翻转的子链表的最后一个节点
            for (int i = 0; i < k && end != null; ++i) {
                end = end.next; // 找到当前需要翻转的子链表的最后一个节点
            }
            if (end == null) {
                break; // 如果剩余节点不足 k 个，结束循环
            }

            ListNode nextGroup = end.next; // nextGroup 指向下一个需要翻转的子链表的第一个节点
            end.next = null; // 将当前子链表与下一个子链表断开

            prev.next = reverse(start); // 翻转当前子链表，并将翻转后的子链表连接到前一个子链表的末尾
            start.next = nextGroup; // 将翻转后的子链表的末尾与下一个子链表的开头连接

            prev = start; // 更新 prev 指向下一个需要翻转的子链表的前一个节点
        }

        return dummy.next; // 返回虚拟头节点的下一个节点作为翻转后的链表的头节点
    }

    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}

public class Main {
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        Solution solution = new Solution();
        ListNode newHead = solution.reverseKGroup(head, 2);

        printList(newHead); // 输出：2 1 4 3 5
    }

    private static void printList(ListNode head) {
        ListNode curr = head;
        while (curr != null) {
            System.out.print(curr.val + " ");
            curr = curr.next;
        }
        System.out.println();
    }
}
```

#### Python

```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head, k):
            prev = None
            curr = head
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev, curr
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            start = prev.next
            end = prev
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next

            next_group = end.next
            end.next = None

            reversed_start, next_start = reverse(start, k)
            prev.next = reversed_start
            start.next = next_group
            prev = start

        return dummy.next

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    new_head = solution.reverseKGroup(head, 2)

    printList(new_head)  # 输出：2 1 4 3 5
```

