'''
    앞으로 백준 문제를 풀때 아래 같이 함수로 만들고 반환하는 값을 출력 하려고 한다!
    보기에도 더 편한거 같다.
'''

def solution(n, p_list, m):
    res = [-1] * (m + 1)

    for i in range(len(p_list) - 1, -1, -1):
        temp = p_list[i]
        for j in range(temp, m + 1):
            res[j] = max(i, res[j], res[j-temp]*10+i)
        
    return max(res)

n = int(input())
p_list = list(map(int, input().split()))
m = int(input())
print(solution(n, p_list, m))

# n, p_list, m = 3, [6, 7, 8], 21
# print(solution(n, p_list, m) == 210) # n, p_list, m = 3, [6, 7, 8], 21

# n, p_list, m = 3, [5, 23, 24], 30
# print(solution(n, p_list, m) == 20) # n, p_list, m = 3, [5, 23, 24], 30

# n, p_list, m = 4, [1, 5, 3, 2], 1
# print(solution(n, p_list, m) == 0) # n, p_list, m = 4, [1, 5, 3, 2], 1

# n, p_list, m = 10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 50
# print(solution(n, p_list, m) == 99999999999999999999999999999999999999999999999999) # n, p_list, m = 10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 50
