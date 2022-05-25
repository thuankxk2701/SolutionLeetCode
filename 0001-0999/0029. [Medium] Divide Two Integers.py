# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def cal_cnt(dd,vv):            
            tempvv=vv
            cnt=1
            hashmap={}
            hashmap[tempvv]=cnt
            while True:
                if dd >= tempvv+tempvv:
                    cnt=cnt+cnt
                    tempvv=tempvv+tempvv
                    hashmap[tempvv]=cnt
                else:
                    break
            print(hashmap)
            cnt=0
            while dd >= vv:
                maxsub = max([x for x in hashmap.keys() if x <= dd])
                dd -=maxsub
                cnt+= hashmap[maxsub]
            return cnt
        if dividend*divisor >0:            
            return min(2**31-1, cal_cnt(abs(dividend), abs(divisor)))
        else:
            return max(-2**31, -cal_cnt(abs(dividend), abs(divisor)))