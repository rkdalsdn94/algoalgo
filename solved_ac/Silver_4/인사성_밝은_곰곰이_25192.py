# 백준 - 실버4 - 인사성 밝은 곰곰이 - 25192 - 자료 구조(해시) 문제
'''
자료 구조(해시) 문제

단순하게 해시(파이썬에서는 set 자료 구조)를 이용하면 되는 문제이다.

풀이 과정
 - 입력 과정을 미리 다 받아놓고, res와 temp를 각각 0과 해시(set)로 초기화 시킨다.
 - 입력받은 n_list에서 'ENTER'가 들어올 때 기존에 temp에 있던 길이를 res에 더하고, temp를 set 자료 구조로 초기화 시킨다.
 - res를 출력하기 전 temp의 길이를 다시 더한 후 res를 출력하면 된다.
'''

import sys; input=sys.stdin.readline

n = int(input())
n_list = [input().rstrip() for _ in range(n)]

# 테스트
# n = 9
# n_list = ['ENTER', 'pjshwa', 'chansol', 'chogahui05', 'lms0806', 'pichulia', 'r4pidstart', 'swoon', 'tony9402'] # 8
# n = 7
# n_list = ['ENTER', 'pjshwa', 'chansol', 'chogahui05', 'ENTER', 'pjshwa', 'chansol'] # 5
# n = 3
# n_list = ['ENTER', 'lms0806', 'lms0806'] # 1

res = 0
temp = set()

for i in n_list:
    if i == 'ENTER':
        res += len(temp)
        temp = set()
        continue

    temp.add(i)
res += len(temp)

print(res)
