# 백준 - 실버2 - 랭킹전 대기열 - 20006 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

배열을 잘 활용해야 된다. (딕셔너리로 풀려고 했는데, m 만큼 채워져 있어서 값을 추가할 때 어려움이 있어서 배열로 풀음)
 - Waiting! 을 테스트하기 위해 입력 예제에서 1을 추가한 뒤 [12, z] 의 값을 추가했다.

풀이 과정
 - 입력을 미리 받아놓고 시작했다. (이때 문자열로 다 받은 후 for 문 내에서 숫자가 필요한 부분을 int로 바꿈)
 - 입력받은 사람들 리스트로 반복문을 시작하는데, res의 길이만큼 2중 반복문으로 다음의 조건들을 확인한다.
    - res의 i 값이 m만큼 채워졌는지 확인한다. 만약, m만큼 채워졌다면 새로 append 해야 된다.
    - i의 값의 범위가 res 리스트에서 k번째 인덱스의 0번째 값을 + 10, - 10 한 범위 내에 들어오는지 확인한다.
        - 범위 내에 들어온다면 res에 새로운 값을 append 하고, flag 값을 False로 바꾼 뒤 2번째 반복문을 종료한다.
 - 위 과정이 다 끝난 뒤 res를 잘 정렬한 뒤 출력하면 된다.
'''

p, m = map(int, input().split())
p_list = [list(input().split()) for _ in range(p)]

# 테스트
# p, m = 11, 5
# p_list = [['10', 'a'], ['15', 'b'], ['20', 'c'], ['25', 'd'], ['30', 'e'], ['17', 'f'], ['18', 'g'], ['26', 'h'], ['24', 'i'], ['28', 'j'], ['12', 'z']]
'''
    Started!
    10 a
    15 b
    20 c
    17 f
    18 g
    Started!
    25 d
    30 e
    26 h
    24 i
    28 j
    Waiting!
    10 z
'''

res = []

for i, j in p_list:
    i = int(i)
    flag = True

    for k in range(len(res)):
        if len(res[k][1]) == m:
            continue

        if res[k][0] - 10 <= i <= res[k][0] + 10:
            res[k][1].append([i, j])
            flag = False
            break

    if flag:
        res.append([i, [[i, j]]])

for i in range(len(res)):
    if len(res[i][1]) == m:
        print('Started!')

        for j in sorted(res[i][1], key=lambda x: x[1]):
            print(*j)
    else:
        print('Waiting!')

        for j in sorted(res[i][1], key=lambda x: x[1]):
            print(*j)
