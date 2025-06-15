---
layout: post
title: "LeetCode 75 - Sort Colors"
date: 2025-03-02 03:01:01 +0400
categories: [leetcode programming]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Sorting](#using-sorting)
- [Conclusion](#conclusion)


## Problem Statement
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

## Using Sorting
#### Explanation
The algorithm uses three pointers:
1. low: Points to the boundary where the next 0 should go.
2. mid: Scans through the array.
3. high: Points to the boundary where the next 2 should go.

We iterate through the array with the mid pointer, adjusting the positions of 0s and 2s as follows:
- If nums[mid] is 0, swap it with the element at low, and increment both low and mid.
- If nums[mid] is 1, just move the mid pointer forward.
- If nums[mid] is 2, swap it with the element at high, and decrement high.

This ensures that 0s are moved to the front, 2s are moved to the back, and 1s remain in the middle, effectively sorting the array in a single pass without using any sorting library functions.

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0, mid = 0, high = nums.size() - 1;
        
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums[low], nums[mid]);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {  // nums[mid] == 2
                swap(nums[high], nums[mid]);
                high--;
            }
        }
    }
};
```

## Conclusion
- Time Complexity: 𝑂(𝑛) — The algorithm iterates through the array only once with the mid pointer, making a single pass through the array, where n is the number of elements. Each element is visited at most once, so the time complexity is linear, O(𝑛). 
- Space Complexity: 𝑂(1) — The algorithm sorts the array in place by using only a constant amount of extra space for the three pointers (low, mid, high). No additional data structures (like arrays or lists) are used, so the space complexity is constant, O(1).

#### Source:
[75. Sort Colors](https://leetcode.com/problems/sort-colors/description/)
