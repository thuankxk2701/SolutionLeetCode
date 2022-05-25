# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer= ListNode()
        tempt=answer
        while list1 and list2:
            if list1.val< list2.val:
                tempt.next=list1
                list1=list1.next
            else:
                tempt.next=list2
                list2=list2.next
            tempt=tempt.next
        if (list1): tempt.next=list1
        if (list2): tempt.next=list2
        return  answer.next