# 面试经典算法题48-串联所有单词的子串

LeetCode.30

### 问题描述

给定一个字符串 `s` 和一个字符串数组 `words`**。** `words` 中所有字符串 **长度相同**。

 `s` 中的 **串联子串** 是指一个包含 `words` 中所有字符串以任意顺序排列连接起来的子串。

- 例如，如果 `words = ["ab","cd","ef"]`， 那么 `"abcdef"`， `"abefcd"`，`"cdabef"`， `"cdefab"`，`"efabcd"`， 和 `"efcdab"` 都是串联子串。 `"acdbef"` 不是串联子串，因为他不是任何 `words` 排列的连接。

返回所有串联子串在 `s` 中的开始索引。你可以以 **任意顺序** 返回答案。

**示例 1：**

```
输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
输出顺序无关紧要。返回 [9,0] 也是可以的。
```

**示例 2：**

```
输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
所以我们返回一个空数组。
```

**示例 3：**

```
输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
```

### 思路

1. 初始化：定义一个 `std::unordered_map<std::string, int>`，用于存储 `words` 中每个单词及其出现次数。
2. 遍历起始位置：遍历 `words` 中的每个单词的起始位置，因为任意一个位置开始都有可能是一个子串的起始位置，所以从 `0` 到 `wordLength-1` 开始遍历。
3. 滑动窗口：在每个起始位置开始，使用滑动窗口来扫描 s：
   - 初始化窗口的左右边界 `left` 和 `right` 为当前起始位置 `i`。
   - 在窗口中，以 `wordLength` 为步长向右移动 `right` 指针，并截取出一个单词 `word`。
   - 如果 `word` 不在 `wordMap` 中，说明当前子串不是有效的串联子串，重置窗口位置和 `windowMap`。
   - 如果 `word` 在 `wordMap` 中，则将其加入到 `windowMap` 中，并增加计数 `count`。
   - 检查窗口中的 `word` 是否超出了 `wordMap` 中对应的单词数量，如果超出，需要移动 `left` 指针，并调整 `windowMap` 和 `count`。
   - 当 `count` 达到 `wordCount` 时，表示找到一个符合条件的串联子串，将其起始位置 `left` 加入到结果中。
4. 返回结果：返回所有符合条件的起始位置。

### 图解

![流程图](https://cdn.jsdelivr.net/gh/aqjsp/Pictures/202405112319814.png)

### 参考代码

#### C++

```
#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> findSubstring(std::string s, std::vector<std::string>& words) {
    std::vector<int> result;
    if (s.empty() || words.empty()) {
        return result;
    }

    int wordLength = words[0].size();   // 单词长度
    int wordCount = words.size();       // 单词个数
    int totalLength = wordLength * wordCount; // 总长度

    std::unordered_map<std::string, int> wordMap; // 存储每个单词及其出现次数
    for (const std::string& word : words) {
        wordMap[word]++;
    }

    // 从每个可能的起始位置开始遍历
    for (int i = 0; i < wordLength; ++i) {
        int left = i;   // 窗口左边界
        int right = i;  // 窗口右边界
        std::unordered_map<std::string, int> windowMap; // 窗口中的单词及其出现次数
        int count = 0;  // 窗口中已经包含的单词个数

        // 在窗口右边界未超出字符串长度时继续扩展窗口
        while (right + wordLength <= s.size()) {
            std::string word = s.substr(right, wordLength); // 获取窗口右边界的单词
            right += wordLength; // 右边界移动一个单词的长度

            // 如果当前单词不在给定单词列表中，重置窗口位置和窗口内的单词统计
            if (wordMap.find(word) == wordMap.end()) {
                left = right;
                windowMap.clear();
                count = 0;
            } else {
                // 更新窗口内单词的统计信息
                windowMap[word]++;
                count++;

                // 如果窗口内某个单词数量超过了给定单词列表中的数量，缩小窗口
                while (windowMap[word] > wordMap[word]) {
                    std::string leftWord = s.substr(left, wordLength); // 获取窗口左边界的单词
                    left += wordLength; // 左边界移动一个单词的长度
                    windowMap[leftWord]--; // 更新窗口内单词的统计信息
                    count--; // 更新窗口内的单词个数
                }

                // 如果窗口内包含了所有给定单词，将窗口左边界加入结果中
                if (count == wordCount) {
                    result.push_back(left);
                }
            }
        }
    }

    return result;
}

int main() {
    std::string s = "barfoothefoobarman";
    std::vector<std::string> words = {"foo", "bar"};
    std::vector<int> result = findSubstring(s, words);

    std::cout << "起始索引：";
    for (int idx : result) {
        std::cout << idx << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

#### Java

```
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SubstringWithConcatenationOfAllWords {

    public static List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return result;
        }

        int wordLength = words[0].length();
        int wordCount = words.length;
        int totalLength = wordLength * wordCount;

        Map<String, Integer> wordMap = new HashMap<>();
        for (String word : words) {
            wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
        }

        for (int i = 0; i < wordLength; ++i) {
            int left = i;
            int right = i;
            Map<String, Integer> windowMap = new HashMap<>();
            int count = 0;

            while (right + wordLength <= s.length()) {
                String word = s.substring(right, right + wordLength);
                right += wordLength;

                if (!wordMap.containsKey(word)) {
                    left = right;
                    windowMap.clear();
                    count = 0;
                } else {
                    windowMap.put(word, windowMap.getOrDefault(word, 0) + 1);
                    count++;

                    while (windowMap.getOrDefault(word, 0) > wordMap.getOrDefault(word, 0)) {
                        String leftWord = s.substring(left, left + wordLength);
                        left += wordLength;
                        windowMap.put(leftWord, windowMap.getOrDefault(leftWord, 0) - 1);
                        count--;
                    }

                    if (count == wordCount) {
                        result.add(left);
                    }
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        String s = "barfoothefoobarman";
        String[] words = {"foo", "bar"};
        List<Integer> result = findSubstring(s, words);

        System.out.print("起始索引：");
        for (int idx : result) {
            System.out.print(idx + " ");
        }
        System.out.println();
    }
}
```

#### Python

```
from typing import List
from collections import defaultdict

def findSubstring(s: str, words: List[str]) -> List[int]:
    result = []
    if not s or not words:
        return result

    word_length = len(words[0])
    word_count = len(words)
    total_length = word_length * word_count

    word_map = defaultdict(int)
    for word in words:
        word_map[word] += 1

    for i in range(word_length):
        left = i
        right = i
        window_map = defaultdict(int)
        count = 0

        while right + word_length <= len(s):
            word = s[right:right + word_length]
            right += word_length

            if word not in word_map:
                left = right
                window_map.clear()
                count = 0
            else:
                window_map[word] += 1
                count += 1

                while window_map[word] > word_map[word]:
                    left_word = s[left:left + word_length]
                    left += word_length
                    window_map[left_word] -= 1
                    count -= 1

                if count == word_count:
                    result.append(left)

    return result

# 测试代码
s = "barfoothefoobarman"
words = ["foo", "bar"]
result = findSubstring(s, words)
print("起始索引:", result)
```

