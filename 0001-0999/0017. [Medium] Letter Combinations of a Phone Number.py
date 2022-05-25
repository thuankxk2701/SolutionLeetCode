# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length=len(digits)
        if length==0:
            return []
        result=[]
        maps=['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def Helper(idx,currString):
            if idx==length:
                result.append(currString[:])
                return
            for char in maps[int(digits[idx])]:
                Helper(idx+1,currString+char)

        Helper(0,"")
        return result