# 백준 - 실버3 - 한동이는 공부가 하기 싫어! - 3182 - 그래프, 완전 탐색 문제
'''
그래프, 완전 탐색 문제

bfs 방식으로 풀었다.
간단한 그래프 문제라서 따로 bfs 함수를 만들지 않고, while 문으로 바로 답을 구하도록 만들었다.
dfs 방식은 제일 아래 적어놓았다. (while문 부분을 dfs 함수로 만들면 된다.)

풀이 과정
1. 입력을 받고, 그래프를 만든다.
2. 첫 번째 노드부터 시작해서 다음 노드로 이동하면서 방문한 노드를 체크한다.
3. 방문한 노드가 다시 나오면 끝낸다. 방문한 노드의 개수를 세기 위해 res를 배열로 만들었다.
4. 방문한 노드의 개수(res) 중 가장 큰 값의 인덱스를 출력한다.
'''

n = int(input())
g = [0] + [int(input()) for _ in range(n)]

# 테스트
# n = 3
# g = [0] + [3, 3, 1] # 2
# n = 4
# g = [0] + [2, 3, 4, 1] # 2
# n = 6
# g = [0] + [2, 3, 4, 3, 1, 1] # 5

res = [0] * (n + 1)

for i in range(1, n + 1):
    ck = [0] * (n + 1)
    ck[i] = 1
    temp = g[i]

    while ck[temp] == 0:
        res[i] += 1
        ck[temp] = 1
        temp = g[temp]

print(res.index(max(res)))


'''
dfs 방식

def dfs(idx, cnt):
    temp = g[idx]
    ck[idx] = 1

    if ck[temp] == 0:
        cnt = dfs(temp, cnt + 1)

    return cnt

n = int(input())
g = [0] + [int(input()) for _ in range(n)]
res = [0] * (n + 1)

for i in range(1, n + 1):
    ck = [0] * (n + 1)
    res[i] = dfs(i, 1)

print(res.index(max(res)))
'''
