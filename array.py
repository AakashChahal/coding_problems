class Array:
    def __init__(self) -> None:
        self.len = 0
        self.data = {}

    def get(self, ind):
        return self.data[ind]

    def push(self, val):
        self.data[self.len]  = val
        self.len += 1 
        return self # ? to make the methods chainable

    def pop(self):
        self.len -= 1
        last = self.data[self.len]
        del self.data[self.len]
        return last


arr1 = Array()
print(arr1.push("Hello").get(0))
arr1.push("world!")
print(arr1.get(1))
print(arr1.pop())