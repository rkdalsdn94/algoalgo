# 백준 - 실버5 - 종이자르기 - 2628 - 구현, 정렬 문제
'''
구현, 정렬 문제

풀이 과정
 - 행과 열을 각각의 리스트로 담은 뒤, 정렬한다.
 - 각 리스트들의 앞 인덱스와 현재 인덱스의 차를 구한다.
    - 이때 max 함수를 이용해 초기값은 0으로 더 큰 값으로 갱신해야 되낟.
 - res_x * res_y 를 출력하면 된다.

in
    10 8
    3
    0 3
    1 4
    0 2
out
    30
'''

r, c = map(int, input().split())
row = [0, r]
column = [0, c]
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    if a == 1:
        row.append(b)
    else:
        column.append(b)

row.sort()
column.sort()
res_x, res_y = 0, 0

for i in range(len(row) - 1):
    res_x = max(res_x, row[i + 1] - row[i])
for i in range(len(column) -1):
    res_y = max(res_y, column[i + 1] - column[i])

print(res_x * res_y)
