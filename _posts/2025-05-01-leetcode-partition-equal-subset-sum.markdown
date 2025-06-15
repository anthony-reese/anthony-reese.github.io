---
layout: post
title: "LeetCode 416 - Partition Equal Subset Sum"
date: 2025-05-01 16:08:22 +0400
categories: [leetcode programming, dp, string, c++, unordered-set]
tags: [dynamic-programming]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Dynamic Programming](#using-dynamic-programming)
- [Complexity](#complexity)
- [Conclusion](#conclusion)


## Problem Statement
Given an integer array `nums`, return `true` if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or `false` otherwise.

## Using Dynamic Programming

To solve the problem of partitioning the array into two subsets with equal sums, we can use dynamic programming (DP).

1. Sum Calculation:  
  
    - Calculate the total sum of the array using a loop.
    - If the sum is **odd**, return `false` immediately since it can't be split evenly.
    <br><br>
2. Subset Sum Reduction:  
  
    - Set `target = totalSum / 2`. Now, we need to determine if there exists a subset whose elements sum to `target`.  
    <br>
3. Dynamic Programming Array:  
  
    - Initialize a boolean DP array of size `target + 1`, where `dp[i]` means "is a subset sum of `i` achievable?"
    - Set `dp[0] = true` (a sum of 0 is always achievable).
    - For each number in `nums`, update the DP array in reverse to avoid using the same number multiple times.
    <br><br>
4. Final Check:  
  
    - If `dp[target]` is `true`, then such a subset exists, and partitioning is possible.

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
            
        if (totalSum % 2 != 0) return false;

        int target = totalSum / 2;

        vector<bool> dp(target + 1, false);
        dp[0] = true; 

        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                dp[i] = dp[i] || dp[i - num];
            }
        }
            
        return dp[target];
    }
};
```

## Complexity
Time Complexity: 𝑂(𝑛 × target) 
- Where 𝑛 is the size of `nums` and `target = totalSum / 2`.  
- The outer loop iterates over `nums`, and the inner loop iterates up to `target`.

Space Complexity: 𝑂(target)
- The DP array stores information about achievable subset sums.  

## Conclusion
This implementation efficiently checks for partitioning conditions, leveraging dynamic programming to handle large arrays and sums.  
### Source:
[416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/description/)
