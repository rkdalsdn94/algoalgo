# 백준 - 브론즈3 - 리그 - 5544 - 수학, 구현, 사칙연산 문제
'''
수학, 구현, 사칙연산 문제

풀이 과정
    1. n을 입력받고 n_list에 n * (n - 1) // 2개의 수를 입력받는다.
    2. temp에 n만큼 0을 넣어준다.
    3. n_list를 순회하면서 a, b, c, d를 입력받는다.
    4. a, b를 1씩 감소시켜준다.
    5. c가 d보다 크면 temp[a]에 3을 더해준다.
    6. c가 d보다 작으면 temp[b]에 3을 더해준다.
    7. c와 d가 같으면 temp[a]와 temp[b]에 1을 더해준다.
    8. res에 temp[:n]을 넣어준다.
    9. res를 내림차순으로 정렬한다.
    10. temp를 순회하면서 res에서 temp[i]의 인덱스를 찾아서 출력한다.
'''

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n * (n - 1) // 2)]

# 테스트
# n = 4
# n_list = [
#     [1, 2, 0, 1], [1, 3, 2, 1], [1, 4, 2, 2],
#     [2, 3, 1, 1], [2, 4, 3, 0], [3, 4, 1, 3]
# ] # 2  \  1  \  4  \  2
# n = 5
# n_list = [
#     [1, 2, 1, 1], [3, 4, 3, 1], [5, 1, 1, 2], [2, 3, 0, 0], [4, 5, 2, 3],
#     [1, 3, 0, 2], [5, 2, 2, 2], [4, 1, 4, 5], [3, 5, 4, 0], [2, 4, 0, 1]
# ] # 2  \  4  \  1  \  4  \  3

temp = [0] * n

for a, b, c, d in n_list:
    a, b = a - 1, b - 1

    if c > d:
        temp[a] += 3
    elif c < d:
        temp[b] += 3
    else:
        temp[a] += 1
        temp[b] += 1

res = temp[:n]
res = sorted(res, reverse=True)

for i in range(n):
    print(res.index(temp[i]) + 1)
