#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        v = 0
        if root.val < low:
            v += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            v += self.rangeSumBST(root.left, low, high)
        else:
            v += root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        return v
        
# @lc code=end

