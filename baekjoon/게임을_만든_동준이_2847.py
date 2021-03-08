# n = 4
# n_list = [5,3,7,5]  # 6
# # n = int(input())
# # n_list = [int(input()) for _ in range(n)]

# res = 0
# for i in range(1, n):
#     temp = 0
#     if n_list[i-1] > n_list[i]:
#         temp = n_list[i]
#         n_list[i] = n_list[i-1] + 1
#         res += n_list[i-1] + 1 - temp

# print(res)

# n_list = [6,5,4,8]  # -> 6이 나와야 하는데 7이 나옴..
# 처음에 위에처럼 풀었다가,, 위처럼 반례가 존재해서 배열 뒷 부분부터 감소하는 형식으로 바꿈

# n = 4
# n_list = [5,3,7,5] # 6
n = int(input())
n_list = [int(input()) for _ in range(n)]
res = 0
for i in range(n-2, -1, -1):
    temp = 0
    if n_list[i] >= n_list[i+1]:
        temp = n_list[i]
        n_list[i] = n_list[i+1] - 1
        res += temp - n_list[i]
print(res)
