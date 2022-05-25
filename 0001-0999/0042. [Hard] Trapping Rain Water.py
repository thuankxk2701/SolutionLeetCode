# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ans=0
        maxrig=[0]*(n+1)
        for i in range(n-1,-1,-1):
            maxrig[i] = max(height[i],maxrig[i+1])       
        lmax=height[0]
        for i in range(1,n-1):
            ans += max(0, min(lmax,maxrig[i]) - height[i])
            if height[i]>lmax:
                lmax=height[i]        
        return ans