class MyStack:
    def __init__(self):
        self.arr1 = []
        self.arr2 = []
        self.topi = -1

    def push(self, x: int) -> None:
        self.arr1.append(x)
        self.topi += 1

    def pop(self) -> int:
        if self.topi == -1:
            return -1
        leng = len(self.arr1)
        for i in self.arr1[: leng - 1]:
            self.arr1.pop(0)
            self.arr2.append(i)
        self.arr1 += self.arr2
        self.topi -= 1
        return self.arr1.pop(0)

    def top(self) -> int:
        leng = len(self.arr1)
        if self.topi == -1:
            return -1
        return self.arr1[self.topi]

    def empty(self) -> bool:
        if self.topi == -1:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
