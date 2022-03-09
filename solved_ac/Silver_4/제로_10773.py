'''
0이면 pop 아니면 append 단순한 스택 문제이다.
혹시 스택이 비어 있을때만 pop하게 만들었지만,
다른 사람들 풀이 보면 그런 경우는 없는거 같다.

in
    4
    3
    0
    4
    0
out
    0

in
    10
    1
    3
    5
    4
    0
    0
    7
    0
    0
    6
out
    7
'''
k = int(input())
k_list = []

for i in range(k):
    num = int(input())

    if num != 0:
        k_list.append(num)
    else:
        if k_list:
            k_list.pop()

print(sum(k_list))
