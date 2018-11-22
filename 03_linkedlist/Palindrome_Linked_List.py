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

# # 234. Palindrome Linked List

# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
# ```bash
# Input: 1->2
# Output: false
# ```
#
# Example 2:
#
# ```bash
# Input: 1->2->2->1
# Output: true
# ```
#
# Follow up:
# Could you do it in O(n) time and O(1) space?

# +
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def palindrome(p, head):
            if not p.next:
                # already reach the tail, then stack-back to compare, so should with head.next popup
                return (p.val == head.val, head.next)
            ret, hnext=palindrome(p.next, head)
            return (ret and hnext.val == p.val, hnext.next)
        
        if not head:
            return True
        status, _=palindrome(head, head)
        return status
# -

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            
            ret = Solution().isPalindrome(head)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
