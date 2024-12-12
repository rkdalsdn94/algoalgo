# 백준 - 실버5 - 공포의 면담실 - 30088 - 그리디, 정렬, 누적 합
'''
그리디, 정렬, 누적 합 문제

입력받은 n_list를 정렬하고, 누적 합을 구하는 문제이다.

풀이 과정
    1. n과 n_list를 입력받는다.
        1.1. n_list를 정렬하는데 첫 번째 값은 무시하고 두 번째 값부터 더한다. (면담이 필요한 부분만 더하는 과정)
    2. 누적 합을 구한다.
    3. 누적 합을 출력한다.
'''

n = int(input())
n_list = sorted([sum(list(map(int, input().split()))[1:]) for _ in range(n)])

# 테스트
# n = 3
# n_list = sorted([
#     sum([2, 5, 50][1:]), sum([2, 20, 10][1:]), sum([1, 100][1:])
# ])

prefix_sum = [0] * n
res = [0] * n

for i in range(n):
    prefix_sum[i] = prefix_sum[i - 1] + n_list[i]
    res[i] = res[i - 1] + prefix_sum[i]

print(res[-1])
