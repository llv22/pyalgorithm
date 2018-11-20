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

# # 5. Longest Palindromic Substring
#
# Reference: https://leetcode.com/problems/longest-palindromic-substring/
#
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
# ```basg
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# ```
#
# Example 2:
# ```bash
# Input: "cbbd"
# Output: "bb"
# ```

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        ## issue:
        # dp = [[False] * l] * l
        # modify the reference in 2-dimension array
        dp = [[False for _ in range(l)] for _ in range(l)]
        lbegin = 0; maxlen = 1
        for i in range(l):
            dp[i][i] = True
        for i in range(l-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                lbegin = i; maxlen = 2
        for i in range(l-3, -1, -1):
            for j in range(i+2, l):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j-i+1>maxlen:
                        lbegin = i;maxlen = j-i+1 
        return s[lbegin:lbegin+maxlen]

def stringToString(input):
    import json
    return json.loads(input)

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
            s = stringToString(line);
            
            ret = Solution().longestPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
