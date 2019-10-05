class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""

        traversal = []
        
        self.preorder_print(self.root, traversal)

        return '-'.join(str(k) for k in traversal)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""

        node = start

        if node.value == find_val:
            return True
        
        if node.left is not None:
            return self.preorder_search(node.left, find_val)

        if node.right is not None:
            return self.preorder_search(node.right, find_val)

        if node.left is None and node.right is None:
            return False

        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""

        node = start

        traversal.append(node.value)
        
        if node.left is not None:
            self.preorder_print(node.left, traversal)

        if node.right is not None:
            self.preorder_print(node.right, traversal)

        if node.left is None and node.right is None:
            return 

        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()