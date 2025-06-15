---
layout: post
title: "LeetCode 234 - Palindrome Linked List"
date: 2025-03-15 20:13:14 +0400
categories: [leetcode programming]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Two Pointers](#using-two-pointers)
- [Conclusion](#conclusion)


## Problem Statement
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

## Using Two Pointers
#### Explanation

1. Finding the Middle:
    - Use two pointers (slow and fast) to identify the middle of the linked list. The slow pointer moves one step at a time, while fast moves two steps. When fast reaches the end, slow will be at the middle.
<br>
2. Reversing the Second Half:
    - Reverse the portion of the linked list starting from the middle. This allows for an in-place comparison of values.
<br>
3. Comparing Both Halves:
    - Compare the first half of the linked list to the reversed second half. If all values match, the list is a palindrome.

/**\
 &nbsp;\* Definition for singly-linked list.\
 &nbsp;\* struct ListNode {\
 &nbsp;\*     int val;\
 &nbsp;\*     ListNode *next;\
 &nbsp;\*     ListNode() : val(0), next(nullptr) {}\
 &nbsp;\*     ListNode(int x) : val(x), next(nullptr) {}\
 &nbsp;\*     ListNode(int x, ListNode *next) : val(x), next(next) {}\
&nbsp;\* };\
&nbsp;\*/

```cpp
class Solution {
    public:
        bool isPalindrome(ListNode* head) {
            if (!head || !head->next) return true;

            ListNode* slow = head;
            ListNode* fast = head;
            while (fast && fast->next) {
                slow = slow->next;
                fast = fast->next->next;
            }
            
            ListNode* prev = nullptr;
            ListNode* current = slow;
            while (current) {
                ListNode* temp = current->next;
                current->next = prev;
                prev = current;
                current = temp;
            }

            ListNode* left = head;
            ListNode* right = prev;
            while (right) {
                if (left->val != right->val) {
                    return false;
                }
                left = left->next;
                right = right->next;                    
            }            
            return true;
        }
    };
```

## Conclusion
- Time Complexity: 𝑂(𝑛) — \
    The list is traversed multiple times:
    1. To find the middle of the list.
    2. To reverse the second half.
    3. To compare the two halves.
<br>

- Space Complexity: 𝑂(1) — No additional space is used other than pointers.

### Source:
[234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/description/)
