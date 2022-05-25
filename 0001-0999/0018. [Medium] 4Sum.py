# https://leetcode.com/problems/4sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)        
        results = {}        
        n = len(nums)
        for a in range(n-3):
            for b in range(a+1, n-2):
                trgt = target - nums[a] - nums[b]
                c, d = b+1, n-1
                while c < d:
                    sum_val = nums[c] + nums[d]
                    if sum_val == trgt:
                        soln = [nums[a], nums[b], nums[c], nums[d]]
                        results[str(soln)] = soln
                        c += 1
                        d -= 1
                    elif sum_val < trgt:
                        c += 1
                    else:
                        d -= 1                        
        return list(results.values())