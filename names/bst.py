class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, node):
        if node.value < self.value:
            if not self.left:
                self.left = node
            else:
                self.left.insert(node)
        if node.value > self.value:
            if not self.right:
                self.right = node
            else:
                self.right.insert(node)
    
    def contains(self, value):
        if self.value == value:
            return True
        
        if value < self.value:
            if not self.left:
                return False
            return self.left.contains(value)
        if value > self.value:
            if not self.right:
                return False
            return self.right.contains(value)
        

bst = BSTNode(8)
bst.insert(BSTNode(4))
bst.insert(BSTNode(6))
bst.insert(BSTNode(12))
bst.insert(BSTNode(3))
bst.insert(BSTNode(5))

