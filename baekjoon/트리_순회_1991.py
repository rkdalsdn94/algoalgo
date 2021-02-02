'''
input 
    7
    A B C
    B D .
    C E F
    E . .
    F . G
    D . .
    G . .

result
    ABDCEFG 전위(pre_order)
    DBAECFG 중위(in_order)
    DBEGFCA 후위(post_order)
'''

class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

n = int(input())
tree = dict()

for _ in range(n):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

def pre_order(node):
    print(node.data, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])
def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        in_order(tree[node.right])
def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.data, end='')

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])