# 백준 - 실버2 - 용돈 관리 - 6236 - 이진 탐색 문제
'''
이진 탐색 문제

전형적인 이진 탐색 문제이다.
start와 end를 각각 list에서 제일 작은 값, 제일 큰 값으로 초기화 해준 다음에
두 값의 합에서 나누기 2 한 몫을 mid로 설정한다.

mid값으로 n만큼 반복하면서 temp값으로 돈을 몇 번 출금했는지 계산 한 다음
n일이 지난 후 mid값, 출금한 횟수인 num값으로 start와 end를 갱신하면서 답을 찾아가면 된다.
'''

n, m = map(int, input().split())
n_list = [ int(input()) for _ in range(n) ]

# 테스트
# n, m = 7, 5
# n_list = [100,400,300,100,500,101,400]

start, end = min(n_list), sum(n_list)

while start <= end:
    mid = (start + end) // 2
    temp = mid
    num = 1

    for i in range(n):
        if temp < n_list[i]:
            temp = mid
            num += 1
        temp -= n_list[i]
    
    if num > m or mid < max(n_list):
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)