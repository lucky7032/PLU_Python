class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c

d = Node(25)
d.next = c
b.next = d

node = a
while node:
    print(node.data, end=" ")
    node = node.next