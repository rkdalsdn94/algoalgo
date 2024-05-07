# 백준 - 골드2 - 가장 긴 증가하는 부분 수열 2 - 12015 - 이분 탐색, 가장 긴 증가하는 부분 수열(LIS) 문제
'''
이분 탐색, 가장 긴 증가하는 부분 수열(LIS) 문제

풀이 과정
 1. 입력을 받는다.
 2. n_list를 받아서 이분 탐색을 사용해 LIS를 구한다.
    - lis 리스트를 만들어서 n_list의 값이 lis의 마지막 값보다 크면 lis에 추가한다.
    - 그렇지 않으면 이분 탐색을 사용해 lis에 들어갈 위치를 찾아서 값을 변경한다.
 3. lis의 길이에서 1을 빼서 출력한다.
    - lis의 길이에서 1을 빼는 이유는 lis의 첫 번째 값이 0이기 때문이다.
    - 즉, 0부터 시작하는 것이 아니라 1부터 시작하는 것이다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 6
# n_list = [10, 20, 10, 30, 20, 50] # 4

lis = [0]
for i in range(n):
    if n_list[i] > lis[-1]:
        lis.append(n_list[i])
    else:
        start, end = 0, len(lis) - 1
        while start < end:
            mid = (start + end) // 2
            if lis[mid] < n_list[i]:
                start = mid + 1
            else:
                end = mid
        lis[end] = n_list[i]

print(len(lis) - 1)
