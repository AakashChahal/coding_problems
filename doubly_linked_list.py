class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, val) -> None:
        self.head = Node(val)
        self.tail = self.head
        self.length = 1

    def add(self, val):
        nextData = Node(val)
        if self.head == self.tail:
            nextData.prev = self.head
            self.head.next = nextData
            self.tail = nextData
            self.length += 1

        else:
            nextData.prev = self.tail
            self.tail.next = nextData
            self.tail = nextData
            self.length += 1

        return self

    def insert(self, index, val):
        if index >= self.length:
            return self.add(val)
        newData = Node(val)
        if index == 0:
            newData.next = self.head
            newData.prev = None
            self.head = newData

        else:
            temp = self.head
            prev = None
            for i in range(1, index+1):
                temp = temp.next
                if i == index - i:
                    prev = temp
            
            newData.next = temp
            prev.next = newData
            newData.prev = prev

        return self

    def prepend(self, val):
        self.insert(0, val)
        return self

    def display(self):
        temp = self.head
        while temp:
            # print("One:", temp["data"])
            yield temp.data
            temp = temp.next

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            temp = self.head
            self.head = temp.next
            self.length -= 1
            del temp

        else:
            temp = self.head
            print(index)
            for i in range(1, index+1):
                temp = temp.next
                print(i, temp.data)
                # if i == index == 1:
                #     self.head.next = temp.next
                #     temp.prev = self.head
                if i == index:
                    print("entered")
                    print(temp.data, temp.prev.data, temp.next.data)
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    del temp
                    self.length -= 1

        return self


ll = LinkedList(20)
ll.add(30)
ll.add(50)
ll.add(60)
ll.insert(index=2, val=40)
ll.prepend(10)
print(list(ll.display()))
ll.remove(2)
print(list(ll.display()))
ll.remove(3)
print(list(ll.display()))
# ll.remove(4)
# print(list(ll.display()))

    