# 백준 - 실버3 - 대표 자연수 - 2548 - 완전 탐색, 정렬 문제
'''
완전 탐색, 정렬 문제

n_list를 정렬 한 뒤 완전 탐색 방시과 이분 탐색을 섞은 듯한 방식으로 문제를 푼다.

for 문으로 height(이분 탐색에서 mid 느낌)를 구한 뒤 res를 찾는 것이다.
'''

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
