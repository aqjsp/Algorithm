# 字符串

## 1、字符串变形

### 1.1、问题描述

对于一个长度为 n 字符串，我们需要对它做一些变形。

首先这个字符串中包含着一些空格，就像"Hello World"一样，然后我们要做的是把这个字符串中由空格隔开的单词反序，同时反转每个字符的大小写。

比如"Hello World"变形后就变成了"wORLD hELLO"。

> 输入描述：
>
> 给定一个字符串s以及它的长度n(1 ≤ n ≤ 10^6)
>
> 返回值描述：
>
> 请返回变形后的字符串。题目保证给定的字符串均由大小写字母和空格构成。
>
> 示例1
>
> 输入："This is a sample",16
>
> 返回值："SAMPLE A IS tHIS"
>
> 示例2
>
> 输入："nowcoder",8
>
> 返回值："NOWCODER"
>
> 示例3
>
> 输入："iOS",3
>
> 返回值："Ios"

### 1.2、思路及代码

思路：

1. 分割字符串：将输入的字符串按空格分割成单词，得到一个单词数组。
2. 反序单词数组：将得到的单词数组反序排列，即颠倒数组中单词的顺序。
3. 反转每个单词的大小写：遍历每个单词，将其中的每个字符的大小写进行反转。
4. 输出结果：将处理后的单词数组连接成一个字符串，并输出。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

// 函数：分割字符串
vector<string> splitString(const string& input) {
    vector<string> result;
    istringstream iss(input);
    string word;

    while (iss >> word) {
        result.push_back(word);
    }

    return result;
}

// 函数：反转单词数组
void reverseWords(vector<string>& words) {
    int start = 0;
    int end = words.size() - 1;

    while (start < end) {
        swap(words[start], words[end]);
        start++;
        end--;
    }
}

// 函数：反转每个单词的大小写
void reverseCase(vector<string>& words) {
    for (string& word : words) {
        for (char& c : word) {
            if (isupper(c)) {
                c = tolower(c);
            } else if (islower(c)) {
                c = toupper(c);
            }
        }
    }
}

// 函数：输出结果
void printResult(const vector<string>& words) {
    for (const string& word : words) {
        cout << word << " ";
    }
    cout << endl;
}

int main() {
    // 输入原始字符串
    string input;
    cout << "请输入字符串: ";
    getline(cin, input);

    // 分割字符串
    vector<string> words = splitString(input);

    // 反转单词数组
    reverseWords(words);

    // 反转每个单词的大小写
    reverseCase(words);

    // 输出结果
    cout << "变形后的字符串: ";
    printResult(words);

    return 0;
}
```

## 2、最长公共前缀

### 2.1、问题描述

给你一个大小为 n 的字符串数组 strs ，其中包含n个字符串 , 编写一个函数来查找字符串数组中的最长公共前缀，返回这个公共前缀。

> 示例1
>
> 输入：["abca","abc","abca","abc","abcc"]
>
> 返回值："abc"
>
> 示例2
>
> 输入：["abc"]
>
> 返回值："abc"

### 2.2、思路及代码

思路：

1. 特殊情况处理：如果字符串数组为空，直接返回空字符串。
2. 初始化公共前缀：将第一个字符串设为初始公共前缀。
3. 遍历字符串数组：从第二个字符串开始，逐个比较字符，更新公共前缀。
4. 返回结果：最终得到的公共前缀即为结果。

参考代码：

```C++
#include <iostream>
#include <vector>

using namespace std;

// 函数：查找最长公共前缀
string longestCommonPrefix(vector<string>& strs) {
    // 特殊情况处理：如果字符串数组为空，直接返回空字符串
    if (strs.empty()) {
        return "";
    }

    // 初始化公共前缀为第一个字符串
    string commonPrefix = strs[0];

    // 遍历字符串数组
    for (int i = 1; i < strs.size(); ++i) {
        int j = 0;
        // 逐个比较字符，更新公共前缀
        while (j < commonPrefix.length() && j < strs[i].length() && commonPrefix[j] == strs[i][j]) {
            ++j;
        }

        // 截取更新后的公共前缀
        commonPrefix = commonPrefix.substr(0, j);

        // 如果公共前缀为空，说明没有公共前缀，直接返回
        if (commonPrefix.empty()) {
            return "";
        }
    }

    // 返回最终结果
    return commonPrefix;
}

int main() {
    // 输入字符串数组
    vector<string> strs1 = {"abca","abc","abca","abc","abcc"};
    vector<string> strs2 = {"abc"};

    // 输出结果
    cout << "示例1结果: " << longestCommonPrefix(strs1) << endl; // 期望输出: "abc"
    cout << "示例2结果: " << longestCommonPrefix(strs2) << endl; // 期望输出: "abc"

    return 0;
}
```

## 3、验证IP地址

### 3.1、问题描述

编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。 IPv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1； 同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。 IPv6 地址由8组16进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。 然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。 比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。 同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。

说明: 你可以认为给定的字符串里没有空格或者其他特殊字符。

> 示例1
>
> 输入："172.16.254.1"
>
> 返回值："IPv4"
>
> 说明：这是一个有效的 IPv4 地址, 所以返回 "IPv4" 
>
> 示例2
>
> 输入："2001:0db8:85a3:0:0:8A2E:0370:7334"
>
> 返回值："IPv6"
>
> 说明：这是一个有效的 IPv6 地址, 所以返回 "IPv6" 
>
> 示例3
>
> 输入："256.256.256.256"
>
> 返回值："Neither"
>
> 说明：这个地址既不是 IPv4 也不是 IPv6 地址 

### 3.2、思路及代码

思路：

1. 判断IPv4还是IPv6： 首先判断输入字符串是IPv4还是IPv6。可以通过检查是否包含'.'或':'来判断。
2. IPv4验证： 如果是IPv4，使用'.'分割地址，检查每个分割的部分是否是有效的十进制数，范围在0到255之间，且不能以0开头。
3. IPv6验证： 如果是IPv6，使用':'分割地址，检查每个分割的部分是否是有效的十六进制数，长度在1到4之间，且只包含数字和字母（大小写不敏感）。
4. IPv6压缩零处理： 对IPv6地址进行零压缩处理，即将连续的多个0替换为一个'::'，但要注意不能出现多个'::'。
5. 输出结果： 最终输出验证结果。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

// 函数：验证IPv4地址
bool isValidIPv4(string address) {
    stringstream ss(address);
    string part;
    int count = 0;

    // 以'.'分割地址
    while (getline(ss, part, '.')) {
        count++;

        // 检查每个分割的部分是否是有效的十进制数
        if (part.empty() || part.size() > 1 && part[0] == '0' || part.size() > 3 || !all_of(part.begin(), part.end(), ::isdigit) || stoi(part) > 255) {
            return false;
        }
    }

    // 分割出的部分必须为4个
    return count == 4;
}

// 函数：验证IPv6地址
bool isValidIPv6(string address) {
    stringstream ss(address);
    string part;
    int count = 0;

    // 以':'分割地址
    while (getline(ss, part, ':')) {
        count++;

        // 检查每个分割的部分是否是有效的十六进制数
        if (part.empty() || part.size() > 4 || !all_of(part.begin(), part.end(), ::isxdigit)) {
            return false;
        }
    }

    // 分割出的部分必须为8个
    return count == 8;
}

// 函数：压缩IPv6地址中的零
string compressIPv6(string address) {
    string compressedAddress;

    // 以':'分割地址
    stringstream ss(address);
    string part;

    while (getline(ss, part, ':')) {
        // 连续多个0替换为一个'::'
        if (part.empty()) {
            compressedAddress += "::";
        } else {
            compressedAddress += part + ":";
        }
    }

    // 移除末尾的冒号
    if (!compressedAddress.empty() && compressedAddress.back() == ':') {
        compressedAddress.pop_back();
    }

    return compressedAddress;
}

// 函数：验证IPv4或IPv6地址
bool isValidIPAddress(string address) {
    if (address.find('.') != string::npos) {
        return isValidIPv4(address);
    } else if (address.find(':') != string::npos) {
        return isValidIPv6(compressIPv6(address));
    }

    return false;
}

int main() {
    // 输入IPv4和IPv6地址
    string ipv4Address = "172.16.254.1";
    string ipv6Address = "2001:0db8:85a3:0000:0000:8a2e:0370:7334";

    // 输出验证结果
    cout << "IPv4验证结果: " << (isValidIPAddress(ipv4Address) ? "有效" : "无效") << endl; // 期望输出: "有效"
    cout << "IPv6验证结果: " << (isValidIPAddress(ipv6Address) ? "有效" : "无效") << endl; // 期望输出: "有效"

    return 0;
}
```

## 4、**大数加法**

### 4.1、问题描述

以字符串的形式读入两个数字，编写一个函数计算它们的和，以字符串形式返回。

> 示例1
>
> 输入："1","99"
>
> 返回值："100"
>
> 说明：1+99=100       
>
> 示例2
>
> 输入："114514",""
>
> 返回值："114514"

### 4.2、思路及代码

思路：

1. 字符串转整数： 将输入的两个字符串转换成整数。
2. 计算和： 对两个整数进行求和。
3. 整数转字符串： 将求和得到的整数转换为字符串。
4. 输出结果： 返回计算得到的字符串。

参考代码：

```C++
#include <iostream>
#include <string>

using namespace std;

// 函数：计算两个字符串形式数字的和
string addStrings(string num1, string num2) {
    // 将字符串转换为整数
    int intNum1 = stoi(num1);
    int intNum2 = stoi(num2);

    // 计算和
    int sum = intNum1 + intNum2;

    // 将整数转换为字符串
    string result = to_string(sum);

    // 返回结果
    return result;
}

int main() {
    // 输入两个字符串形式的数字
    string num1 = "1";
    string num2 = "99";

    // 输出结果
    string result = addStrings(num1, num2);
    cout << "示例1结果: " << result << endl; // 期望输出: "100"

    // 输入一个字符串和一个空字符串
    string num3 = "114514";
    string num4 = "";

    // 输出结果
    result = addStrings(num3, num4);
    cout << "示例2结果: " << result << endl; // 期望输出: "114514"

    return 0;
}
```