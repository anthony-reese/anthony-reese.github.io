---
layout: post
title: "LeetCode 238 - Product of Array Except Self"
date: 2025-03-02 03:01:01 +0400
categories: [leetcode programming]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Sliding Window](#using-sliding-window)
- [Conclusion](#conclusion)


## Problem Statement
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

## Using Sliding Window
#### Explanation
Left Products Pass:
- Initialize left_product to 1.
- Iterate through the array from left to right.
- For each index i, set answer[i] to left_product.
- Update left_product by multiplying it with nums[i].

This pass fills the answer array with the products of all elements to the left of each index.

Right Products Pass:
- Initialize right_product to 1.
- Iterate through the array from right to left.
- For each index i, multiply answer[i] by right_product.
- Update right_product by multiplying it with nums[i].

This pass adjusts the answer array to include the products of all elements to the right of each index.

By combining these two passes, we achieve the desired result where answer[i] is the product of all elements in nums except nums[i].

```cpp
class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            int length = nums.size();
            vector<int> answer(length,1);

            int left_product = 1;
            for (int i = 0; i < length; ++i) {
                answer[i] = left_product;
                left_product *= nums[i];
            }

            int right_product = 1;
            for (int i = length - 1; i >= 0; --i) {
                answer[i] *= right_product;
                right_product *= nums[i];
            }
            return answer;
        }
    };
```

## Conclusion
- Time Complexity: 𝑂(𝑛) — The algorithm makes two passes over the array, resulting in linear time complexity.
- Space Complexity: 𝑂(𝑛) — The space complexity is linear due to the output array.

### Source:
[238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)
