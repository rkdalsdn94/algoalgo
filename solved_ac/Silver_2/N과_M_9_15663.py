# 백준 - 실버2 - N과 M 9 - 15663 - 백 트래킹 문제
'''
백 트래킹 문제

기존의 n과 m 문제들과 비슷하게 풀면 되는데, 중복 체크를 해야 된다.
다른 사람들의 풀이에선 temp를 이용해 많이 푼 거 같은데, 여기선 set을 이용했다. (검사하는 로직은 사실상 동일)

풀이 과정
- 재귀 형식으로 문제를 풀고, 재귀의 종료 조건은 depth가 m과 같아졌을 때 현재 담겨있는 res 리스트를 출력하고 종료시킨다.
- 종료 조건에 만족하지 않았으면 m의 길이에 오지 못한 상황이므로 중복을 체크하기 위해 temp를 빈 set 자료 구조로 초기화한다.
- 0 ~ n 까지 반복하면서 n_list 의 값들을 하나 씩 순회한다.
    - 순회 중 현재 위치가 방문하지 않은 곳이고, temp에 추가되어 있지 않다면 종료 조건을 만족시킬 때까지 back_tracking 함수를 실행시킨다.
    - 함수를 종료 후엔 방문 했다는 위치를 초기화 시키고, res의 값도 pop 해야 된다.
'''

n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n, m = 3, 1
# n_list = sorted([4, 4, 2]) # 2  \  4
# n, m = 4, 2
# n_list = sorted([9, 7, 9, 1])
# '''
#     1 7
#     1 9
#     7 1
#     7 9
#     9 1
#     9 7
#     9 9
# '''
# n, m = 4, 4
# n_list = sorted([1, 1, 1, 1]) # 1 1 1 1

res = []
ck = [0] * n

def back_tracking(depth):
    if depth == m:
        print(*res)
        return

    temp = set()
    for i in range(n):
        if not ck[i] and n_list[i] not in temp:
            ck[i] = 1
            res.append(n_list[i])
            temp.add(n_list[i])
            back_tracking(depth + 1)
            ck[i] = 0
            res.pop()

back_tracking(0)
