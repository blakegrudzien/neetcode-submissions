class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.curr_min:
            self.curr_min.append(min(self.curr_min[-1],val))
        else:
            self.curr_min.append(val)
   

    def pop(self) -> None:
        self.stack.pop()
        self.curr_min.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.curr_min[-1]
        
