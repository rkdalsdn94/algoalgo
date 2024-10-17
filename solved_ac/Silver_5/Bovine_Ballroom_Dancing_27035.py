# 백준 - 실버5 - Bovine Ballroom Dancing - 27035 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

단순히 그리디 알고리즘과 정렬을 사용하면 된다.
두 리스트를 입력받아, 각 리스트의 원소의 차이의 절대값을 모두 더한 값을 출력하는 문제이다.

풀이 과정
    1. n을 입력받고, 수컷 소(mail cows)와 암컷 소(female cows)의 리스트를 입력받는다.
    2. 두 리스트를 정렬한다.
    3. res를 0으로 초기화하고 두 리스트를 zip하여 순회하며 res에 i - j의 절대값을 더한다.
    4. res를 출력한다.
'''

n = int(input())
male_cows = sorted([int(input()) for _ in range(n)])
female_cows = sorted([int(input()) for _ in range(n)])

# 테스트
# n = 4
# male_cows = sorted([2, 8, 5, 5])
# female_cows = sorted([1, 4, 10, 7]) # 6

res = 0
for i, j in zip(male_cows, female_cows):
    res += abs(i - j)

print(res)
