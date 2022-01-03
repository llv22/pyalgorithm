#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, Tuple


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inOrder(cur: Optional[TreeNode]) -> Tuple[int, int]:
            """[Return the min, max pair for current subtree]

            Args:
                cur (Optional[TreeNode]): [root node of subtree]

            Returns:
                Tuple[int, int]: [min, max value in leftmost, rightmost side of tree]
            """
            l = r = cur.val
            nonlocal miniDifference
            if cur.left:
                ll, lr = inOrder(cur.left)
                miniDifference = min(miniDifference, abs(cur.val - lr))
                l = ll
            if cur.right:
                rl, rr = inOrder(cur.right)
                miniDifference = min(miniDifference, abs(cur.val - rl))
                r = rr
            return l, r
        
        if not root:
            return 0
        miniDifference = 100001
        inOrder(root)
        return miniDifference
        
# @lc code=end

