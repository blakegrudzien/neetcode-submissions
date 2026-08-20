# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        fast = head.next
        temp = head
        head.next = None
        
        while fast:
            temp = fast.next
            fast.next = head
            head = fast
            fast = temp
      
        return head
            
        