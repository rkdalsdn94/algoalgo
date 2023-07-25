# 백준 - 실버2 - 차이를 최대로 - 10819 - 완전 탐색, 백 트래킹 문제
'''
완전 탐색, 백 트래킹 문제

완전 탐색과 백 트래킹 방식으로 푸는 문제이다.
기존에 백 트래킹에서 풀던 방시대로 방문한 곳을 체크하기 위한 ck 변수를 둔 후에 방문하지 않은 곳이면 n 까지 될 때까지 재귀 함수를 실행한다.
재귀 함수를 실행하면서 완전 탐생을 하기 위해 n_list 의 값을 temp 리스트에 추가해 놓은 뒤 재귀가 n 까지 실행 됐을 때 계산하기 위해 calculate 함수를 실행한다.
calculate 함수에선 temp에 담아놓은 값들의 차를 절댓값으로 sum_temp 에 담아 놓은 후 res 와 비교해서 max 값으로 갱신하면 된다.
마지막으로 제일 큰 값이 담긴 res 변수를 출력하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 6
# n_list = [20, 1, 15, 8, 4, 10] # 62

res, ck, temp = 0, [0] * n, []

def calculate():
    global res
    sum_temp = 0

    for i in range(n - 1):
        sum_temp += abs(temp[i] - temp[i + 1])

    res = max(res, sum_temp)

def recursive(depth):
    if depth == n:
        calculate()
        return

    for i in range(n):
        if not ck[i]:
            ck[i] = 1
            temp.append(n_list[i])
            recursive(depth + 1)
            temp.pop()
            ck[i] = 0

recursive(0)
print(res)
