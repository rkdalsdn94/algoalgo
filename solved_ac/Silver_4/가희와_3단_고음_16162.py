# 백준 - 실버4 - 가희와 3단 고음 - 16162 - 단순 구현, 그리디 문제
'''
단순 구현, 그리디 문제

나이브하게 구현하면 된다. temp 를 a로 초기화 한 후,
n_list 에서 temp 와 같은 값이 나오면 res 를 더하고, temp 에 d를 더해가면서 찾으면 된다.
'''

n, a, d = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, a, d = 3, 1, 2
# n_list = [1, 3, 5] # 3
# n, a, d = 3, 1, 2
# n_list = [3, 1, 5] # 1
# n, a, d = 7, 3, 3
# n_list = [3, 3, 9, 7, 2, 6, 9] # 3

res = 0
temp = a

for i in range(n):
    if n_list[i] == temp:
        res += 1
        temp += d

print(res)
