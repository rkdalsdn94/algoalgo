# 백준 - 실버4 - 수도꼭지 - 30803 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

수도꼭지를 잠궜을 때는 나오는 물의 양이 변하더라도 값이 바뀌면 안 된다.
  - 이를 위해 ck 리스트를 활용했다.
q_list의 첫 번째 값이 1일 때는 물의 양이 변하는 때이고, 2일 때는 수도꼭지를 잠구는 것이다.

풀이 과정
    1. 입력을 받는다.
    2. n_list를 받는다.
    3. q_list를 받는다.
    4. q_list의 값에 따라 다음을 실행한다.
        4.1. q_list의 첫 번째 값이 1일 때
            4.1.1. q_list의 두 번째 값이 True일 때 n_list의 값을 더하고, False일 때 n_list의 값을 빼고, n_list의 값을 출력한다.
        4.2. q_list의 첫 번째 값이 2일 때
            4.2.1. q_list의 두 번째 값이 True일 때 n_list의 값을 더하고, False일 때 n_list의 값을 빼고, n_list의 값을 출력한다.
'''

n = int(input())
n_list = list(map(int, input().split()))
q = int(input())
q_list = [list(map(int, input().split())) for _ in range(q)]

# 테스트
# n = 3
# n_list = [6, 1, 4]
# q = 4
# q_list = [
#     [2, 1],
#     [2, 3],
#     [1, 2, 3],
#     [2, 3]
# ] # 11  \  5  \  1  \  3  \  7
# n = 5
# n_list = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
# q = 4
# q_list = [
#     [1, 1, 999999999],
#     [2, 1],
#     [1, 1, 999999998],
#     [2, 1]
# ] # 5000000000  \  4999999999  \  4000000000  \  4000000000  \  4999999998

res = sum(n_list)
ck = [True] * n

print(res)
for i in q_list:
    if i[0] == 1:
        a, b, c = i

        if ck[b - 1]:
            res -= n_list[b - 1]
            n_list[b - 1] = c
            res += n_list[b - 1]
        else:
            n_list[b - 1] = c

    elif i[0] == 2:
        a, b = i

        if ck[b - 1]:
            ck[b - 1] = False
            res -= n_list[b - 1]
        else:
            ck[b - 1] = True
            res += n_list[b - 1]

    print(res)
