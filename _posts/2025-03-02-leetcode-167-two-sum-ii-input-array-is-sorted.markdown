---
layout: post
title: "LeetCode 167 - Two Sum II - Input Array Is Sorted"
date: 2025-03-02 03:01:01 +0400
categories: [leetcode programming, Java, CS Foundations]
permalink: /posts/2025-03-02-leetcode-167-two-sum-ii-input-array-is-sorted
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Two Pointers](#using-two-pointers)
- [Conclusion](#conclusion)


## Problem Statement
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

## Using Two Pointers
In this approach, we use two pointers, left and right, to scan the array from both ends. If the sum of the elements at these pointers matches the target, we return their 1-indexed positions. If the sum is less than the target, we move the left pointer to the right to increase the sum. If the sum is greater than the target, we move the right pointer to the left to decrease the sum. This ensures that we find the correct pair of indices using only constant extra space.

```cpp
class Solution {
    public:
        vector<int> twoSum(vector<int>& numbers, int target) {
            int left = 0, right = numbers.size() - 1;

            while (left < right) {
                int current_sum = numbers[left] + numbers[right];

                if (current_sum == target) {
                    return {left + 1, right + 1};
                } else if (current_sum < target) {
                    left++;
                } else {
                    right--;
                }                
            }
            return {};
        }
    };
```

## Conclusion
- Time Complexity: 𝑂(𝑛) — In the worst case, we traverse the array once, checking each element with two pointers. Since each pointer only moves once, the time complexity is linear, or O(n), where n is the number of elements in the array.
- Space Complexity: 𝑂(1) — We are using only a constant amount of extra space (the two pointers), which means the space complexity is constant, or 𝑂(1). No additional data structures are being used that scale with the input size.

### Source:
[167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
