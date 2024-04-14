# 面试经典算法题43-Z字形变换

LeetCode.6

### 问题描述

将一个给定字符串 `s` 根据给定的行数 `numRows` ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"PAYPALISHIRING"` 行数为 `3` 时，排列如下：

```
P   A   H   N
A P L S I I G
Y   I   R
```

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。

请你实现这个将字符串进行指定行数变换的函数：

```
string convert(string s, int numRows);
```

**示例 1：**

```
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
```

**示例 2：**

```
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
```

**示例 3：**

```
输入：s = "A", numRows = 1
输出："A"
```

### 思路

1. 创建一个大小为 numRows 的数组，数组中的每个元素代表 Z 字形中的一行。
2. 遍历输入字符串，根据当前字符应该放置在哪一行，将其加入对应行的字符串中。
3. 如果当前行是第一行或最后一行，则改变方向。
4. 最后将所有行拼接起来，即为最终结果。

### 图解

```
+-----------------------------+
|        开始执行程序           |
+-----------------------------+
			 |
			 v 
+-----------------------------+
|       初始化变量              |
|       rows  = ["", "", ""]  |
|       currentRow = 0        |
|       goingDown = false     |
+-----------------------------+
			 |
			 v
+-----------------------------+
|       循环处理每个字符         |
+-----------------------------+
			 |
			 v
+-----------------------------+
|       当前字符 P：            |
|       rows[0]  += P         |
|       currentRow = 1        |
|       goingDown = true      |
+-----------------------------+
        	 |
	         v
+-----------------------------+
|       当前字符 A：            |
|       rows[1]  += A         |
|       currentRow = 2        |
|       goingDown = true      |
+-----------------------------+
             |
             v
+-----------------------------+
|       当前字符 Y：            |
|       rows[1]  += Y         |
|       currentRow = 1        |
|       goingDown = true      |
+-----------------------------+
             |
             v
+-----------------------------+
|       当前字符 P：            |
|       rows[0]  += P         |
|       currentRow = 0        |
|       goingDown = false     |
+-----------------------------+
             |
             v
+-----------------------------+
|       当前字符 A：            |
|       rows[1]  += A         |
|       currentRow = 1        |
|       goingDown = true      |
+-----------------------------+
             |                    
             v                    
+-----------------------------+
|       当前字符 L：            |
|       rows[2]  += L         |
|       currentRow = 2        |
|       goingDown = true      |
+-----------------------------+
             |
             v
+-----------------------------+
|       当前字符 I：            |
|       rows[1]  += I         |
|       currentRow = 1        |
|       goingDown = true      |
+-----------------------------+
             |                    
             v                    
+-----------------------------+
|       当前字符 S：            |
|       rows[0]  += S         |
|       currentRow = 0        |
|       goingDown = false     |
+-----------------------------+
             |
             v
+-----------------------------+
|       当前字符 H：            |
|       rows[1]  += H         |
|       currentRow = 1        |
|       goingDown = true      |
+-----------------------------+
             |
             v
+-----------------------------+
|       当前字符 I：            |
|       rows[2]  += I         |
|       currentRow = 2        |
|       goingDown = true      |
+-----------------------------+
             |
             v
+-----------------------------+
|       当前字符 R：            |
|       rows[1]  += R         |
|       currentRow = 1        |
|       goingDown = true      |
+-----------------------------+
             |
             v
+-----------------------------+
|   	当前字符 I：            |
|   	rows[0]  += I         |
|   	currentRow = 0        |
|   	goingDown = false     |
+-----------------------------+
             |                    
             v                    
+-----------------------------+
|   	当前字符 N：            |
|   	rows[1]  += N         |
|   	currentRow = 1        |
|   	goingDown = true      |
+-----------------------------+
             |
             v
+-----------------------------+
|      判断是否完成遍历          |
|   返回结果 "PAHNAPLSIIGYIR"  |
+-----------------------------+
```

### 参考代码

#### C++

```
#include <iostream>
#include <string>
#include <vector>

std::string convert(std::string s, int numRows) {
    if (numRows == 1) {
        return s;  // 如果只有一行，直接返回原字符串
    }

    // 创建一个大小为 numRows 的数组，用于存储 Z 字形排列后的每一行
    std::vector<std::string> rows(std::min(numRows, int(s.size())));
    int curRow = 0;  // 当前字符应该放置的行数
    bool goingDown = false;  // 标记当前方向是否向下

    for (char c : s) {
        rows[curRow] += c;  // 将当前字符加入对应行的字符串中

        // 如果当前行是第一行或最后一行，则改变方向
        if (curRow == 0 || curRow == numRows - 1) {
            goingDown = !goingDown;
        }

        curRow += goingDown ? 1 : -1;  // 根据当前方向更新行数
    }

    std::string result;
    for (const std::string& row : rows) {
        result += row;  // 将每一行拼接起来
    }

    return result;
}

int main() {
    std::string s = "PAYPALISHIRING";
    int numRows = 3;
    std::string result = convert(s, numRows);
    std::cout << result << std::endl;
    return 0;
}
```

#### Java

```
public class Main {
    public static String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;  // 如果只有一行，直接返回原字符串
        }

        // 创建一个大小为 numRows 的数组，用于存储 Z 字形排列后的每一行
        StringBuilder[] rows = new StringBuilder[Math.min(numRows, s.length())];
        for (int i = 0; i < rows.length; i++) {
            rows[i] = new StringBuilder();
        }

        int curRow = 0;  // 当前字符应该放置的行数
        boolean goingDown = false;  // 标记当前方向是否向下

        for (char c : s.toCharArray()) {
            rows[curRow].append(c);  // 将当前字符加入对应行的字符串中

            // 如果当前行是第一行或最后一行，则改变方向
            if (curRow == 0 || curRow == numRows - 1) {
                goingDown = !goingDown;
            }

            curRow += goingDown ? 1 : -1;  // 根据当前方向更新行数
        }

        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);  // 将每一行拼接起来
        }

        return result.toString();
    }

    public static void main(String[] args) {
        String s = "PAYPALISHIRING";
        int numRows = 3;
        String result = convert(s, numRows);
        System.out.println(result);
    }
}
```

#### Python

```
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s  # 如果只有一行，直接返回原字符串

    # 创建一个大小为 numRows 的数组，用于存储 Z 字形排列后的每一行
    rows = [''] * min(numRows, len(s))
    cur_row = 0  # 当前字符应该放置的行数
    going_down = False  # 标记当前方向是否向下

    for c in s:
        rows[cur_row] += c  # 将当前字符加入对应行的字符串中

        # 如果当前行是第一行或最后一行，则改变方向
        if cur_row == 0 or cur_row == numRows - 1:
            going_down = not going_down

        cur_row += 1 if going_down else -1  # 根据当前方向更新行数

    return ''.join(rows)

# 测试
s = "PAYPALISHIRING"
numRows = 3
result = convert(s, numRows)
print(result)
```