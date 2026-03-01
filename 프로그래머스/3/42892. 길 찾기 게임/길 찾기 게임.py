import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    class Node:
        def __init__(self, x, y, idx):
            self.x = x
            self.y = y
            self.idx = idx
            self.left = None
            self.right = None
    
    def make_tree():
        nodes = []
        for i, (x, y) in enumerate(nodeinfo):
            new_node = Node(x, y, i + 1)
            nodes.append(new_node)
        
        nodes.sort(key = lambda n: (-n.y, n.x))
        
        root = nodes[0]
        
        def insert(parent, child):
            if child.x < parent.x:
                if parent.left is None:
                    parent.left = child
                else:
                    insert(parent.left, child)
            else:
                if parent.right is None:
                    parent.right = child
                else:
                    insert(parent.right, child)
                
        
        for node in nodes[1:]:
            insert(root, node)
        return root
    tree = make_tree()
    pre = []
    post = []
    def preorder(node):
        if node == None:
            return
        pre.append(node.idx)
        preorder(node.left)
        preorder(node.right)
    
    def postorder(node):
        if node == None:
            return
        postorder(node.left)
        postorder(node.right)
        post.append(node.idx)
    preorder(tree)
    postorder(tree)
    return [pre, post]
