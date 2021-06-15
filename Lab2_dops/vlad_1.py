def traverse(Node):
    yield Node.value
    if Node.left:
        yield from traverse(Node.left)
    if Node.right:
        yield from traverse(Node.right)


class BSTGenerator(object):

    def __init__(self, root):
        self.root = root

    def __call__(self):
        return traverse(self.root)


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


node2 = Node(3)
node = Node(4, node2)
bstGenerator = BSTGenerator(node)
for elem in bstGenerator():
    print(elem)
