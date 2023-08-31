# 백준 - 브론즈3 - 플러그 - 2010 - 수학, 사칙연산 문제
'''
수학, 사칙연산 문제

sys.stdin.readline 을 안하면 시간 초과가 난다.
이 부분이 싫으면 sum 함수를 이용하지 말고, 다음과 같이 temp에다 n 번 반복하면서 값을 더해주면 된다.
    temp = 0
    for _ in range(n):
        temp += int(input())

콘센트를 몇 개 꽂을 수 있는지 생각하면 되는 단순한 문제이다.

멀티탭의 플러그 총 합에서 (n - 1)의 값을 출력하면 된다.
    -1의 이유는 모든 멀티탭은 각각 한 개의 플러그를 사용하고 있다. (본인이 앞에 있는 플러그를 사용해야 멀티탭 연결이 가능)
'''

import sys; input=sys.stdin.readline

n = int(input())
n_list = [int(input()) for _ in range(n)]

# 테스트
# n = 3
# n_list = [1,1,1] # 1
# n = 2
# n_list = [5, 8] # 12

print(sum(n_list) - (n - 1))
