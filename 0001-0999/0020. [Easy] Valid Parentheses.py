# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == "[" or char == "{": stack.append(ord(char))
            else:
                if not stack: return False
                else:
                    val = ord(char) - stack.pop()
                    if val != 1 and val != 2: return False
        return False if stack else True