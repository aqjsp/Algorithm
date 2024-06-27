# 面试经典算法题67-单词规律

LeetCode.290

### 问题描述

给定一种规律 `pattern` 和一个字符串 `s` ，判断 `s` 是否遵循相同的规律。

这里的 **遵循** 指完全匹配，例如， `pattern` 里的每个字母和字符串 `s` 中的每个非空单词之间存在着双向连接的对应规律。

**示例1:**

```
输入: pattern = "abba", s = "dog cat cat dog"
输出: true
```

**示例 2:**

```
输入:pattern = "abba", s = "dog cat cat fish"
输出: false
```

**示例 3:**

```
输入: pattern = "aaaa", s = "dog cat cat dog"
输出: false
```

### 思路

1. 字符串拆分：将字符串 `s` 按照空格拆分成单词列表 `words`。
2. 长度校验：检查 `pattern` 和 `words` 长度是否相同，如果不同，直接返回 `false`。
3. 映射关系：利用两个哈希表分别建立 `pattern` 字符和 `words` 单词之间的双向映射。
4. 逐一匹配：遍历 `pattern` 和 `words`，检查每个字符和单词是否符合已建立的映射关系，不符合则返回 `false`。
5. 完全匹配：遍历结束后，所有字符和单词都符合映射关系则返回 `true`。

### 参考代码

#### C++

```
#include <iostream>
#include <unordered_map>
#include <vector>
#include <sstream>

bool wordPattern(std::string pattern, std::string s) {
    // 将字符串 s 按空格拆分成单词列表
    std::vector<std::string> words;
    std::istringstream stream(s);
    std::string word;
    while (stream >> word) {
        words.push_back(word);
    }
    
    // 如果 pattern 和 words 长度不同，直接返回 false
    if (pattern.length() != words.size()) {
        return false;
    }
    
    // 建立字符和单词之间的映射关系
    std::unordered_map<char, std::string> charToWord;
    std::unordered_map<std::string, char> wordToChar;
    
    for (size_t i = 0; i < pattern.length(); ++i) {
        char c = pattern[i];
        std::string w = words[i];
        
        if (charToWord.count(c)) {
            if (charToWord[c] != w) {
                return false;
            }
        } else {
            charToWord[c] = w;
        }
        
        if (wordToChar.count(w)) {
            if (wordToChar[w] != c) {
                return false;
            }
        } else {
            wordToChar[w] = c;
        }
    }
    
    return true;
}

// 测试用例
int main() {
    std::string pattern1 = "abba", s1 = "dog cat cat dog";
    std::string pattern2 = "abba", s2 = "dog cat cat fish";
    std::string pattern3 = "aaaa", s3 = "dog cat cat dog";
    
    std::cout << wordPattern(pattern1, s1) << std::endl; // 输出: true
    std::cout << wordPattern(pattern2, s2) << std::endl; // 输出: false
    std::cout << wordPattern(pattern3, s3) << std::endl; // 输出: false
    
    return 0;
}
```

#### Java

```
import java.util.HashMap;

public class Solution {
    public boolean wordPattern(String pattern, String s) {
        // 将字符串 s 按空格拆分成单词列表
        String[] words = s.split(" ");
        
        // 如果 pattern 和 words 长度不同，直接返回 false
        if (pattern.length() != words.length) {
            return false;
        }
        
        // 建立字符和单词之间的映射关系
        HashMap<Character, String> charToWord = new HashMap<>();
        HashMap<String, Character> wordToChar = new HashMap<>();
        
        for (int i = 0; i < pattern.length(); ++i) {
            char c = pattern.charAt(i);
            String w = words[i];
            
            if (charToWord.containsKey(c)) {
                if (!charToWord.get(c).equals(w)) {
                    return false;
                }
            } else {
                charToWord.put(c, w);
            }
            
            if (wordToChar.containsKey(w)) {
                if (!wordToChar.get(w).equals(c)) {
                    return false;
                }
            } else {
                wordToChar.put(w, c);
            }
        }
        
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String pattern1 = "abba", s1 = "dog cat cat dog";
        String pattern2 = "abba", s2 = "dog cat cat fish";
        String pattern3 = "aaaa", s3 = "dog cat cat dog";
        
        System.out.println(solution.wordPattern(pattern1, s1)); // 输出: true
        System.out.println(solution.wordPattern(pattern2, s2)); // 输出: false
        System.out.println(solution.wordPattern(pattern3, s3)); // 输出: false
    }
}
```

#### Python

```
def word_pattern(pattern: str, s: str) -> bool:
    # 将字符串 s 按空格拆分成单词列表
    words = s.split()
    
    # 如果 pattern 和 words 长度不同，直接返回 false
    if len(pattern) != len(words):
        return False
    
    # 建立字符和单词之间的映射关系
    char_to_word = {}
    word_to_char = {}
    
    for c, w in zip(pattern, words):
        if c in char_to_word:
            if char_to_word[c] != w:
                return False
        else:
            char_to_word[c] = w
        
        if w in word_to_char:
            if word_to_char[w] != c:
                return False
        else:
            word_to_char[w] = c
    
    return True

# 示例测试
print(word_pattern("abba", "dog cat cat dog"))  # 输出: True
print(word_pattern("abba", "dog cat cat fish")) # 输出: False
print(word_pattern("aaaa", "dog cat cat dog"))  # 输出: False
```

