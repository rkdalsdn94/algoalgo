'''
이분 탐색 문제
전형적인 이분탐색 문제이다.
start, end(나는 보통 res로 한다)를 설정해놓고, mid값을 구한다(둘의 값을 더한 후 2로 나눈 값)
해당 mid값이랑 임시로 담을 변수 temp를 설정한 뒤에,
둘의 값을 비교해가며 start와 end(res)값을 바꾸면서 비교해간다.

백준 문제 중 '나무 자르기 - 2805' 문제와 되게 유사하다
'''

# n = int(input())
# n_list = list(map(int, input().split()))
# total = int(input())

# 테스트
n = 4
n_list = [120, 110, 140, 150]
total = 485 # 127
# n = 5
# n_list = [70, 80, 30, 40, 100]
# total = 450 # 100

start, res = 0, max(n_list)

while start <= res:
    mid = (start + res) // 2
    temp = 0

    for i in n_list:
        if i > mid:
            temp += mid
        else:
            temp += i
    
    if temp <= total:
        start = mid + 1
    else:
        res = mid - 1

print(res)
