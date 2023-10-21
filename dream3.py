class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None
        self.parent = None

def swap_nodes(root, v):
    if not root:
        return root
    if root.num == v:
        return root
    if root.left and root.left.num == v:
        root.left.parent, root.parent = root.parent, root.left.parent
        root.left.right, root.left = root.left, root.left.right
        return root
    if root.right and root.right.num == v:
        root.right.parent, root.parent = root.parent, root.right.parent
        root.right.left, root.right = root.right, root.right.left
        return root
    if root.left:
        root.left = swap_nodes(root.left, v)
    if root.right:
        root.right = swap_nodes(root.right, v)
    return root

def in_order_traversal(root):
    if not root:
        return []
    result = []
    if root.left:
        result += in_order_traversal(root.left)
    result.append(str(root.num))
    if root.right:
        result += in_order_traversal(root.right)
    return result

def main():
    N, Q = map(int, input().split())
    swaps = list(map(int, input().split()))

    nodes = [Node(i+1) for i in range(N)]
    root = nodes[0]
    for i in range(N):
        if 2*i + 1 < N:
            nodes[i].left = nodes[2*i + 1]
            nodes[2*i + 1].parent = nodes[i]
        if 2*i + 2 < N:
            nodes[i].right = nodes[2*i + 2]
            nodes[2*i + 2].parent = nodes[i]

    for swap in swaps:
        root = swap_nodes(root, swap)

    result = in_order_traversal(root)
    print(" ".join(result))

if __name__ == "__main__":
    main()
