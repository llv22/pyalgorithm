#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums: List[int], cur: int):
            nonlocal result
            if cur == len(nums):
                result.append(nums.copy())
                return
            for i in range(cur, len(nums)):
                nums[cur], nums[i] = nums[i], nums[cur]
                if nums[:cur+1] not in [l[:cur+1] for l in result]:
                    dfs(nums, cur+1)
                nums[cur], nums[i] = nums[i], nums[cur]
        
        result = []
        dfs(nums, 0)
        return result
        
# @lc code=end

if __name__ == '__main__':
    proxy = Solution()
    proxy.permuteUnique([1,1,2])
    