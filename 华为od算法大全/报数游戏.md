# 报数游戏

## 问题描述

有N个人围成一个圈，从第一个人开始报数，报到M的人出列，然后从下一个人开始重新报数，重复此过程，直到所有人都出列。需要输出出列的顺序。

## 输入格式

- 第一行：两个整数N（1 ≤ N ≤ 1000）和M（1 ≤ M ≤ 1000），分别表示人数和报数的数字。

## 输出格式

- 一行N个整数，表示出列的顺序。

## 示例

**输入：**

```
5 3
```

**输出：**

```
3 1 5 2 4
```

## 解题思路

1. **模拟过程**：使用一个队列或列表模拟围成圈的人。
2. **报数出列**：每次从队列中取出M-1个人，然后将第M个人出列，并将未出列的人放回队列尾部。
3. **重复过程**：重复上述步骤，直到队列为空。

## 解决方案

### Java

```java
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            queue.offer(i);
        }
        StringBuilder sb = new StringBuilder();
        while (!queue.isEmpty()) {
            for (int i = 0; i < M - 1; i|<|) {
                int front = queue.poll();
                queue.offer(front);
            }
            sb.append(queue.poll()).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
```

### Python3

```python
from collections import deque

N, M = map(int, input().split())
queue = deque(range(1, N + 1))
result = []
while queue:
    for _ in range(M - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
print(' '.join(map(str, result)))
```

### C++

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    queue<int> q;
    for (int i = 1; i <= N; i++) {
        q.push(i);
    }
    vector<int> result;
    while (!q.empty()) {
        for (int i = 0; i < M - 1; i++) {
            int front = q.front();
            q.pop();
            q.push(front);
        }
        result.push_back(q.front());
        q.pop();
    }
    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << " ";
    }
    cout << endl;
    return 0;
}
```

### C语言

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    Node* head = createNode(1);
    Node* current = head;
    for (int i = 2; i <= N; i++) {
        current->next = createNode(i);
        current = current->next;
    }
    current->next = head;  // 形成环
    Node* prev = current;
    current = head;
    int count = 0;
    while (current->next != current) {
        count++;
        if (count == M) {
            printf("%d ", current->data);
            prev->next = current->next;
            Node* temp = current;
            current = current->next;
            free(temp);
            count = 0;
        } else {
            prev = current;
            current = current->next;
        }
    }
    printf("%d\n", current->data);
    free(current);
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

rl.on('line', (line) => {
    const [N, M] = line.split(' ').map(Number);
    const queue = [];
    for (let i = 1; i <= N; i++) {
        queue.push(i);
    }
    const result = [];
    while (queue.length > 0) {
        for (let i = 0; i < M - 1; i++) {
            const front = queue.shift();
            queue.push(front);
        }
        result.push(queue.shift());
    }
    console.log(result.join(' '));
    rl.close();
});
```

### Go

```go
package main

import (
    "container/ring"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    var N, M int
    fmt.Scan(&N, &M)
    r := ring.New(N)
    for i := 1; i <= N; i++ {
        r.Value = i
        r = r.Next()
    }
    var result []string
    for r.Len() > 0 {
        for i := 0; i < M - 1; i++ {
            r = r.Next()
        }
        result = append(result, strconv.Itoa(r.Value.(int)))
        r = r.Unlink(1)
    }
    fmt.Println(strings.Join(result, " "))
}
```