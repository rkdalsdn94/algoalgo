# 백준 - 실버2 - Hoof, Paper, Scissors (Silver) - 14453 - dp, 누적 합 문제
'''
dp, 누적 합 문제

풀이 과정 (with. Claude)
1. 누적 합을 이용한 접근
   - H, P, S 각각에 대해 해당 제스처가 나온 횟수를 누적하여 저장
   - 이를 통해 특정 구간에서 각 제스처가 몇 번 나왔는지 O(1)로 계산 가능
2. 최대 한 번의 변경을 고려한 계산
   - i번째에서 변경한다고 할 때:
     * 앞부분(1~i-1)과 뒷부분(i~n)으로 나누어 계산
     * 가능한 모든 조합을 고려: P→H, P→S, H→S, H→P, S→P, S→H
   - 예: P →, -> H의 경우
     * 앞부분: 1~(i-1)까지 P를 냈을 때 이긴 횟수 = p[i-1]
     * 뒷부분: i~n까지 H를 냈을 때 이긴 횟수 = h[n] - h[i-1]
     * 총합 = p[i-1] + h[n] - h[i-1]
3. 최댓값 계산
   - 모든 i와 가능한 변경 조합에 대해 최댓값 계산
   - 이 중 가장 큰 값이 Bessie가 이길 수 있는 최대 게임 수

in
    5
    P
    P
    H
    P
    S
out
    4
'''

n = int(input())

h, p, s = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
res = 0
n_list = [0] + [input() for _ in range(n)]

for i in range(1, n + 1):
    if n_list[i] == 'H':
        h[i] = h[i - 1] + 1
        p[i] = p[i - 1]
        s[i] = s[i - 1]
    elif n_list[i] == 'P':
        h[i] = h[i - 1]
        p[i] = p[i - 1] + 1
        s[i] = s[i - 1]
    elif n_list[i] == 'S':
        h[i] = h[i - 1]
        p[i] = p[i - 1]
        s[i] = s[i - 1] + 1

for i in range(1, n + 1):
    p_h = p[i - 1] + h[n] - h[i - 1]
    p_s = p[i - 1] + s[n] - s[i - 1]
    h_s = h[i - 1] + s[n] - s[i - 1]
    h_p = h[i - 1] + p[n] - p[i - 1]
    s_p = s[i - 1] + p[n] - p[i - 1]
    s_h = s[i - 1] + h[n] - h[i - 1]

    res = max(res, p_h, p_s, h_s, h_p, s_p, s_h)

print(res)
