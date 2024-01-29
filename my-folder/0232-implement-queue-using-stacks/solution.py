class MyQueue:

    def __init__(self):
        self.st = []
        self.t = []

    def push(self, x: int) -> None:
        while self.st:
            self.t.append(self.st.pop())
        self.st.append(x)
        while self.t:
            self.st.append(self.t.pop())

    def pop(self) -> int:
        return self.st.pop()

    def peek(self) -> int:
        return self.st[-1]

    def empty(self) -> bool:
        return not self.st


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
