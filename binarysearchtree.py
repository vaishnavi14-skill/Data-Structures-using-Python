class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current
def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root
root = None
for key in [50, 30, 20, 40, 70, 60, 80]:
    root = insert(root, key)

print("Inorder traversal after insertion:")
inorder(root)
print()
key_to_search = 40
found = search(root, key_to_search)
print(f"Search for {key_to_search}: {'Found' if found else 'Not Found'}")
key_to_delete = 30
root = delete(root, key_to_delete)
print(f"Inorder traversal after deleting {key_to_delete}:")
inorder(root)
print()
print("Postorder traversal after deleting", key_to_delete)
postorder(root)
print()
