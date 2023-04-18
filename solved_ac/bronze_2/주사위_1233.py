# 백준 - 브론즈2 - 주사위 - 1233 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

res를 a, b, c를 다 곱한 상태에서 + 1 한 상태로 빈 배열을 만들어 준다.
a, b, c 전체 범위를 3중 for 문으로 i + j + k의 인덱스 값을 1씩 더해준 후
res의 가장 큰 값의 인덱스를 출력한다.
 - 문제에서 '답이 여러개라면 가장 합이 작은 것을 출력한다.'라고 나와 있으므로
 - max가 동일한 값이 있어도 해당 값 중에서 제일 먼저 출력되는 index 함수를 써도 괜찮다.
'''

a, b, c = map(int, input().split())

# 테스트
# a, b, c = 3, 2, 3 # 5

res = [0] * ((a * b * c) + 1)

for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            res[i + j + k] += 1

print(res.index(max(res)))
