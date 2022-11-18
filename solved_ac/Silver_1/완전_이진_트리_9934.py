# 백준 - 완전 이진 트리 - 9934 - 실버1 - 트리, 재귀 문제
'''
트리, 재귀 문제

재귀를 사용해서 입력으로 주어진 리스트를 트리로 바꾸면 된다.

풀이 과정
1. 입력으로 들어오는 값들을 잘 입력받고, 출력을 위한 res 리스트를 k의 크기를 가진 2중 리스트를 만든다.
2. 입력으로 받은 tree와 처음부터 실행하기 위해 0을 인자로 넣고, recursive 함수를 실행한다.
    2.1 함수 안에서 tree리스트를 절반으로 자른다.
    2.2 두 번째 인자 값인 res의 idx 위치에 절반을 자른 값을 append한다.
    2.3 재귀의 종료 조건을 설정해 놓는다. list의 길이가 1이 되면 종료 조건이다.
    2.4 각각의 mid값을 list의 (처음부터 : mid - 1까지), (mid + 1위치부터 : 마지막까지) idx를 1씩 증가시켜 재귀 함수를 실행한다.
3. res에 append된 값을 출력한다.
'''

k = int(input())
tree = list(map(int, input().split()))

# 테스트
# k = 2
# tree = [2,1,3] # 1  \  2 3
# k = 3
# tree = [1,6,4,3,5,2,7] # 3  \  6 2  \  1 4 5 7

res = [ [] for _ in range(k) ]

def recursive(li, idx):
    mid = len(li) // 2
    res[idx].append(li[mid])

    if len(li) == 1:
        return

    recursive(li[:mid], idx + 1)
    recursive(li[mid + 1:], idx + 1)

recursive(tree, 0)

for i in range(k):
    print(*res[i])
