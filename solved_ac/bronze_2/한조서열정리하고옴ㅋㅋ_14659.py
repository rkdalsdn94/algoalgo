n = int(input())
n_list = list(map(int, input().split()))
n_list.append(100001)

# 테스트
# n = 7
# n_list = [6, 4, 10, 2, 5, 7, 11]
# n_list.append(100001)

def solution(n, n_list):
    res = []
    temp = 0
    n = 0

    for i in n_list:
        if i < n:
            temp += 1
        else:
            res.append(temp)
            temp = 0
            n = i

    return max(res)

print(solution(n, n_list))

# 6 4 10 2 5 7 11