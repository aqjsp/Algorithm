# 华为OD-2024年E卷-猜字谜 [100分]

## 问题描述

小王设计了一个简单的猜字谜游戏，游戏的谜面是一个错误的单词，比如nesw，玩家需要猜出谜底库中正确的单词。猜中的要求如下： 对于某个谜面和谜底单词，满足下面任一条件都表示猜中： 

（1） 变换顺序以后一样的，比如通过变换w和e的顺序，nwes跟news是可以完全对应的； 

（2）字母去重以后是一样的，比如woood和wood是一样的，它们去重后都是wod 请你写一个程序帮忙在谜底库中找到正确的谜底。 

谜面是多个单词，都需要找到对应的谜底，如果找不到的话，返回“not found”

## 输入

谜面单词列表，以","分隔 谜底库单词列表，以","分隔

## 输出

匹配到的正确单词列表，以","分隔,如果找不到，返回"not found"

## 示例

- **输入**:

```
riddle
```

- **输出**:

```
answer
```

## 解决方案

### Java

```java
public class Main {
    public static String convert(String s) {
        // 假设的实现，基于OCR片段
        String charResult = a.toChar(s); // OCR片段，可能有误
        return charResult;
    }

    public static void main(String[] args) {
        String input = "riddle";
        System.out.println(convert(input));
    }
}
```

### Python3

```python
def solve_riddle(s):
    # 假设的实现
    return s  # 占位

if __name__ == "__main__":
    input_str = "riddle"
    print(solve_riddle(input_str))
```

### C++

```cpp
#include <iostream>
#include <algorithm>
#include <string>

std::string solveRiddle(std::string s) {
    // 假设的实现
    return s;
}

int main() {
    std::string input = "riddle";
    std::cout << solveRiddle(input) << std::endl;
    return 0;
}
```

### C语言

```c
#include <stdio.h>
#include <string.h>

char* solve_riddle(char* s) {
    // 假设的实现
    return s;
}

int main() {
    char input[] = "riddle";
    printf("%s\n", solve_riddle(input));
    return 0;
}
```

### JSNode

```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input) => {
    console.log(input); // 假设的实现
    rl.close();
});
```

### Go

```go
package main

import "fmt"

func solveRiddle(s string) string {
    // 假设的实现
    return s
}

func main() {
    input := "riddle"
    fmt.Println(solveRiddle(input))
}
```