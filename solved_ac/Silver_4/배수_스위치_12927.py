# 백준 - 실버4 - 배수 스위치 - 12927 - 그리디 문제
'''
그리디 문제

완전 탐색과, 그리디 방식으로 풀었다.
    다른 사람 풀이로 확인했을 땐 비트 연산자를 사용하면 훨씬 빠르다.

입력으로 들어오는 전구(bulb)을 하나씩 확인하면서 상태를 변경시킨다.
상태를 변경 시킬 때마다 res를 1씩 증가시킨다.
이 과정을 blub이 모두 'N'이 될 때까지 반복하면 된다. (while 문까지는 안써도 됨, blub len까지 돌아도 해결 가능)
'''

bulb = [0] + list(input())
res = 0

for i in range(1, len(bulb)):
    if bulb == [0] + ['N'] * (len(bulb) - 1):
        break
    if bulb[i] == 'N':
        continue
    for j in range(i, len(bulb)):
        if j % i == 0:
            if bulb[j] == 'Y':
                bulb[j] = 'N'
            else:
                bulb[j] = 'Y'
    res += 1

print(res)
