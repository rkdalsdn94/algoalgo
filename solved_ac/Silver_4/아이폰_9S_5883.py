# 백준 - 실버4 - 아이폰 9S - 5883 - 구현, 완전 탐색
'''
구현, 완전 탐색 문제

set으로 문자열을 중복을 제거한 뒤 반복문을 시작한다.
num을 1로 초기화 한 다음에 n_list의 값을 순회하면서 set으로 제거된 값이 나올경우 무시한다.
temp로 이전 값과 같은 값이 나오면 num을 1씩 증가시키면서 res의 값과 비교하면서 더 큰 값으로 바꿔준다.
마지막 출력하기 전에 한번 더 비교한 후 출력해야 정답이 된다. -> 이 부분을 안하고 몇번 틀렸었다...
'''

n = int(input())
n_list = [ int(input()) for _ in range(n) ]

# 테스트
# n = 9
# n_list = [2, 7, 3, 7, 7, 3, 7, 5, 7] # 4
# n = 10
# n_list = [123, 123, 123, 123, 123, 123, 123, 123, 123, 123] # 0

res = 0
temp = 0

for i in set(n_list):
    num = 1

    for j in n_list:
        if j == i:
            continue
        if temp == j:
            num += 1
            res = max(res, num)
        else:
            num = 1
            temp = j

print(max(res, num)) # 마지막에 한번 더 검사해야 된다.