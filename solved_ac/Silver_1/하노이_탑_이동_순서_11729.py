'''
재귀 문제로 엄청 유명한 하노이 탑 문제이다.

in
    3

out
    7
    1 3
    1 2
    3 2
    1 3
    2 1
    2 3
    1 3
'''

n = int(input())

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)

print(2**n - 1)
hanoi(n, 1, 3)
