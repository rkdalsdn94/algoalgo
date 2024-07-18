# 백준 - 실버4 - Q - 4540 - 구현 문제
'''
구현 문제

처음에 '시작 위치 to 이동할 위치'를 시착 위치의 값을 이동할 위치로 생각하고 pop, insert로 풀려다 예제가 틀려 다시 생각했다.
방식을 바꿔, res 배열을 만들어 연산이 들어오는 부분을 바꾸고, 나머지는 0인 부분을 찾아 넣어주는 방식으로 풀었다.

풀이 과정 (이 문제는 코드로 이해하는 게 편함)
1. 테스트 케이스의 개수를 입력 받는다.
2. 테스트 케이스의 개수만큼 반복하며 다음을 수행한다.
    2.1. m, n을 입력 받는다.
    2.2. 아이템을 입력 받는다.
    2.3. 연산을 입력 받는다.
    2.4. res 배열을 만들어 연산이 들어오는 부분을 바꾸고, 나머지는 0인 부분을 찾아 넣어준다.

in
    3
    5 1
    alpha beta gamma delta epsilon
    5 2
    8 6
    a b c d e f g h
    2 6
    6 3
    4 5
    5 2
    7 4
    8 1
    3 2
    foo bar baz
    3 1
    1 3
out
    alpha epsilon beta gamma delta
    h e f g d b a c
    baz bar foo
'''

t = int(input().strip())
results = []

for _ in range(t):
    m, n = map(int, input().split())
    items = input().strip().split()
    operations = [list(map(int, input().split())) for _ in range(n)]

    res = [0] * m
    for i, j in operations:
        res[j - 1] = items[i - 1]

    idx = 0
    for i in range(m):
        if res[i] == 0:
            while items[idx] in res: # idx의 값을 찾기 위해
                idx += 1
            res[i] = items[idx]

    print(*res)
