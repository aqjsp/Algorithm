# 面试经典算法题65-赎金信

LeetCode.383

### 问题描述

给你两个字符串：`ransomNote` 和 `magazine` ，判断 `ransomNote` 能不能由 `magazine` 里面的字符构成。

如果可以，返回 `true` ；否则返回 `false` 。

`magazine` 中的每个字符只能在 `ransomNote` 中使用一次。

**示例 1：**

```
输入：ransomNote = "a", magazine = "b"
输出：false
```

**示例 2：**

```
输入：ransomNote = "aa", magazine = "ab"
输出：false
```

**示例 3：**

```
输入：ransomNote = "aa", magazine = "aab"
输出：true
```

### 思路

1. **计数每个字符的出现次数**：使用两个哈希表（或数组），分别统计 `ransomNote` 和 `magazine` 中每个字符的出现次数。
2. **比较字符频次**：遍历 `ransomNote` 的字符频次表，检查每个字符在 `magazine` 中的出现次数是否足够。如果任一字符在 `magazine` 中的出现次数少于在 `ransomNote` 中的出现次数，则返回 `false`。
3. **返回结果**：如果所有字符在 `magazine` 中的出现次数都满足 `ransomNote` 的需求，则返回 `true`。

### 参考代码

#### C++

```
#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

bool canConstruct(string ransomNote, string magazine) {
    // 定义两个哈希表，用于存储 ransomNote 和 magazine 中每个字符的出现次数
    unordered_map<char, int> ransomCount;
    unordered_map<char, int> magazineCount;
    
    // 统计 ransomNote 中每个字符的出现次数
    for (char c : ransomNote) {
        ransomCount[c]++;
    }
    
    // 统计 magazine 中每个字符的出现次数
    for (char c : magazine) {
        magazineCount[c]++;
    }
    
    // 比较 ransomNote 中每个字符的出现次数是否在 magazine 中有足够的数量
    for (auto pair : ransomCount) {
        char c = pair.first;
        int count = pair.second;
        if (magazineCount[c] < count) {
            return false; // 如果某个字符在 magazine 中的数量不足，则返回 false
        }
    }
    
    return true; // 如果所有字符在 magazine 中的数量都满足需求，则返回 true
}

int main() {
    // 示例输入
    string ransomNote1 = "a";
    string magazine1 = "b";
    cout << "输入: ransomNote = \"a\", magazine = \"b\"" << endl;
    cout << "输出: " << (canConstruct(ransomNote1, magazine1) ? "true" : "false") << endl << endl;

    string ransomNote2 = "aa";
    string magazine2 = "ab";
    cout << "输入: ransomNote = \"aa\", magazine = \"ab\"" << endl;
    cout << "输出: " << (canConstruct(ransomNote2, magazine2) ? "true" : "false") << endl << endl;

    string ransomNote3 = "aa";
    string magazine3 = "aab";
    cout << "输入: ransomNote = \"aa\", magazine = \"aab\"" << endl;
    cout << "输出: " << (canConstruct(ransomNote3, magazine3) ? "true" : "false") << endl;

    return 0;
}
```

##### 输出

![输出](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202406240033703.png)

#### Java

```
import java.util.HashMap;
import java.util.Map;

public class RansomNote {
    public static boolean canConstruct(String ransomNote, String magazine) {
        // 定义两个哈希表，用于存储 ransomNote 和 magazine 中每个字符的出现次数
        Map<Character, Integer> ransomCount = new HashMap<>();
        Map<Character, Integer> magazineCount = new HashMap<>();
        
        // 统计 ransomNote 中每个字符的出现次数
        for (char c : ransomNote.toCharArray()) {
            ransomCount.put(c, ransomCount.getOrDefault(c, 0) + 1);
        }
        
        // 统计 magazine 中每个字符的出现次数
        for (char c : magazine.toCharArray()) {
            magazineCount.put(c, magazineCount.getOrDefault(c, 0) + 1);
        }
        
        // 比较 ransomNote 中每个字符的出现次数是否在 magazine 中有足够的数量
        for (Map.Entry<Character, Integer> entry : ransomCount.entrySet()) {
            char c = entry.getKey();
            int count = entry.getValue();
            if (magazineCount.getOrDefault(c, 0) < count) {
                return false; // 如果某个字符在 magazine 中的数量不足，则返回 false
            }
        }
        
        return true; // 如果所有字符在 magazine 中的数量都满足需求，则返回 true
    }

    public static void main(String[] args) {
        // 示例输入
        String ransomNote1 = "a";
        String magazine1 = "b";
        System.out.println("输入: ransomNote = \"a\", magazine = \"b\"");
        System.out.println("输出: " + canConstruct(ransomNote1, magazine1));
        
        String ransomNote2 = "aa";
        String magazine2 = "ab";
        System.out.println("输入: ransomNote = \"aa\", magazine = \"ab\"");
        System.out.println("输出: " + canConstruct(ransomNote2, magazine2));
        
        String ransomNote3 = "aa";
        String magazine3 = "aab";
        System.out.println("输入: ransomNote = \"aa\", magazine = \"aab\"");
        System.out.println("输出: " + canConstruct(ransomNote3, magazine3));
    }
}
```

#### Python

```
def canConstruct(ransomNote: str, magazine: str) -> bool:
    # 定义一个字典，用于存储 magazine 中每个字符的出现次数
    char_count = {}
    
    # 统计 magazine 中每个字符的出现次数
    for char in magazine:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # 检查 ransomNote 中的字符是否在 magazine 中有足够的数量
    for char in ransomNote:
        if char in char_count and char_count[char] > 0:
            char_count[char] -= 1
        else:
            return False  # 如果某个字符在 magazine 中的数量不足，则返回 False
    
    return True  # 如果所有字符在 magazine 中的数量都满足需求，则返回 True

# 示例输入和输出
ransomNote1 = "a"
magazine1 = "b"
print(f"输入: ransomNote = \"{ransomNote1}\", magazine = \"{magazine1}\"")
print(f"输出: {canConstruct(ransomNote1, magazine1)}")  # 输出: False

ransomNote2 = "aa"
magazine2 = "ab"
print(f"输入: ransomNote = \"{ransomNote2}\", magazine = \"{magazine2}\"")
print(f"输出: {canConstruct(ransomNote2, magazine2)}")  # 输出: False

ransomNote3 = "aa"
magazine3 = "aab"
print(f"输入: ransomNote = \"{ransomNote3}\", magazine = \"{magazine3}\"")
print(f"输出: {canConstruct(ransomNote3, magazine3)}")  # 输出: True
```

