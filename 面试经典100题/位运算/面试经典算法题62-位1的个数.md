# 面试经典算法题62-位1的个数

LeetCode.191

### 问题描述

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中 设置位 的个数（也被称为[汉明重量](https://baike.baidu.com/item/汉明重量)）。

**示例 1：**

```
输入：n = 11
输出：3
解释：输入的二进制串 1011 中，共有 3 个设置位。
```

**示例 2：**

```
输入：n = 128
输出：1
解释：输入的二进制串 10000000 中，共有 1 个设置位。
```

**示例 3：**

```
输入：n = 2147483645
输出：30
解释：输入的二进制串 11111111111111111111111111111101 中，共有 30 个设置位。
```

### 思路

1. 初始化计数器：设置一个计数器来记录1的个数。
2. 循环检查每一位：在每一轮循环中，将整数与1按位与运算，检查最低位是否为1。如果是，则计数器加1。
3. 右移整数：将整数右移一位，重复步骤2，直到整数为0。
4. 返回计数器：最后返回计数器的值，即为二进制中1的个数。

### 参考代码

#### C++

```
#include <iostream>
using namespace std;

// 计算二进制表达式中1的个数
int hammingWeight(uint32_t n) {
    int count = 0; // 初始化计数器
    while (n != 0) { // 当n不为0时循环
        if (n & 1) { // 检查最低位是否为1
            count++; // 计数器加1
        }
        n >>= 1; // 右移整数一位
    }
    return count; // 返回计数器的值
}

int main() {
    // 示例1
    uint32_t n1 = 11; // 二进制: 1011
    cout << "输入：" << n1 << endl;
    cout << "输出：" << hammingWeight(n1) << endl; // 输出：3

    // 示例2
    uint32_t n2 = 128; // 二进制: 10000000
    cout << "输入：" << n2 << endl;
    cout << "输出：" << hammingWeight(n2) << endl; // 输出：1

    // 示例3
    uint32_t n3 = 2147483645; // 二进制: 11111111111111111111111111111101
    cout << "输入：" << n3 << endl;
    cout << "输出：" << hammingWeight(n3) << endl; // 输出：30

    return 0;
}
```

#### Java

```
public class HammingWeight {
    // 计算二进制表达式中1的个数
    public static int hammingWeight(int n) {
        int count = 0; // 初始化计数器
        while (n != 0) { // 当n不为0时循环
            if ((n & 1) == 1) { // 检查最低位是否为1
                count++; // 计数器加1
            }
            n = n >>> 1; // 无符号右移一位
        }
        return count; // 返回计数器的值
    }

    public static void main(String[] args) {
        // 示例1
        int n1 = 11; // 二进制: 1011
        System.out.println("输入：" + n1);
        System.out.println("输出：" + hammingWeight(n1)); // 输出：3

        // 示例2
        int n2 = 128; // 二进制: 10000000
        System.out.println("输入：" + n2);
        System.out.println("输出：" + hammingWeight(n2)); // 输出：1

        // 示例3
        int n3 = 2147483645; // 二进制: 11111111111111111111111111111101
        System.out.println("输入：" + n3);
        System.out.println("输出：" + hammingWeight(n3)); // 输出：30
    }
}
```

#### Python

```
def hamming_weight(n: int) -> int:
    count = 0  # 初始化计数器，用于记录1的个数
    while n != 0:  # 当n不为0时循环
        count += n & 1  # 检查最低位是否为1，如果是，计数器加1
        n = n >> 1  # 将n右移一位，检查下一位
    return count  # 返回计数器的值

if __name__ == "__main__":
    # 示例1
    n1 = 11  # 二进制: 1011
    print("输入：", n1)
    print("输出：", hamming_weight(n1))  # 输出：3

    # 示例2
    n2 = 128  # 二进制: 10000000
    print("输入：", n2)
    print("输出：", hamming_weight(n2))  # 输出：1

    # 示例3
    n3 = 2147483645  # 二进制: 11111111111111111111111111111101
    print("输入：", n3)
    print("输出：", hamming_weight(n3))  # 输出：30
```

