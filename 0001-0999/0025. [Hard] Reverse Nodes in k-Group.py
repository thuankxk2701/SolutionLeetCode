# https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		if head is None or head.next is None:
			return head
		if k==1:
			return head

		def has_k_nodes(cur, k):
			while cur and k:
				cur = cur.next
				k -= 1
			return k==0

		def reverse_k_nodes(cur, k):
			new_tail = cur
			prev = None
			for i in range(k): 
				nxt = cur.next
				cur.next = prev
				prev = cur
				cur = nxt
			new_head = prev
			beyond = cur
			return beyond, new_head, new_tail

		dummy_node = ListNode(0)
		prev = dummy_node
		cur = head
		while has_k_nodes(cur, k):
			beyond, new_head, new_tail = reverse_k_nodes(cur, k)
			prev.next = new_head
			cur = beyond
			prev = new_tail
		prev.next = cur
		return dummy_node.next