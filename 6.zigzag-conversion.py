#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        # don't need to consider (i, j) both
        output = [''] * numRows
        i, step = 0, 1
        for c in s:
            output[i] += c
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step
        return ''.join(output)
    
    def convert1(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows == 1:
            return s
        output = [[] for _ in range(numRows)]
        i = 0; j = 0; output[0].append(s[0])
        for index, c in enumerate(s[1:]):
            m = (int)(index / (numRows - 1)) % 2
            if m == 0:
                i += 1
            else:
                i -= 1; j += 1
            output[i].append(c)
        return ''.join([''.join(o) for o in output])
        
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.convert("PAYPALISHIRING", 1)
    