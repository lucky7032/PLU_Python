class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)

a.next = b
b.next = c
c.next = d
d.next = e

count = 0
node = a

while node:
    count = count + 1
    node = node.next

print("Total number of nodes:", count)