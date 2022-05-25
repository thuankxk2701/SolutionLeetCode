# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, val in enumerate(nums):
            if target - val in values:
                return [values[target-val], idx]
            else:
                values[val] = idx