# 백준 - 골드1 - 구간 합 구하기 - 2042 - 세그먼트 트리 문제
'''
세그먼트 트리 문제

세그먼트 트리 문제이다.
https://www.youtube.com/watch?v=ahFB9eCnI6c C++로 세그먼트 트리를 설명하는 영상인데, 해당 영상을 통해 공부하고 문제를 풀었다.
merge_sort를 구현할 때랑 비슷하게 리스트를 절반씩 쪼개면서 두 수의 합을 tree에 추가하면 된다. 그 과정에서 재귀로 빡세게 구현하는 문제다.
아래 코드가 이해가 잘 안되면 위에 유투브 영상을 보고 난 후, 아래 코드를 공책에 직접 그려보면서 분석하면 이해가 된다.
'''

import sys; input = sys.stdin.readline

n, m, k = map(int, input().split())
n_list = [ int(input()) for _ in range(n) ]
command = [ list(map(int, input().split())) for _ in range(m + k) ]

# 테스트
# n, m, k = 5, 2, 2
# n_list = [1,2,3,4,5]
# command = [ [1, 3, 6], [2, 2, 5], [1, 5, 2], [2, 3, 5] ] # 17  \  12

tree = [0] * n * 4

def build(arr, node, node_left, node_right):
    if node_left == node_right:
        tree[node] = arr[node_left]
        return tree[node]

    mid = (node_left + node_right) // 2
    left_value = build(arr, node * 2, node_left, mid)
    right_value = build(arr, node * 2 + 1, mid + 1, node_right)
    tree[node] = left_value + right_value
    return tree[node]

def update(index, new_value, node, node_left, node_right):
    if index < node_left or index > node_right:
        return tree[node]
    if node_left == node_right:
        tree[node] = new_value
        return tree[node]

    mid = (node_left + node_right) // 2
    left_value = update(index, new_value, node * 2, node_left, mid)
    right_value = update(index, new_value, node * 2 + 1, mid + 1, node_right)
    tree[node] = left_value + right_value
    return tree[node]

def query(left, right, node, node_left, node_right):
    if right < node_left or left > node_right:
        return 0
    if left <= node_left and right >= node_right:
        return tree[node]

    mid = (node_left + node_right) // 2
    left_value = query(left, right, node * 2, node_left, mid)
    right_value = query(left, right, node * 2 + 1, mid + 1, node_right)
    return left_value + right_value

build(n_list, 1, 0, n - 1)
for i in command:
    a, b, c = i

    if a == 1:
        update(b - 1, c, 1, 0, n - 1)
    elif a == 2:
        print(query(b - 1, c - 1, 1, 0, n - 1))
