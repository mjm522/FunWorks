class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        
        def insert_recursion(node, n_val):

            if node.value < n_val:
                if node.left is None:
                    node.left = Node(n_val)
                else:
                    insert_recursion(node.left, n_val)
                return
            if node.value > n_val:
                if node.right is None:
                    node.right = Node(n_val)
                else:
                    insert_recursion(node.right, n_val)
                return

        insert_recursion(self.root, new_val)


    def search(self, find_val):
        
        def find_recursion(node, find_val):

            if node is not None:
                if node.value == find_val:
                    return True
                elif node.value < find_val:
                    return find_recursion(node.left, find_val)
                elif node.value > find_val:
                    return find_recursion(node.right, find_val)
            else:
                return False
        
        return find_recursion(self.root, find_val)
        
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)