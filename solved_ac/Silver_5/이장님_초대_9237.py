# 백준 - 이장님 초대 - 9237 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

예제 1을 손으로 풀어보면 아래와 같이 된다.
내림차순으로 정렬하면 [4, 3, 3, 2] 가 된다.
해당 상태에서 풀어보면 아래와 같이 된다.

1일
    4
2일
    3 3
3일
    2 2 3
4일
    1 1 2 2
5일
    0 0 1 1
6일
    0 0 0 0
7일
    이장님 도착 # 나무가 다 자란 다음날 이장님 초대

n_list[i] = n_list[i] + i(하루에 한 그루만 심을수 있는 조건) + 1(날짜 수)
'''

n = int(input())
n_list = sorted(map(int, input().split()), reverse=True)

# 테스트
# n = 4
# n_list = sorted([2,3,4,3], reverse=True) # 7
# n = 6
# n_list = sorted([39, 38, 9, 35, 39, 20], reverse=True) # 42

for i in range(n):
    n_list[i] = n_list[i] + i + 1

print(max(n_list) + 1)
