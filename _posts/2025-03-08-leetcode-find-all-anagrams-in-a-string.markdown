---
layout: post
title: "LeetCode 438 - Find All Anagrams in a String"
date: 2025-03-08 17:28:58 +0400
categories: [leetcode programming]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Sliding Window](#using-sliding-window)
- [Conclusion](#conclusion)


## Problem Statement
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

## Using Sliding Window
#### Explanation

1. Frequency Arrays:
    - `count_p` stores the character frequencies of `p`.
    - `count_window` tracks the character frequencies in the current window of `s`.
2. Initialize the First Window:
    - Process the first `p.length()` characters of `s` to initialize `count_window`.
    - Compare `count_window` with `count_p`—if they match, store the starting index (`0`).
3. Sliding the Window:
    - For every new character in `s` (starting from index `p.length()`), adjust `count_window`:
        - Remove the character that is slides out of the window.
        - Add the new character that slides into the window.
    - After each adjustment, compare `count_window` and `count_p`. If they match, store the current starting index.

```cpp
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        if (s.length() < p.length()) return result;

        vector<int> count_p(26, 0);
        vector<int> count_window(26, 0);

        for (int i = 0; i < p.length(); i++) {
            count_p[p[i] - 'a']++;
            count_window[s[i] - 'a']++;
        }
        if (count_window == count_p) {
            result.push_back(0);
            }
        for (int i = p.length(); i < s.length(); i++) {
            count_window[s[i - p.length()] - 'a']--;

            count_window[s[i] - 'a']++;
            
            if (count_window == count_p) {
                result.push_back(i - p.length() + 1);
            }
        }   
        return result;
    }
};
```

## Conclusion
- Time Complexity: 𝑂(𝑛) — Each character is processed once.
- Space Complexity: 𝑂(1) — The frequency arrays have a fixed size of 26, meaning constant space is used.

### Source:
[438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)
