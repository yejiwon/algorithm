sums = []


class BinarySearch:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def branchSums(root):
    dfs(root, 0)
    return sums


def dfs(node, sumVal):
    global sums

    if node is None:
        return

    currSum = sumVal + node.value
    if node.right is None and node.left is None:
        sums.append(currSum)
        return

    dfs(node.right, currSum)
    dfs(node.left, currSum)
