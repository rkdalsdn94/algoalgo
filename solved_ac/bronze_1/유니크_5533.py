# 백준 - 브론즈1 - 유니크 - 5533 - 구현, 수학, 사칙연산 문제
'''
구현, 수학, 사칙연산 문제

new_n_list로 n_list의 값을 새로 만든다. (n_list의 열 별로 다시 만드는 작업)
new_n_list의 값을 temp_num이라는 이름으로 만든 후, 그 값이 new_n_list 반복중인 인덱스에 2개 이상 있다면 중복되는 값이 존재하는 것이다.
따라서, 중복된 값이 있으면 res에 반복중인 인덱스의 값에다가 0을 더하고, 2보다 작으면 아니면 temp_num을 더하면 된다.

위 설명보다 아래 링크에서 아래 테스트 되어 있는 부분 주석을 풀고 실행해 보는것이 더 직관적으로 이해하기 쉽다.
https://pythontutor.com/visualize.html#mode=display
'''

n = int(input())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 5
# n_list = [
#     [100, 99, 98], [100, 97, 92], [63, 89, 63], [99, 99, 99], [89, 97, 98],
# ] # 0  92  215  198  89
# n = 3
# n_list = [
#     [89, 92, 77], [89, 92, 63], [89, 63, 77]
# ] # 0  63  63

res = [0] * n

new_n_list = []
for i in range(3):
    temp = []

    for j in range(n):
        temp.append(n_list[j][i])

    new_n_list.append(temp)

for i in range(3):
    for j in range(n):
        temp_num = new_n_list[i][j]

        if new_n_list[i].count(temp_num) >= 2:
            res[j] += 0
        else:
            res[j] += temp_num

for i in res:
    print(i)
