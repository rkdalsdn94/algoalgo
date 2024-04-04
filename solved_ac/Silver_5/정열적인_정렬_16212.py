# 백준 - 실버5 - 정열적인 정렬 - 16212 - 정렬 문제
'''
정렬 문제

python 내장 정렬 함수를 이용해서 풀었다.

나중에 여러 정렬들을 직접 구현해보자.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 6
# n_list = sorted([14, 5, 8, 7, 1, 10]) # 1 5 7 8 10 14

print(*n_list)
