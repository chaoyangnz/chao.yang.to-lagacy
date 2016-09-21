title: 'LeetCode #2 Add Two Numbers'
date: 2016-02-03 23:18:25
tags: LeetCode
---

# Question

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

# Analysis

We need to be familiar with linked list operations, especially the case in the boundary. There is no time complexity to concern.

# Solution

``` java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = null;
        ListNode tail = null;
        int carry = 0;
        
        while(true) {
            if(l1 == null && l2 == null) break;
            int val1 = 0;
            int val2 = 0;
            if(l1 != null) { val1 = l1.val; l1 = l1.next; }
            if(l2 != null) { val2 = l2.val; l2 = l2.next; }
            int val = val1 + val2 + carry;
            carry = val / 10;
            ListNode node  = new ListNode(val % 10);
            if(head == null) {
                head = node;
                tail = node;
            } else {
                tail.next = node;
                tail = node;
            }
        }
        
        // especially notice the rest carry bit
        if(carry != 0) tail.next = new ListNode(carry);
        
        return head;
    }
}
```

# Submisssion & Judgement

[Sumbission in LeetCode](https://leetcode.com/submissions/detail/52578127/)



