# 백준 - 브론즈1 - 기상청 인턴 신현수 - 2435 - 완전 탐색, 누적 합 문제
'''
완전 탐색, 누적 합 문제

입력 범위가 적어 완전 탐색으로 풀면 된다.
만약, 입력 범위가 늘어나는 경우(난이도가 높아질 수록) 누적 합을 활용해야 된다.

풀이 과정
 - 완전 탐색 방식으로 입력받은 k_list 중에서 k 구간들의 합이 가장 큰 값으로 res로 바꿔주면 된다.
'''

n, k = map(int, input().split())
k_list = list(map(int, input().split()))

# 테스트
# n, k = 10, 2
# k_list = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3] # 21

res = -101
for i in range(n - k + 1):
    res = max(res, sum(k_list[i:i + k]))

print(res)
