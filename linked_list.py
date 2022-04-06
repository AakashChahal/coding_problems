class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self, val) -> None:
        self.head = Node(val)
        self.tail = self.head
        self.length = 1

    def add(self, val):
        nextData = Node(val)
        if self.head == self.tail:
            self.head.next = nextData
            self.tail = nextData
            self.length += 1

        else:
            self.tail.next = nextData
            self.tail = nextData
            self.length += 1

    def insert(self, index, val):
        newData = Node(val)
        if index == 0:
            newData.next = self.head
            self.head = newData

        else:
            temp = self.head
            prev = None
            for i in range(1, index+1):
                temp = temp.next
                if i == index - 2:
                    prev = temp.next
            
            newData.next = temp
            prev.next = newData

    def prepend(self, val):
        self.insert(0, val)

    def display(self):
        temp = self.head
        while temp:
            # print("One:", temp["data"])
            yield temp.data
            temp = temp.next


ll = LinkedList(20)
ll.add(30)
ll.add(40)
ll.add(60)
ll.insert(index=3, val=50)
ll.prepend(10)
print(list(ll.display()))

    