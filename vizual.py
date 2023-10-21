# пример визуализации дерева
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def plot_tree(root, x, y, dx, dy):
    if root is None:
        return

    plt.text(x, y, root.val, fontsize=12, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

    if root.left is not None:
        plt.plot([x, x - dx], [y - dy, y - 1], 'k-')
        plot_tree(root.left, x - dx, y - 1, dx / 2, dy)
          
    if root.right is not None:
        plt.plot([x, x + dx], [y - dy, y - 1], 'k-')
        plot_tree(root.right, x + dx, y - 1, dx / 2, dy)


# Создаем дерево и добавляем элементы
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# Визуализируем дерево
fig, ax = plt.subplots()
plt.axis('off')
plot_tree(root, 0, 0, 3, 3)
plt.show()