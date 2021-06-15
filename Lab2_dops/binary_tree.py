class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)

    def __iter__(self):
        if self.left is not None:
            yield from self.left

        yield self

        if self.right is not None:
            yield from self.right


class BSTree:
    def __init__(self, values):
        self.root = None

        for value in values:
            self.add(value)

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, value):
        if self.root is not None:
            self.root = self._delete(value, self.root)
        else:
            raise ValueError()

    def _delete(self, value, node):
        if node is None:
            return node
        elif value < node.value:
            node.left = self._delete(value, node.left)
        elif value > node.value:
            node.right = self._delete(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                to_del = self.get_min(node.right)
                node.value = to_del.value
                node.right = self._delete(to_del.value, node.right)
        return node

    def __repr__(self):
        nodes = []
        for n in BSTIterator(self.root):
            nodes.append(str(n))
        return " ".join(nodes)


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        curr = root
        while curr is not None:
            self.stack.append(curr)
            curr = curr.left

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.stack) == 0:
            raise StopIteration()
        node = self.stack.pop()
        to_ret = node
        node = node.right
        while node is not None:
            self.stack.append(node)
            node = node.left
        return to_ret


class BSTreeGenerator(object):
    def __init__(self, root):
        self.root = root

    def __iter__(self):
        return self.traverse(self.root)

    def traverse(self, node):
        if node.left is not None:
            yield from self.traverse(node.left)
        yield node
        if node.right is not None:
            yield from self.traverse(node.right)


tree = BSTree([10, 9, 3, 5, 6, 4, 2, 12, 14])
print(tree)
tree.delete(3)
for i in BSTreeGenerator(tree.root):
    print(i)
