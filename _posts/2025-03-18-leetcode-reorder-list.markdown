---
layout: post
title: "LeetCode 143 - Reorder List"
date: 2025-03-18 19:10:14 +0400
categories: [leetcode programming]
---
## Table of Contents
- [Problem Statement](#problem-statement)
- [Using Two Pointers](#using-two-pointers)
- [Conclusion](#conclusion)


## Problem Statement
You are given the head of a singly linked-list. The list can be represented as:

L<sub>0</sub> → L<sub>1</sub> → … → L<sub>n</sub> - <sub>1</sub> → L<sub>n</sub>
Reorder the list to be on the following form:

L<sub>0</sub> → L<sub>n</sub> → L<sub>1</sub> → L<sub>n</sub> - <sub>1</sub> → L<sub>2</sub> → L<sub>n</sub> - <sub>2</sub> → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Using Two Pointers
#### Explanation

1. Finding the Middle:
    - Use a slow pointer that moves one step at a time and a fast pointer that moves two steps at a time. When the fast pointer reaches the end, the slow pointer will be at the middle.

2. Reversing the Second Half:
    - Starting from the middle, reverse the pointers in the second half of the list using standard reverse-linked-list logic.

3. Merging:
    - Alternate nodes from the first and second halves. Stop when the second list is exhausted.

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
    void reorderList(ListNode* head) {
        if (!head || !head->next || !head->next->next) {
            return;
        }
        
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
            
        ListNode* prev = nullptr;
        ListNode* current = slow->next;
        slow->next = nullptr;
        while (current) {
            ListNode* temp = current->next;
            current->next = prev;
            prev = current;
            current = temp;
        }

        ListNode* first = head;
        ListNode* second = prev;
        while (second) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;

            first->next = second;
            second->next = temp1;

            first = temp1;
            second = temp2;
        }            
    }
};
```

## Conclusion
- Time Complexity: 𝑂(𝑛) — Where n is the number of nodes in the list. Each step (finding the middle, reversing, and merging) takes linear time.
<br>

- Space Complexity: 𝑂(1) — No additional space is used other than pointers.

### Source:
[143. Reorder List](https://leetcode.com/problems/reorder-list/description/)
