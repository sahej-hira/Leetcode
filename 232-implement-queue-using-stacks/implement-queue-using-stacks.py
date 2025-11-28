class MyQueue:

    def __init__(self):
        self.s = [] # stack: to push into
        self.rs = [] # reverse stack: to pop from
        

    def push(self, x: int) -> None:
        self.s.append(x)
        
        

    def pop(self) -> int:
        if not self.rs:
            while self.s:
                val = self.s.pop()
                self.rs.append(val)
        return self.rs.pop()
        

    def peek(self) -> int:  
        if not self.rs:
            while self.s:
                val = self.s.pop()
                self.rs.append(val)
        return self.rs[-1]       # we sont want to pop just peek 

    def empty(self) -> bool:
        if not self.s and not self.rs:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()