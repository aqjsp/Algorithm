# 面试经典算法15-LRU缓存

LeetCode.146

### 问题描述

请你设计并实现一个满足 [LRU (最近最少使用) 缓存](https://baike.baidu.com/item/LRU) 约束的数据结构。

实现 `LRUCache` 类：

- `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存
- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。
- `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity` ，则应该 **逐出** 最久未使用的关键字。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

**示例：**

```
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
```

**提示：**

- `1 <= capacity <= 3000`
- `0 <= key <= 10000`
- `0 <= value <= 105`
- 最多调用 `2 * 105` 次 `get` 和 `put`

### 思路

1. 定义双向链表节点结构体`DLinkedNode`，包含`key`、`value`、`pre`（前驱指针）和`next`（后继指针）四个成员变量。
2. 定义LRUCache类，私有成员变量包括一个哈希表`cache`（用于存储key到节点的映射）、头指针`head`（指向双向链表的头部哨兵节点）、尾指针`tail`（指向双向链表的尾部哨兵节点）、当前缓存节点数量`size`和缓存容量`capacity`。
3. LRUCache构造函数初始化容量`capacity`和`size`为0，创建头部和尾部哨兵节点，并连接头尾节点。
4. `get`方法先判断key是否存在于哈希表中，如果不存在则返回-1；如果存在，则从哈希表中获取对应节点，并将该节点移动至双向链表头部，最后返回节点的值。
5. `put`方法先判断key是否存在于哈希表中，如果不存在则创建一个新节点，并将节点添加至双向链表头部，更新哈希表映射，并判断缓存是否超过容量，如果超过则删除双向链表尾部节点和哈希表映射；如果存在则更新节点值，并将节点移动至双向链表头部。
6. 私有方法`addToHead`用于将节点添加至双向链表头部，`removeNode`用于移除指定节点，`moveToHead`用于将指定节点移动至双向链表头部，`removeTail`用于移除双向链表尾部节点并返回该节点。

### 图解

> [146. LRU 缓存 - 力扣（LeetCode）](https://leetcode.cn/problems/lru-cache/solutions/259678/lruhuan-cun-ji-zhi-by-leetcode-solution/?envType=study-plan-v2&envId=top-interview-150)

今天我就不给大家画这个了，我把官方的一个图解放到这儿，画得非常好，大家可以参考代码看看图解，自己加深理解一下。

### 参考代码

#### C++

```
#include <iostream>
#include <unordered_map>

using namespace std;

// 双向链表节点
struct DLinkedNode {
    int key, value;
    DLinkedNode* pre;
    DLinkedNode* next;
    DLinkedNode(): key(0), value(0), pre(nullptr), next(nullptr) {}
    DLinkedNode(int _key, int _value): key(_key), value(_value), pre(nullptr), next(nullptr) {}
};

class LRUCache {
private:
    unordered_map<int, DLinkedNode*> cache; // 哈希表，存储key到节点的映射
    DLinkedNode* head; // 头指针，指向双向链表的头部哨兵节点
    DLinkedNode* tail; // 尾指针，指向双向链表的尾部哨兵节点
    int size; // 当前缓存的节点数量
    int capacity; // 缓存的容量

public:
    // 构造函数，初始化LRU缓存
    LRUCache(int _capacity): capacity(_capacity), size(0) {
        head = new DLinkedNode(); // 创建头部哨兵节点
        tail = new DLinkedNode(); // 创建尾部哨兵节点
        head->next = tail; // 头部哨兵节点的next指针指向尾部哨兵节点
        tail->pre = head; // 尾部哨兵节点的pre指针指向头部哨兵节点
    }

    // 获取缓存中指定key的值，如果不存在则返回-1
    int get(int key) {
        if (!cache.count(key)) {
            return -1; // 如果key不存在，返回-1
        }
        // 如果key存在，先通过哈希表定位，再移到头部
        DLinkedNode* node = cache[key];
        moveToHead(node); // 将节点移动到双向链表头部
        return node->value; // 返回节点的值
    }

    // 向缓存中插入或更新指定key的值
    void put(int key, int value) {
        if (!cache.count(key)) {
            // 如果key不存在，创建一个新的节点
            DLinkedNode* node = new DLinkedNode(key, value);
            // 添加哈希表映射
            cache[key] = node;
            // 添加至双向链表的头部
            addToHead(node);
            ++size;
            if (size > capacity) {
                // 如果超出容量，删除双向链表的尾部节点
                DLinkedNode* removed = removeTail();
                // 删除哈希表中对应的项
                cache.erase(removed->key);
                // 防止内存泄露，释放删除的节点内存
                delete removed;
                --size;
            }
        } else {
            // 如果key存在，先通过哈希表定位，再修改value，并移动到头部
            DLinkedNode* node = cache[key];
            node->value = value;
            moveToHead(node); // 将节点移动到双向链表头部
        }
    }

private:
    // 将节点添加至双向链表头部
    void addToHead(DLinkedNode* node) {
        node->pre = head;
        node->next = head->next;
        head->next->pre = node;
        head->next = node;
    }

    // 移除指定节点
    void removeNode(DLinkedNode* node) {
        node->pre->next = node->next;
        node->next->pre = node->pre;
    }

    // 将指定节点移动至双向链表头部
    void moveToHead(DLinkedNode* node) {
        removeNode(node);
        addToHead(node);
    }

    // 移除双向链表尾部节点，并返回该节点
    DLinkedNode* removeTail() {
        DLinkedNode* node = tail->pre;
        removeNode(node);
        return node;
    }
};

int main() {
    LRUCache cache(2); // 创建容量为2的LRU缓存
    cache.put(1, 1); // 缓存中：(1,1)
    cache.put(2, 2); // 缓存中：(2,2) -> (1,1)
    cout << cache.get(1) << endl; // 输出：1，缓存中：(1,1) -> (2,2)
    cache.put(3, 3); // 缓存中：(3,3) -> (1,1)
    cout << cache.get(2) << endl; // 输出：-1，未找到key=2
    cache.put(4, 4); // 缓存中：(4,4) -> (3,3)
    cout << cache.get(1) << endl; // 输出：1，缓存中：(1,1) -> (4,4)
    cout << cache.get(3) << endl; // 输出：3，缓存中：(3,3) -> (1,1)
    cout << cache.get(4) << endl; // 输出：4，缓存中：(4,4) -> (3,3)
    return 0;
}
```

#### Java

```
import java.util.*;

class LRUCache {
    private int capacity;
    private Map<Integer, Node> cache;
    private Node head;
    private Node tail;

    // 定义双向链表节点
    private class Node {
        int key;
        int value;
        Node prev;
        Node next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    // 初始化LRU Cache
    public LRUCache(int capacity) {
        this.capacity = capacity;
        cache = new HashMap<>();
        head = new Node(-1, -1); // 哨兵节点，不存储数据
        tail = new Node(-1, -1); // 哨兵节点，不存储数据
        head.next = tail;
        tail.prev = head;
    }

    // 获取key对应的value，并将节点移到链表头部
    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        Node node = cache.get(key);
        moveToHead(node);
        return node.value;
    }

    // 存入key-value键值对，如果key已存在则更新value，并将节点移到链表头部；否则插入新节点，并移除最近最少使用的节点
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            node.value = value;
            moveToHead(node);
        } else {
            Node newNode = new Node(key, value);
            cache.put(key, newNode);
            addToHead(newNode);
            if (cache.size() > capacity) {
                Node tailNode = removeTail();
                cache.remove(tailNode.key);
            }
        }
    }

    // 将节点添加到链表头部
    private void addToHead(Node node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }

    // 移除节点
    private void removeNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    // 将节点移到链表头部
    private void moveToHead(Node node) {
        removeNode(node);
        addToHead(node);
    }

    // 移除链表尾部节点
    private Node removeTail() {
        Node tailNode = tail.prev;
        removeNode(tailNode);
        return tailNode;
    }

    public static void main(String[] args) {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        System.out.println(cache.get(1)); // 返回 1
        cache.put(3, 3); // 该操作会使得关键字 2 作废
        System.out.println(cache.get(2)); // 返回 -1 (未找到)
        cache.put(4, 4); // 该操作会使得关键字 1 作废
        System.out.println(cache.get(1)); // 返回 -1 (未找到)
        System.out.println(cache.get(3)); // 返回 3
        System.out.println(cache.get(4)); // 返回 4
    }
}
```

#### Python

```
class LRUCache:

    def __init__(self, capacity: int):
        # 初始化LRU Cache
        self.capacity = capacity  # 缓存容量
        self.cache = {}  # 存储缓存数据的字典
        self.head = Node(-1, -1)  # 头部哨兵节点
        self.tail = Node(-1, -1)  # 尾部哨兵节点
        self.head.next = self.tail  # 头部哨兵节点指向尾部哨兵节点
        self.tail.prev = self.head  # 尾部哨兵节点指向头部哨兵节点

    def get(self, key: int) -> int:
        # 获取缓存中的值
        if key not in self.cache:
            return -1  # 如果key不存在，返回-1
        node = self.cache[key]  # 获取对应的节点
        self.move_to_head(node)  # 将该节点移动到链表头部
        return node.value  # 返回节点的值

    def put(self, key: int, value: int) -> None:
        # 向缓存中存入值
        if key in self.cache:
            node = self.cache[key]  # 如果key已存在，获取对应的节点
            node.value = value  # 更新节点的值
            self.move_to_head(node)  # 将节点移动到链表头部
        else:
            if len(self.cache) >= self.capacity:
                tail_key = self.remove_tail()  # 如果缓存已满，移除尾部节点
                del self.cache[tail_key]  # 从缓存中删除对应的键
            new_node = Node(key, value)  # 创建新节点
            self.cache[key] = new_node  # 将新节点添加到缓存中
            self.add_to_head(new_node)  # 将新节点添加到链表头部

    def add_to_head(self, node):
        # 将节点添加到链表头部
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        # 移除指定节点
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        # 将节点移动到链表头部
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self):
        # 移除尾部节点并返回其对应的key
        tail_key = self.tail.prev.key
        self.remove_node(self.tail.prev)
        return tail_key

class Node:
    # 节点类
    def __init__(self, key, value):
        self.key = key  # 节点的键
        self.value = value  # 节点的值
        self.prev = None  # 前驱节点
        self.next = None  # 后继节点

# 测试
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 返回 1
cache.put(3, 3)  # 该操作会使得关键字 2 作废
print(cache.get(2))  # 返回 -1 (未找到)
cache.put(4, 4)  # 该操作会使得关键字 1 作废
print(cache.get(1))  # 返回 -1 (未找到)
print(cache.get(3))  # 返回 3
print(cache.get(4))  # 返回 4
```

