# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        stack = []
        for num in arr:
            while stack and num > stack[-1]:
                stack.pop()
            stack.append(num)  
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        for num in stack:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

            
        
        
        f