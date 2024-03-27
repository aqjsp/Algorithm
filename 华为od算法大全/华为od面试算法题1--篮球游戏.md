# 华为od面试算法题1--篮球游戏

### 题目描述

幼儿园里有一个放倒的圆桶，它是一个线性结构，允许在桶的右边将篮球放入，可以在桶的左边和右边将篮球取出。每个篮球有单独的编号，老而可以连续放入一个或多个篮球，小朋友可以在桶左边或右边将篮球取出，当桶里只有一个篮球的情况下，必须从左边取出。

如老师按顺序放入1、2、3、4、5 共5个编号的篮球，那么小朋友可以依次取出的编号为1、2、3、4、5或者3、1、2、4、5编号的篮球，无法取出5、1、3、2、4编号的篮球

其中3、1、2、4、5的取出场景为: 连续放入1、2、3号 -> 从右边取出3号 -> 从左边取出1号 -> 从左边取出2号 -> 放入4号 -> 从左边取出4号 -> 放入5号>从左边取出5号，简单起见，我们以L表示左，R表示右，此时的篮球的依次取出序列为"RLLLL"。

### 输入描述

每次输入包含一个测试用例:

1、第一行的数字作为老师依次放入的篮球编号

2、第二行的数字作为要检查是否能够按照放入顺序取出的篮球编号

其中篮球编号用逗号进行分隔。

### 输出描述

对于每个篮球的取出序列，如果确实可以获取，请打印出其按照左右方向的操作的取出顺序，如果无法获取则打印`"NO"`

### 示例

#### 输入

```
4,5,6,7,0,1,2
6,4,0,1,2,5,7
```

#### 输出

```
RLRRRLL
```

### 解题思路

使用模拟的方法来解决。首先，需要将放入篮球的顺序和要检查的篮球取出顺序分别存入两个双端队列中。然后，模拟放入篮球的过程，并根据要检查的篮球取出顺序依次从左边或右边取出篮球。具体步骤如下：

1. 读取输入的放入篮球顺序和要检查的篮球取出顺序，分别存入两个双端队列中。
2. 使用一个双端队列模拟放入篮球的过程。遍历放入篮球的顺序，依次将篮球放入队列中。
3. 在放入篮球的过程中，检查是否可以按照给定的篮球取出顺序取出篮球。如果可以，则从左边或右边取出篮球，并记录取出操作。
4. 最终，如果成功按照给定的篮球取出顺序取出所有篮球，则输出取出顺序；否则输出"NO"。

这种方法的时间复杂度为O(N)，其中N为放入篮球的数量。因为在每次放入篮球或取出篮球时，都只需常数时间操作。

### 参考代码

#### C++

```
#include <iostream>
#include <deque>
#include <sstream>
#include <string>

using namespace std;

int main() {
    // 读取输入的放入篮球顺序和要检查的篮球取出顺序
    string pushInput, popInput;
    getline(cin, pushInput);
    getline(cin, popInput);

    // 将输入的放入篮球顺序和要检查的篮球取出顺序分别存入双端队列
    stringstream pushStream(pushInput);
    stringstream popStream(popInput);

    deque<int> pushList;
    deque<int> popList;

    string token;
    while (getline(pushStream, token, ',')) {
        pushList.push_back(stoi(token));
    }

    while (getline(popStream, token, ',')) {
        popList.push_back(stoi(token));
    }

    // 用于模拟放入和取出篮球的过程的双端队列
    deque<int> bucket;
    // 用于记录篮球的取出顺序
    string output;

    int i = 0;
    // 模拟放入篮球的过程
    for (int pushNum : pushList) {
        bucket.push_back(pushNum);

        // 检查是否可以按照给定的篮球取出顺序取出篮球
        while (!bucket.empty()) {
            if (bucket.front() == popList[i]) {
                // 从左边取出篮球
                bucket.pop_front();
                i++;
                output += "L";
            }
            else if (!bucket.empty() && bucket.back() == popList[i]) {
                // 从右边取出篮球
                bucket.pop_back();
                i++;
                output += "R";
            }
            else {
                // 无法按照给定的篮球取出顺序取出篮球，退出循环
                break;
            }
        }
    }

    // 如果成功按照给定的篮球取出顺序取出所有篮球，则输出取出顺序，否则输出"NO"
    if (output.length() == pushList.size()) {
        cout << output << endl;
    }
    else {
        cout << "NO" << endl;
    }

    return 0;
}
```

#### Java

```
import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 从标准输入读取放入篮球的顺序和要检查的篮球取出顺序
        Scanner scanner = new Scanner(System.in);
        String[] pushInput = scanner.nextLine().split(",");
        String[] popInput = scanner.nextLine().split(",");
        scanner.close();

        // 使用双端队列存放放入篮球的顺序和要检查的篮球取出顺序
        ArrayDeque<Integer> pushList = new ArrayDeque<>();
        ArrayDeque<Integer> popList = new ArrayDeque<>();

        // 将放入篮球的顺序和要检查的篮球取出顺序分别存入对应的双端队列中
        for (String s : pushInput) {
            pushList.add(Integer.parseInt(s));
        }

        for (String s : popInput) {
            popList.add(Integer.parseInt(s));
        }

        // 用于模拟篮球桶
        ArrayDeque<Integer> bucket = new ArrayDeque<>();
        // 用于存放取出操作的序列
        StringBuilder output = new StringBuilder();

        // 依次按照放入篮球的顺序模拟放入和取出篮球的过程
        for (int pushNum : pushList) {
            bucket.add(pushNum);
            while (!bucket.isEmpty()) {
                // 如果桶顶的篮球编号和要检查的篮球取出顺序的第一个篮球编号相同，从桶顶取出篮球
                if (bucket.peek().equals(popList.peek())) {
                    bucket.poll();
                    popList.poll();
                    output.append("L"); // 记录取出操作为L（左边）
                } else if (!bucket.isEmpty() && bucket.peekLast().equals(popList.peek())) {
                    // 如果桶底的篮球编号和要检查的篮球取出顺序的第一个篮球编号相同，从桶底取出篮球
                    bucket.pollLast();
                    popList.poll();
                    output.append("R"); // 记录取出操作为R（右边）
                } else {
                    break;
                }
            }
        }

        // 判断是否能够按照放入顺序取出篮球，并输出结果
        if (output.length() == pushList.size() + popList.size()) {
            System.out.println(output);
        } else {
            System.out.println("NO");
        }
    }
}
```

