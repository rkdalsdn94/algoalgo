# 백준 - 골드1 - 구간 곱 구하기 - 11505 - 세그먼트 트리 문제
'''
세그먼트 트리 문제

문제를 맞게 푼거 같은데 PyPy3, command를 입력 받으면서 처리하는거 모두 시간 초과가 나왔다.
왜 그런지 이해가 잘 안돼서 다른 사람들의 코드를 찾아보기 시작했는데, 구조는 모두 비슷한데 한 군데만 달랐다.
아래 코드에서 merge 할 때 다른 사람들의 코드는 % 1000000007 <-- 이 부분이 있어서 merge 하는 부분을 모두 저렇게 하니까 통과 되었다.
파이썬이 느린건 알았지만 % 1000000007 이걸 했다고 통과하는게 신기했다. 나중에 찾아보려고 한다.

문제 링크에 출력 부분을 보면 '첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지를 출력한다.' 이렇게 적혀있다... 문제를 잘 읽어야 된다.
또한, % 1000000007 부분을 찾아보는 데 재밌는 링크가 있어 아래 첨부한다.
https://sohyeonnn.tistory.com/36 위 링크를 요약하면 아래와 같다.
- 연산자 분배 법칙에 의해 mod 결과 같은 값을 도출해 내기 위함
- int overflow 방지
- 소수로 나눠진 값이므로 정확도를 높일 수 있다.

일단 풀이는 어제 풀었던 구간 곱 구하기이랑 똑같이 풀었다.
단, 이 문제는 곱을 구해야 되는 문제이므로 merge 함수에서 곱셈을 활용하고, query 함수에서 범위에 벗어나는 부분은 1로 return 했다.
합을 구하는 문제에선 merge 함수 부분을 따로 적진 않았지만 return 할 때 left_value + right_value 부분을 생각하면 된다.
'''

import sys; input=sys.stdin.readline

n, m, k = map(int, input().split())
n_list = [ int(input()) for _ in range(n) ]
command = [ list(map(int, input().split())) for _ in range(m + k) ]

# 테스트
# n, m, k = 5, 2, 2
# n_list = [ 1, 2, 3, 4, 5 ]
# command = [ [1, 3, 6], [2, 2, 5], [1, 5, 2], [2, 3, 5] ] # 240  \  48

tree = [0] * n * 4

def merge(left, right):
    return left * right % 1000000007

def build(arr, node, left_node, right_node):
    if left_node == right_node:
        tree[node] = arr[left_node]
        return tree[node]
    
    mid = (left_node + right_node) // 2
    left_value = build(arr, node * 2, left_node, mid)
    right_value = build(arr, node * 2 + 1, mid + 1, right_node)
    tree[node] = merge(left_value, right_value)
    return tree[node]

def update(index, new_value, node, left_node, right_node):
    if index > right_node or index < left_node:
        return tree[node]
    if left_node == right_node:
        tree[node] = new_value
        return tree[node]
    
    mid = (left_node + right_node) // 2
    left_value = update(index, new_value, node * 2, left_node, mid)
    right_value = update(index, new_value, node * 2 + 1, mid + 1, right_node)
    tree[node] = merge(left_value, right_value)
    return tree[node]

def query(left, right, node, left_node, right_node):
    if right < left_node or left > right_node:
        return 1
    if left <= left_node and right >= right_node:
        return tree[node]
    
    mid = (left_node + right_node) // 2
    left_value = query(left, right, node * 2, left_node, mid)
    right_value = query(left, right, node * 2 + 1, mid + 1, right_node)
    return merge(left_value, right_value)

build(n_list, 1, 0, n - 1)
for i in command:
    a, b, c = i

    if a == 1:
        update(b - 1, c, 1, 0, n - 1)
    elif a == 2:
        print(query(b - 1, c - 1, 1, 0, n - 1))
