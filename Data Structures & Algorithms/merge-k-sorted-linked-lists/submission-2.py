# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [l for l in lists if l]
        if not lists:
            return None
        fringe = []
        
     
        for node in lists:
            if node:
                heapq.heappush(fringe,(node.val,id(node), node))
        
        temp_val, temp_id, temp = heapq.heappop(fringe)
        head = temp
        if head.next:
            heapq.heappush(fringe, (head.next.val, id(head.next), head.next))

        
        slow = head
        fast = slow.next

        while fringe:

            temp_val,temp_id, fast= heapq.heappop(fringe)
            if fast.next:
                heapq.heappush(fringe, (fast.next.val,id(fast.next),fast.next))
            slow.next = fast
            slow = slow.next
        
        return head




        
        