class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(10)
root.right = Node(30)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("Inorder Traversal:")
inorder(root)