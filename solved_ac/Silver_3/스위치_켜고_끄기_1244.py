'''
index를 편하게 계산하기 위해서 앞에 [0]을 더한 상태로 추가를 했고,
변환하는 부분(0->1, 1->0)을 자주 만들어서 함수로 만들었다.

여자일 때 절반까지 한 이유는 switch_status의 상태 변경을 인덱스의 앞 뒤로 해야 돼서 절반까지 했다.
'''

switch_cnt = int(input())
switch_status = [0] + list(map(int, input().split()))
studunt_cnt = int(input())
studunt = [ list(map(int, input().split())) for _ in range(studunt_cnt) ]

# 테스트
# switch_cnt = 8
# switch_status = [0] + [0,1,0,1,0,0,0,1]
# studunt_cnt = 2
# studunt = [ [1,3], [2,3] ] # 1 0 0 0 1 1 0 1

def change(n):
    if switch_status[n] == 0:
        switch_status[n] = 1
    else:
        switch_status[n] = 0

for i in studunt:
    a, b = i

    if a == 1:
        for j in range(b, switch_cnt + 1, b):
            change(j)

    elif a == 2:
        change(b)
        
        for j in range(switch_cnt // 2):
            if b + j > switch_cnt or b - j < 1: break
            if switch_status[b + j] == switch_status[b - j]:
                change(b - j)
                change(b + j)
            break

for i in range(1, switch_cnt + 1, 20):
    print(*switch_status[i:i+20])
