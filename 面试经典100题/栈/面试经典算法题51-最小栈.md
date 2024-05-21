# 面试经典算法题51-最小栈

LeetCode.155

### 问题描述

设计一个支持 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类:

- `MinStack()` 初始化堆栈对象。
- `void push(int val)` 将元素val推入堆栈。
- `void pop()` 删除堆栈顶部的元素。
- `int top()` 获取堆栈顶部的元素。
- `int getMin()` 获取堆栈中的最小元素。

**示例 1:**

```
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```

### 思路

1. 在`MinStack`类中，我们使用两个栈来实现：一个用于正常操作的栈`s`，另一个用于存储当前最小元素的栈`minStack`。
2. 在`MinStack`的构造函数中，我们初始化`minStack`，将INT_MAX（整型最大值）压入栈顶，作为初始最小值。
3. 在`push`操作中，我们首先将元素压入普通栈`s`，然后检查是否需要更新最小元素栈`minStack`。如果新压入的元素`val`小于等于当前最小元素栈顶的值，就将`val`也压入`minStack`，保证`minStack`的栈顶始终是当前最小值。
4. 在`pop`操作中，我们先检查要删除的元素是否为当前最小元素。如果是，就将`minStack`的栈顶元素也弹出，确保`minStack`的栈顶始终是当前最小值。然后再从普通栈`s`中弹出元素。
5. `top`操作直接返回普通栈`s`的栈顶元素。
6. `getMin`操作直接返回最小元素栈`minStack`的栈顶元素，即当前最小值。

### 参考代码

#### C++

```
#include <stack>
#include <climits> // for INT_MAX

class MinStack {
private:
    std::stack<int> s; // 存储元素的栈
    std::stack<int> minStack; // 存储最小元素的栈

public:
    MinStack() {
        // 初始化最小元素栈，将INT_MAX压入栈顶
        minStack.push(INT_MAX);
    }
    
    void push(int val) {
        // 将元素压入普通栈
        s.push(val);
        // 更新最小元素栈，如果val比当前最小元素小或者等于，将val压入最小元素栈
        if (val <= minStack.top()) {
            minStack.push(val);
        }
    }
    
    void pop() {
        // 如果栈顶元素等于最小元素栈的栈顶元素，说明要删除的是最小元素，同时将最小元素栈的栈顶元素出栈
        if (s.top() == minStack.top()) {
            minStack.pop();
        }
        // 删除普通栈的栈顶元素
        s.pop();
    }
    
    int top() {
        // 返回普通栈的栈顶元素
        return s.top();
    }
    
    int getMin() {
        // 返回最小元素栈的栈顶元素，即当前最小元素
        return minStack.top();
    }
};

int main() {
    MinStack stack;
    stack.push(-2);
    stack.push(0);
    stack.push(-3);
    // 输出：-3
    std::cout << stack.getMin() << std::endl;
    stack.pop();
    // 输出：0
    std::cout << stack.top() << std::endl;
    // 输出：-2
    std::cout << stack.getMin() << std::endl;
    
    return 0;
}
```

#### Java

```
import java.util.Stack;

class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
        // 初始化最小元素栈，将Integer.MAX_VALUE压入栈顶
        minStack.push(Integer.MAX_VALUE);
    }
    
    public void push(int val) {
        // 将元素压入普通栈
        stack.push(val);
        // 更新最小元素栈，如果val比当前最小元素小或者等于，将val压入最小元素栈
        if (val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        // 如果栈顶元素等于最小元素栈的栈顶元素，说明要删除的是最小元素，同时将最小元素栈的栈顶元素出栈
        if (stack.peek().equals(minStack.peek())) {
            minStack.pop();
        }
        // 删除普通栈的栈顶元素
        stack.pop();
    }
    
    public int top() {
        // 返回普通栈的栈顶元素
        return stack.peek();
    }
    
    public int getMin() {
        // 返回最小元素栈的栈顶元素，即当前最小元素
        return minStack.peek();
    }

    public static void main(String[] args) {
        MinStack stack = new MinStack();
        stack.push(-2);
        stack.push(0);
        stack.push(-3);
        // 输出：-3
        System.out.println(stack.getMin());
        stack.pop();
        // 输出：0
        System.out.println(stack.top());
        // 输出：-2
        System.out.println(stack.getMin());
    }
}
```

#### Python

```
class MinStack:
    def __init__(self):
        # 用于正常操作的栈
        self.stack = []
        # 用于存储当前最小元素的栈
        self.minStack = [float('inf')]  # 初始最小值为正无穷大
    
    def push(self, val: int) -> None:
        # 将元素压入普通栈
        self.stack.append(val)
        # 更新最小元素栈，如果val比当前最小元素小或者等于，将val压入最小元素栈
        if val <= self.minStack[-1]:
            self.minStack.append(val)
    
    def pop(self) -> None:
        # 如果栈顶元素等于最小元素栈的栈顶元素，说明要删除的是最小元素，同时将最小元素栈的栈顶元素出栈
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        # 删除普通栈的栈顶元素
        self.stack.pop()
    
    def top(self) -> int:
        # 返回普通栈的栈顶元素
        return self.stack[-1]
    
    def getMin(self) -> int:
        # 返回最小元素栈的栈顶元素，即当前最小元素
        return self.minStack[-1]

# 示例用法
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
# 输出：-3
print(stack.getMin())
stack.pop()
# 输出：0
print(stack.top())
# 输出：-2
print(stack.getMin())
```

