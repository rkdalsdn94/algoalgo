# 백준 - 실버1 - 단어 맞추기 - 9081 - 수학, 구현, 문자열, 조합론 문제
'''
수학, 구현, 문자열, 조합론 문제

처음에 permutations를 이용해 모든 순열을 구한 다음 해당 순열 정렬 후, input으로 구한 index 값의 다음 번째 값을 출력하려고 했다.
    - 이 결과는 메모리 초과와 시간 초과를 맞았다.
따라서 다른 방식을 구해야 되는데, 이때 검색을 통해 next_permuations의 대한 정보를 알았고 next_permutations 함수를 만들고 문제를 해결했다.
    - C++에는 해당하는 함수가 존재하는데 JAVA나 Python은 직접 구핸해야 된다고 한다.

풀이 과정
 - next_permutation 함수를 구현하면 되는 문제이다. 이에 대한 참고는 다음의 영상을 보면 된다.
    - https://www.youtube.com/watch?v=uCst0TJHJvg (릿코드 문제를 푸는 영상, 영어)
    - 위 영상을 기준으로 그대로 풀면 안 된다. (수정해야 됨)
 - 기준점을 찾고고
 - 기준점과 기준점보다 큰 첫 번째 값이랑 swap 한다.
 - 기준점 이후의 값들을 reverse 시킨다.
     - 여기서 reverse를 안 시켜도 통과가 된다.
'''

import sys; input=sys.stdin.readline

t = int(input())
t_list = [list(input().rstrip()) for _ in range(t)]

# 테스트
# t = 4
# t_list = [ list('HELLO'), list('DRINK'), list('SHUTTLE'), list('ZOO') ] # HELOL  \  DRKIN  \  SLEHTTU  \  ZOO

def next_permutation(arr):
    n = len(arr)
    pivot = 0

    for i in range(n - 1, 0, -1):
        if arr[i - 1] < arr[i]:
            pivot = i
            break

    if pivot == 0:
        return ''.join(arr)

    swap = n - 1
    while arr[pivot - 1] >= arr[swap]:
        swap -= 1

    arr[swap], arr[pivot - 1] = arr[pivot - 1], arr[swap]
    arr[pivot:] = reversed(arr[pivot:])
    return ''.join(arr)

for i in t_list:
    print(next_permutation(i))

'''
최초 풀이 (메모리 초과)

from itertools import permutations

t_list = [
    'HELLO',
    'DRINK',
    'SHUTTLE',
    'ZOO'
]

for i in t_list:
    temp = []

    for j in permutations(i, len(i)):
        temp.append(''.join(j))

    res = sorted(set(sorted(temp)))

    try:
        print(res[res.index(i) + 1])
    except:
        print(i)

-----------------------------
메모리 초과를 피하기 위한 수정 (시간 초과)

import sys; input=sys.stdin.readline
from itertools import permutations

t = int(input())
# t_list = [
#     'HELLO',
#     'DRINK',
#     'SHUTTLE',
#     'ZOO'
# ]

for _ in range(t):
    i = input().rstrip()
    temp = set()

    for j in permutations(i, len(i)):
        temp.add(''.join(j))
    res = sorted(temp)

    try:
        print(res[res.index(i) + 1])
    except:
        print(i)
'''
