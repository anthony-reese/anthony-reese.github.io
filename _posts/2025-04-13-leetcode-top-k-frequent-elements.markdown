---
layout: post
title: "LeetCode 347 - Top K Frequent Elements"
date: 2025-04-13 21:55:08 +0400
categories: leetcode programming
tags: [hashmap, heap, bucket-sort, leetcode, c++]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Bucket Sort](#using-bucket-sort)
- [Complexity](#complexity)
- [Conclusion](#conclusion)


## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Using Bucket Sort

We use Bucket Sort to distribute the elements of an array into a number of buckets.

1. Counting Frequencies:

    - The hash map `freq` associates each element in `nums` with its count.
<br><br>

2. Bucket Sort:

    - Elements with the same frequency are grouped into buckets (e.g., all elements appearing 3 times go into bucket 3).

    - The maximum frequency cannot exceed the size of the array `n`.

3. Retrieve Top `k` Elements:

    - Start from the bucket with the highest frequency and work downward.

    - Collect elements until `k` elements are retrieved.

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
            
        int n = nums.size();
        vector<vector<int>> buckets(n + 1);
        for (auto& pair : freq) {
            int element = pair.first;
            int count = pair.second;
            buckets[count].push_back(element);
        }

        vector<int> result;
        for (int i = n; i >= 0 && result.size() < k; --i) {
            for (int element : buckets[i]) {
                result.push_back(element);
                if (result.size() == k) break;
            }
        }
            
        return result;
    }
};
```

## Complexity
- Time Complexity:
    - Counting frequencies: 𝑂(𝑛), where 𝑛 is the size of nums.
    - Bucket traversal: 𝑂(𝑛) (each element is processed once).
    - Total: 𝑂(𝑛).

- Space Complexity: 
    - 𝑂(𝑛) for the buckets and frequency map.

## Conclusion
This implementation efficiently returns the `k` most frequent elements, in any order.
### Source:
[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)
