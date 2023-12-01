# 백준 - 실버5 - 욕심쟁이 돼지 - 3060 - 시뮬레이션, 수학, 구현 문제
'''
시뮬레이션, 수학, 구현 문제

2번째 사이클부터 양쪽과 사이드의 합이 필요하다.
처음에는 이 부분을 while 문으로 n보다 커질 때까지 list[i - 1] + list[i] + list[i - 3] + list[i - 5] 이러한 방식으로 풀었다가
다른 사람의 풀이를 보니 이 문제는 규칙이 있었다.
양 옆과 반대편 합의 리스트는 처음 리스트의 전체 합 * 3과 같다. 즉, total을 통해 이 문제를 쉽게 해결할 수 있다. (total += total * 3)
규칙을 찾을 수 있도록 연습도 많이 해야 될 거 같다.

in
    2
    21
    1 2 3 4 5 6
    21
    1 2 3 4 5 7
out
    2
    1
'''

t = int(input())
for _ in range(t):
    res = 1
    n = int(input())
    total = sum(list(map(int, input().split())))

    while n >= total:
        total += total * 3
        res += 1

    print(res)
