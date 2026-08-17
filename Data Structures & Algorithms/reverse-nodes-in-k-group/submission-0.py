# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        furthest = head
        slow = None
        fast = head.next
        current = head
        front = head

        for i in range(k-1):
                if not furthest:
                    return head
                furthest = furthest.next
        head = furthest
        

        while head:
            while fast and current != furthest:
                current.next = slow
                slow = current
                current = fast
                fast = fast.next
            current.next = slow
            slow = None 
            current = fast
            if not fast:
                return head
            fast = fast.next
            furthest = current
            
           # if furthest:
           #     furthest = furthest.next
           # else:
           #     return head
           # slow = None

            for i in range(k-1):
                furthest = furthest.next
                if not furthest:
                    front.next = current
                    return head
                
            print(furthest.val)
            

            front.next = furthest
            front = current
            
            
            
        return head
                



        

        