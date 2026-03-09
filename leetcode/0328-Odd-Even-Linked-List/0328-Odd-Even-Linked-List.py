# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odds = head
        even = head.next
        evens = even
        while even and even.next:
            odds.next = even.next
            even.next = even.next.next
            odds = odds.next
            even = even.next
        odds.next = evens
        return head