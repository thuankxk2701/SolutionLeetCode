# https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        presentnums = set()
        for num in nums:
            if num > 0:
                presentnums.add(num)
        i = 1
        while True:
            if i not in presentnums:
                return i            
            i += 1        
        return -1