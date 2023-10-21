class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

def swap_nodes(root, v):
    """
    Перебирает узлы, выполняет обмен,
    обновляя ссылки.
    """
    if not root:
        return
    if root.num == v:
        # root.left, root.right = root.right, root.left
        return
    if root.left:
        if root.left.num == v:
            root.left, root.right, root.left.left, root.left.right = root.right, root.left, root.left.right, root.left.left
        swap_nodes(root.left, v)
    if root.right:
        if root.right.num == v:
            root.left, root.right, root.right.left, root.right.right = root.right, root.left, root.right.right, root.right.left
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
    if 2*i + 2 < N:
        nodes[i].right = nodes[2*i + 2]

# Применение всех обменов
for swap in swaps:
    swap_nodes(root, swap)

# Вывод результата
result = in_order_traversal(root)
print(" ".join(result))
