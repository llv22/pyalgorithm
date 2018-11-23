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

# # 530. Minimum Absolute Difference in BST

# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
#
# Example:
#
# ```bash
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
# ```
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
#  
#
# Note: There are at least two nodes in this BST.

# +
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifferenceGeneric(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def diff(s, tree):
            """
            return min{s-tree}, having s for all subtree tree
            type s: TreeNode
            type tree: TreeNode
            rtype: int
            """
            cval = abs(s.val - tree.val)
            if tree.left:
                cval = min(cval, diff(s, tree.left))
            if tree.right:
                cval = min(cval, diff(s, tree.right))
            return cval
        
        v1 = (1<<31)
        if root.left:
            v1 = diff(root, root.left)
        if root.right:
            v1 = diff(root, root.right)
        
        if root.left:
            v1 = min(self.getMinimumDifference(root.left), v1)
        if root.right:
            v1 = min(self.getMinimumDifference(root.right), v1)
        return v1
    
    
    def getMinimumDifference(self, root):
        """
        For BST, just take nearest nodes of root in inorder traverse
        :type root: TreeNode
        :rtype: int
        """
        def inOrder(cur, preval):
            diff = (1<<31)
            if cur.left:
                diff = min(diff, inOrder(cur.left, preval))
            diff = min(diff, abs(cur.val - preval))
            if cur.right:
                diff = min(diff, inOrder(cur.right, cur.val))
            return diff
        
        return inOrder(root, 0)
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
            root = stringToTreeNode(line);
            
            ret = Solution().getMinimumDifference(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
