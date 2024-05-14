# 面试经典算法题50-有效的括号

LeetCode.20

### 问题描述

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

**示例 1：**

```
输入：s = "()"
输出：true
```

**示例 2：**

```
输入：s = "()[]{}"
输出：true
```

**示例 3：**

```
输入：s = "(]"
输出：false
```

### 思路

1. 初始化一个空栈：使用栈来存放左括号，每当遇到一个左括号时，就将其压入栈中。
2. 遍历字符串：我们从头到尾遍历字符串中的每个字符。
3. 处理括号：
   - 如果当前字符是左括号（`'('`，`'{'`，`'['`），我们将其压入栈中。
   - 如果当前字符是右括号（`')'`，`'}'`，`']'`），我们需要判断栈顶的左括号是否与其匹配。如果匹配，则将栈顶的左括号出栈；否则，返回 false。
4. 判断栈是否为空：在遍历完整个字符串后，我们需要检查栈是否为空。如果栈为空，说明所有的括号都有匹配的右括号，返回 true；否则，返回 false。

### 参考代码

#### C++

```
#include <iostream>
#include <stack>
#include <unordered_map>

using namespace std;

bool isValid(string s) {
    stack<char> stk; // 用于存放左括号的栈
    unordered_map<char, char> mappings = {
        {')', '('},
        {'}', '{'},
        {']', '['}
    }; // 用于存放右括号与其对应的左括号的映射关系

    // 遍历输入字符串
    for (char c : s) {
        // 如果是左括号，压入栈中
        if (c == '(' || c == '{' || c == '[') {
            stk.push(c);
        } else {
            // 如果是右括号
            // 判断栈是否为空或者栈顶元素是否与当前右括号匹配
            if (stk.empty() || stk.top() != mappings[c]) {
                return false; // 不匹配，返回 false
            }
            stk.pop(); // 匹配，将栈顶元素出栈
        }
    }

    // 最后判断栈是否为空，如果为空则说明所有括号都匹配
    return stk.empty();
}

int main() {
    string s = "{[()]}";
    cout << isValid(s) << endl; // 输出 1，表示有效

    s = "{[(])}";
    cout << isValid(s) << endl; // 输出 0，表示无效

    return 0;
}
```

#### Java

```
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> mappings = new HashMap<>();
        mappings.put(')', '(');
        mappings.put('}', '{');
        mappings.put(']', '[');

        for (char c : s.toCharArray()) {
            if (mappings.containsValue(c)) {
                stack.push(c);
            } else if (mappings.containsKey(c)) {
                if (stack.isEmpty() || stack.pop() != mappings.get(c)) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        ValidParentheses vp = new ValidParentheses();
        String s = "{[()]}";
        System.out.println(vp.isValid(s)); // 输出 true，表示有效

        s = "{[(])}";
        System.out.println(vp.isValid(s)); // 输出 false，表示无效
    }
}
```

#### Python

```
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mappings.values():
                stack.append(char)
            elif char in mappings.keys():
                if not stack or stack.pop() != mappings[char]:
                    return False
            else:
                return False

        return not stack

# 测试代码
s = Solution()
print(s.isValid("{[()]}"))  # 输出 True，表示有效
print(s.isValid("{[(])}"))  # 输出 False，表示无效
```

