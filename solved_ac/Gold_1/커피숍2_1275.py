# 백준 - 골드1 - 커피숍2 - 1275 - 세그먼트 트리 문제
'''
세그먼트 트리 문제

세그먼트 트리를 구성하는 방법을 알면 쉽게 풀 수 있다. 구성하는 방법을 모르면
'백준 - 구간 합 구하기(2042)'에서도 적혀있듯이 https://www.youtube.com/watch?v=ahFB9eCnI6c 해당 영상에서 공부하면 된다.

단, 조심해야 하는 부분은 a가 b보다 클 때 a와 b의 값을 서로 바꿔줘야 한다. ('이 문제에서는 x > y인 경우 y번째 부터 x번째이다.')
이 부분만 조심하고 '구간 합 구하기' 문제랑 똑같이 풀면 된다.
'''

import sys; input=sys.stdin.readline

n, q = map(int, input().split())
n_list = list(map(int, input().split()))
command = [ list(map(int, input().split())) for _ in range(q) ]

# 테스트
# n, q = 5, 2
# n_list = [1,2,3,4,5]
# command = [ [2,3,3,1], [3,5,4,1] ] # 5  \  10

tree = [0] * n * 4

def merge(left, right):
    return left + right

def build(arr, node, left_node, right_node):
    if left_node == right_node:
        tree[node] = arr[left_node]
        return tree[node]
    
    mid = (left_node + right_node) // 2
    left_value = build(arr, node * 2, left_node, mid)
    right_value = build(arr, node * 2 + 1, mid + 1, right_node)
    tree[node] = merge(left_value, right_value)
    return tree[node]

def query(left, right, node, left_node, right_node):
    if left > right_node or right < left_node:
        return 0
    if left <= left_node and right >= right_node:
        return tree[node]
    
    mid = (left_node + right_node) // 2
    left_value = query(left, right, node * 2, left_node, mid)
    right_value = query(left, right, node * 2 + 1, mid + 1, right_node)
    return merge(left_value, right_value)

def update(idx, new_value, node, left_node, right_node):
    if idx > right_node or idx < left_node:
        return tree[node]
    if left_node == right_node:
        tree[node] = new_value
        return tree[node]
    
    mid = (left_node + right_node) // 2
    left_value = update(idx, new_value, node * 2, left_node, mid)
    right_value = update(idx, new_value, node * 2 + 1, mid + 1, right_node)
    tree[node] = merge(left_value, right_value)
    return tree[node]

build(n_list, 1, 0, n - 1)
for i in command:
    a, b, c, d = i

    if a > b:
        a, b = b, a
    print(query(a - 1, b - 1, 1, 0, n - 1))
    update(c - 1, d, 1, 0, n - 1)
