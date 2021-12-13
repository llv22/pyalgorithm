#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0; output = []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            if firstList[i][1] <= secondList[j][1]:
                end = firstList[i][1]; i += 1
            else:
                end = secondList[j][1]; j += 1
            if start <= end:
                output.append([start, end])
        return output

# @lc code=end
