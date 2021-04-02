'''
in
    5
    6 3 2 10 -10
    8
    10 9 -5 2 3 4 5 -10
out
    1 0 0 1 1 0 0 1
'''
n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

for i in range(m):
    s, e, ck = 0, n-1, 0
    while s <= e:
        mid = (s + e) // 2
        if n_list[mid] == m_list[i]:
            ck = 1
            break
        elif n_list[mid] < m_list[i]:
            s = mid + 1
        else:
            e = mid - 1

    print(1, end=' ') if ck else print(0, end=' ')