# 백준 - 골드1 - 수들의 합 7 - 2268 - 세그먼트 트리 문제
'''
세그먼트 트리 문제

command 에서 a의 상태의 따라 아래와 같이 처리한다
0 : Sum 함수
1 : Modify 함수

PyPy3로 제출해야 한다.

전에 풀었던 다른 세그먼트 트리 문제와 똑같이 풀었다. (단, 이 문제에선 arr가 0으로 초기화 되기 때문에 build 함수를 작성하지 않았다.)
풀이 과정은 아래 파일 상단에 적혀있다.
 백준 - 구간 곱 구하기 - 11505
 백준 - 구간 합 구하기 - 2042
 백준 - 최솟값 - 10868

전에 풀던 방식으로 구현한 후 예제에 있는 입력들에 대해서도 통과한 뒤 제출했는데 '틀렸습니다.'가 나왔다.
이유를 모르겠어서 문제를 다시 살펴보니 다음과 같은 내용이 있었다.
  -  i > j일 경우에는 A[j] + A[j+1] + ... + A[i]
해당 부분을 처리한 뒤 제출하니까 통과했다.
'''

import sys; input = sys.stdin.readline

n, m = map(int, input().split())
command = [ list(map(int, input().split())) for _ in range(m) ]

# 테스트
# n, m = 3, 5
# command = [
#     [0,1,3],
#     [1,1,2],
#     [1,2,3],
#     [0,2,3],
#     [0,1,3]
# ] # 0  \  3  \  5

tree = [0] * n * 4

def merge(left, right):
    return left + right

def modify(index, new_value, node, node_left, node_right):
    if index < node_left or index > node_right:
        return tree[node]
    if node_left == node_right:
        tree[node] = new_value
        return tree[node]

    mid = (node_left + node_right) // 2
    left_value = modify(index, new_value, node * 2, node_left, mid)
    right_value = modify(index, new_value, node * 2 + 1, mid + 1, node_right)
    tree[node] = merge(left_value, right_value)
    return tree[node]

def sum_func(left, right, node, node_left, node_right):
    if right < node_left or left > node_right:
        return 0
    if left <= node_left and right >= node_right:
        return tree[node]

    mid = (node_left + node_right) // 2
    left_value = sum_func(left, right, node * 2, node_left, mid)
    right_value = sum_func(left, right, node * 2 + 1, mid + 1, node_right)
    return merge(left_value, right_value)

for i in command:
    a, b, c = i

    if a == 0:
        if b > c: # 문제의 조건 중 'i > j' 일 경우에 대한 분기 처리
            b, c = c, b
            print(sum_func(b - 1, c - 1, 1, 0, n - 1))
        else:
            print(sum_func(b - 1, c - 1, 1, 0, n - 1))
    elif a == 1:
        modify(b - 1, c, 1, 0, n - 1)
