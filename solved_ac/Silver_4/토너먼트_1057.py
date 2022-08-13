'''
수학, 완전 탐색 문제

while 반복문으로 a(jimin)와 b(hansu)가 같아질 때까지 구하면 된다.
구하는 식은 a -= a // 2, b -= b // 2로 하면 된다.
이유는 토너먼트 방식이라서 절반씩 줄어 든다고 생각하면 좋다.

ex) 16, 8, 9로 예를 들자면

a -= 8 // 2 -> a = 4
b -= 9 // 2 -> b = 5

a -= 4 // 2 -> a = 2
b -= 5 // 2 -> b = 3

a -= 2 // 2 -> a = 1
b -= 3 // 2 -> b = 2

a -= 1 // 2 -> a = 1
b -= 2 // 2 -> b = 1

4번의 상황 끝에 만날 수 있다.
'''

n, jimin, hansu = map(int, input().split())

# 테스트
# n, jimin, hansu = 16, 1, 2 # 1
# n, jimin, hansu = 16, 8, 9 # 4
# n, jimin, hansu = 1000, 20, 31 # 4
# n, jimin, hansu = 65536, 1000, 35000 # 16
# n, jimin, hansu = 60000, 101, 891 # 10

res = 0

while jimin != hansu:
    jimin -= jimin // 2
    hansu -= hansu // 2
    res += 1

print(res)
