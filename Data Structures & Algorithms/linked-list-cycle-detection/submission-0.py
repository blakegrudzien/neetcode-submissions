# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        key = set()
        tmp = head

        while tmp != None:
            if tmp in key:
                return True
            else:
                key.add(tmp)
            tmp = tmp.next
        return False
        