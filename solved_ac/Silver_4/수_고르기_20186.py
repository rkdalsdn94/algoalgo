# 백준 - 실버4 - 수 고르기 - 20186 - 수학, 그리디, 정렬 문제
'''
수학, 그리디, 정렬 문제

n_list에서 k개의 숫자를 선택해서 최댓값을 만드는 법은 정렬 후 -k 번째부터 sum 함수를 사용하면 된다.
그리고 빼야 되는 수를 고르는 법은 (k - 1) * k // 2를 통해 구하면 된다.
'''

n, k = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n, k = 5, 3
# n_list = sorted([2, 3, 1, 2, 1]) # 4
# n, k = 6, 2
# n_list = sorted([4, 1, 5, 2, 6, 3]) # 10

a = sum(n_list[-k:])
b = (k - 1) * k // 2
print(a - b)
