#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
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
    
    def getMinimumDifference1(self, root: Optional[TreeNode]) -> int:
        def inOrder(cur: Optional[TreeNode]):
            if not cur:
                return;
            inOrder(cur.left)
            if self.prev:
                self.miniDifference = min(self.miniDifference, abs(cur.val - self.prev.val))
            self.prev = cur
            inOrder(cur.right)
        
        if not root:
            return 0
        self.miniDifference = 100001
        self.prev = None
        inOrder(root)
        return self.miniDifference
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inOrder(cur: Optional[TreeNode]):
            l = r = cur.val
            if cur.left:
                ll, lr = inOrder(cur.left)
                self.miniDifference = min(self.miniDifference, abs(cur.val - lr))
                l = ll
            if cur.right:
                rl, rr = inOrder(cur.right)
                self.miniDifference = min(self.miniDifference, abs(cur.val - rl))
                r = rr
            return l, r
        
        if not root:
            return 0
        self.miniDifference = 100001
        inOrder(root)
        return self.miniDifference
        
# @lc code=end

