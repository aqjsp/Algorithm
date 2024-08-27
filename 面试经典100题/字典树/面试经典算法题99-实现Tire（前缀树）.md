# 面试经典算法题99-实现Tire（前缀树）

LeetCode.208

### 问题描述

**[Trie](https://baike.baidu.com/item/字典树/9825209?fr=aladdin)**（发音类似 "try"）或者说 **前缀树** 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

- `Trie()` 初始化前缀树对象。
- `void insert(String word)` 向前缀树中插入字符串 `word` 。
- `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；否则，返回 `false` 。
- `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。

**示例：**

```
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
```

### 思路

1. 数据结构定义：字典树（Trie）是一种用于高效存储和检索字符串的数据结构，特别适用于自动补全和拼写检查等应用。Trie 由节点（Node）组成，每个节点代表一个字符，每个节点有一个指向子节点的指针数组（或哈希表），这些子节点表示可能的下一个字符。

2. 插入操作（insert）：

   - 从根节点开始，逐字符插入单词。

   - 对于单词中的每一个字符，检查当前节点是否有对应的子节点。

   - 如果没有，则创建一个新的节点并插入。

   - 如果有，则移动到下一个子节点。

   - 插入结束时，标记最后一个节点为一个单词的结束节点。

3. 查找操作（search）：

   - 从根节点开始，逐字符搜索单词。

   - 如果在搜索过程中某个字符没有对应的子节点，返回 `false`。

   - 如果成功到达最后一个字符，检查该节点是否是一个单词的结束节点。

4. 前缀查找操作（startsWith）：

   - 从根节点开始，逐字符搜索前缀。

   - 如果在搜索过程中某个字符没有对应的子节点，返回 `false`。

   - 如果成功到达最后一个字符，返回 `true`，因为此时所有路径均为给定前缀的扩展。

### 参考代码

#### C++

```
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

// 定义 TrieNode 类表示字典树中的节点
class TrieNode {
public:
    unordered_map<char, TrieNode*> children; // 子节点映射表
    bool isEndOfWord; // 标识是否是一个完整单词的结尾

    TrieNode() {
        isEndOfWord = false; // 初始化时，节点不是单词的结尾
    }
};

// 定义 Trie 类表示字典树
class Trie {
private:
    TrieNode* root; // 根节点

public:
    // 初始化 Trie
    Trie() {
        root = new TrieNode();
    }

    // 向 Trie 中插入一个单词
    void insert(string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (node->children.find(ch) == node->children.end()) {
                node->children[ch] = new TrieNode(); // 如果没有子节点则创建
            }
            node = node->children[ch]; // 移动到子节点
        }
        node->isEndOfWord = true; // 单词插入完成，标记结尾节点
    }

    // 检查 Trie 中是否存在指定单词
    bool search(string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (node->children.find(ch) == node->children.end()) {
                return false; // 如果某个字符没有对应的子节点，返回 false
            }
            node = node->children[ch]; // 移动到下一个子节点
        }
        return node->isEndOfWord; // 返回是否到达单词结尾
    }

    // 检查 Trie 中是否存在指定前缀
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char ch : prefix) {
            if (node->children.find(ch) == node->children.end()) {
                return false; // 如果某个字符没有对应的子节点，返回 false
            }
            node = node->children[ch]; // 移动到下一个子节点
        }
        return true; // 成功遍历前缀
    }
};

// 测试 Trie 功能
int main() {
    Trie trie;

    trie.insert("apple");
    cout << boolalpha; // 输出布尔值的文字表示（true/false）
    cout << "search(\"apple\"): " << trie.search("apple") << endl;   // 输出: true
    cout << "search(\"app\"): " << trie.search("app") << endl;       // 输出: false
    cout << "startsWith(\"app\"): " << trie.startsWith("app") << endl; // 输出: true

    trie.insert("app");
    cout << "search(\"app\"): " << trie.search("app") << endl;       // 输出: true

    return 0;
}
```

#### Java

```
import java.util.HashMap;
import java.util.Map;

// 定义 TrieNode 类表示字典树的节点
class TrieNode {
    Map<Character, TrieNode> children; // 子节点映射表
    boolean isEndOfWord; // 标识是否是一个完整单词的结尾

    // 构造函数初始化 TrieNode
    public TrieNode() {
        children = new HashMap<>(); // 使用 HashMap 存储子节点
        isEndOfWord = false; // 初始化时，不是单词的结尾
    }
}

// 定义 Trie 类表示字典树
public class Trie {
    private final TrieNode root; // 根节点

    // 构造函数初始化 Trie
    public Trie() {
        root = new TrieNode();
    }

    // 向 Trie 中插入一个单词
    public void insert(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            // 如果当前字符的子节点不存在，则创建一个新的节点
            if (!node.children.containsKey(ch)) {
                node.children.put(ch, new TrieNode());
            }
            // 移动到子节点
            node = node.children.get(ch);
        }
        // 单词插入完成，标记结尾节点
        node.isEndOfWord = true;
    }

    // 检查 Trie 中是否存在指定单词
    public boolean search(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            // 如果某个字符没有对应的子节点，返回 false
            if (!node.children.containsKey(ch)) {
                return false;
            }
            // 移动到下一个子节点
            node = node.children.get(ch);
        }
        // 返回是否到达单词结尾
        return node.isEndOfWord;
    }

    // 检查 Trie 中是否存在指定前缀
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (char ch : prefix.toCharArray()) {
            // 如果某个字符没有对应的子节点，返回 false
            if (!node.children.containsKey(ch)) {
                return false;
            }
            // 移动到下一个子节点
            node = node.children.get(ch);
        }
        // 成功遍历前缀，返回 true
        return true;
    }

    public static void main(String[] args) {
        Trie trie = new Trie();

        trie.insert("apple");
        System.out.println("search(\"apple\"): " + trie.search("apple")); // 输出: true
        System.out.println("search(\"app\"): " + trie.search("app"));     // 输出: false
        System.out.println("startsWith(\"app\"): " + trie.startsWith("app")); // 输出: true

        trie.insert("app");
        System.out.println("search(\"app\"): " + trie.search("app"));     // 输出: true
    }
}
```

#### Python

```
class TrieNode:
    def __init__(self):
        """
        初始化 TrieNode。每个节点包含一个字典 children 存储子节点，
        和一个布尔变量 is_end_of_word 表示是否是一个完整单词的结束。
        """
        self.children = {}  # 子节点字典，键为字符，值为 TrieNode
        self.is_end_of_word = False  # 是否是完整单词的结束

class Trie:
    def __init__(self):
        """
        初始化 Trie。根节点是一个空的 TrieNode。
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        向 Trie 中插入一个单词。
        """
        node = self.root
        for char in word:
            # 如果当前字符不存在于子节点中，则创建一个新的 TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            # 移动到子节点
            node = node.children[char]
        # 单词插入完成，标记结尾节点
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        检查 Trie 中是否存在指定单词。
        """
        node = self.root
        for char in word:
            # 如果某个字符没有对应的子节点，返回 False
            if char not in node.children:
                return False
            # 移动到下一个子节点
            node = node.children[char]
        # 返回是否到达单词结尾
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        检查 Trie 中是否存在指定前缀。
        """
        node = self.root
        for char in prefix:
            # 如果某个字符没有对应的子节点，返回 False
            if char not in node.children:
                return False
            # 移动到下一个子节点
            node = node.children[char]
        # 成功遍历前缀，返回 True
        return True


# 测试用例
trie = Trie()

trie.insert("apple")
print(trie.search("apple"))   # 输出: True
print(trie.search("app"))     # 输出: False
print(trie.starts_with("app")) # 输出: True

trie.insert("app")
print(trie.search("app"))     # 输出: True
```

