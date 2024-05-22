# 面试经典算法题52-逆波兰表达式求值

LeetCode.150

### 问题描述

给你一个字符串数组 `tokens` ，表示一个根据 逆波兰表示法表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

**注意：**

- 有效的算符为 `'+'`、`'-'`、`'*'` 和 `'/'` 。
- 每个操作数（运算对象）都可以是一个整数或者另一个表达式。
- 两个整数之间的除法总是 **向零截断** 。
- 表达式中不含除零运算。
- 输入是一个根据逆波兰表示法表示的算术表达式。
- 答案及所有中间计算结果可以用 **32 位** 整数表示。

**示例 1：**

```
输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
```

**示例 2：**

```
输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
```

**示例 3：**

```
输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

### 思路

1. 创建一个栈：用来存储操作数。
2. 遍历输入的每个元素：
   - 如果元素是操作数（即数字），将其转换为整数并压入栈中。
   - 如果元素是操作符（`+`, `-`, `*`, `/`），从栈中弹出两个操作数进行相应的运算，并将结果压入栈中。
3. 最终结果：遍历结束后，栈中应只剩下一个元素，即为表达式的结果。

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st; // 创建一个栈用于存储操作数
        for (const string& token : tokens) {
            if (isOperator(token)) { // 判断是否为操作符
                int b = st.top(); st.pop(); // 弹出第一个操作数
                int a = st.top(); st.pop(); // 弹出第二个操作数
                int result = performOperation(a, b, token); // 执行运算
                st.push(result); // 将运算结果压入栈中
            } else {
                st.push(stoi(token)); // 将数字转换为整数并压入栈中
            }
        }
        return st.top(); // 最终结果应是栈中唯一的元素
    }

private:
    bool isOperator(const string& token) {
        return token == "+" || token == "-" || token == "*" || token == "/";
    }

    int performOperation(int a, int b, const string& op) {
        if (op == "+") return a + b;
        if (op == "-") return a - b;
        if (op == "*") return a * b;
        if (op == "/") return a / b;
        throw invalid_argument("Invalid operator");
    }
};

int main() {
    Solution solution;
    vector<string> tokens = {"2", "1", "+", "3", "*"};
    int result = solution.evalRPN(tokens);
    cout << "表达式的值: " << result << endl; // 输出 9
    return 0;
}
```

#### Java

```
import java.util.Stack;

public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>(); // 创建一个栈用于存储操作数
        
        for (String token : tokens) {
            if (isOperator(token)) { // 判断是否为操作符
                int b = stack.pop(); // 弹出第一个操作数
                int a = stack.pop(); // 弹出第二个操作数
                int result = performOperation(a, b, token); // 执行运算
                stack.push(result); // 将运算结果压入栈中
            } else {
                stack.push(Integer.parseInt(token)); // 将数字转换为整数并压入栈中
            }
        }
        return stack.pop(); // 最终结果应是栈中唯一的元素
    }

    // 判断是否为操作符
    private boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/");
    }

    // 根据操作符执行相应的运算
    private int performOperation(int a, int b, String op) {
        switch (op) {
            case "+":
                return a + b;
            case "-":
                return a - b;
            case "*":
                return a * b;
            case "/":
                return a / b;
            default:
                throw new IllegalArgumentException("Invalid operator");
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] tokens1 = {"2", "1", "+", "3", "*"};
        int result1 = solution.evalRPN(tokens1);
        System.out.println("表达式的值: " + result1); // 输出 9

        String[] tokens2 = {"4", "13", "5", "/", "+"};
        int result2 = solution.evalRPN(tokens2);
        System.out.println("表达式的值: " + result2); // 输出 6
    }
}
```

#### Python

```
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # 创建一个栈用于存储操作数
        
        for token in tokens:
            if self.is_operator(token):  # 判断是否为操作符
                b = stack.pop()  # 弹出第一个操作数
                a = stack.pop()  # 弹出第二个操作数
                result = self.perform_operation(a, b, token)  # 执行运算
                stack.append(result)  # 将运算结果压入栈中
            else:
                stack.append(int(token))  # 将数字转换为整数并压入栈中
        
        return stack.pop()  # 最终结果应是栈中唯一的元素
    
    def is_operator(self, token: str) -> bool:
        # 判断字符串是否为操作符
        return token in {"+", "-", "*", "/"}
    
    def perform_operation(self, a: int, b: int, op: str) -> int:
        # 根据操作符执行相应的运算
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            # 注意 Python 整数除法的向下取整特性
            return int(a / b)
        else:
            raise ValueError("Invalid operator")

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    tokens1 = ["2", "1", "+", "3", "*"]
    result1 = solution.evalRPN(tokens1)
    print("表达式的值:", result1)  # 输出 9

    tokens2 = ["4", "13", "5", "/", "+"]
    result2 = solution.evalRPN(tokens2)
    print("表达式的值:", result2)  # 输出 6
```

