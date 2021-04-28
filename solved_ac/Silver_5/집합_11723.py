'''
x가 최대 20이라 시간초과에 대해서 생각 없이 풀었는데
나중에 문제를 다시 읽어보니 수행해야될 연산의 수가 최대 3백만까지라 해서.. 허무했었음
매번 이럴때 느끼지만 문제를 잘 읽는게 중요한거 같음
'''

from sys import stdin

m = int(stdin.readline())
s = set()

# m = 26
# test = [['add', 1],['add', 2],['check', 1], ['check', 2],
# ['check', 3], ['remove', 2], ['check', 1], ['check', 2], ['toggle', 3],
# ['check', 1], ['check', 2], ['check', 3], ['check', 4], ['all',],
# ['check', 10], ['check', 20], ['toggle', 10], ['remove', 20],
# ['check', 10], ['check', 20], ['empty',], ['check', 1],
# ['toggle', 1], ['check', 1], ['toggle', 1], ['check', 1]]
# out -->  [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0]

# for temp in test:
for _ in range(m):
    temp = stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue
    temp[0], int(temp[1])

    if temp[0] == 'add':
        s.add(int(temp[1]))
    elif temp[0] == 'remove':
        s.discard(int(temp[1]))
    elif temp[0] == 'check':
        print(1 if int(temp[1]) in s else 0)
    elif temp[0] == 'toggle':
        s.discard(int(temp[1])) if int(temp[1]) in s else s.add(int(temp[1]))
