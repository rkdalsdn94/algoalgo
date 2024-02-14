# 백준 - 실버3 - 이건 꼭 풀어야 해! - 17390 - 정렬, 누적 합 문제
'''
정렬, 누적 합 문제

풀이 과정
 - 누적합으로 사용할 prefix_sum을 만들고, 누적 합을 계산하면 된다.
 - q_list에서 i가 1일 때 2을 빼면 -1 이므로 제대로 된 답을 못 구한다.
     - 따라서 q_list의 첫 번째 인자(i)가 1일 때만 조건을 달고, 나머진 누적합으로 구해놨던 prefix_sum 에서 값을 구하면 된다.
 - 이 문제의 핵심은 누적 합을 구하고, 구간 합을 구하고 싶은 구간에서 이전의 누적 합을 뺀 뒤 출력하면 된다.
'''

n, q = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
q_list = [list(map(int, input().split())) for _ in range(q)]

# 테스트
# n, q = 5, 6
# n_list = sorted([2, 5, 1, 4, 3])
# q_list = [[1, 5], [2, 4], [3, 3], [1, 3], [2, 5], [4, 5]] # 15  \  9  \  3  \  6  \  14  \  9
# n, q = 5, 3
# n_list = sorted([2, 5, 1, 2, 3])
# q_list = [[1, 3], [2, 3], [1, 5]] # 5  \  4  \  13

prefix_sum = [0] * n
prefix_sum[0] = n_list[0]

for i in range(1, n):
    prefix_sum[i] = n_list[i] + prefix_sum[i - 1]

for i, j in q_list:
    if i == 1:
        print(prefix_sum[j - 1])
    else:
        print(prefix_sum[j - 1] - prefix_sum[i - 2])
