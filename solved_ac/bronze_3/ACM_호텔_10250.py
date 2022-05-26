'''
수학, 구현 문제

in
    2
    6 12 10
    30 50 72
out
    402
    1203

딱히 설명을 적기엔 몇 층인지, 방 호수가 몇 호인지 구하는 문제라...
'''

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    floor = n % h
    room_number = ( n // h ) + 1

    if not floor:
        floor = h
        room_number -= 1
    
    print(floor * 100 + room_number)
