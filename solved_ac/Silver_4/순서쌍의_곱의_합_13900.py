# 백준 - 실버4 - 순서쌍의 곱의 합 - 13900 - 수학, 누적 합 문제
"""
수학, 누적 합 문제

[핵심 아이디어]
     - 서로 다른 위치의 두 수를 뽑는 모든 경우의 곱의 합은 combinations로 구할 수 있지만 O(N^2) 시간복잡도를 가진다.
     - 이를 수학 공식을 활용하면 더 효율적이다. (전체 합)² = (각 원소의 제곱합) + 2×(우리가 구하려는 값)
     - 따라서 구하려는 값 = ((전체 합)² - (각 원소의 제곱합)) / 2 으로 구할 수 있다.

[풀이 과정]
    1. 입력받은 모든 수의 합(total_sum)을 구한다.
    2. 입력받은 모든 수의 제곱의 합(square_sum)을 구한다.
    3. 수학 공식 = (total_sum² - square_sum) // 2를 계산한다. (BigO(N) 시간복잡도)
"""

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 3
# n_list = [2, 3, 4] # 26
# n = 4
# n_list = [1, 2, 3, 4] # 35
# n = 4
# n_list = [2, 3, 2, 4] # 44

# 수학적 접근법 - O(N) 시간복잡도
total_sum = sum(n_list)
square_sum = sum(x * x for x in n_list)

# (a+b+c+...)² = a²+b²+c²+... + 2(ab+ac+bc+...)
# 따라서 ab+ac+bc+... = ((a+b+c+...)² - (a²+b²+c²+...)) / 2
res = (total_sum * total_sum - square_sum) // 2
print(res)
