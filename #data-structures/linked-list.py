# Linked List
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def printList(self):
        print(self.value)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head.next.next.printList()
