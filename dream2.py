class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None
        # self.parent = None

def swap_nodes(root, v):
    """
    Перебирает узлы, выполняет обмен,
    обновляя ссылки.
    """
    if not root:
        return
    if root.num == v:
        return
    if root.left:
        if root.left.num == v:
            # root.left.parent, root.parent = root.parent, root.left.parent
            # root.left.left, root.left = root.left, root.left.left
            root.num, root.left.num = root.left.num, root.num
            root.right.num, root.left.right.num = root.left.right.num, root.right.num
        else:
            swap_nodes(root.left, v)
    if root.right:
        if root.right.num == v:
            # root.right.parent, root.parent = root.parent, root.right.parent
            # root.right.right, root.right = root.right, root.right.right
            root.num, root.right.num = root.right.num, root.num
            root.left.num, root.right.left.num = root.right.left.num, root.left.num
        else:
            swap_nodes(root.right, v)

def in_order_traversal(root):
    """
    Обходит дерево, возвращает список строк,
    представляющих номера узлов.
    """
    res = []
    if root:
        res = in_order_traversal(root.left)
        res.append(str(root.num))
        res += in_order_traversal(root.right)
    return res

# Чтение входных данных
N, Q = map(int, input().split())
swaps = list(map(int, input().split()))

# Создание дерева
nodes = [Node(i+1) for i in range(N)]
root = nodes[0]
for i in range(N):
    if 2*i + 1 < N:
        nodes[i].left = nodes[2*i + 1]
        # nodes[2*i + 1].parent = nodes[i]
    if 2*i + 2 < N:
        nodes[i].right = nodes[2*i + 2]
        # nodes[2*i + 2].parent = nodes[i]

# Применение всех обменов
for swap in swaps:
    swap_nodes(root, swap)

# Вывод результата
result = in_order_traversal(root)
print(" ".join(result))
