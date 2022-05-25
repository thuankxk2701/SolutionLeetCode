# https://leetcode.com/problems/wildcard-matching

class Solution:
        def isMatch(self, s: str, p: str) -> bool:

            n, m, lastMatched, star, i, j = len(s), len(p), -1, -1, 0, 0
            while i < n:
                if j < m and (p[j] == s[i] or p[j] == '?'):
                    i += 1
                    j += 1
                elif j< m and p[j] == '*':
                    lastMatched = i
                    star = j
                    j += 1
                elif star != -1:
                    i = lastMatched + 1
                    lastMatched = i 
                    j = star + 1
                else:
                    return False
            while j < m and p[j] == '*':
                j += 1
            return j == m 