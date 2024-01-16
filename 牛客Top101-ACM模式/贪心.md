# 贪心

## 1、**分糖果问题**

### 1.1、问题描述

一群孩子做游戏，现在请你根据游戏得分来发糖果，要求如下：

1. 每个孩子不管得分多少，起码分到一个糖果。
2. 任意两个相邻的孩子之间，得分较多的孩子必须拿多一些糖果。(若相同则无此限制)

给定一个数组*arr* 代表得分数组，请返回最少需要多少糖果。

> 示例1
>
> 输入：[1,1,2]
>
> 返回值：4
>
> 说明：最优分配方案为1,1,2 
>
> 示例2
>
> 输入：[1,1,1]
>
> 返回值：3
>
> 说明：最优分配方案是1,1,1 

### 1.2、思路及代码

思路：

1. 初始化一个糖果数组 `candies`，所有元素初始值为1，表示每个孩子初始至少分到一个糖果。
2. 从左到右遍历一次数组 `arr`，如果右边的孩子得分比左边的孩子高，右边的孩子的糖果数量应该比左边的多。因此，如果 `arr[i] > arr[i-1]`，则 `candies[i] = candies[i-1] + 1`。
3. 从右到左遍历一次数组 `arr`，如果左边的孩子得分比右边的孩子高，并且左边的糖果数量不大于右边的，那么更新左边孩子的糖果数量。即，如果 `arr[i] > arr[i+1]` 且 `candies[i] <= candies[i+1]`，则 `candies[i] = candies[i+1] + 1`。
4. 累计所有孩子的糖果数量。

参考代码：

```C++
#include <iostream>
#include <vector>

using namespace std;

// 函数：计算最少需要多少糖果
int minCandies(vector<int>& arr) {
    int n = arr.size();
    if (n <= 1) {
        return n; // 当数组长度小于等于1时，每个孩子至少分到一个糖果，返回数组长度
    }

    vector<int> candies(n, 1); // 初始化糖果数组，所有元素初始值为1

    // 从左到右遍历数组，更新右边孩子的糖果数量
    for (int i = 1; i < n; i++) {
        if (arr[i] > arr[i-1]) {
            candies[i] = candies[i-1] + 1;
        }
    }

    // 从右到左遍历数组，更新左边孩子的糖果数量
    for (int i = n - 2; i >= 0; i--) {
        if (arr[i] > arr[i+1] && candies[i] <= candies[i+1]) {
            candies[i] = candies[i+1] + 1;
        }
    }

    // 累计所有孩子的糖果数量
    int result = 0;
    for (int candy : candies) {
        result += candy;
    }

    return result;
}

int main() {
    // 输入数组
    vector<int> arr1 = {1,0,2};
    vector<int> arr2 = {1,2,2};

    // 输出结果
    cout << "示例1结果: " << minCandies(arr1) << endl; // 期望输出: 5
    cout << "示例2结果: " << minCandies(arr2) << endl; // 期望输出: 4

    return 0;
}
```

## 2、**主持人调度（二）**

### 2.1、问题描述

有 n 个活动即将举办，每个活动都有开始时间与活动的结束时间，第 i 个活动的开始时间是 start(i) ,第 i 个活动的结束时间是 end(i) ,举办某个活动就需要为该活动准备一个活动主持人。 一位活动主持人在同一时间只能参与一个活动。并且活动主持人需要全程参与活动，换句话说，一个主持人参与了第 i 个活动，那么该主持人在 (start(i),end(i)) 这个时间段不能参与其他任何活动。求为了成功举办这 n 个活动，最少需要多少名主持人。

> 示例1
>
> 输入：2,[[1,2],[2,3]]
>
> 返回值：1
>
> 说明：只需要一个主持人就能成功举办这两个活动      
>
> 示例2
>
> 输入：2,[[1,3],[2,4]]
>
> 返回值：2
>
> 说明：需要两个主持人才能成功举办这两个活动

### 2.2、思路及代码

思路：

1. 将所有活动按照结束时间的先后顺序进行排序。
2. 选择第一个活动，并为其分配一个主持人。
3. 遍历排序后的活动列表，对于每个活动：
   1. 如果该活动的开始时间在当前主持人的空闲时间之后，将该活动分配给当前主持人。
   2. 否则，新开辟一个主持人，为该活动分配新的主持人。
4. 统计总共开辟的主持人数量即为最少需要的主持人数量。

参考代码：

```C++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 函数：计算最少需要的主持人数量
int minHosts(int n, vector<vector<int>>& activities) {
    if (n <= 0 || activities.empty()) {
        return 0; // 没有活动或活动数量为0时，不需要主持人，返回0
    }

    // 对活动按照结束时间进行排序
    sort(activities.begin(), activities.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });

    int hosts = 1; // 初始化主持人数量为1，因为第一个活动至少需要一个主持人
    int currentEndTime = activities[0][1]; // 记录当前主持人的空闲时间

    // 遍历排序后的活动列表
    for (int i = 1; i < n; i++) {
        int activityStartTime = activities[i][0];
        int activityEndTime = activities[i][1];

        // 如果当前活动的开始时间在当前主持人的空闲时间之后
        if (activityStartTime >= currentEndTime) {
            // 将该活动分配给当前主持人，并更新当前主持人的空闲时间
            currentEndTime = activityEndTime;
        } else {
            // 否则，新开辟一个主持人，为该活动分配新的主持人，并更新当前主持人的空闲时间
            hosts++;
            currentEndTime = activityEndTime;
        }
    }

    return hosts;
}

int main() {
    // 输入活动数量和活动列表
    int n1 = 2;
    vector<vector<int>> activities1 = {{1, 2}, {2, 3}};

    int n2 = 2;
    vector<vector<int>> activities2 = {{1, 3}, {2, 4}};

    // 输出结果
    cout << "示例1结果: " << minHosts(n1, activities1) << endl; // 期望输出: 1
    cout << "示例2结果: " << minHosts(n2, activities2) << endl; // 期望输出: 2

    return 0;
}
```