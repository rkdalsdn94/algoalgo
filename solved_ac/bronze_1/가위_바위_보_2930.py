# 백준 - 브론즈1 - 가위 바위 보 - 2930 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

풀이 과정
    1. 입력 값을 입력 받는다.
    2. for문을 돌면서 가위, 바위, 보를 비교하여 점수를 계산한다.
    3. 최대 점수를 계산한다.
    4. 결과를 출력한다.
'''

r = int(input())
s_rsp = input()
n = int(input())
f_rsp = [input() for _ in range(n)]

# 테스트
# r = 5
# s_rsp = 'SSPPR'
# n = 1
# f_rsp = 'SSPPR' # 5  \  10
# r = 5
# s_rsp = 'SSPPR'
# n = 2
# f_rsp = 'RRSSP' # 10  \  15

rsp = {'R': 0,'S': 1,'P': 2}

res = max_res = 0
for i in range(r):
    ts = [[0,'R'],[0,'S'],[0,'P']]

    for j in range(n):
        if (rsp[s_rsp[i]] + 1) % 3 == rsp[f_rsp[j][i]]:
            res += 2
        elif s_rsp[i] == f_rsp[j][i]:
            res += 1

        for t in ts:
            if (rsp[t[1]] + 1) % 3 == rsp[f_rsp[j][i]]:
                t[0] += 2
            elif t[1] == f_rsp[j][i]:
                t[0] += 1

    max_res += max(ts)[0]

print(res)
print(max_res)
