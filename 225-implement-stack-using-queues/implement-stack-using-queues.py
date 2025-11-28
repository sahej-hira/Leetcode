class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))
        required_val = self.q1.pop()
        self.q1,self.q2 = self.q2,self.q1   # swap the queues
        return required_val

        

    def top(self) -> int:
        return self.q1[-1]
        

    def empty(self) -> bool:
        if max(len(self.q1),len(self.q2)) <= 0 :
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()