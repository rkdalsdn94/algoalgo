# 백준 - 선택 정렬1 - 23881 - 브론즈1 - 구현, 정렬, 시뮬레이션 문제
'''
구현, 정렬, 시뮬레이션 문제

선택 정렬을 구현하면 되는 문제다. 여기서는 list의 맨 뒤부터 정렬을 했다.
'''

n, k = map(int, input().split())
a_list = list(map(int, input().split()))

# 테스트
# n, k = 5, 2
# a_list = [3,1,2,5,4] # 2 3
# n, k = 5, 4
# a_list = [3,1,2,5,4] # -1

sorted_a_list = sorted(a_list)
res = []

for i in range(n - 1, -1, -1):
    idx = i

    for j in range(i - 1, -1, -1):
        if a_list[idx] < a_list[j]:
            idx = j

    if a_list[idx] != a_list[i]:
        res.append([a_list[i], a_list[idx]])
        a_list[i], a_list[idx] = a_list[idx], a_list[i]

if len(res) >= k:
    print(*res[k - 1])
else:
    print(-1)
