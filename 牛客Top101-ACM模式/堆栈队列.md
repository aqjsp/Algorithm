# 堆/栈/队列

## 1、**用两个栈实现队列**

### 1.1、问题描述

用两个栈来实现一个队列，使用n个元素来完成 n 次在队列尾部插入整数(push)和n次在队列头部删除整数(pop)的功能。 队列中的元素为int类型。保证操作合法，即保证pop操作时队列内已有元素。

> **示例1**
>
> 输入：["PSH1","PSH2","POP","POP"]
>
> 返回值：1,2
>
> 说明："PSH1":代表将1插入队列尾部
>
> **示例2**
>
> 输入：["PSH2","POP","PSH1","POP"]
>
> 返回值：2,1

### 1.2、思路及代码

思路：

1. 使用两个栈，称其为 `stack1` 和 `stack2`。
2. 对于入队操作（push），将元素压入 `stack1`。
3. 对于出队操作（pop），首先检查 `stack2` 是否为空。
   1. 如果 `stack2` 不为空，直接从 `stack2` 弹出元素作为出队结果。
   2. 如果 `stack2` 为空，将 `stack1` 中的元素逐个弹出并压入 `stack2`，然后从 `stack2` 弹出元素作为出队结果。
4. 当需要出队操作时，首先检查 `stack2` 是否为空。如果为空，则将 `stack1` 的元素倒入 `stack2`，然后从 `stack2` 弹出元素。

参考代码：

```C++
#include <iostream>
#include <stack>

class MyQueue {
public:
    MyQueue() {}

    // 入队操作，将元素压入 stack1
    void push(int x) {
        stack1.push(x);
    }

    // 出队操作，返回队头元素
    int pop() {
        // 如果 stack2 为空，需要从 stack1 倒入元素
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }

        // 弹出并返回队头元素
        int front = stack2.top();
        stack2.pop();
        return front;
    }

    // 检查队列是否为空
    bool empty() {
        return stack1.empty() && stack2.empty();
    }

private:
    std::stack<int> stack1; // 用于入队操作的栈
    std::stack<int> stack2; // 用于出队操作的栈
};

int main() {
    MyQueue q;

    q.push(1);
    q.push(2);
    q.push(3);

    std::cout << q.pop() << std::endl; // 输出：1
    std::cout << q.pop() << std::endl; // 输出：2

    q.push(4);

    std::cout << q.pop() << std::endl; // 输出：3
    std::cout << q.pop() << std::endl; // 输出：4

    std::cout << (q.empty() ? "队列为空" : "队列不为空") << std::endl; // 输出：队列为空

    return 0;
}
```

## 2、**包含min函数的栈**

### 2.1、问题描述

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 min 函数，输入操作时保证 pop、top 和 min 函数操作时，栈中一定有元素。

此栈包含的方法有：

push(value):将value压入栈中

pop():弹出栈顶元素

top():获取栈顶元素

min():获取栈中最小元素

> 示例:
>
> 输入:    ["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"]
>
> 输出:    -1,2,1,-1
>
> 解析:
>
> "PSH-1"表示将-1压入栈中，栈中元素为-1
>
> "PSH2"表示将2压入栈中，栈中元素为2，-1
>
> “MIN”表示获取此时栈中最小元素==>返回-1
>
> "TOP"表示获取栈顶元素==>返回2
>
> "POP"表示弹出栈顶元素，弹出2，栈中元素为-1
>
> "PSH1"表示将1压入栈中，栈中元素为1，-1
>
> "TOP"表示获取栈顶元素==>返回1
>
> “MIN”表示获取此时栈中最小元素==>返回-1
>
> **示例1**
>
> 输入： ["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"]
>
> 返回值：-1,2,1,-1

### 2.2、思路及代码

思路：

1. 使用两个栈：一个用于存储数据元素，另一个用于存储最小元素。
2. 在入栈操作时，将元素压入数据栈，并维护最小元素栈的状态。
3. 在出栈操作时，同时检查数据栈和最小元素栈，确保它们保持一致。
4. 在获取栈中最小元素时，直接返回最小元素栈的栈顶元素。

参考代码：

```C++
#include <iostream>
#include <stack>

class MinStack {
public:
    MinStack() {}

    // 入栈操作，将元素压入数据栈
    void push(int value) {
        dataStack.push(value);

        // 如果辅助栈为空或者新元素小于等于辅助栈的栈顶元素，将新元素也压入辅助栈
        if (minStack.empty() || value <= minStack.top()) {
            minStack.push(value);
        }
    }

    // 出栈操作，同时检查数据栈和辅助栈是否需要弹出
    void pop() {
        if (!dataStack.empty()) {
            if (dataStack.top() == minStack.top()) {
                minStack.pop();
            }
            dataStack.pop();
        }
    }

    // 获取栈顶元素
    int top() {
        return dataStack.top();
    }

    // 获取栈中的最小元素
    int min() {
        return minStack.top();
    }

private:
    std::stack<int> dataStack; // 数据栈
    std::stack<int> minStack;  // 辅助栈，用于存储最小元素
};

int main() {
    MinStack stack;

    stack.push(3);
    stack.push(5);
    stack.push(2);
    stack.push(1);

    std::cout << "栈中最小元素: " << stack.min() << std::endl; // 输出：1

    stack.pop();
    std::cout << "栈中顶部元素: " << stack.top() << std::endl; // 输出：2

    return 0;
}
```

## 3、**有效括号序列**

### 3.1、问题描述

给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列，

括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

> **示例1**
>
> 输入："["
>
> 返回值：false
>
> **示例2**
>
> 输入："[]"
>
> 返回值：true

### 3.2、思路及代码

思路：

1. 创建一个栈，用来存储打开的括号。
2. 遍历输入的字符串中的每个字符。
3. 如果当前字符是打开括号（'('，'{'，'['），将其入栈。
4. 如果当前字符是关闭括号（')'，'}'，']'），检查栈是否为空。
   1. 如果栈为空，返回 false，因为没有匹配的打开括号。
   2. 如果栈不为空，弹出栈顶元素，检查是否与当前字符匹配。
      - 如果匹配，继续遍历下一个字符。
      - 如果不匹配，返回 false。
5. 完成字符串遍历后，检查栈是否为空。
   1. 如果栈为空，说明所有括号都有匹配，返回 true。
   2. 如果栈不为空，说明有未闭合的括号，返回 false。

参考代码：

```C++
#include <stack>
#include <string>

bool isValid(std::string s) {
    std::stack<char> charStack; // 用于存储括号字符的栈
    
    for (char c : s) {
        if (c == '(' || c == '{' || c == '[') {
            charStack.push(c); // 如果是打开括号，入栈
        } else if (c == ')' || c == '}' || c == ']') {
            if (charStack.empty()) {
                return false; // 栈为空，没有匹配的打开括号
            }
            char top = charStack.top(); // 获取栈顶元素
            charStack.pop(); // 弹出栈顶元素
            if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) {
                return false; // 括号不匹配
            }
        }
    }
    
    return charStack.empty(); // 检查栈是否为空
}

int main() {
    std::string input;
    std::cout << "Enter a string of brackets: ";
    std::cin >> input;

    if (isValid(input)) {
        std::cout << "The input is a valid bracket sequence." << std::endl;
    } else {
        std::cout << "The input is not a valid bracket sequence." << std::endl;
    }

    return 0;
}
```

## 4、**滑动窗口的最大值**

### 4.1、问题描述

给定一个长度为 n 的数组 num 和滑动窗口的大小 size ，找出所有滑动窗口里数值的最大值。

例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

窗口大于数组长度或窗口长度为0的时候，返回空。

> **示例1**
>
> 输入：[2,3,4,2,6,2,5,1],3
>
> 返回值：[4,4,6,6,6,5]
>
> **示例2**
>
> 输入：[9,10,9,-7,-3,8,2,-6],5
>
> 返回值：[10,10,9,8]
>
> **示例3**
>
> 输入：[1,2,3,4],5
>
> 返回值：[]

### 4.2、思路及代码

思路：

这个问题可以通过维护一个双端队列（deque）来解决，队列中存储的是数组元素的索引，而不是元素本身。我们可以保持队列头部始终是当前滑动窗口中的最大值的索引。每当我们在队列尾部添加一个新元素时，就需要检查队列头部的索引是否在当前滑动窗口中，如果不在，就将其从队列中弹出。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <deque>

std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
    std::vector<int> result; // 用于存放每个窗口的最大值
    std::deque<int> dq; // 双端队列，用于存储元素的索引

    for (int i = 0; i < nums.size(); i++) {
        // 清理队列：删除超出窗口范围的元素
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }

        // 清理队列：删除队列中所有小于当前元素的元素
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }

        // 添加元素：将当前元素的索引添加到队列尾部
        dq.push_back(i);

        // 检查窗口：如果当前位置已经达到了窗口大小 k，将队列头部的索引对应的元素添加到结果中
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }

    return result;
}

int main() {
    std::vector<int> nums = {2, 3, 4, 2, 6, 2, 5, 1};
    int k = 3;

    std::vector<int> result = maxSlidingWindow(nums, k);

    for (int maxVal : result) {
        std::cout << maxVal << " ";
    }

    return 0;
}
```

这段代码首先维护一个双端队列 `dq`，然后遍历数组 `nums`。在每个位置上，执行了三个步骤：

1. 清理队列：删除超出窗口范围的元素。
2. 清理队列：删除队列中所有小于当前元素的元素，因为它们不可能是窗口内的最大值。
3. 添加元素：将当前元素的索引添加到队列尾部。
4. 检查窗口：如果当前位置已经达到了窗口大小 `k`，将队列头部的索引对应的元素添加到结果中。

## 5、**最小的K个数**

### 5.1、问题描述

给定一个长度为 n 的可能有重复值的数组，找出其中不去重的最小的 k 个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4(任意顺序皆可)。

> **示例1**
>
> 输入：[4,5,1,6,2,7,3,8],4 
>
> 返回值：[1,2,3,4]
>
> 说明：返回最小的4个数即可，返回[1,3,2,4]也可以        
>
> **示例2**
>
> 输入：[1],0
>
> 返回值：[]
>
> **示例3**
>
> 输入：[0,1,2,1,2],3
>
> 返回值：[0,1,1]

### 5.2、思路及代码

思路：

1. 创建一个空的结果数组 `result` 以存储最终的结果。
2. 检查特殊情况：
   1. 如果 `k` 小于等于 0，返回一个空数组，因为不需要找任何元素。
   2. 如果 `k` 大于等于数组的大小，直接返回原始数组，因为无需去重，它本身就是最小的 `k` 个数。
3. 创建一个最小堆（Min Heap），用于存储最小的 `k` 个数。
4. 遍历数组的前 `k` 个元素，并将它们添加到最小堆中。
5. 继续遍历数组的剩余部分，从第 `k+1` 个元素开始，与堆顶元素（最小值）比较：
   1. 如果当前元素小于堆顶元素，弹出堆顶元素，将当前元素加入堆中，确保堆中始终包含最小的 `k` 个数。
   2. 如果当前元素大于等于堆顶元素，继续遍历下一个元素。
6. 完成遍历后，堆中的元素就是最小的 `k` 个数，但它们可能会包含重复的元素。
7. 将堆中的元素按顺序弹出，加入 `result` 数组，以确保它们按升序排列。
8. 返回 `result` 数组，其中包含了不去重的最小的 `k` 个数。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <queue>

std::vector<int> getLeastNumbers(std::vector<int>& arr, int k) {
    std::vector<int> result;
    if (k <= 0) {
        return result; // 如果 k 小于等于 0，返回空数组
    }
    
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap; // 创建最小堆
    
    // 遍历数组，将前 k 个元素添加到最小堆中
    for (int i = 0; i < k; i++) {
        minHeap.push(arr[i]);
    }
    
    // 继续遍历数组的剩余部分
    for (int i = k; i < arr.size(); i++) {
        if (arr[i] < minHeap.top()) {
            minHeap.pop(); // 如果当前元素小于堆顶元素，弹出堆顶元素
            minHeap.push(arr[i]); // 将当前元素加入堆中
        }
    }
    
    // 将堆中的元素按顺序加入结果数组
    while (!minHeap.empty()) {
        result.push_back(minHeap.top());
        minHeap.pop();
    }
    
    return result;
}

int main() {
    std::vector<int> arr = {4, 5, 1, 6, 2, 7, 3, 8};
    int k = 4;

    std::vector<int> result = getLeastNumbers(arr, k);

    for (int num : result) {
        std::cout << num << " ";
    }

    return 0;
}
```

## 6、**寻找第K大**

### 6.1、问题描述

有一个整数数组，请你根据快速排序的思路，找出数组中第 k 大的数。

给定一个整数数组 a ,同时给定它的大小n和要找的 k ，请返回第 k 大的数(包括重复的元素，不用去重)，保证答案存在。

> **示例1**
>
> 输入：[1,3,5,2,2],5,3
>
> 返回值：2
>
> **示例2**
>
> 输入：[10,10,9,9,8,7,5,6,4,3,4,2],12,3
>
> 返回值：9
>
> 说明：去重后的第3大是8，但本题要求包含重复的元素，不用去重，所以输出9 

### 6.2、思路及代码

思路：

1. 定义一个辅助函数 `quickSelect`，该函数用于在数组中选择第 k 大的元素，类似于快速排序的思想。
2. 在 `quickSelect` 函数中，首先选取一个基准元素，将数组分为两部分，左边的元素小于基准，右边的元素大于基准。
3. 基准元素的选择可以采用不同的策略，例如随机选择、中位数选择或者固定选择。在这里，选择数组的中间元素作为基准。
4. 通过交换元素，将比基准元素大的元素移到右边，比基准元素小的元素移到左边。
5. 记录基准元素在新数组中的索引，称为 `pivotRank`，它表示在当前数组中的排名。
6. 如果 `k` 等于 `pivotRank`，则找到了第 k 大的元素，返回基准元素。
7. 如果 `k` 小于 `pivotRank`，则继续在左侧部分中寻找第 k 大的元素。
8. 如果 `k` 大于 `pivotRank`，则继续在右侧部分中寻找第 `k - pivotRank - 1` 大的元素。
9. 递归地调用 `quickSelect` 直到找到第 `k` 大的元素。

参考代码：

```C++
#include <iostream>
#include <vector>
using namespace std;

// 快速选择算法，用于找出数组中第 k 大的元素
int quickSelect(vector<int>& nums, int left, int right, int k) {
    if (left == right) {
        return nums[left];
    }

    // 选择一个基准元素，将数组分为两部分，左边比基准小，右边比基准大
    int pivotIndex = left + (right - left) / 2;
    int pivot = nums[pivotIndex];
    swap(nums[pivotIndex], nums[right]);

    int i = left;
    for (int j = left; j < right; j++) {
        if (nums[j] > pivot) {
            swap(nums[i], nums[j]);
            i++;
        }
    }
    swap(nums[i], nums[right]);

    // 基准的索引
    int pivotRank = i - left;

    if (k == pivotRank) {
        return pivot; // 找到第 k 大的元素
    } else if (k < pivotRank) {
        return quickSelect(nums, left, i - 1, k);
    } else {
        return quickSelect(nums, i + 1, right, k - pivotRank - 1);
    }
}

// 主函数，找出第 k 大的元素
int findKthLargest(vector<int>& nums, int k) {
    int n = nums.size();
    if (k < 1 || k > n) {
        return -1; // 无效的 k 值
    }

    return quickSelect(nums, 0, n - 1, k - 1);
}

int main() {
    vector<int> nums = {3, 2, 1, 5, 6, 4};
    int k = 2;

    int result = findKthLargest(nums, k);
    cout << "第 " << k << " 大的元素是: " << result << endl;
    return 0;
}
```

## 7、**数据流中的中位数**

### 7.1、问题描述

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

> **示例1**
>
> 输入：[5,2,3,4,1,6,7,0,8]
>
> 返回值："5.00 3.50 3.00 3.50 3.00 3.50 4.00 3.50 4.00 "
>
> 说明：数据流里面不断吐出的是5,2,3...,则得到的平均数分别为5,(5+2)/2,3...   
>
> **示例2**
>
> 输入：[1,1,1]
>
> 返回值："1.00 1.00 1.00 "

### 7.2、思路及代码

思路：

1. 创建一个最大堆（左半部分）和一个最小堆（右半部分），分别用来存储数据流中较小的一半和较大的一半元素。
2. 为了保证最大堆和最小堆的平衡，可以约定：
   1. 如果两个堆的元素个数相等或者相差最多为1，那么最大堆的堆顶元素（堆中最大的元素）将是中位数。
   2. 如果两个堆的元素个数相差大于1，需要调整元素，将多余的元素移到另一个堆中，以保持平衡。
3. 在 `Insert` 方法中，根据以下步骤来处理新的数据：
   1. 如果新数据小于等于最大堆的堆顶元素，将它插入到最大堆中。
   2. 否则，将它插入到最小堆中。
4. 在 `GetMedian` 方法中，根据当前数据流的大小（奇数或偶数）来计算中位数：
   1. 如果数据流的大小为奇数，中位数是最大堆的堆顶元素。
   2. 如果数据流的大小为偶数，中位数是最大堆和最小堆的堆顶元素的平均值。

参考代码：

```C++
#include <iostream>
#include <queue>
using namespace std;

class Solution {
public:
    // 插入新数据
    void Insert(int num) {
        // 如果当前数据流大小是偶数，插入到最小堆
        if (((minHeap.size() + maxHeap.size()) & 1) == 0) {
            if (!maxHeap.empty() && num < maxHeap.top()) {
                maxHeap.push(num);
                num = maxHeap.top();
                maxHeap.pop();
            }
            minHeap.push(num);
        } else {  // 当前数据流大小是奇数，插入到最大堆
            if (!minHeap.empty() && num > minHeap.top()) {
                minHeap.push(num);
                num = minHeap.top();
                minHeap.pop();
            }
            maxHeap.push(num);
        }
    }

    // 获取中位数
    double GetMedian() {
        int size = minHeap.size() + maxHeap.size();
        if (size == 0)
            throw runtime_error("No numbers are available.");
        if ((size & 1) == 0) {  // 数据流大小为偶数
            return (minHeap.top() + maxHeap.top()) / 2.0;
        } else {  // 数据流大小为奇数
            return minHeap.top();
        }
    }

private:
    priority_queue<int, vector<int>, less<int>> maxHeap;  // 最大堆，存储较小的一半元素
    priority_queue<int, vector<int>, greater<int>> minHeap;  // 最小堆，存储较大的一半元素
};

int main() {
    Solution solution;
    solution.Insert(1);
    solution.Insert(2);
    solution.Insert(3);
    cout << "当前中位数：" << solution.GetMedian() << endl; // 输出 2.0
    solution.Insert(4);
    cout << "当前中位数：" << solution.GetMedian() << endl; // 输出 2.5
    return 0;
}
```

## 8、**表达式求值**

### 8.1、问题描述

请写一个整数计算器，支持加减乘三种运算和括号。

> **示例1**
>
> 输入："1+2"
>
> 返回值：3
>
> **示例2**
>
> 输入："(2*(3-4))*5"
>
> 返回值：-10
>
> **示例3**
>
> 输入："3+2
>
> 返回值：26

### 8.2、思路及代码

思路：

1. 我们使用一个栈 `sum` 来存储中间结果，用于执行加法和减法操作。同时，我们使用一个变量 `sign` 来存储前一个运算符，初始化为 `+`。
2. 我们遍历输入的字符串 `s` 中的每一个字符，一个字符一个字符地处理。首先，我们检查是否遇到了数字字符。如果是数字字符，我们将其转化为对应的整数并累积到 `num` 中。
3. 如果遇到左括号 `(`，说明我们需要进一步计算括号内的表达式。我们记录下左括号的位置，并找到与其匹配的右括号 `)`。然后，我们递归地计算括号内的表达式，得到结果并将其存储在 `num` 变量中。
4. 当我们遇到右括号 `)` 或者字符串的末尾，或者遇到加法 `+`、减法 `-`、乘法 `*` 操作符时，说明我们需要进行结算。
5. 如果前一个运算符是加法 `+`，我们将 `num` 入栈 `sum`，表示加法运算。如果前一个运算符是减法 `-`，我们将 `-num` 入栈 `sum`，相当于减法运算。
6. 如果前一个运算符是乘法 `*`，我们将栈顶元素与 `num` 相乘，并将结果重新入栈 `sum`，实现乘法运算。
7. 然后，我们更新 `sign` 为当前遇到的运算符，重置 `num` 为 0，以准备处理下一个数字。
8. 循环结束后，我们还需要将栈 `sum` 中的所有元素弹出并相加，得到最终结果。
9. 最后，返回计算结果 `res`。

参考代码：

```C++
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int calculate(string s) {
    int res = 0; //用于返回当前字符串的计算结果
    stack<int> sum; //用于求和
    char sign = '+'; //记录前一个符号，初始化为+，因为可以看成当前字符串前先加0
    int num = 0; //用于将连续数字字符串转化成数字或者记录递归结果
    for(int i = 0; i < s.size(); i++) { //遍历每一个字符
        if(s[i] >= '0' && s[i] <= '9') //先处理数字字符
            num = 10 * num + s[i] - '0'; //进位后加个位数
        if(s[i] == '(') { //对于括号
            int left = i++, count = 1; //用left记录最左括号位置，count记录左括号数，i当成右指针右移一格
            while(count > 0) { //最终目的是找到与最左括号匹配的右括号，类似于栈操作
                if(s[i] == '(') count++;
                else if(s[i] == ')') count--;
                i++;
            }
            num = solve(s.substr(left + 1, i - left - 2)); //迭代计算括号内数值，注意不要包含最左最右括号，不然会死循环
            i--; //此时i是最右括号下一位，需要左移一位防止最右括号在字符串尾时发生越界从而使下面的判定失效
        }
        if(i == s.size() - 1 || s[i] == '+' || s[i] == '-' || s[i] == '*') { //对于字符串尾，或者加减乘，此时我们用的符号是上一次的，结算当前数字
            if(sign == '+') sum.push(num); //加法入栈
            else if(sign == '-') sum.push(-num); //减法相当于加负数
            else if(sign == '*') sum.top() *= num; //乘法与栈顶相乘
            sign = s[i]; //更新符号，若为末尾的右括号也无妨，因为马上就退出循环了
            num = 0; //重置当前数
        }
    }
    while(!sum.empty()) { //将栈内所有数字相加
        res += sum.top();
        sum.pop();
    }
    return res; //返回当前字符串计算结果
}

int main() {
    string expression = "(1+(4+5+2)-3)+(6+8)";
    int result = calculate(expression);
    cout << "计算结果: " << result << endl; // 输出 23
    return 0;
}
```