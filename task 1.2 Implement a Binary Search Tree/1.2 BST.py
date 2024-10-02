class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if root.val == key:
            return root
        if root.val < key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)
        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.val, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val, end=" ")

    def find(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.find(root.left, key)
        else:
            return self.find(root.right, key)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            succ = self.find_min(root.right)
            root.val = succ.val
            root.right = self.delete(root.right, succ.val)
        return root

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        if root is None:
            return True

        lh = self.height(root.left)
        rh = self.height(root.right)

        if abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True

        return False

    def print_nodes_at_depth(self, root, depth):
        if root is None:
            return
        if depth == 0:
            print(root.val, end=" ")
        else:
            self.print_nodes_at_depth(root.left, depth - 1)
            self.print_nodes_at_depth(root.right, depth - 1)

    def print_tree_structure(self, root, space=0, level_space=5):
        if root is None:
            return
        
        # Increase distance between levels
        space += level_space
        
        # Process right child first (to print from top down)
        self.print_tree_structure(root.right, space)
        
        # Print current node after space count
        print()
        for i in range(level_space, space):
            print(" ", end="")
        print(root.val)
        
        # Process left child
        self.print_tree_structure(root.left, space)


# Test code
bst = BinarySearchTree()
bst.root = bst.insert(bst.root, 50)
bst.root = bst.insert(bst.root, 30)
bst.root = bst.insert(bst.root, 20)
bst.root = bst.insert(bst.root, 40)
bst.root = bst.insert(bst.root, 70)
bst.root = bst.insert(bst.root, 60)
bst.root = bst.insert(bst.root, 80)

print("In-order traversal:")
bst.inorder_traversal(bst.root)
print()

print("Pre-order traversal:")
bst.preorder_traversal(bst.root)
print()

print("Post-order traversal:")
bst.postorder_traversal(bst.root)
print()

print("Find 40 in the BST:")
node = bst.find(bst.root, 40)
print("Found" if node else "Not found")

# Print the tree structure
print("\nTree structure:")
bst.print_tree_structure(bst.root)

if bst.isBalanced(bst.root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")

print("Height of the tree:", bst.height(bst.root))

depth = 0
print(f"Nodes at depth {depth}:")
bst.print_nodes_at_depth(bst.root, depth)
print()

