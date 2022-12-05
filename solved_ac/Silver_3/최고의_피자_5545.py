# 백준 - 5545 - 최고의 피자 - 실버3 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

역순으로 정렬(그리디) 후 문제에 주어진 대로 가격을 계속 계산하면서 풀면 된다.

풀이 과정
1. input을 잘 입력 받은 후, n_list를 역순으로 정렬한다.
2. res를 c를 a로 나눈 몫으로 초기화를 진행한다.
3. n만큼 반복문을 시작한다.
    3.1. c에 현재 토핑의 칼로리(a)를 더한다.
    3.2. 토핑을 더 할때마다 토핑의 가격(b)을 더한다.
    3.3. 피자의 가격을 계산 후(a + (b * k)) 더 비싼 수가 된다면 res를 해당 값으로 바꿔준다.
4. res를 출력한다.
'''

n = int(input())
a, b = map(int, input().split())
c = int(input())
n_list = sorted([ int(input()) for _ in range(n) ], reverse=True)

# 테스트
# n = 3
# a, b = 12, 2
# c = 200
# n_list = sorted([50, 300, 100], reverse=True) # 37
# n = 4
# a, b = 20, 3
# c = 900
# n_list = sorted([300, 100, 400, 1300], reverse=True) # 100

res = c // a

for i in range(n):
    c += n_list[i]
    a += b
    res = max(res, c // a)

print(res)
