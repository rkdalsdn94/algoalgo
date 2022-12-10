# 백준 - 캥거루 세마리2 - 브론즈3 - 11034 - 그리디, 수학 문제
'''
그리디, 수학 문제

단순한 문제이다. 더하기 빼기로 답을 구할 수 있다.
문제 조건이 0 < A < B < C < 100 이므로 b에서 a를 빼고, c에서 b를 빼면 된다.
의외로 종료 조건이 없어서 당황했던 문제이다. try except(catch)로 해결하면 된다.

풀이 과정.
a, b, c를 입력받고, 두 수를 서로 뺏을 때 가장 큰 결과에서 현재 위치인 1을 빼고 출력하면 된다.

in
    2 3 5
out
    1

in
    3 5 9
out
    3
'''

while True:
    try:
        a, b, c = map(int, input().split())
        res = max(b - a, c - b)
        print(res - 1)
    except:
        exit()