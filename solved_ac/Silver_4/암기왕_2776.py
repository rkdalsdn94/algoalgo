'''
자료 구조 문제

n1, n2 리스트를 받은 후에 n2가 n1에 있으면 1 없으면 0 을 출력하면 된다.
근데 n1을 list로 받으면 시간 초과가 나온다. 그래서 set자료 구조를 사용했다.

in
    1
    5
    4 1 5 2 3
    5
    1 3 7 9 5
out
    1
    1
    0
    0
    1
'''

t = int(input())

for _ in range(t):
    n1 = int(input())
    n1_list = set(map(int, input().split()))
    n2 = int(input())
    n2_list = list(map(int, input().split()))

    for i in n2_list:
        if i in n1_list:
            print(1)
        else:
            print(0)
