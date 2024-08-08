# 백준 - 실버4 - 필터 - 1895 - 구현, 완전 탐색, 정렬 문제
'''
구현, 완전 탐색, 정렬 문제

r, c의 최댓값이 40이므로 완전 탐색으로 풀어도 된다.

풀이 과정
    1. 입력을 받는다.
    2. res를 0으로 초기화한다.
    3. 3x3 필터를 탐색한다.
        3.1. 필터를 탐색하면서 정렬한 값을 temp에 저장한다.
    4. temp_list에 temp를 저장한다.
    5. temp_list를 탐색하면서 4번째 값이 t보다 크거나 같으면 res에 1을 더한다.
    6. res를 출력한다.
'''

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
t = int(input())

# 테스트
# r, c = 6, 5
# arr = [
#     [49, 36, 73, 62, 21],
#     [27, 88, 14, 11, 12],
#     [99, 18, 36, 91, 21],
#     [45, 96, 72, 12, 10],
#     [12, 48, 49, 75, 56],
#     [12, 15, 48, 86, 78]
# ]
# t = 40

res = 0
temp_list = []

for i in range(r - 2):
    for j in range(c - 2):
        temp = []

        for k in range(i, i + 3):
            for l in range(j, j + 3):
                temp.append(arr[k][l])

        temp_list.append(sorted(temp))

for i in temp_list:
    if i[4] >= t:
        res += 1

print(res)
