class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    # Height of the node
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    # Balance factor
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    # Right rotation
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    # Left rotation
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    # Insert node
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        # Balance the tree
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    # Find the node with the minimum key
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)
    # Delete node
    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        # Balance the tree
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    # Search node
    def search(self, root, key):
        if not root:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
    # Inorder traversal (Left, Root, Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
    # Return sorted list via inorder
    def inorder_list(self, root, result=None):
        if result is None:
            result = []
        if root:
            self.inorder_list(root.left, result)
            result.append(root.key)
            self.inorder_list(root.right, result)
        return result
    # Count total nodes
    def count_nodes(self, root):
        if not root:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
if __name__ == "__main__":
    avl = AVLTree()
    root = None
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            key = int(input("Enter key to insert: "))
            root = avl.insert(root, key)
            print("Inserted.")
        elif choice == "2":
            key = int(input("Enter key to delete: "))
            root = avl.delete(root, key)
            print("Deleted (if key existed).")
        elif choice == "3":
            key = int(input("Enter key to search: "))
            found = avl.search(root, key)
            print("Found!" if found else "Not .")
        elif choice == "4":
            print("Inorder Traversal:")
            avl.inorder(root)
            print()
        elif choice == "5":
            sorted_list = avl.inorder_list(root)
            print("Sorted elements:", sorted_list)
        elif choice == "6":
            count = avl.count_nodes(root)
            print("Total number of nodes:", count)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
