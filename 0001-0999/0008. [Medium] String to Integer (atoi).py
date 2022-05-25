# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0 
        sign = 1
        idx = 0 
        n = len(s)
        MAX= 2**31 - 1
        MIN=-2**31        
        while idx < n and s[idx] == " ":
            idx += 1         
        if idx < n and s[idx] in "+-":
            sign = 1 if s[idx] == "+" else -1
            idx += 1             
        while idx < n and s[idx].isdigit():
            ans = ans*10 + int(s[idx])
            idx += 1            
        if sign*ans > MAX: 
            return MAX        
        if sign*ans < MIN: 
            return MIN        
        return sign*ans