# 백준 - 실버4 - 비트 우정지수 - 12782 - 수학, 그리디 문제
'''
수학, 그리디 문제

수학적으로도 풀 수 있을거 같은데, 완전 탐색 방식으로 그리디하게 문제를 해결했다.

n과 m에서 서로 다른 글자가 있을 때 '0'과 '1' 글자 수의 큰 값을 구하면 되는 문제이다. (위치를 바꿀 수 있으므로)

n과 m 한 글자씩 비교하면서 두 글자가 서로 다를 때 n을 기준으로 서로 다른 값이면 1이면 one_cnt를 증가시키고
아니면 one_cnt를 증가 시킨다. 마지막으로 출력할 때는 둘 중 max값을 출력하면 된다.

in
    3
    1011 1100
    100101 110100
    00110100 10010111
out
    2
    1
    3
'''

t = int(input())

for _ in range(t):
    n, m = input().split()
    zero_cnt, one_cnt = 0, 0

    for i in range(len(n)):
        if n[i] != m[i]:
            if n[i] == '1':
                one_cnt += 1
            else:
                zero_cnt += 1

    print(max(zero_cnt, one_cnt))
