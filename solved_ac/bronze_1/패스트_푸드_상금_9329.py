# 백준 - 브론즈1 - 패스트 푸드 상금 - 9329 - 구현, 그리디 문제
'''
구현, 그리디 문제

풀이 과정
 1. 입력을 받고, 스티커의 최대 개수를 temp에 저장한다.
 2. 스티커의 최대 개수를 계산하고, 상금을 계산한다.
 3. 상금을 출력한다.

in
    3
    2 10
    3 1 2 3 100
    4 4 5 6 7 200
    2 3 1 4 5 2 2 1 3 4
    3 6
    2 1 2 100
    3 3 4 5 200
    1 6 300
    1 2 3 4 5 6
    3 6
    2 1 2 100
    3 3 4 5 200
    1 6 300
    1 2 0 4 5 6
out
    500
    2500
    1900
'''

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    k = []
    ans = 0

    for _ in range(n):
        k.append(list(map(int, input().split(" "))))

    sticker_list = list(map(int, input().split(" ")))

    for i in range(n):
        temp = 100 # 스티커의 최대 개수

        for j in range(1, k[i][0]+1):
            temp = min(temp, sticker_list[k[i][j] - 1])
        ans += temp * k[i][-1]

    print(ans)
