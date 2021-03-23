# pypy3로 제출해야 시간초과 안남 !!
# 최빈값을 구하려고 고민하다 구글 검색해보니 Counter를 사용하면 좋다고 해서 사용해서 풀음
from collections import Counter

'''
in
    5
    1
    3
    8
    -2
    2
out
    2
    2
    1
    10
'''
n = int(input())
n_list = sorted([int(input()) for _ in range(n)])

print(round(sum(n_list) / len(n_list)))
print(n_list[len(n_list)//2])
temp = Counter(n_list).most_common()

if len(n_list) > 1:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(n_list[0])

print(n_list[-1] - n_list[0])