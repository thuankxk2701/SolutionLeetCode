# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            h=[]
            for i in lists:
                while i:
                    heapq.heappush(h, i.val)
                    i=i.next

            head = ans = ListNode() 
            while h:
                head.next=ListNode(heapq.heappop(h))
                head=head.next
            return ans.next