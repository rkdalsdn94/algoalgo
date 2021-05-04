'''
in
    9
    -1 0 0 2 2 4 4 6 6
    4
out
    2
'''
from sys import stdin
input = stdin.readline

n = int(input())
parent_node = list(map(int, input().split()))
del_node = int(input())
tree = {}
res = 0

for i in range(n):
    if i == del_node or parent_node[i] == del_node:
        continue
    if parent_node[i] in tree:
        tree[parent_node[i]].append(i)
    else:
        tree[parent_node[i]] = [i]

if -1 in tree:
    temp = [-1]
else:
    temp = []
while temp:
    node = temp.pop()
    if node not in tree:
        res += 1
    else:
        temp += tree[node]
print(res)
