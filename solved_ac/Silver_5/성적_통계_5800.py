'''
단순 구현 문제

gap_num만 어떻게 구할지 생각하면 된다.
n을 빼고 정렬한 n_list에서 1번째 인덱스부터 j - 1로 gap이 더 큰 값이 생기면
gap_num을 갱신하는 방식으로 풀었다.

in
    2
    5 30 25 76 23 78
    6 25 50 70 99 70 90
out
    Class 1
    Max 78, Min 23, Largest gap 46
    Class 2
    Max 99, Min 25, Largest gap 25
'''

k = int(input())

for i in range(1, k + 1):
    temp = list(map(int, input().split()))
    n, n_list = temp[0], sorted(temp[1:])
    gap_num = 0

    for j in range(1, len(n_list)):
        if gap_num < n_list[j] - n_list[j - 1]:
            gap_num = n_list[j] - n_list[j - 1]

    print(f'Class {i}')
    print(f'Max {max(n_list)}, Min {min(n_list)}, Largest gap {gap_num}')
