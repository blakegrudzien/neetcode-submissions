# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        head = head.next

        while head and head.next:
            if head == slow:
                return True
            head = head.next.next
            slow = slow.next
        return False
        