# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
     def longestPalindrome(self, s: str) -> str:
            max_str = ""
            ptr = 0
            while ptr < len(s):
                # consider odd str
                l = ptr-1
                r = ptr+1
                while (l>=0 and r < len(s)) and (s[l] == s[r]):
                    l -= 1
                    r += 1
                if r-l > len(max_str):
                    max_str = s[l+1: r]
                # now the even case
                l=ptr
                r = ptr + 1
                while (l>=0 and r<len(s)) and (s[l]==s[r]):
                    l -= 1
                    r += 1
                if r-l > len(max_str):
                    max_str = s[l+1: r]
                ptr += 1
            return max_str