# 백준 - 브론즈1 - 다오의 경주 대회 - 31067 - 수학, 구현, 그리디, 사칙연산 문제
'''
수학, 구현, 그리디, 사칙연산 문제

풀이 과정
    1. n, k를 입력받는다.
    2. n_list를 입력받는다.
    3. n_list를 정렬한다.
    4. n_list에서 k번째 값을 출력한다.
'''

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, k = 3, 2
# n_list = [4, 3, 4] # 2
# n, k = 3, 5
# n_list = [7, 5, 5] # -1
# n, k = 6, 5
# n_list = [2, 4, 3, 9, 5, 8] # 3

res = 0

for i in range(n - 1):
    if n_list[i] < n_list[i + 1]:
        continue

    n_list[i + 1] += k
    res += 1

flag = 0
for i in range(n - 1):
    if n_list[i] < n_list[i + 1]:
        continue

    flag = 1
    break

if flag:
    print(-1)
else:
    print(res)
