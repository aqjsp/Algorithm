# 面试经典算法题60-二进制求和

LeetCode.67

### 问题描述

给你两个二进制字符串 `a` 和 `b` ，以二进制字符串的形式返回它们的和。

**示例 1：**

```
输入:a = "11", b = "1"
输出："100"
```

**示例 2：**

```
输入：a = "1010", b = "1011"
输出："10101"
```

### 思路

1. 初始化：创建一个空字符串 `result` 来保存结果，并初始化两个指针 `i` 和 `j` 分别指向 `a` 和 `b` 的末尾。同时，初始化一个变量 `carry` 用于保存进位值，初始值为 0。

2. 逐位相加：

   - 从 `a` 和 `b` 的末尾开始逐位相加。

   - 每次循环中，取出当前位的值并转换为整数，处理进位情况。
   - 计算当前位的和，并根据和的结果更新进位 `carry`。
   - 将当前位的结果添加到 `result` 字符串中。

3. 处理进位：当所有位都处理完后，检查是否还有进位。如果有，将其添加到结果字符串中。

4. 返回结果：由于是从末尾开始逐位相加，最终得到的结果需要反转。

### 参考代码

#### C++

```
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string addBinary(string a, string b) {
    string result = "";  // 初始化结果字符串
    int i = a.length() - 1, j = b.length() - 1;  // 初始化指针指向a和b的末尾
    int carry = 0;  // 初始化进位为0

    // 循环处理a和b的每一位
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;  // 当前位的和，初始值为进位

        // 如果i>=0，说明a还有未处理的位
        if (i >= 0) {
            sum += a[i--] - '0';  // 将a的当前位转换为整数并加到sum中
        }

        // 如果j>=0，说明b还有未处理的位
        if (j >= 0) {
            sum += b[j--] - '0';  // 将b的当前位转换为整数并加到sum中
        }

        result += to_string(sum % 2);  // 计算当前位的结果并添加到结果字符串中
        carry = sum / 2;  // 更新进位
    }

    reverse(result.begin(), result.end());  // 反转结果字符串

    return result;  // 返回最终结果
}

int main() {
    string a, b;

    // 输入a和b
    cout << "输入a: ";
    cin >> a;
    cout << "输入b: ";
    cin >> b;

    // 计算a和b的二进制和
    string result = addBinary(a, b);

    // 输出结果
    cout << "输出: " << result << endl;

    return 0;
}
```

#### Java

```
import java.util.Scanner;

public class AddBinary {
    public static String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder(); // 初始化结果字符串
        int i = a.length() - 1, j = b.length() - 1; // 初始化指针指向a和b的末尾
        int carry = 0; // 初始化进位为0

        // 循环处理a和b的每一位
        while (i >= 0 || j >= 0 || carry != 0) {
            int sum = carry; // 当前位的和，初始值为进位

            // 如果i>=0，说明a还有未处理的位
            if (i >= 0) {
                sum += a.charAt(i--) - '0'; // 将a的当前位转换为整数并加到sum中
            }

            // 如果j>=0，说明b还有未处理的位
            if (j >= 0) {
                sum += b.charAt(j--) - '0'; // 将b的当前位转换为整数并加到sum中
            }

            result.append(sum % 2); // 计算当前位的结果并添加到结果字符串中
            carry = sum / 2; // 更新进位
        }

        return result.reverse().toString(); // 反转结果字符串并返回最终结果
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 输入a和b
        System.out.print("输入a: ");
        String a = scanner.nextLine();
        System.out.print("输入b: ");
        String b = scanner.nextLine();

        // 计算a和b的二进制和
        String result = addBinary(a, b);

        // 输出结果
        System.out.println("输出: " + result);
    }
}
```

#### Python

```
def add_binary(a, b):
    result = []  # 用于保存结果的列表
    i, j = len(a) - 1, len(b) - 1  # 初始化指针指向a和b的末尾
    carry = 0  # 初始化进位为0

    # 循环处理a和b的每一位
    while i >= 0 or j >= 0 or carry:
        sum = carry  # 当前位的和，初始值为进位

        # 如果i >= 0，说明a还有未处理的位
        if i >= 0:
            sum += int(a[i])  # 将a的当前位转换为整数并加到sum中
            i -= 1

        # 如果j >= 0，说明b还有未处理的位
        if j >= 0:
            sum += int(b[j])  # 将b的当前位转换为整数并加到sum中
            j -= 1

        result.append(str(sum % 2))  # 计算当前位的结果并添加到结果列表中
        carry = sum // 2  # 更新进位

    return ''.join(result[::-1])  # 反转结果列表并转换为字符串返回


# 示例1
a1 = "11"
b1 = "1"
print(f"输入: a = {a1}, b = {b1}")
print(f"输出: {add_binary(a1, b1)}")

# 示例2
a2 = "1010"
b2 = "1011"
print(f"输入: a = {a2}, b = {b2}")
print(f"输出: {add_binary(a2, b2)}")
```

