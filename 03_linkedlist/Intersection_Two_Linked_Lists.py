# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.7
# ---

# # 160. Intersection of Two Linked Lists

# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# ```bash
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# ```
#
# begin to intersect at node c1.
#
#
# Notes:
#
# * If the two linked lists have no intersection at all, return null.
# * The linked lists must retain their original structure after the function returns.
# * You may assume there are no cycles anywhere in the entire linked structure.
# * Your code should preferably run in O(n) time and use only O(1) memory.
#
# Status: Passed - 192 ms

# Analysis:
#
# <img src="analysis.jpg"/>

# +
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        # check if they are on the same node, when reaching the tail
        p1=headA; p2=headB
        while p1.next:
            p1=p1.next
        while p2.next:
            p2=p2.next
        if p1!=p2:
            return None
        # now to check the intersection part, they will definitely meet for 2 intersection, refer to my prove in 
        p1=headA; p2=headB
        while p1!=p2:
            p1=p1.next
            if not p1:
                # then redirect to headB
                p1=headB
            p2=p2.next
            if not p2:
                # then redirect to headA
                p2=headA
        # after x1 step after first intersection, they will meet
        return p1
# -

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            # fix issue, metioned in https://blog.csdn.net/gaifuxi9518/article/details/81059938
            line = lines.__next__()
            headA = stringToListNode(line)
            line = lines.__next__()
            headB = stringToListNode(line)
            
            ret = Solution().getIntersectionNode(headA, headB)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
