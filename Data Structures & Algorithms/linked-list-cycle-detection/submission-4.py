# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        key = set()
        if not head:
            return False

        while head.next:
            if head in key:
                return True
            key.add(head)
            head = head.next
        return False
        