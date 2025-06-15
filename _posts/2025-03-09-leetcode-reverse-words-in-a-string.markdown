---
layout: post
title: "LeetCode 151 - Reverse Words in a String"
date: 2025-03-09 00:21:58 +0400
categories: [leetcode programming]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Two Pointers](#using-two-pointers)
- [Conclusion](#conclusion)


## Problem Statement
Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Using Two Pointers
#### Explanation

- Trimming Spaces: Remove leading and trailing spaces by finding the first and last non-space characters.

- Splitting Words: Use a `stringstream` to extract words, automatically discarding extra spaces between them.

- Reversing Order: Store the words in a `vector<string>` and use `reverse()` to rearrange them.

- Joining Words: Combines the reversed words back into a single string with only one space between them.

```cpp
class Solution {
    public:
        string reverseWords(string s) {
            int left = 0, right = s.size() - 1;
            while (left <= right && s[left] == ' ') left++;
            while (right >= left && s[right] == ' ') right--;
            s = s.substr(left, right - left + 1);

            stringstream ss(s);
            string word;
            vector<string> words;
            while (ss >> word) {
                words.push_back(word);
            }
            
            reverse(words.begin(), words.end());

            string result;
            for (int i = 0; i < words.size(); ++i) {
                if (i > 0) result += " ";
                result += words[i];
            }
            return result;
        }
    };
```

## Conclusion
- Time Complexity: 𝑂(𝑛) — We perform a few linear scans over `s` for trimming, splitting, reversing, and joining.
- Space Complexity: 𝑂(𝑛) — A `vector<string>` stores words, and the final output string requires extra space.

### Source:
[151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/description/)
