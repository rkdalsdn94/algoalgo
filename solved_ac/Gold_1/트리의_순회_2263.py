# 백준 - 골드1 - 트리의 순회 - 2263 - 트리, 분할 정복, 재귀 문제
'''
트리, 분할 정복, 재귀 문제

재귀 풀이
메모리 361536KB 시간 3364ms

in_order = left -> root -> right
post_order = left -> right -> root
pre_order = root -> left -> right

in_order, post_order를 받아서 pre_order를 출력하는 문제이다.
다음 영상을 참고해 재귀 방식으로 풀었다.
  - https://www.youtube.com/watch?v=18ncLrRKGiM&t=70s
주의할 점으론 평소와 같이 setrecursionlimit을 10**6 이런 식으로 하면 메모리 초과, 시간 초과에 시달린다.
문제의 최대 조건인 100.000으로 실행하니 통과됐다.

풀이 과정
    1. 입력을 받는다.
    2. calc 함수를 만들어서 in_order, post_order, in_start, post_start, size를 받아서 트리를 만든다.
        2.1. size가 0보다 작거나 같으면 None을 반환한다.
        2.2. post_order의 마지막 값을 root로 설정한다.
        2.3. in_order에서 root의 인덱스를 찾는다.
        2.4. left_size는 r_idx - in_start이다.
        2.5. right_size는 size - left_size - 1이다.
        2.6. left는 calc 함수를 재귀적으로 호출한다.
        2.7. right는 calc 함수를 재귀적으로 호출한다.
        2.8. Node를 만들어서 반환한다.
    3. pre_print 함수를 만들어서 tree를 받아서 전위 순회를 출력한다.
    4. solved 함수를 만들어서 풀이를 실행한다.

in
    3
    1 2 3
    1 3 2
out
    2 1 3
'''

import sys; sys.setrecursionlimit(100000)

class Node:
    def __init__(self, root, left, right):
        self.value = root
        self.left = left
        self.right = right

def findIdx(arr, idx, target):
    while 1:
        if arr[idx] == target:
            return idx
        idx += 1

def calc(in_order, post_order, in_start, post_start, size):
    if size <= 0:
        return None

    root = post_order[post_start + size - 1]
    r_idx = findIdx(in_order, in_start, root)
    left_size = r_idx - in_start
    right_size = size - left_size - 1
    left = calc(in_order, post_order, in_start, post_start,left_size)
    right = calc(in_order, post_order, r_idx + 1, post_start + left_size,right_size)

    return Node(root, left, right)

def pre_print(tree):
    if tree == None:
        return

    print(tree.value, end=' ')
    pre_print(tree.left)
    pre_print(tree.right)

def solved():
    n = int(input())
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    tree = calc(in_order, post_order, 0, 0, n)
    pre_print(tree)

solved()

'''
반복문으로 푼 다른 사람 풀이 (훨씬 효율적)
  - 메모리 53164KB 시간 148ms

import sys
def main():
    input = sys.stdin.readline
    n = int(input())
    *inorder, = map(int, input().split())
    *post, = map(int, input().split())
    loc = [0]*(n+1)

    for i, v in enumerate(inorder):
        loc[v] = i

    stack = [(0, n, 0, n)]
    ans = []

    while stack:
        p, q, r, s = stack.pop()

        if p == q:
            continue

        q -= 1
        ans.append(post[q])
        i = loc[post[q]]
        tmp = p+i-r
        stack.append((tmp, q, i+1, s))
        stack.append((p, tmp, r, i))

    print(' '.join(map(str, ans)))
main()
'''
