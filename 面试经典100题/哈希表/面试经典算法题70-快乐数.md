# 面试经典算法题70-快乐数

LeetCode.202

### 问题描述

编写一个算法来判断一个数 `n` 是不是快乐数。

**「快乐数」** 定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
- 然后重复这个过程直到这个数变为 1，也可能是 **无限循环** 但始终变不到 1。
- 如果这个过程 **结果为** 1，那么这个数就是快乐数。

如果 `n` 是 *快乐数* 就返回 `true` ；不是，则返回 `false` 。

**示例 1：**

```
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

**示例 2：**

```
输入：n = 2
输出：false
```

### 思路

1. 计算数位平方和：定义一个函数 `digitSquareSum`，计算给定数字各位上的平方和。
2. 使用快慢指针检测循环：类似于链表中检测环的算法，使用快慢指针（`slow` 和 `fast`）来检测是否存在循环。
3. 判断是否为快乐数：如果在过程中 `fast` 指针变为1，则说明是快乐数；如果 `slow` 和 `fast` 指针相遇且不为1，则说明存在循环，不是快乐数。

### 参考代码

#### C++

```
#include <iostream>
#include <unordered_set>

// 计算一个数各位数字的平方和
int digitSquareSum(int n) {
    int sum = 0;
    while (n) {
        int digit = n % 10;
        sum += digit * digit;
        n /= 10;
    }
    return sum;
}

// 判断一个数是否为快乐数
bool isHappy(int n) {
    int slow = n;
    int fast = digitSquareSum(n);
    
    while (fast != 1 && slow != fast) {
        slow = digitSquareSum(slow);  // 慢指针每次移动一步
        fast = digitSquareSum(digitSquareSum(fast));  // 快指针每次移动两步
    }
    
    return fast == 1;
}

int main() {
    int n;
    std::cout << "输入一个正整数: ";
    std::cin >> n;
    
    if (isHappy(n)) {
        std::cout << n << " 是一个快乐数。" << std::endl;
    } else {
        std::cout << n << " 不是一个快乐数。" << std::endl;
    }
    
    return 0;
}
```

#### Java

```
import java.util.HashSet;
import java.util.Set;

public class HappyNumber {
    
    // 计算一个数各位数字的平方和
    public static int digitSquareSum(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
    
    // 判断一个数是否为快乐数
    public static boolean isHappy(int n) {
        int slow = n;
        int fast = digitSquareSum(n);
        
        while (fast != 1 && slow != fast) {
            slow = digitSquareSum(slow);  // 慢指针每次移动一步
            fast = digitSquareSum(digitSquareSum(fast));  // 快指针每次移动两步
        }
        
        return fast == 1;
    }
    
    public static void main(String[] args) {
        int n = 19;
        System.out.println(isHappy(n));  // 输出: true
    }
}
```

#### Python

```
def digit_square_sum(n):
    """计算一个数各位数字的平方和"""
    sum_ = 0
    while n > 0:
        digit = n % 10
        sum_ += digit * digit
        n //= 10
    return sum_

def is_happy(n):
    """判断一个数是否为快乐数"""
    slow = n
    fast = digit_square_sum(n)
    
    while fast != 1 and slow != fast:
        slow = digit_square_sum(slow)  # 慢指针每次移动一步
        fast = digit_square_sum(digit_square_sum(fast))  # 快指针每次移动两步
    
    return fast == 1

# 示例测试
n = 19
print(is_happy(n))  # 输出: True
```

