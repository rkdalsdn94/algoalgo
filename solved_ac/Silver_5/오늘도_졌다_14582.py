'''
단순 구현 문제

처음에 문제를 제대로 이해하지 못해서 틀렸었다.
야구는 초(ex. 1회 초)와 말(ex. 1회 말)이 있어서 초에 이기고 있다가 말에 역전패를 당할 경우도 생각해야 된다.
그래서 temp_a 를 먼저 더한 후에 비교를 하고, b가 역전 했을 경우 res를 True로 바꾸면 된다.
'''

a, b = list(map(int, input().split())), list(map(int, input().split()))

# 테스트
# a = [1, 0, 0, 0, 0, 0, 2, 2, 1]
# b = [0, 0, 3, 0, 0, 0, 0, 1, 4] # Yes
# a = [0, 0, 0, 0, 0, 0, 0, 1, 0]
# b = [1, 0, 0, 0, 0, 0, 0, 4, 0] # No

res = False
temp_a, temp_b = 0, 0

for i, j in zip(a, b):
    temp_a += i

    if temp_a > temp_b:
        res = True
        break
    temp_b += j

if res:
    print('Yes')
else:
    print('No')
