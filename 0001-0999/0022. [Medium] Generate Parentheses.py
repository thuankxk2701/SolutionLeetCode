# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        def rec_gen(l, r, acc=""):
            if l == 0 and r == 0:
                yield acc
            if l > 0:
                yield from rec_gen(l-1, r, acc+'(')
            if r > l:
                yield from rec_gen(l, r-1, acc+')')
        
        return list(rec_gen(n, n))