# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        retList = []
        if(length==1):
            return [nums]
        if(length==2):
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
        for i in range(length):
            perm = self.permute(nums[:i]+nums[i+1:])
            for lis in perm:
                retList.append([nums[i]] + lis)
        return retList