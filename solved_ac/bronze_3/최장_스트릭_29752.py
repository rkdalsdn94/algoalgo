# 백준 - 브론즈3 - 최장 스트릭 - 29752 - 단순 구현 문제
'''
단순 구현 문제

입력으로 들어오는 n_list의 값 중 0 이상의 값이 연속될 때 temp를 1씩 증가시킨 다음
max 함수를 이용해서 res와 temp 중 더 큰 값을 res에 담아주고,
0이 들어왔을 때도 위와 마찬가지로 max 함수를 이용해 res와 temp중 더 큰 값을 res에 담아준 뒤
최종적으로 res를 출력하면 되는 단순한 문제이다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 4
# n_list = [1, 4, 0, 1] # 2
# n = 5
# n_list = [1, 6, 3, 8, 3] # 5
# n = 3
# n_list = [0, 100, 0] # 1
# n = 1
# n_list = [0] # 0

res = 0
temp = 0
for i in n_list:
    if i:
        temp += 1
        res = max(res, temp)
    else:
        res = max(res, temp)
        temp = 0

print(res)
