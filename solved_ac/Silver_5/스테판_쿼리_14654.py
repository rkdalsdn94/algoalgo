'''
구현, 시뮬레이션 문제

    1 : 가위
    2 : 바위
    3 : 보
문제를 잘못 이해하고, 이긴 사람은 계속 자신의 숫자를 내야 되는지 알고 idx로 값을 비교하면서
반목문을 while문으로 구현하고 있었는데 이 문제의 질문 검색 게시판을 가도 그렇지 않다고 한다....
연승의 기준 - https://www.acmicpc.net/board/view/17797

그래서 문제를 다시 푸는데 다른 부분은 간단하고, 비겼을 때만 조심하면 된다.
처음 시작을 비기는 경우가 없으니까 그 다음 수부터 비긴다면 무조건 반대편이 이기게 된다.
그래서, a가 숫자가 있는 상태(바로 전에 이겼을 경우)면 b를 1 더하고 a를 0으로 만든다.
반대의 경우는 반대로 하면 된다.
그 후에 res값을 max로 비교하면서 갱신하면 된다.
'''

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# 테스트
# n = 4
# a_list = [1,2,3,1]
# b_list = [2,1,3,1] # 1
# n = 5
# a_list = [2,3,1,3,1]
# b_list = [1,1,2,3,2] # 2

res = 0
a, b = 0, 0

for x, y in zip(a_list, b_list):
    temp = x - y

    if temp == 0: # 비김
        if a: # '새로 출전한 사람이 승리한 것으로 간주하며'라는 부분 때문에 a가 있으면 b 승, b가 있으면 a 승
            b += 1
            a = 0
        else:
            a += 1
            b = 0
            
    if temp == 1 or temp == -2: # a가 승리
        a += 1
        b = 0

    if temp == -1 or temp == 2: # b가 승리
        b += 1
        a = 0
    
    res = max(res, a, b)

print(res)