def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapChildNode(current)
        queue.append(current.left)
        queue.append(current.right)


def swapChildNode(node):
    node.right, node.left = node.left, node.right


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
