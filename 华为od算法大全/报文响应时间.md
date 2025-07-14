# 报文响应时间

## 问题描述

在网络通信中，发送方在时间S发送报文，接收方在时间R响应。需要计算在时间段[S, R)内，发送方发送的报文在接收方响应之前的时间。

## 输入格式

- 第一行：一个整数T（1 ≤ T ≤ 1000），表示时间段的数量。
- 接下来T行，每行两个整数S和R（0 ≤ S < R ≤ 1000），分别表示发送时间和响应时间。

## 输出格式

- T行，每行一个整数，表示在该时间段内，发送方发送的报文在接收方响应之前的时间。

## 示例

**输入：**

```
2
1 3
2 4
```

**输出：**

```
2
2
```

## 解题思路

1. **计算时间差**：对于每个时间段[S, R)，计算R - S。
2. **输出结果**：直接输出R - S作为结果。

## 解决方案

### Java

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            int S = scanner.nextInt();
            int R = scanner.nextInt();
            System.out.println(R - S);
        }
    }
}
```

### Python3

```python
T = int(input())
for _ in range(T):
    S, R = map(int, input().split())
    print(R - S)
```

### C++

```cpp
#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int S, R;
        cin >> S >> R;
        cout << R - S << endl;
    }
    return 0;
}
```

### C语言

```c
#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        int S, R;
        scanf("%d %d", &S, &R);
        printf("%d\n", R - S);
    }
    return 0;
}
```

### JsNode

```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let T;
rl.on('line', (line) => {
    if (!T) {
        T = parseInt(line);
    } else {
        const [S, R] = line.split(' ').map(Number);
        console.log(R - S);
        T--;
        if (T === 0) {
            rl.close();
        }
    }
});
```

### Go

```go
package main

import (
    "fmt"
)

func main() {
    var T int
    fmt.Scan(&T)
    for i := 0; i < T; i++ {
        var S, R int
        fmt.Scan(&S, &R)
        fmt.Println(R - S)
    }
}
```