# 백준 - 골드5 - 탑 - 2493 - 자료 구조(스택) 문제
'''
자료 구조(스택) 문제

완전 탐색 방식으로 풀려고 했다가 실패했다. (n^2 이면, 500_000*500_000 = 250_000_000_000 이므로 시간 초과가 난다.)
따라서 다른 방식으로 풀어야 되는데 그때, stack을 활용하면 된다.
stack에 탑의 인덱스(i)와 해당 탑의 높이(n_list[i])를 추가한 뒤 값을 비교하는 방식으로 풀었다.

풀이 과정
- 제일 처음 값은 무조건 0이므로 res에 0을 추가한 채 초기화 하고, stack에도 0과 0번째 인덱스의 탑의 높이를 추가한 채로 초기화한다.
- for 문으로 1 ~ n을 실행하고, while문으로 stack에서 마지막으로 추가된 탑의 높이 값과 현재 반복중인 타워 높이의 값을 비교한다.
    - stack에 들어있는 같이 크거나 같다면 해당 인덱스를 1을 추가한 채로 res에 추가하고, while 문을 종료한다.
    - 현재 반복중인 n_list의 값이 더 크다면 stack에서 제거한다.
- while 문이 끝났을 때 stack이 비어있다면 0을 추가한다.
- stack이 비어있든 아니든 현재 반복중인 타워의 인덱스와 해당 인덱스의 값을 stack에 추가한다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [6, 9, 5, 7, 4] # 0 0 2 2 4

res = [0]
stack = [[0, n_list[0]]]

for i in range(1, n):
    while stack:
        if stack[-1][1] >= n_list[i]:
            res.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()

    if not stack:
        res.append(0)
    stack.append([i, n_list[i]])

print(*res)
