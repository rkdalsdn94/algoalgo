# 백준 - 실버5 - Toy Shopping - 6032 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

단순하게 입력으로 들어온 값을 나눈 뒤 정렬을 해서 가장 큰 값 3개를 뽑아서 출력하면 된다.

풀이 과정
    1. 입력을 받고, n_list에 저장한다.
    2. n_list를 순회하면서 x / y를 계산한 뒤 happy_list에 저장한다.
    3. happy_list를 정렬한 뒤, 가장 큰 값 3개를 뽑아서 출력한다.
'''

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 6
# n_list = [[0, 521], [442, 210], [119, 100], [120, 108], [619, 744], [48, 10]]

happy_list = []
for i, j in enumerate(n_list):
    x, y = j[0], j[1]
    happy_list.append([i, x / y])

happy_list.sort(key=lambda x: x[1], reverse=True)
total_price = 0
res = []
for i in range(3):
    a, b = happy_list[i]
    total_price += n_list[a][1]
    res.append(a)

print(total_price)
for i in res:
    print(i)
