# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def getStart(self, nums: List[int], target: int):
        left, right = 1, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (nums[mid] == target) and (nums[mid - 1] < target):
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target or (nums[mid - 1] == target):
                right = mid - 1

        if nums[right] == target:
            return right
        else:
            return -1
        
    def getStop(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 2
        while left <= right:
            mid = left + (right - left) // 2
            if (nums[mid] == target) and (nums[mid + 1] > target):
                return mid
            elif nums[mid] < target or (nums[mid + 1] == target):
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
    
        if nums[left] == target:
            return left
        else:
            return -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        return [self.getStart(nums, target), self.getStop(nums, target)]