# 补种未成活胡杨

## 问题描述

在一条直线上有N个连续的树位，每个树位上可能有已成活的胡杨树（用1表示）或未成活的树位（用0表示）。需要补种M棵胡杨树到未成活的树位上。补种时，相邻的树位不能同时补种，以确保树木有足够的生长空间。目标是补种后，计算剩余未成活的树位数量。

## 输入格式

- 第一行：一个整数N（1 ≤ N ≤ 1000），表示树位的数量。
- 第二行：N个整数（0或1），表示每个树位的状态。
- 第三行：一个整数M（0 ≤ M ≤ N），表示补种的树木数量。

## 输出格式

- 一个整数，表示补种后未成活树位的数量。

## 示例

**输入：**

```
5
1 0 0 1 0
2
```

**输出：**

```
1
```

## 解题思路

1. **统计未成活树位**：首先统计出所有未成活的树位（0）的数量。
2. **确定可补种位置**：在未成活的树位中，找到可以补种的位置。补种时需要确保相邻的树位不被同时补种。
3. **优先补种**：优先在可以补种的位置上补种M棵树。
4. **计算剩余未成活树位**：补种后，计算剩余的未成活树位数量。

## 解决方案

### Java

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] trees = new int[N];
        for (int i = 0; i < N; i++) {
            trees[i] = scanner.nextInt();
        }
        int M = scanner.nextInt();
        int unplanted = 0;
        for (int tree : trees) {
            if (tree == 0) unplanted++;
        }
        int canPlant = 0;
        for (int i = 0; i < N; i++) {
            if (trees[i] == 0) {
                if ((i == 0 || trees[i - 1] == 0) && (i == N - 1 || trees[i + 1] == 0)) {
                    canPlant++;
                    i++; // 跳过下一个树位
                }
            }
        }
        int planted = Math.min(M, canPlant);
        int remaining = unplanted - planted;
        System.out.println(remaining);
    }
}
```

### Python3

```python
N = int(input())
trees = list(map(int, input().split()))
M = int(input())
unplanted = trees.count(0)
can_plant = 0
i = 0
while i < N:
    if trees[i] == 0:
        if (i == 0 or trees[i - 1] == 0) and (i == N - 1 or trees[i + 1] == 0):
            can_plant += 1
            i += 1  # 跳过下一个树位
    i += 1
planted = min(M, can_plant)
remaining = unplanted - planted
print(remaining)
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> trees(N);
    for (int i = 0; i < N; i++) {
        cin >> trees[i];
    }
    int M;
    cin >> M;
    int unplanted = 0;
    for (int tree : trees) {
        if (tree == 0) unplanted++;
    }
    int canPlant = 0;
    for (int i = 0; i < N; ) {
        if (trees[i] == 0) {
            if ((i == 0 || trees[i - 1] == 0) && (i == N - 1 || trees[i + 1] == 0)) {
                canPlant++;
                i += 2;  // 跳过下一个树位
            } else {
                i++;
            }
        } else {
            i++;
        }
    }
    int planted = min(M, canPlant);
    int remaining = unplanted - planted;
    cout << remaining << endl;
    return 0;
}
```

### C语言

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int N;
    scanf("%d", &N);
    int* trees = (int*)malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        scanf("%d", &trees[i]);
    }
    int M;
    scanf("%d", &M);
    int unplanted = 0;
    for (int i = 0; i < N; i++) {
        if (trees[i] == 0) unplanted++;
    }
    int canPlant = 0;
    for (int i = 0; i < N; ) {
        if (trees[i] == 0) {
            if ((i == 0 || trees[i - 1] == 0) && (i == N - 1 || trees[i + 1] == 0)) {
                canPlant++;
                i += 2;  // 跳过下一个树位
            } else {
                i++;
            }
        } else {
            i++;
        }
    }
    int planted = (M < canPlant) ? M : canPlant;
    int remaining = unplanted - planted;
    printf("%d\n", remaining);
    free(trees);
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

let N, trees, M;
rl.on('line', (line) => {
    if (!N) {
        N = parseInt(line);
    } else if (!trees) {
        trees = line.split(' ').map(Number);
    } else {
        M = parseInt(line);
        let unplanted = trees.filter(t => t === 0).length;
        let canPlant = 0;
        for (let i = 0; i < N; ) {
            if (trees[i] === 0) {
                if ((i === 0 || trees[i - 1] === 0) && (i === N - 1 || trees[i + 1] === 0)) {
                    canPlant++;
                    i += 2;  // 跳过下一个树位
                } else {
                    i++;
                }
            } else {
                i++;
            }
        }
        let planted = Math.min(M, canPlant);
        let remaining = unplanted - planted;
        console.log(remaining);
        rl.close();
    }
});
```

### Go

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin);
    scanner.Scan();
    N, _ := strconv.Atoi(scanner.Text());
    scanner.Scan();
    treesStr := strings.Split(scanner.Text(), " ");
    trees := make([]int, N);
    for i, s := range treesStr {
        trees[i], _ = strconv.Atoi(s);
    }
    scanner.Scan();
    M, _ := strconv.Atoi(scanner.Text());
    unplanted := 0;
    for _, tree := range trees {
        if tree == 0 {
            unplanted++;
        }
    }
    canPlant := 0;
    for i := 0; i < N; {
        if trees[i] == 0 {
            if (i == 0 || trees[i-1] == 0) && (i == N-1 || trees[i+1] == 0) {
                canPlant++;
                i += 2; // 跳过下一个树位
            } else {
                i++;
            }
        } else {
            i++;
        }
    }
    planted := M;
    if canPlant < M {
        planted = canPlant;
    }
    remaining := unplanted - planted;
    fmt.Println(remaining);
}
```