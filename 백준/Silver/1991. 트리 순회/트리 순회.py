from collections import defaultdict


class Node:
    def __init__(self, par, left = None, right = None):
        self.par = par
        self.left = left
        self.right = right

def make_tree(arr):
    dic = defaultdict()
    dic["."] = None
    for node in arr:
        newNode = Node(node[0])
        dic[node[0]] = newNode

    for node in arr:
        dic[node[0]].left = dic[node[1]]
        dic[node[0]].right = dic[node[2]]

    return dic[arr[0][0]]

def preorder(node):
    if node is None:
        return
    print(node.par, end='')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.par, end='')
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.par, end='')

n = int(input())
arr = [ input().split() for _ in range(n)]
t = make_tree(arr)
preorder(t)
print()
inorder(t)
print()
postorder(t)