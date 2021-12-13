#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        maxLen = curLen = 0; c = ''
        for ch in s:
            if ch == c:
                curLen += 1
            else:
                c = ch; curLen = 1
            if curLen > maxLen:
                maxLen = curLen
        return maxLen
        
# @lc code=end

