'''
단순 구현

최댓값 - 최솟값을 한 후에 출력하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [27, 35, 92, 75, 42] # 65
# n = 8
# n_list = [85, 42, 79, 95, 37, 11, 72, 32] # 84

print(max(n_list) - min(n_list))
