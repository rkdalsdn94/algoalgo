# 백준 - 골드5 - 이진 검색 트리 - 5639 - 트리, 그래프, 재귀 문제
'''
트리, 그래프, 재귀 문제

전위 방식으로 입력으로 들어온 리스트를 후위 순회한 결과로 출력하는 문제이다.

풀이
방식으론 재귀를 이용해서 리스트의 0 번째 인덱스의 값을 mid로 사용하고, mid보다 큰 값이 있는지 검사한다.
    - 큰 값이 있을 경우
        - left는 mid를 제외한 큰 값이 나오기 전 인덱스로 만들고, (슬라이싱을 이용하면 1 : i 까지)
        - right는 큰 값부터 나머지 모두(i:)로 만든다.
    - 큰 값이 없을 경우
        - mid가 제일 큰 값이므로 right는 필요 없다. left 리스트에서만 mid를 제외한 나머지(1:)로 초기화한다.
left와 right를 각각 재귀 함수로 반복한다.
재귀 함수의 종료 조건으론 입력으로 들어온 리스트의 길이가 0일 때 즉, 빈 값이 일 때 종료한다.
이때 left와 right 모두 빈 값으로 리턴될 때 mid가 후위 순회로 진행된 값이 되므로 mid를 계속 출력하면 된다.

in
    50
    30
    24
    5
    28
    45
    98
    52
    60
out
    5
    28
    24
    45
    30
    60
    52
    98
    50
'''

import sys; sys.setrecursionlimit(10**9)

preorder = []
while 1:
    try:
        preorder.append(int(input()))
    except:
        break

# arr = [50, 30, 24, 5, 28, 45, 98, 52, 60] # 5 28 24 45 30 60 52 98 50

def recursive(li):
    if len(li) == 0:
        return

    left, right = [], []
    mid = li[0]
    for i in range(1, len(li)):
        if li[i] > mid:
            left = li[1:i]
            right = li[i:]
            break
    else:
        left = li[1:]

    recursive(left)
    recursive(right)
    print(mid)

recursive(preorder)
