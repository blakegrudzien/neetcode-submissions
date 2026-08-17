# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = head
        i = 0
        while h:
            h = h.next
            i+=1
        h = head
        if i == 1:
            return None
        if i == n:
            return head.next

        for j in range(i-n-1):
            h= h.next
        print(h.val)
        if n == 1:
            h.next = None
        else:
            n = h.next.next
            h.next = n

        return head

