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

class Solution:
    # leetcode link - https://leetcode.com/problems/reverse-bits/
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0; cnt = 0
        while n > 0:
            result = result * 2 + (n%2)
            n = n // 2; cnt += 1
        return result << (32 - cnt)

if __name__ == "__main__":
    proxy = Solution()
    assert 964176192 == proxy.reverseBits(43261596)
