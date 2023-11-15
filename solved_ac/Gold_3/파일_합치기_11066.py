# 백준 - 골드3 - 파일 합치기 - 11066 - dp 문제
'''
dp 문제

PyPy3로 제출해야 된다.

단순하게 완전 탐색 방식으로 생각해보면  O(n^3) 이 된다. 따라서, 메이이제이션을 활용할 수 있는 방법을 찾아야 하므로 dp 문제이다.
이 전의 계산했던 값을 기록하는 방식으론 2차원 배열을 만든 뒤, 다음과 같이 진행하면 된다.

첫 번째 예를 통해 누적합을 확인하면 다음과 같다.
    A   B            C                        D
A   0  A+B      (B+C) + (A+B+C)     (A+B) + (C+D) + (A+B+C+D)
B       0           B+C                 (B+C) + (B+C+D)
C                    0                       C+D
D                                             0

위 표에서 C를 구할 때 A + B 를 사용하지 않고, B + C 가 되는 이유는 min을 구해야 돼서 그렇다.
이해가 잘 안 된다면 다음 영상을 보면 쉽게 된다. 해당 영상을 참고해서 푼 문제이다.
    - https://www.youtube.com/watch?v=4OdIDIYLHlY
    - 위 영상을 보고 아래 코드를 https://pythontutor.com/render.html#mode=display 여기에서 돌려보면 이해가 잘 된다.

in
    2
    4
    40 30 30 50
    15
    1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
out
    300
    864
'''

t = int(input())
for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))

    res = [[0] * n for _ in range(n)]

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            temp = int(1e9)

            for k in range(i - j):
                temp = min(temp, res[j][j + k] + res[j + k + 1][i])
            res[j][i] = temp + sum(n_list[j:i + 1])

    print(res[0][n - 1])
