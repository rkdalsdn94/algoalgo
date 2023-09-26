# 백준 - 실버4 - 가위 바위 보 - 8896 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

쉽게 생각했다가 시간이 꽤 오래 걸린 문제이다. (대략 2시간 가량..)
다 풀고 보니 다시 정리해보니 문제인데 중간에 한 번 꼬이니까 꽤 헤멘거 같다. (시뮬레이션 문제는 더 많이 풀어야 될 듯..)

개인적으로 풀이 방식의 핵심은 다음과 같다 (코드에 있는 주석을 봐도 됨)
    1. 로봇들의 가위바위보 들을 입력받아 놓은 후, temp를 사용해 각각의 로봇들의 턴마다 무엇을 내는지 temp에 담는다.
    2. 서로 다른 로봇들이 각자 가위, 바위, 보 따로 낸 상황이면 건너뛴다.
    3. 가위가 이겼을 때, 보가 이겼을 때, 주먹이 이겼을 때 상황에 맞게 lowers, winner 셋 자료 구조(중복을 제거하기 위해)에 담는다.
    4. winner 에서 lowers와 겹치는 부분이 있을 수 있으므로 lowers 의 값들을 제거한다.
        이때, remove를 사용하면 없는 key를 제거한다는 에러가 나올 수 있으니 discard 함수를 사용하는 것이 좋다.
    5. winner의 길이가 1보다 크면 무승부로 끝나는 상황이므로 0을 출력하고, 1이면 1을 더한 상태로 출력하면 된다.

문제를 다 풀고, 다른 사람의 코드를 보다 winner 변수는 없어도 풀 수 있다는 사실을 알았다.
3번 상황에서 lowers 들만 담아놓은 뒤,
    if n - len(lowers) > 1 일 경우 0 출력
    아닐 경우 0 ~ n을 돌면서 lowers 에 없는 인덱스가 나올 경우 해당 인덱스 + 1 을 출력하면 된다.

in
    3
    5
    RPSSSPR
    SSRPRPS
    PRSSRSP
    RRRPSPP
    SSSSSRP
    4
    RPSPSPSPRPRPSR
    SPSSRRRSSRPRRR
    RSPRPPPPSSRPSR
    PRRSSSRRPRSRRR
    3
    SPPPSS
    SPRRRR
    SSSSPP
out
    2
    0
    3
'''

t = int(input())
for _ in range(t):
    n = int(input())
    robot = [input() for _ in range(n)]
    lowers = set()
    winner = set()

    for i in range(len(robot[0])):
        temp = ''

        for j in range(n):
            if j not in lowers:
                temp += robot[j][i]
            else:
                temp += '0'

        if 'R' in temp and 'S' in temp and 'P' in temp: # 서로 다른 로봇들이 가위, 바위, 보 를 낸 상황(무승부)
            continue
        # 주먹 vs 보
        elif 'R' in temp and 'P' in temp:
            for k, c in enumerate(temp):
                if c == 'R':
                    lowers.add(k) # 주먹은 lowers 추가

            for k, c in enumerate(temp):
                if c == 'P':
                    winner.add(k) # 보는 winner 추가
        # 주먹 vs 가위
        elif 'R' in temp and 'S' in temp:
            for k, c in enumerate(temp):
                if c == 'S':
                    lowers.add(k) # 가위는 lowers 추가

            for k, c in enumerate(temp):
                if c == 'R':
                    winner.add(k) # 바위는 winner 추가
        # 가위 vs 보
        elif 'S' in temp and 'P' in temp:
            for k, c in enumerate(temp):
                if c == 'P':
                    lowers.add(k) # 보는 lowers 추가

            for k, c in enumerate(temp):
                if c == 'S':
                    winner.add(k) # 가위는 winner 추가

    # 진 로봇들의 set을 돌면서 winner에서 제거 remove를 사용하면 에러가 나므로 dicard 함수 사용
    for i in lowers:
        winner.discard(i)

    if len(winner) == 1: # 이긴 사람인덱스의 1을 더해야 됨
        print(int(*winner) + 1)
    else: # 만약 이긴 사람이 1보다 큰 경우 무승부로 승부가 끝까지 이어졌으므로 0출력
        print(0)
