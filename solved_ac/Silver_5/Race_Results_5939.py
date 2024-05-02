# 백준 - 실버5 - Race Results - 5939 - 단순 구현, 정렬 문제
'''
단순 구현, 정렬 문제

입력으로 들어온 값을 단순히 정렬한 다음 출력하면 되는 간단한 문제이다.
'''

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 3
# n_list = [[11, 20, 20], [11, 15, 12], [14, 20, 14]] # 11 15 12  \  11 20 20  \  14 20 14

for i in sorted(n_list):
    print(*i)
