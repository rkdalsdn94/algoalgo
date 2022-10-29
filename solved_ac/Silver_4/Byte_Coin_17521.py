# 백준 - 실버4 - Byte Coin - 17521 - 단순 구현, 그리디 문제
'''
그리디 문제

단순하게 처음 드는 생각대로 그리디하게 풀면 된다.

풀이 과정
1. 1부터 n까지 반복하면서 temp에 현재 반복 중인 i - 1의 값을 할당한다.
2. 몇 개의 코인을 살 수 있을지 구하고 팔았을 때 이득되는 값을 구한다.
    2.1 몇 개의 코인을 살 수 있는지 구하는 식은 current_coin // temp 이 식으로 구할 수 있다. -> a
    2.2 이전 코인을 사고 현재 코인을 팔았을 때 이득이 되는 값을 구하는 식은 n_list[i] - temp 이다. -> b
3. 위 (a, b) 값들의 곱을 현재 코인에 더한 다음에 반복문이 끝나면 출력하면 된다.
'''

n, current_coin = map(int, input().split())
n_list = [ int(input()) for _ in range(n) ]

# 테스트
# n, current_coin = 10, 24
# n_list = [ 5, 7, 5, 4, 2, 7, 8, 5, 3, 4 ] # 170
# n, current_coin = 5, 15
# n_list = [ 5, 4, 4, 2, 7 ] # 50
# n, current_coin = 7, 54
# n_list = [ 7, 5, 5, 4, 2, 2, 1 ] # 54

res = 0

for i in range(1, n):
    temp = n_list[i - 1]

    if temp < n_list[i]:
        a = current_coin // temp
        b = n_list[i] - temp
        current_coin += a * b

print(current_coin)
