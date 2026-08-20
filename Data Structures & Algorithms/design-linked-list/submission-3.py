class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        h = self.head
        print("length: " , self.length)
        while h:
            print(h.val)
            h = h.next

        if not self.head or index >= self.length:
            return -1
        
        t = self.head 
        while index > 0:
            t = t.next
            index-=1
        
        return t.val
        

    def addAtHead(self, val: int) -> None:
        h = self.head
        print("length: " , self.length)
        while h:
            print(h.val)
            h = h.next
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
            self.length+=1
            return
        
        new_head = ListNode(val)
        
        self.head.prev = new_head
        new_head.next = self.head
        self.head = new_head
        self.length +=1
        

    def addAtTail(self, val: int) -> None:
        h = self.head
        print("length: " , self.length)
        while h:
            print(h.val)
            h = h.next
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
            self.length +=1
            return

        new_tail = ListNode(val)
        new_tail.prev = self.tail
        self.tail.next = new_tail
        self.tail = new_tail

        self.length+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if not self.head or index > self.length+1:
            return -1
        
        if index == self.length:
            self.addAtTail(val)
            return

        t = self.head

        while index > 0:
            t = t.next
            index -=1

        new_node = ListNode(val)

        
        new_node.next = t
        new_node.prev = t.prev

        t.prev.next = new_node
        t.prev = new_node

        self.length +=1
        
        
            

        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        if index == self.length:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -=1

        t = self.head
        while index > 0:
            t = t.next
            index -=1

        if t != self.tail:
            t.prev.next = t.next
            t.next.prev = t.prev
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length-=1
            

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)