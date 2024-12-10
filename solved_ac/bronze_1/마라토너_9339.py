# 백준 - 브론즈1 - 마라토너 - 9339 - 구현 문제
'''
구현 문제

입력받은 k_list에 있는 숫자가 나오면 그 숫자의 시간을 d_nums에 저장한다.
그리고 그 시간 중 가장 작은 시간을 best에 저장한다.
그리고 d_nums에 있는 시간 중 0이 아니고 360 이하인 시간을 카운트한다.
그리고 가장 작은 시간과 같은 시간이 나오면 그 숫자를 b_nums에 저장한다.
그리고 카운트한 시간을 출력한다.

풀이 과정
    1. k_list에 있는 숫자가 나오면 그 숫자의 시간을 d_nums에 저장한다.
    2. 그 시간 중 가장 작은 시간을 best에 저장한다.
    3. d_nums에 있는 시간 중 0이 아니고 360 이하인 시간을 카운트한다.
    4. 가장 작은 시간과 같은 시간이 나오면 그 숫자를 b_nums에 저장한다.
    5. 카운트한 시간을 출력한다.

in
    2
    4
    123 456 999 73
    6
    111 5 3
    456 -1 -1
    123 4 59
    73 6 0
    520 -1 -1
    999 6 0
    5
    3 5 2 7 1
    10
    5 8 3
    4 6 20
    9 4 10
    10 5 20
    1 6 1
    2 4 20
    3 4 20
    6 4 20
    7 4 15
    8 4 10
out
    123 3
    7 3
'''

t = int(input())
for i in range(t):
    k = int(input())
    d_nums = {}
    k_list = list(map(int, input().split()))
    n = int(input())
    best = 360

    for i in range(n):
        a, b, c = map(int, input().split())
        if a in k_list:
            if b == -1:
                pass
            else:
                d_nums[a] = b * 60 + c
                if best > d_nums[a]:
                    best = d_nums[a]

    cnt = 0
    b_nums = []
    for key in d_nums.keys():
        if d_nums[key] == best:
            b_nums.append(key)
        if d_nums[key] != 0 and d_nums[key] <= 360:
            cnt += 1
    print(*b_nums, cnt)
