# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        char_dict={}
        ans=0
        while j<len(s):
            if s[j] in char_dict and char_dict[s[j]]>=i:
                ans=max(ans,j-i)
                i=char_dict[s[j]]+1
            char_dict[s[j]]=j
            j+=1
        ans=max(ans,j-i)
        return ans