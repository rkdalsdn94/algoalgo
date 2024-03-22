# 백준 - 브론즈1 - 동전 게임 - 2684 - 구현, 문자열 문제
'''
구현, 문자열 문제

coin을 3개씩 잘라 뒤뒤뒤, 뒤뒤앞, 뒤앞뒤, 뒤앞앞, 앞뒤뒤, 앞뒤앞, 앞앞뒤, 앞앞앞 순서대로 res 인덱스에 맞춰 1씩 더하면 된다.
뒤 : T, 앞 : H

in
    4
    HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    HHTTTHHTTTHTHHTHHTTHTTTHHHTHTTHTTHTTTHTH
    HTHTHHHTHHHTHTHHHHTTTHTTTTTHHTTTTHTHHHHT
out
    0 0 0 0 0 0 0 38
    38 0 0 0 0 0 0 0
    4 7 6 4 7 4 5 1
    6 3 4 5 3 6 5 6
'''

t = int(input())
for _ in range(t):
    res = [0] * 8
    coin = input()

    for i in range(0, len(coin) - 2):
        temp = coin[i:i + 3]
        if temp == 'TTT':
            res[0] += 1
        elif temp == 'TTH':
            res[1] += 1
        elif temp == 'THT':
            res[2] += 1
        elif temp == 'THH':
            res[3] += 1
        elif temp == 'HTT':
            res[4] += 1
        elif temp == 'HTH':
            res[5] += 1
        elif temp == 'HHT':
            res[6] += 1
        elif temp == 'HHH':
            res[7] += 1

    print(*res)
