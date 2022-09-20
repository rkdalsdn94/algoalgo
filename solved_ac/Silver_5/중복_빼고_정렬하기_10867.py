# 백준 - 실버5 - 10867 - 정렬 문제
'''
정렬 문제

중복을 제거하기 위해 set 자료형으로 중복 제거 후 출력하면 된다.
'''

n = int(input())
n_list = sorted(set(map(int, input().split())))

# 테스트
# n = 10
# n_list = sorted(set([1, 4, 2, 3, 1, 4, 2, 3, 1, 2]))

print(*n_list)
