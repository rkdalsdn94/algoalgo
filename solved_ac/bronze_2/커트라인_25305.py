# 백준 - 브론즈2 - 커트라인 - 25305 - 단순 구현, 정렬 문제
'''
단순 구현, 정렬 문제

오름차순으로 정렬 후 뒤에서 n번째 값을 출력하면 되는 간단한 문제다.
'''

n, k = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n, k = 5, 2
# n_list = sorted([100, 76, 85, 93, 98]) # 98

print(n_list[-k])
