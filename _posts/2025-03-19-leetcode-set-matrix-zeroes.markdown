---
layout: post
title: "LeetCode 73 - Set Matrix Zeroes"
date: 2025-03-19 01:19:48 +0400
categories: [leetcode programming]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using In-place](#using-in-place)
- [Conclusion](#conclusion)


## Problem Statement
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.\
You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).

## Using In-place
#### Explanation

1. Use First Row and First Column as Markers:
    - Traverse the matrix, and if an element is `0`, mark the corresponding row and column in the first row and first column.

2. Set the Matrix Elements to Zero:
    - Traverse the matrix again, and based on the markers, set the elements in the corresponding rows and columns to `0`.

3. Handle the First Row and First Column Separately:
    - Since they are used as markers, use separate flags to determine if they themselves need to be set to `0`.

```cpp
class Solution {
    public:
        void setZeroes(vector<vector<int>>& matrix) {
            int m = matrix.size(), n = matrix[0].size();
            bool firstRowZero = false, firstColZero = false;

            for (int i = 0; i < m; i++)
                if (matrix[i][0] == 0) firstColZero = true;
            for (int j = 0; j < n; j++) 
                if (matrix[0][j] == 0) firstRowZero = true;

            for (int i = 1; i < m; i++) {
                for (int j = 1; j < n; j++) {
                    if (matrix[i][j] == 0) {
                        matrix[i][0] = 0;
                        matrix[0][j] = 0;
                    }
                }
            }

            for (int i = 1; i < m; i++) {
                for (int j = 1; j < n; j++) {
                    if (matrix[i][0] == 0 || matrix[0][j] == 0)
                        matrix[i][j] = 0;
                }
            }

            if (firstRowZero)
                fill(matrix[0].begin(), matrix[0].end(), 0);
            if (firstColZero)
                for (int i = 0; i < m; i++) matrix[i][0] = 0;
        }
    };
```

## Conclusion
- Time Complexity: 𝑂(𝑚 × 𝑛) — The matrix is traversed multiple times, but the traversal remains linear relative to its size.

- Space Complexity: 𝑂(1) — No additional space is used beyond a few extra variables.

### Source:
[73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/submissions/1578293394/)
