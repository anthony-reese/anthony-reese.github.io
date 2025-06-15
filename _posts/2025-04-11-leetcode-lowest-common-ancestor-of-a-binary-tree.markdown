---
layout: post
title: "LeetCode 236 - Lowest Common Ancestor of a Binary Tree"
date: 2025-04-11 18:46:34 +0400
categories: [leetcode programming]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Tree DFS (Depth First Search)](#using-tree-dfs)
- [Conclusion](#conclusion)


## Problem Statement
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

## Using Tree DFS
### Explanation

We use Tree DFS to efficiently traverse a tree.

1. Base Case:

    - If the current node is `nullptr`, that means we’ve reached the end of a branch.

    - If the current node matches `p` or `q`, we’ve found one of the nodes.

2. Recursive Search:

    - Traverse both left and right subtrees to search for `p` and `q`.    
<br>
3. Combine Results:

    - If one node is found in the left subtree and the other in the right subtree, the current node is their LCA.

    - If both are in the same subtree, propagate the result up the tree.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root || root == p || root == q) {
                return root;
            }
            
            TreeNode* left = lowestCommonAncestor(root->left, p, q);
            TreeNode* right = lowestCommonAncestor(root->right, p, q);

            if (left && right) {
                return root;
            }
            
            return left ? left : right;
    }
};
```

## Conclusion
- Time Complexity: 𝑂(𝑛) - Where 𝑛 is the number of nodes in the binary tree.

- Space Complexity: 𝑂(ℎ) - Where ℎ is the height of the binary tree, due to the recursion stack.

### Source:
[236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)
