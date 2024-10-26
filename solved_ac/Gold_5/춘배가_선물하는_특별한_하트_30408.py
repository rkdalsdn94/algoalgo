# 백준 - 골드5 - 춘배가 선물하는 특별한 하트 - 30408 - 자료 구조(set) 문제
'''
자료 구조(set) 문제

짝수일 때도 2로 나눈 값과 1더한 값을 추가하고,
홀수일 경우에는 1을 뺀 상태로 2로 나눈 값과 1을 더한 값을 res에 추가한다.

풀이 과정
    1. n, m을 입력받는다.
    2. res를 set으로 선언하고 n을 추가한다.
    3. n이 1보다 크면
        4. n이 짝수면 n을 2로 나누고 res에 추가하고 n + 1을 res에 추가한다.
        5. n이 홀수면 n에서 1을 빼고 2로 나누고 res에 추가하고 n + 1을 res에 추가한다.
    6. m이 res에 있으면 YES를 출력하고, 없으면 NO를 출력한다.
'''

n, m = map(int, input().split())

# 테스트
# n, m = 13, 4 # YES
# n, m = 13, 5 # NO

res = set()
res.add(n)

while n > 1:
    if n % 2 == 0:
        n //= 2
        res.add(n)
        res.add(n + 1)
    else:
        n = (n - 1) // 2
        res.add(n)
        res.add(n + 1)

if m in res:
    print('YES')
else:
    print('NO')
