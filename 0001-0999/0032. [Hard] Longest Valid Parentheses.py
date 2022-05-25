# https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len = 0
        beg, end = -1, -1
        for i in range(len(s)):
            if stack and s[i] == ')' and stack[-1][0] == '(':
                new_beg = stack.pop()[1]
                if not stack:
                    new_beg = 0
                elif stack[-1][1] + 1 < new_beg:
                    new_beg = stack[-1][1] + 1
                if i - new_beg + 1 > max_len:
                    beg, end = new_beg, i
                    max_len = end - beg + 1
            else:
                stack.append((s[i], i))
        return max_len