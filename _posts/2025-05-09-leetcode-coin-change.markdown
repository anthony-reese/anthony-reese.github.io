---
layout: post
title: "LeetCode 322 - Coin Change"
date: 2025-05-09 10:07:45 +0400
categories: [leetcode programming, dp, c++]
tags: [dynamic-programming]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Dynamic Programming](#using-dynamic-programming)
- [Complexity](#complexity)
- [Conclusion](#conclusion)


## Problem Statement
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

## Using Dynamic Programming

We can use Dynamic Programming (DP) to calculate the minimum number of coins needed to form the given amount or return `-1` if it's not possible.

1. Initialization:

    - `dp[i] = amount + 1` is used as a sentinel value to represent an initially impossible number of coins. This value ensures that comparisons with `min()` always work correctly.  
<br>
2. Dynamic Programming Transition:

    - For each coin, iterate through the possible amounts starting from `coin` to amount. If a solution exists for `dp[i - coin]`, update `dp[i]` by considering the new coin.  
<br>
3. Result:

    - If `dp[amount]` has been updated to a valid value, return it. Otherwise, return `-1`.  
<br>

{% raw %}
```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0; 

        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
            
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
```
{% endraw %}

## Complexity
Time Complexity: 𝑂(𝑛 ⋅ 𝑚)
- Where 𝑛 is the number of coins and 𝑚 is the amount. Each coin is used to update the `dp` array for all amounts up to `amount`.

Space Complexity: 𝑂(𝑚)
- Where 𝑚 is the amount. The `dp` array has a size of 𝑎𝑚𝑜𝑢𝑛𝑡 + 1.

## Conclusion
This implementation is efficient and handles edge cases like when `amount = 0` or `coins` contains duplicates.

This is a classic example of the [Unbounded Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem) where each coin can be used an unlimited number of times.

### Source:
[322. Coin Change](https://leetcode.com/problems/coin-change/description/)
