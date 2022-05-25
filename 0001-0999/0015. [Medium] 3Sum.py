# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            s1=set()
            lst=[]
            for i in range(len(nums)):
                target=-nums[i]
                s={}
                for j in range(i+1,len(nums)):
                    if nums[j] in s:
                        p=[nums[i],target-nums[j],nums[j]]
                        p.sort()
                        t=tuple(p)
                        if t not in s1:
                            s1.add(t)
                            lst.append([nums[i],target-nums[j],nums[j]])

                    else:
                        s[target-nums[j]]=j
            return lst