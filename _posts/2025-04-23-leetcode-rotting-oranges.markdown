---
layout: post
title: "LeetCode 994 - Rotting Oranges"
date: 2025-04-23 17:27:07 +0400
categories: [leetcode programming, bfs, vector, c++, queue]
tags: [breadth-first-search]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Breadth First Search](#using-breadth-first-search)
- [Complexity](#complexity)
- [Conclusion](#conclusion)


## Problem Statement
You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell,

- `1` representing a fresh orange, or

- `2` representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

## Using Breadth First Search

We can use Breadth-First Search (BFS) to simulate the rotting process of the oranges.

1. BFS Traversal:

    - BFS allows rotting to propagate minute by minute, in all four directions, matching the problem’s requirement.
<br><br>
2. Tracking Time:

    - Each level of BFS represents one minute passing. We increment `minutes` after processing each level.
<br><br>
3. Edge Cases:

    - If there are no fresh oranges from the start, return `0`.

    - If some fresh oranges cannot be reached, return `-1`.

{% raw %}
```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        queue<pair<int, int>> q;
        int freshCount = 0;
        int minutes = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j}); 
                } else if (grid[i][j] == 1) {
                    freshCount++;
                }
            }
        }
            
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!q.empty() && freshCount > 0) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                auto [x, y] = q.front();
                q.pop();

                for (auto [dx, dy] : directions) {
                    int nx = x + dx;
                    int ny = y + dy;

                    if (nx >= 0 && ny >= 0 && nx < m && ny < n && grid[nx][ny] == 1) {
                        grid[nx][ny] = 2;
                        q.push({nx, ny});
                        freshCount--;
                    }
                }
            }
            minutes++;
        }

        return freshCount == 0 ? minutes : -1;
    }
};
```
{% endraw %}

## Complexity
Time Complexity: 𝑂(𝑚 × 𝑛)
- Every cell is visited at most once.

Space Complexity: 𝑂(𝑚 × 𝑛)
- Space used by the queue and auxiliary structures like the `directions` vector.

## Conclusion
This BFS-based solution effectively simulates the rotting process and determines the minimum time required or detects when it’s impossible to rot all oranges.
### Source:
[994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description/)
