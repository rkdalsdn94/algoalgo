# 백준 - 골드1 - 최솟값 - 10868 - 세그먼트 트리, 희소 배열 문제
'''
세그먼트 트리, 희소 배열 문제

이 전에 푼 세그먼트 트리 문제인 '구간 합 구하기(2042)', '구간 곱 구하기(11505)' 문제랑 똑같이 풀면 된다.
위의 두 문제는 update 도 신경써야 되지만, 이 문제에선 update 부분이 없다.
구간에 대해 query 만 날려 출력하면 된다. '구간 곱 구하기' 문제에서 풀었듯이 merge 부분을 min으로 return 하면 된다.
'''

import sys; input=sys.stdin.readline

n, m = map(int, input().split())
n_list = [ int(input()) for _ in range(n) ]
command = [ list(map(int, input().split())) for _ in range(m) ]

# 테스트
# n, m = 10, 4
# n_list = [ 75, 30, 100, 38, 50, 51, 52, 20, 81, 5 ]
# command = [ [1, 10], [3, 5], [6, 9], [8, 10] ] # 5  \  38  \  20  \  5

tree = [0] * n * 4

def merge(left, right):
    return min(left, right)

def build(arr, node, node_left, node_right):
    if node_left == node_right:
        tree[node] = n_list[node_left]
        return tree[node]

    mid = (node_left + node_right) // 2
    left_value = build(arr, node * 2, node_left, mid)
    right_value = build(arr, node * 2 + 1, mid + 1, node_right)
    tree[node] = merge(left_value, right_value)
    return tree[node]

def query(left, right, node, node_left, node_right):
    if left > node_right or right < node_left:
        return int(1e9)
    if left <= node_left and right >= node_right:
        return tree[node]

    mid = (node_left + node_right) // 2
    left_value = query(left, right, node * 2, node_left, mid)
    right_value = query(left, right, node * 2 + 1, mid + 1, node_right)
    return merge(left_value, right_value)

build(n_list, 1, 0, n - 1)
for i in command:
    a, b = i
    print(query(a - 1, b - 1, 1, 0, n - 1))
