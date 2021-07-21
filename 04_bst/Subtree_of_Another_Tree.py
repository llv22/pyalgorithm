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

# # Subtree of Another Tree
#
# **Status:** Not Passed 
#
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
#
# Example 1:
#
# ```bash
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# ```
# Return true, because t has the same structure and node values with a subtree of s.
#
#
# Example 2:
#
# ```bash
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# ```
# Return false.

# $$ 
# isSubtree(s, t) = \begin{cases}
# tree(s) == tree(t), \text{  s and t is equal for tree} \\
# isSubtree(s.left, t), \text{  s.left and t is is equal for tree} \\
# isSubtree(s.right, t), \text{  s.right and t is is equal for tree}
# \end{cases}
# $$

# +
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def equals(s, t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)
        
        return s is not None and (equals(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))

    def isSubtreeIncorrect(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        elif not s or not t:
            return False
        
        # both s and t aren't null
        # issue : 1->1 and 1
        # Function incorrect: s.val == t.val and self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right)
        return (s.val == t.val and self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right)) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
# -

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

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
            s = stringToTreeNode(line);
            line = next(lines)
            t = stringToTreeNode(line);
            
            ret = Solution().isSubtree(s, t)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
