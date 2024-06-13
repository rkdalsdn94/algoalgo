# 백준 - 실버3 - 대표 자연수 - 2548 - 완전 탐색, 정렬 문제
'''
완전 탐색, 정렬 문제

n_list를 정렬 한 뒤 완전 탐색 방시과 이분 탐색을 섞은 듯한 방식으로 문제를 푼다.

for 문으로 height(이분 탐색에서 mid 느낌)를 구한 뒤 res를 찾는 것이다.

완전 탐색 방식과 정렬하는 방식 풀이 추가

정렬 풀이 과정
    1. 입력을 받고, 리스트를 정렬한다.
    2. 리스트의 길이를 구한다.
    3. 리스트 길이가 홀수인 경우 중앙값을 반환한다.
    4. 리스트 길이가 짝수인 경우 두 중앙값 중 하나를 반환한다.
         4.1. 중앙값 두 개는 sorted_numbers[n // 2 - 1]와 sorted_numbers[n // 2]이다.
         4.2. 여기서는 둘 중 작은 값을 반환한다.
    5. 반환한 값을 출력한다.

완전 탐색 풀이 과정
    1. 입력을 받고, 리스트를 정렬한다.
    2. 최솟값과 최댓값을 구한다.
    3. res와 temp를 0으로 초기화한다.
    4. temp_res를 int(1e9)로 초기화한다.
    5. i를 최솟값부터 최댓값까지 돌면서 temp_res를 구한다.
    6. temp_res가 temp보다 작으면 temp_res를 temp에 저장하고 res를 i로 저장한다.
    7. res를 출력한다.
'''

# 정렬 방식
n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 6
# n_list = [4, 3, 2, 2, 9, 10] # 3

def find_representative_number(n, numbers):
    sorted_numbers = sorted(numbers)

    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        return sorted_numbers[n // 2 - 1]

representative_number = find_representative_number(n, n_list)
print(representative_number)

'''
완전 탐색 풀이

import sys;input=sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 6
# n_list = [4, 3, 2, 2, 9, 10] # 3

n_list.sort()

min_num, max_num = n_list[0], n_list[-1]
res = 0
temp = int(1e9)

for i in range(min_num, max_num + 1):
    temp_res = 0

    for j in n_list:
        temp_res += abs(i - j)

    if temp_res < temp:
        temp = temp_res
        res = i

print(res)
'''

'''
기존 풀이

n = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 6
# n_list = sorted([4, 3, 2, 2, 9, 10]) # 3

left, right = 0, sum(n_list) - n_list[0] * n
res, temp = 0, right

for i in range(1, n):
    height = n_list[i] - n_list[i - 1]
    left += height * i
    right -= height * (n - i)

    if left + right < temp:
        res = i
        temp = left + right

print(n_list[res])
'''
