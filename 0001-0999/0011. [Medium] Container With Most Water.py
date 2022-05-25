# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, nums: List[int]) -> int:
        a = 0
        b = len(nums)-1
        max = 0
        while a <= b:
            if nums[a] <= nums[b]:
                temp = nums[a] * abs(b-a)
                a += 1
            else:
                temp = nums[b] * abs(b-a)
                b -= 1
            if temp > max:
                max = temp
        return max