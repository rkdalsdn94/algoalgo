'''
단순 구현, 정렬 문제

문제에서 주어진 값을 숫자를 기준으로 정렬한 후에 학교명만 출력하면 된다.
'''

t = int(input())

for _ in range(t):
    n = int(input())
    res = sorted([ list(input().split()) for _ in range(n) ], key=lambda x: int(x[1]), reverse=True)[0]
    print(res[0])