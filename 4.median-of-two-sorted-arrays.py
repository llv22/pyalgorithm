#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findInSorted(L: List[int], ll:int, lr: int, R: List[int], rl:int, rr: int, pivotPsn: int) -> float:
            if ll > lr:
                return R[rl + pivotPsn]
            if rl > rr:
                return L[ll + pivotPsn]
            lmed = (ll + lr)//2; rmed = (rl + rr)//2
            if L[lmed] > R[rmed]:
                L, ll, lr, lmed, R, rl, rr, rmed = R, rl, rr, rmed, L, ll, lr, lmed
            # now L[lmed] <= R[rmed], binary search L[lmed] in R[rl, rmed]
            l=rl; r=rmed
            while l < r-1:
                p = (l + r) //2; 
                if R[p] <= L[lmed]:
                    l = p
                else:
                    r = p
            if R[l] >= L[lmed]:
                re = l
            elif R[r] >= L[lmed]:
                re = r
            if lmed - ll + re - rl == pivotPsn or (R[re] == L[lmed] and lmed - ll + re - rl + 1 == pivotPsn):
                return L[lmed]
            elif pivotPsn - (lmed - ll + re - rl + 1) >= 0:
                return findInSorted(L, lmed + 1, lr, R, re, rr, pivotPsn - (lmed - ll + re - rl + 1))
            else:
                return findInSorted(L, ll, lmed - 1, R, rl, re, pivotPsn)
        
        n = len(nums1); m = len(nums2)
        if (n+m)%2 == 0:
            med0 = findInSorted(nums1, 0, n-1, nums2, 0, m-1, (n+m)//2 - 1)
            med1 = findInSorted(nums1, 0, n-1, nums2, 0, m-1, (n+m)//2)
            return (med0 + med1) / 2.
        else:
            return findInSorted(nums1, 0, n-1, nums2, 0, m-1, (n+m)//2)
            

# @lc code=end
if __name__ == "__main__":
    proxy = Solution()
    # ## case 2: passed
    # nums1 = [1, 2]
    # nums2 = [3, 4]
    # ## case 3: passed
    # nums1 = [1, 2, 3, 4]
    # nums2 = [1, 2, 3, 4]
    # ## case 1: passed
    # nums1 = [1, 2]
    # nums2 = [3]
    # ## case 4: passed
    # nums1 = [2]
    # nums2 = []
    # ## case 5: passed
    # nums1 = [2,2,4,4]
    # nums2 = [2,2,4,4]
    # ## case 6: passed
    # nums1 = [1]
    # nums2 = [2,3,4]
    # nums1 = [2]
    # nums2 = [1, 3, 4]
    nums1 = [2,4]
    nums2 = [1,3,5,6]
    print(proxy.findMedianSortedArrays(nums1, nums2))
