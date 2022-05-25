# https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n, result = len(nums), set()
        def backtrack(idx):
            if idx == n:
                result.add(tuple(nums))
                return
            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
            return result
        return backtrack(0)