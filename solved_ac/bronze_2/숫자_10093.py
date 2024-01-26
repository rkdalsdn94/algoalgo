# 백준 - 브론즈2 - 숫자 - 10093 - 단순 구현 문제
'''
단순 구현 문제

두 숫자를 입력받고, 두 수 사이의 수의 개수와 두 수 사이의 있는 수를 오름차순으로 출력하면 되는 간단한 구현 문제이다.
단, a와 b의 크기에 관해 신경써야 된다.
'''

a, b = map(int, input().split())

# 테스트
# a, b = 8, 14 # 5  \  9 10 11 12 13

a, b = min(a, b), max(a, b)

res = []
for i in range(a + 1, b):
    res.append(i)

print(len(res))
if res:
    print(*res)
