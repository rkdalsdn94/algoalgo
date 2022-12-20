# 백준 - 골드4 - 사탕 가게 - 4781 - dp, 배낭(knapsack) 문제
'''
dp, 배낭(knapsack) 문제

다른 배낭 문제처럼 풀면 된다. 단, 소수점 때문에 질문 게시판을 통해 힌트를 얻어서 풀었다.

풀이 과정
1. input을 형식에 맞게 잘 입력 받는다. -> 소수점 때문에 float으로 입력 받은 후, int로 형변환을 진행했다.
    단, 돈의 양인 m은 100을 곱한 후 int로 바꿨다.
    input의 n과 m이 각각 0과 0,00 이면 break를 통해 while 문을 빠져나간다.
2. 탈출 조건이 아니면 while 문을 반복하면서 사탕의 칼로리(c)와 가격(p)를 n과 m이랑 비슷하게 입력 받는다.
    단, p는 100을 곱하고, 0.5를 더한 상태로 int로 형변환을 해야 된다. 자세한 이유는 아래 링크를 살펴보자.
    https://joooing.tistory.com/entry/0과-1만-가지고-실수를-표현하는-방법
3. 첫 번째 반복문은 m + 1로 초기화 한 dp를 1부터 m까지 반복하면서 두 번째 반복문으로 사탕 종류의 수를 2중 반복문을 만든다.
    3.1. 두 번째 반복문인 j의 값이 n_list[j][1] 보다 크거나 같으면
        해당 dp[i]를 dp[i - n_list[j][1]] + n_list[j][0] 값 중 더 큰 값으로 갱신한다.
    3.2. 작으면 다음 반복문을 실행한다.
4. dp[m]을 출력한다.

in
    2 8.00
    700 7.00
    199 2.00
    3 8.00
    700 7.00
    299 3.00
    499 5.00
    0 0.00
out
    796
    798
'''

while 1:
    n, m = map(float, input().split())
    n, m = int(n), int(m * 100)

    if n == 0 and m == 0.00:
        break

    dp = [0] * (m + 1)
    n_list = []

    for _ in range(n):
        c, p = map(float, input().split())
        c, p = int(c), int(p * 100 + 0.5)
        n_list.append([c, p])
    
    for i in range(1, m + 1):
        for j in range(n):
            if i >= n_list[j][1]:
                dp[i] = max(dp[i], dp[i - n_list[j][1]] + n_list[j][0])
    
    print(dp[m])


