'''
in
    3
    26 40 83
    49 60 57
    13 89 99
out
    96
'''

# n = 3
# rgb_list = [[26, 40, 83], [49, 60, 57], [13, 89, 99]] # 96
n = int(input())
rgb_list = [list(map(int, input().split())) for _ in range(n) ]
for i in range(1, n):
    rgb_list[i][0] += min(rgb_list[i-1][1], rgb_list[i-1][2])
    rgb_list[i][1] += min(rgb_list[i-1][0], rgb_list[i-1][2])
    rgb_list[i][2] += min(rgb_list[i-1][0], rgb_list[i-1][1])

print(min(rgb_list[-1]))
