# 백준 - 브론즈1 - 콘도 선정 - 2246 - 완전 탐색, 정렬 문제
'''
완전 탐색, 정렬 문제

콘도의 위치와 가격을 입력받는다.
콘도의 위치와 가격을 정렬하고, 가격이 낮은 콘도를 선택한다.
콘도를 선택할 때, 이전 콘도보다 가격이 낮으면 선택한다.

풀이 과정
    1. n을 입력받는다.
    2. n개의 콘도의 위치와 가격을 입력받는다.
    3. 콘도를 정렬한다.
    4. cost를 10001로 초기화한다.
    5. res를 0으로 초기화한다.
    6. 콘도를 순회하며 temp에 i[1]을 저장한다.
    7. temp가 cost보다 작으면 cost에 temp를 저장하고 res에 1을 더한다.
    8. res를 출력한다.
'''

n = int(input())
condos = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 5
# condos = [[300, 100], [100, 300], [400, 200], [200, 400], [100, 500]] # 2

condos.sort()
cost = 10001
res = 0

for i in condos:
    temp = i[1]
    if temp < cost:
        cost = temp
        res += 1

print(res)
