# https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1[len(nums1):]=nums2;
        nums1.sort();
        mid=len(nums1)//2;
        result=0;
        if len(nums1)%2==0:
            result=(nums1[mid-1]+nums1[mid])/2;
        else:
            result=nums1[mid];        
        return float("{0:.5f}".format(result))