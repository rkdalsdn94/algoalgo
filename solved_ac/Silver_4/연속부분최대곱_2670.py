# 백준 - 연속부분최대곱 - 2670 - 실버4 - dp, 완전 탐색 문제
'''
dp, 완전 탐색 문제

n_list의 1번째 부터 n의 크기까지 반복문을 돌면서 현재 값, 현재 값 * -1의 값 -> 두 값중 더 큰 값을 n_list[현재] 로 만든다.
n_list의 max 값을 소수점 넷째 자리에서 반올림한 후 소수점 셋째 자리까지 출력하면 된다.
'''

n = int(input())
n_list = [ float(input()) for _ in range(n) ]

# 테스트
# n = 8
# n_list = [ 1.1, 0.7, 1.3, 0.9, 1.4, 0.8, 0.7, 1.4 ] # 1.638

for i in range(1, n):
    n_list[i] = max(n_list[i], n_list[i - 1] * n_list[i])

print('{:.3f}'.format(max(n_list)))
